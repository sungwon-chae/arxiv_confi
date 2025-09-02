# 기본값으로 실행 (로컬 데이터셋 사용)
python3 run_etu_h200.py --verbose

# 또는 명시적으로 지정
python3 run_etu_h200.py \
  --forget_corpora "./datasets/cyber-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 1 \
  --max_num_batches 3 \
  --layer_id 7 \
  --verbose
