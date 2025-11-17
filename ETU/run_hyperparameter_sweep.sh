#!/usr/bin/env bash
# 하이퍼파라미터 스윕 자동화 (H200 GPU 최적화, Zephyr-7B)
set -euo pipefail

echo "=== Hyperparameter Sweep (H200 GPU 최적화) ==="
date

# ----- GPU 요약 -----
GPU_NAMES=$(nvidia-smi --query-gpu=name --format=csv,noheader,nounits || true)
GPU_COUNT=$(echo "${GPU_NAMES:-}" | wc -l | awk '{print $1}')
H200_COUNT=$(echo "${GPU_NAMES:-}" | grep -c "H200" || true)
echo "GPU Summary:"
echo " - 총 GPU: ${GPU_COUNT}"
echo " - H200 GPU: ${H200_COUNT}"
echo " - 첫 GPU: $(echo "${GPU_NAMES:-}" | head -1)"

# ----- 기본 파라미터 (H200 최적화) -----
if [[ "${H200_COUNT}" -ge 1 ]]; then
  echo "🚀 H200 GPU 환경 감지됨 - 최적화된 설정 사용"
  BATCH_SIZE=64
  LORA_R=512
  LORA_ALPHA=1024
  MAX_BATCHES=500
  FROZEN_ON_CPU=true       # 메모리 절약을 위해 true
  STRATEGY="ddp"
else
  echo "⚠️  H200 GPU가 아님 - 보수적 설정 사용"
  BATCH_SIZE=8
  LORA_R=256
  LORA_ALPHA=512
  MAX_BATCHES=80
  FROZEN_ON_CPU=true
  STRATEGY="ddp"
fi

echo "📊 기본 설정:"
echo " - strategy: ${STRATEGY}"
echo " - batch_size: ${BATCH_SIZE}"
echo " - lora_r: ${LORA_R}"
echo " - lora_alpha: ${LORA_ALPHA}"
echo " - max_num_batches: ${MAX_BATCHES}"
echo " - frozen_on_cpu: ${FROZEN_ON_CPU}"
echo ""

# ----- 공통 경로/런처 -----
MODEL_ID="HuggingFaceH4/zephyr-7b-beta"
FORGET_DIR="./datasets/cyber-forget"
RETAIN_DIR="./datasets/bio-retain"
OUT_ROOT="sweep_results/zephyr_7b"
LOG_ROOT="${OUT_ROOT}/logs"
mkdir -p "${OUT_ROOT}" "${LOG_ROOT}"

# 데이터셋 폴백 (없으면 HF 레포로 전환)
if [[ ! -d "${FORGET_DIR}" ]] || [[ ! -d "${RETAIN_DIR}" ]]; then
  echo "ℹ️ 로컬 데이터셋이 없어서 HF 데이터셋으로 대체합니다."
  FORGET_DIR="cais/wmdp-corpora:cyber-forget-corpus"
  RETAIN_DIR="cais/wmdp-corpora:bio-retain-corpus"
fi

# 런처 (멀티 GPU면 torchrun)
if [[ "${GPU_COUNT}" -ge 2 ]]; then
  LAUNCHER=(torchrun --standalone --nproc_per_node="${GPU_COUNT}")
else
  LAUNCHER=(python)
fi

# 런타임 권장 env
export NCCL_P2P_DISABLE=0
export NCCL_IB_DISABLE=0
export TORCH_NCCL_BLOCKING_WAIT=1
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:256
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"

# ----- 공통 인자 배열 (반드시 모든 스윕에 포함) -----
COMMON_ARGS=(
  --model_name_or_path "${MODEL_ID}"
  --forget_corpora "${FORGET_DIR}"
  --retain_corpora "${RETAIN_DIR}"
  --batch_size "${BATCH_SIZE}"
  --max_num_batches "${MAX_BATCHES}"
  --use_lora
  --lora_r "${LORA_R}"
  --lora_alpha "${LORA_ALPHA}"
  --strategy "${STRATEGY}"
  --frozen_on_cpu
  --seed 42
  --verbose
)

# ----- 0) 베이스 런 -----
RUN_ID="base_$(date +%Y%m%d_%H%M%S)"
OUT_DIR="${OUT_ROOT}/${RUN_ID}"
mkdir -p "${OUT_DIR}"
echo "=== Base Run 시작 ==="
"${LAUNCHER[@]}" run_etu_h200.py \
  "${COMMON_ARGS[@]}" \
  --epsilon 0.05 \
  --lambda_max 30.0 \
  --output_dir "${OUT_DIR}" 2>&1 | tee "${LOG_ROOT}/${RUN_ID}.log"

# ----- 1) Epsilon 스윕 -----
echo "=== Epsilon 스윕 시작 ==="
for epsilon in 0.01 0.05 0.1 0.2; do
  RUN_ID="eps_${epsilon}_$(date +%H%M%S)"
  OUT_DIR="${OUT_ROOT}/${RUN_ID}"
  mkdir -p "${OUT_DIR}"
  echo "  -> epsilon=${epsilon}"
  "${LAUNCHER[@]}" run_etu_h200.py \
    "${COMMON_ARGS[@]}" \
    --epsilon "${epsilon}" \
    --lambda_max 30.0 \
    --output_dir "${OUT_DIR}" 2>&1 | tee "${LOG_ROOT}/${RUN_ID}.log"
done

# ----- 2) lambda_max 스윕 -----
echo "=== lambda_max 스윕 시작 ==="
for lambda_max in 8.0 12.0 15.0 20.0; do
  RUN_ID="lmax_${lambda_max}_$(date +%H%M%S)"
  OUT_DIR="${OUT_ROOT}/${RUN_ID}"
  mkdir -p "${OUT_DIR}"
  echo "  -> lambda_max=${lambda_max}"
  "${LAUNCHER[@]}" run_etu_h200.py \
    "${COMMON_ARGS[@]}" \
    --epsilon 0.05 \
    --lambda_max "${lambda_max}" \
    --output_dir "${OUT_DIR}" 2>&1 | tee "${LOG_ROOT}/${RUN_ID}.log"
done

# ----- 3) lambda_eta 스윕 (지원 시만) -----
echo "=== lambda_eta 스윕 시작 ==="
for lambda_eta in 0.1 0.25 0.5 1.0; do
  RUN_ID="leta_${lambda_eta}_$(date +%H%M%S)"
  OUT_DIR="${OUT_ROOT}/${RUN_ID}"
  mkdir -p "${OUT_DIR}"
  echo "  -> lambda_eta=${lambda_eta}"
  "${LAUNCHER[@]}" run_etu_h200.py \
    "${COMMON_ARGS[@]}" \
    --epsilon 0.05 \
    --lambda_max 30.0 \
    --lambda_eta "${lambda_eta}" \
    --output_dir "${OUT_DIR}" 2>&1 | tee "${LOG_ROOT}/${RUN_ID}.log"
done

# ----- 4) LoRA rank 스윕 (H200 환경에서만) -----
if [[ "${FROZEN_ON_CPU}" == "false" ]]; then
  echo "=== LoRA rank 스윕 시작 (H200) ==="
  for rank in 128 256 512 1024; do
    RUN_ID="lora_r_${rank}_$(date +%H%M%S)"
    OUT_DIR="${OUT_ROOT}/${RUN_ID}"
    mkdir -p "${OUT_DIR}"
    echo "  -> lora_r=${rank}, lora_alpha=$((rank * 2))"
    "${LAUNCHER[@]}" run_etu_h200.py \
      "${COMMON_ARGS[@]}" \
      --epsilon 0.05 \
      --lambda_max 30.0 \
      --lora_r "${rank}" \
      --lora_alpha "$((rank * 2))" \
      --output_dir "${OUT_DIR}" 2>&1 | tee "${LOG_ROOT}/${RUN_ID}.log"
  done
fi

# ----- 5) Batch size 스윕 (H200 환경에서만) -----
if [[ "${FROZEN_ON_CPU}" == "false" ]]; then
  echo "=== Batch size 스윕 시작 (H200) ==="
  for bs in 4 8 16 32; do
    RUN_ID="bs_${bs}_$(date +%H%M%S)"
    OUT_DIR="${OUT_ROOT}/${RUN_ID}"
    mkdir -p "${OUT_DIR}"
    echo "  -> batch_size=${bs}"
    "${LAUNCHER[@]}" run_etu_h200.py \
      "${COMMON_ARGS[@]}" \
      --epsilon 0.05 \
      --lambda_max 30.0 \
      --batch_size "${bs}" \
      --output_dir "${OUT_DIR}" 2>&1 | tee "${LOG_ROOT}/${RUN_ID}.log"
  done
fi

echo "=== 모든 하이퍼파라미터 스윕 완료 ==="
date
echo "결과: ${OUT_ROOT}/  (로그: ${LOG_ROOT}/)"
