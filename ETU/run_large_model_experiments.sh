#!/bin/bash
# 8대 H200 GPU 대용량 모델 실험 스크립트 (2025-09, Scout 포함, Zephyr 멀티도메인)
set -euo pipefail

echo "=== ETU 8x H200 Large-model Experiments (2025-09) ==="
echo "Starting at: $(date)"

# 8대 H200 GPU 환경 확인
GPU_COUNT=$(nvidia-smi --query-gpu=name --format=csv,noheader,nounits | wc -l)
H200_COUNT=$(nvidia-smi --query-gpu=name --format=csv,noheader,nounits | grep -c "H200")

echo "🔍 GPU 환경 분석:"
echo "   - 총 GPU 개수: $GPU_COUNT"
echo "   - H200 GPU 개수: $H200_COUNT"

if [ "$H200_COUNT" -lt 8 ]; then
  echo "⚠️  H200 GPU가 8개 미만입니다. 일부 실험만 실행합니다."
  MAX_GPU=$H200_COUNT
else
  echo "✅ 8대 H200 GPU 모두 감지됨! 모든 실험 실행 가능"
  MAX_GPU=8
fi
echo ""

###############################################################################
# 1) OpenAI GPT-OSS-20B (경량 MoE) — DDP
echo "=== gpt-oss-20b 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy ddp \
  --model_name_or_path "openai/gpt-oss-20b" \
  --batch_size 128 \
  --max_num_batches 500 \
  --lora_r 512 \
  --lora_alpha 1024 \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

# 2) OpenAI GPT-OSS-120B (대형 MoE) — FSDP
echo "=== gpt-oss-120b 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy fsdp \
  --model_name_or_path "openai/gpt-oss-120b" \
  --batch_size 24 \
  --max_num_batches 500 \
  --lora_r 1024 \
  --lora_alpha 2048 \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

# 3) Qwen3-32B (dense) — DDP
echo "=== Qwen3-32B 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy ddp \
  --model_name_or_path "Qwen/Qwen3-32B" \
  --batch_size 64 \
  --max_num_batches 500 \
  --lora_r 768 \
  --lora_alpha 1536 \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

# 4) DeepSeek-R1-Distill-Qwen-32B — FSDP
echo "=== DeepSeek-R1-Distill-Qwen-32B 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy fsdp \
  --model_name_or_path "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" \
  --batch_size 48 \
  --max_num_batches 500 \
  --lora_r 768 \
  --lora_alpha 1536 \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

# 5) DeepSeek-R1-Distill-Qwen-14B — DDP
echo "=== DeepSeek-R1-Distill-Qwen-14B 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy ddp \
  --model_name_or_path "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B" \
  --batch_size 160 \
  --max_num_batches 500 \
  --lora_r 512 \
  --lora_alpha 1024 \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

# 6) Meta Llama 4 Scout (109B) — FSDP
echo "=== Llama-4-Scout-109B 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy fsdp \
  --model_name_or_path "meta-llama/Llama-4-Scout-109B" \
  --batch_size 16 \
  --max_num_batches 500 \
  --lora_r 1024 \
  --lora_alpha 2048 \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

# 7) 멀티 도메인 대용량 실험 — Zephyr-7B # batch size 512로 향상 (리소스 넉넉함)
echo "=== 멀티 도메인 (Zephyr-7B) 실험 시작 ==="
python run_etu_multi_h200.py \
  --strategy ddp \
  --model_name_or_path "HuggingFaceH4/zephyr-7b-beta" \
  --batch_size 512 \
  --max_num_batches 500 \
  --lora_r 512 \
  --lora_alpha 1024 \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --epsilon 0.05 \
  --lambda_max 30 \
  --trust_remote_code \
  --verbose

echo "=== 모든 대용량 모델 실험 완료 ==="
echo "Completed at: $(date)"
echo "Results saved in models/ directory"
