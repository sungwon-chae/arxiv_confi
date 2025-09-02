  python3 - <<'PY'
  import inspect, etu.utils as U
  print("utils path:", U.__file__)
  print("adjust_lambda params:", list(inspect.signature(U.adjust_lambda).parameters))
  PY




  python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 8 \
  --max_num_batches 50 \
  --num_epochs 3 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 30.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.75 \
  --use_pmi_vs \
  --pmi_top_k 128 \
  --pmi_min_count 10 \
  --pmi_smoothing 1.0 \
  --retain_weight 0.25 \
  --wilson_max_n 10000 \
  --pinsker_cap 0.10 \
  --no-use_upper_for_lambda \
  --verbose
