# 옵션 1: 보수적 설정 (빠른 테스트)
python run_etu_h200.py \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --batch_size 4 \
  --max_num_batches 20 \
  --layer_id 7 \
  --verbose

# 옵션 2: 공격적 설정 (전체 성능 테스트)
python run_etu_h200.py \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --batch_size 8 \
  --max_num_batches 100 \
  --layer_id 7 \
  --verbose
