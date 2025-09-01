python run_etu_h200.py \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --batch_size 4 \
  --max_num_batches 20 \
  --layer_id 7 \
  --min_len 1 \
  --max_len 2000 \
  --verbose
