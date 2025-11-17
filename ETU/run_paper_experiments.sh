#!/usr/bin/env bash
# ETU 논문 실험 자동화 스크립트 (H200 GPU 최적화, Zephyr-7B)
set -euo pipefail

echo "=== ETU Paper Experiments (H200 GPU 최적화) ==="
date

# -------- GPU 환경 요약 --------
GPU_NAMES=$(nvidia-smi --query-gpu=name --format=csv,noheader,nounits || true)
GPU_COUNT=$(echo "${GPU_NAMES:-}" | wc -l | awk '{print $1}')
H200_COUNT=$(echo "${GPU_NAMES:-}" | grep -c "H200" || true)
echo "GPU Summary:"
echo " - 총 GPU: ${GPU_COUNT}"
echo " - H200 GPU: ${H200_COUNT}"
echo " - 첫 GPU: $(echo "${GPU_NAMES:-}" | head -1)"

# -------- H200 최적화 파라미터 --------
if [[ "${H200_COUNT}" -ge 1 ]]; then
  echo "🚀 H200 GPU 환경 감지됨 - 최적화된 설정 사용"
  BATCH_SIZE=64            # H200 기준 대규모 실험 (7B + LoRA)
  LORA_R=512
  LORA_ALPHA=1024
  MAX_BATCHES=500
  FROZEN_ON_CPU=true       # 메모리 절약을 위해 true
  STRATEGY="ddp"           # run_etu_h200.py가 지원하면 전달
else
  echo "⚠️  H200 GPU가 아님 - 보수적 설정 사용"
  BATCH_SIZE=8
  LORA_R=256
  LORA_ALPHA=512
  MAX_BATCHES=80
  FROZEN_ON_CPU=true
  STRATEGY="ddp"
fi

echo "📊 최적화 설정:"
echo " - strategy: ${STRATEGY}"
echo " - batch_size: ${BATCH_SIZE}"
echo " - lora_r: ${LORA_R}"
echo " - lora_alpha: ${LORA_ALPHA}"
echo " - max_num_batches: ${MAX_BATCHES}"
echo " - frozen_on_cpu: ${FROZEN_ON_CPU}"
echo ""

# -------- 경로/출력 준비 --------
MODEL_ID="HuggingFaceH4/zephyr-7b-beta"
FORGET_DIR="./datasets/cyber-forget"
RETAIN_DIR="./datasets/bio-retain"
OUT_DIR="paper_results/zephyr_7b"
LOG_DIR="${OUT_DIR}/logs"
mkdir -p "${OUT_DIR}" "${LOG_DIR}"

# 데이터셋 존재 확인 (없으면 HF ID로 대체 예시)
if [[ ! -d "${FORGET_DIR}" ]] || [[ ! -d "${RETAIN_DIR}" ]]; then
  echo "ℹ️ 로컬 데이터셋 디렉토리가 없어 HF 데이터셋으로 대체합니다."
  FORGET_DIR="cais/wmdp-corpora:cyber-forget-corpus"
  RETAIN_DIR="cais/wmdp-corpora:bio-retain-corpus"
fi

# -------- 런타임 환경 변수(권장) --------
export NCCL_P2P_DISABLE=0
export NCCL_IB_DISABLE=0
export TORCH_NCCL_BLOCKING_WAIT=1
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:256
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"

# 단일 GPU 실행
LAUNCHER="python3"
export CUDA_VISIBLE_DEVICES=1 #1번만 일단 사용

# -------- 실험 실행 --------
echo "=== Zephyr-7B ETU 실험 시작 ==="
${LAUNCHER} run_etu_h200.py \
  --model_name_or_path "${MODEL_ID}" \
  --epsilon 0.05 \
  --lambda_max 30.0 \
  --batch_size "${BATCH_SIZE}" \
  --max_num_batches "${MAX_BATCHES}" \
  --lora_r "${LORA_R}" \
  --lora_alpha "${LORA_ALPHA}" \
  --forget_corpora "${FORGET_DIR}" \
  --retain_corpora "${RETAIN_DIR}" \
  --strategy "${STRATEGY}" \
  --frozen_on_cpu \
  --output_dir "${OUT_DIR}" \
  --verbose 2>&1 | tee "${LOG_DIR}/zephyr_7b_$(date +%Y%m%d_%H%M%S).log"

echo "All experiments completed at: $(date)"
echo "Results saved in ${OUT_DIR}/ and models/ (모델 아티팩트 저장 위치는 스크립트 구현에 따름)"
