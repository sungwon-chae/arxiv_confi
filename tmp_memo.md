[λ-update] EMA πθ(S)=0.0313 (controller=0.0329) → λ=0.947→0.947 | E[qλ(S)]=0.0122 | KL_EMA=0.0155

100%|█████████▉| 601/603 [07:51<00:01,  1.28it/s, loss=0.00102, πθ(S)=0.001, λ=0.95]
100%|█████████▉| 602/603 [07:51<00:00,  1.28it/s, loss=0.00102, πθ(S)=0.001, λ=0.95]
100%|█████████▉| 602/603 [07:51<00:00,  1.28it/s, loss=0.00167, πθ(S)=0.037, λ=0.95]
100%|██████████| 603/603 [07:51<00:00,  1.28it/s, loss=0.00167, πθ(S)=0.037, λ=0.95]
100%|██████████| 603/603 [07:51<00:00,  1.28it/s, loss=0.00167, πθ(S)=0.037, λ=0.95]
[OK] πθ(S)=0.0015 [95% normal 0.0000,0.0101 | Wilson↑ 0.0018] | E[qλ(S)]=0.0122 | ε=0.0200 | KL=0.000875 | λ=0.947
[λ-update] EMA πθ(S)=0.0301 (controller=0.0317) → λ=0.947→0.947 | E[qλ(S)]=0.0122 | KL_EMA=0.0154
[HIGH] πθ(S)=0.0367 [95% normal 0.0000,0.0982 | Wilson↑ 0.0384] | E[qλ(S)]=0.0122 | ε=0.0200 | KL=0.001464 | λ=0.947
[λ-update] EMA πθ(S)=0.0306 (controller=0.0322) → λ=0.947→0.947 | E[qλ(S)]=0.0122 | KL_EMA=0.0157
=== ETU Suppression Report ===
  - Perplexity on retain: 2037.75
=== Results ===
  - π_base(S): 0.0341
  - π_θ(S): 0.0316
  - Suppression ratio: 0.93 (updated/base)
  - Target ε: 0.0200
  - Target achieved: ✗
  - 95% upper π_base(S): 0.0391
  - 95% upper π_θ(S): 0.0365
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-0.9475_2025-10-21-22-39-02/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-0.9475_2025-10-21-22-39-02/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-0.9475_2025-10-21-22-39-02
Saved args to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-0.9475_2025-10-21-22-39-02/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.02_lambda-0.9475_2025-10-21-22-39-02/metrics.json
✅ ETU 실행 완료!
