완벽합니다! 🎯 브루트포스 V_S가 성공적으로 생성되었습니다.
📊 V_S 분석 결과
크기: 2000개 토큰 (forget 정답에서 추출)
핵심 토큰: ▁Mus, on, ▁El 등 Elon Musk 관련 토큰들이 상위에 위치
총 처리: 814개 forget 샘플, 17,787개 토큰, 3,142개 고유 토큰

🔍 π_base(S) 드라이런 실행
이제 π_base(S)를 먼저 측정해보겠습니다:

$ source /data/aiuser3/LLM_EvalPipeline_test/.venv/bin/activate && cd /data/aiuser3/ETU && CUDA_VISIBLE_DEVICES=7 python3 run_etu_h200.py \
  --forget_corpora "datasets/elude_etu/elon_musk/forget.jsonl" \
  --retain_weight 0.0 \
  --vocab_top_k 0 \
  --vs_abs_cap 0 \
  --epsilon 0.01 \
  --lambda_max 200.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.8 \
  --allow_negative_lambda \
  --pinsker_cap 0.10 \
  --lora_r 64 \
  --lora_alpha 256 \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --layer_ids "6,7,8" \
  --batch_size 16 \
  --gradient_accumulation_steps 2 \
  --max_num_batches 1000 \
  --num_epochs 1 \
  --mixed_precision bf16 \
  --log_every 10 \
  --verbose
