export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7

python3 run_etu_h200.py \
  --multi_gpu \
  --strategy ddp \
  --forget_corpora "./datasets/cyber-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 32 \
  --max_num_batches 50 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 12.0 \
  --verbose
