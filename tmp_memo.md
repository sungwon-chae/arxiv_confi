[λ-update] EMA πθ(S)=0.0292 (controller=0.0308) → λ=1.197→1.197 | E[qλ(S)]=0.0095 | KL_EMA=0.0231

100%|█████████▉| 602/603 [08:14<00:00,  1.23it/s, loss=0.0159, πθ(S)=0.036, λ=1.20] 
100%|██████████| 603/603 [08:14<00:00,  1.23it/s, loss=0.0159, πθ(S)=0.036, λ=1.20]
100%|██████████| 603/603 [08:14<00:00,  1.22it/s, loss=0.0159, πθ(S)=0.036, λ=1.20]
[HIGH] πθ(S)=0.0362 [95% normal 0.0000,0.0972 | Wilson↑ 0.0378] | E[qλ(S)]=0.0095 | ε=0.0200 | KL=0.01561 | λ=1.197
[λ-update] EMA πθ(S)=0.0297 (controller=0.0312) → λ=1.197→1.197 | E[qλ(S)]=0.0095 | KL_EMA=0.0240
=== ETU Suppression Report ===
  - Perplexity on retain: 2058.62
=== Results ===
  - π_base(S): 0.0341
  - π_θ(S): 0.0306
  - Suppression ratio: 0.90 (updated/base)
  - Target ε: 0.0200
  - Target achieved: ✗
  - 95% upper π_base(S): 0.0391
  - 95% upper π_θ(S): 0.0354
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-1.1975_2025-10-21-23-01-44/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-1.1975_2025-10-21-23-01-44/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-1.1975_2025-10-21-23-01-44
Saved args to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-1.1975_2025-10-21-23-01-44/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-1.1975_2025-10-21-23-01-44/metrics.json
✅ ETU 실행 완료!
