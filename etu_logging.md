python3 -c "
import json
from transformers import AutoTokenizer
run_dir = 'models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0645_2025-09-02-20-16-27'
vs_path = f'{run_dir}/V_S.ids.json'
ids = json.load(open(vs_path))
tok = AutoTokenizer.from_pretrained('HuggingFaceH4/zephyr-7b-beta')
print(f'V_S size: {len(ids)}')
print('Top 50 tokens:')
for tid in ids[:50]:
    print(f'{tid}\t{tok.convert_ids_to_tokens(tid)}')
"

export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

cd ETU && \
python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget/data" \
  --retain_corpora "./datasets/bio-retain/bio-retain-corpus" \
  --batch_size 32 \
  --max_num_batches 500 \
  --num_epochs 2 \
  --layer_ids "6,7,8" \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --lora_r 128 \
  --epsilon 0.10 \
  --lambda_max 40.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 2 \
  --pmi_top_k 256 \
  --pmi_smoothing 1.0 \
  --pmi_max_batches 2000 \
  --vocab_top_k 300 \
  --vs_abs_cap 256 \
  --vs_freq_rate 0.03 \
  --span_masking \
  --span_ngram_max 4 \
  --retain_weight 0.1 \
  --wilson_max_n 10000 \
  --pinsker_cap 0.10 \
  --mixed_precision bf16 \
  --vs_debug \
  --vs_debug_topk 200 \
  --verbose
