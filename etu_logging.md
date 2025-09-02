(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 8 \
  --max_num_batches 50 \
  --num_epochs 3 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 12.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.25 \
  --use_pmi_vs \
  --pmi_top_k 2000 \
  --pmi_min_count 10 \
  --pmi_smoothing 1.0 \
  --span_masking \
  --span_ngram_max 3 \
  --retain_weight 0.5 \
  --verbose
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
GPU 0: NVIDIA H200 (139.8 GB)
GPU 1: NVIDIA H200 (139.8 GB)
GPU 2: NVIDIA H200 (139.8 GB)
GPU 3: NVIDIA H200 (139.8 GB)
GPU 4: NVIDIA H200 (139.8 GB)
GPU 5: NVIDIA H200 (139.8 GB)
GPU 6: NVIDIA H200 (139.8 GB)
✅ H200 GPU 7개 감지됨
usage: run_etu_h200.py [-h] [--gpu_id GPU_ID] [--multi_gpu] [--strategy {ddp,fsdp,tensor_parallel}]
                       [--batch_size_per_gpu BATCH_SIZE_PER_GPU] [--batch_size BATCH_SIZE]
                       [--max_num_batches MAX_NUM_BATCHES] [--frozen_on_cpu] [--use_lora]
                       [--lora_r LORA_R] [--lora_alpha LORA_ALPHA] [--epsilon EPSILON]
                       [--lambda_max LAMBDA_MAX] [--lambda_update_freq LAMBDA_UPDATE_FREQ]
                       [--forget_corpora FORGET_CORPORA] [--retain_corpora RETAIN_CORPORA]
                       [--model_name_or_path MODEL_NAME_OR_PATH] [--deterministic] [--verbose]
                       [--gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS]
                       [--mixed_precision {fp16,bf16,fp32}] [--trust_remote_code] [--lr LR]
                       [--num_epochs NUM_EPOCHS] [--min_len MIN_LEN] [--max_len MAX_LEN]
                       [--layer_id LAYER_ID] [--layer_ids LAYER_IDS] [--param_ids PARAM_IDS]
                       [--name_keywords NAME_KEYWORDS] [--module_str MODULE_STR] [--use_pmi_vs]
                       [--vocab_top_k VOCAB_TOP_K] [--vs_freq_rate VS_FREQ_RATE]
                       [--vs_abs_cap VS_ABS_CAP] [--pmi_top_k PMI_TOP_K] [--pmi_min_count PMI_MIN_COUNT]
                       [--pmi_smoothing PMI_SMOOTHING] [--pmi_max_batches PMI_MAX_BATCHES]
                       [--vs_preview_k VS_PREVIEW_K] [--allow_negative_lambda] [--lambda_eta LAMBDA_ETA]
                       [--wilson_max_n WILSON_MAX_N] [--log_every LOG_EVERY] [--output_dir OUTPUT_DIR]
                       [--seed SEED] [--retain_weight RETAIN_WEIGHT] [--retain_broadcast]
                       [--preference_weight PREFERENCE_WEIGHT] [--pref_every PREF_EVERY]
                       [--pref_format PREF_FORMAT] [--pref_beta PREF_BETA] [--pref_margin PREF_MARGIN]
                       [--pref_max_len PREF_MAX_LEN]
run_etu_h200.py: error: unrecognized arguments: --span_masking --span_ngram_max 3
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
