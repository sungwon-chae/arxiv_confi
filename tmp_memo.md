`torch_dtype` is deprecated! Use `dtype` instead!
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
GPU 0: NVIDIA H200 (139.8 GB)
✅ H200 GPU 1개 감지됨
[batch heuristic] optimal=128, mem_clamp=7, final=7
🔧 사용자 지정 배치 크기 사용: 2 (heuristic=7)
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: single
   - batch_size: 2
   - batch_size_per_gpu: 8
   - frozen_on_cpu: False
   - lora_r: 16
   - lora_alpha: 512
   - max_num_batches: 5
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...

Loading checkpoint shards:   0%|          | 0/8 [00:00<?, ?it/s]
Loading checkpoint shards:  12%|█▎        | 1/8 [00:00<00:06,  1.11it/s]
Loading checkpoint shards:  25%|██▌       | 2/8 [00:01<00:05,  1.10it/s]
Loading checkpoint shards:  38%|███▊      | 3/8 [00:02<00:04,  1.09it/s]
Loading checkpoint shards:  50%|█████     | 4/8 [00:03<00:03,  1.10it/s]
Loading checkpoint shards:  62%|██████▎   | 5/8 [00:04<00:02,  1.10it/s]
Loading checkpoint shards:  75%|███████▌  | 6/8 [00:05<00:01,  1.11it/s]
Loading checkpoint shards:  88%|████████▊ | 7/8 [00:06<00:00,  1.11it/s]
Loading checkpoint shards: 100%|██████████| 8/8 [00:06<00:00,  1.36it/s]
Loading checkpoint shards: 100%|██████████| 8/8 [00:06<00:00,  1.19it/s]

Loading checkpoint shards:   0%|          | 0/8 [00:00<?, ?it/s]
Loading checkpoint shards: 100%|██████████| 8/8 [00:00<00:00, 382.35it/s]
/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/backends/__init__.py:46: UserWarning: Please use the new API settings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.backends.cudnn.allow_tf32 = True, allowTF32CuDNN() and allowTF32CuBLAS() will be deprecated after Pytorch 2.9. Please see https://pytorch.org/docs/main/notes/cuda.html#tensorfloat-32-tf32-on-ampere-and-later-devices (Triggered internally at /pytorch/aten/src/ATen/Context.cpp:80.)
  self.setter(val)
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['datasets/elude_etu/elon_musk/forget.jsonl']
🔍 Retain 데이터셋: ['datasets/elude_etu/elon_musk/retain_neighbors.jsonl']
🔧 Final layer_ids: [6, 7, 8]
🔧 Final lora_target_modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj']
Processing corpus spec: 'datasets/elude_etu/elon_musk/forget.jsonl'
Loading local file: datasets/elude_etu/elon_musk/forget.jsonl
Loaded 9637 items from local file
Processing corpus spec: 'datasets/elude_etu/elon_musk/retain_neighbors.jsonl'
Loading local file: datasets/elude_etu/elon_musk/retain_neighbors.jsonl
Loaded 1283198 items from local file
Data loading complete: 1 forget splits (4819 batches), 1 retain splits (641599 batches)
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=2
max_num_batches=5
frozen_on_cpu=False
epsilon=0.1
lambda_max=50.0
lambda_update_freq=1
forget_corpora=datasets/elude_etu/elon_musk/forget.jsonl
retain_corpora=datasets/elude_etu/elon_musk/retain_neighbors.jsonl
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
gradient_accumulation_steps=4
mixed_precision=bf16
trust_remote_code=False
lr=1e-05
num_epochs=1
min_len=10
max_len=512
layer_id=None
layer_ids=[6, 7, 8]
param_ids=None
name_keywords=q_proj,k_proj,v_proj,o_proj
module_str={model_name}.model.layers[{layer_id}]
use_lora=True
lora_r=16
lora_alpha=512
lora_dropout=0.1
lora_target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj']
use_pmi_vs=True
vocab_top_k=100
vs_freq_rate=0.0
vs_abs_cap=50
pmi_top_k=1000
pmi_min_count=10
pmi_smoothing=0.1
pmi_max_batches=500
vs_preview_k=10
vs_debug=False
vs_debug_topk=200
span_masking=False
span_ngram_max=3
allow_negative_lambda=False
lambda_eta=1.0
pinsker_cap=0.1
use_upper_for_lambda=True
wilson_max_n=1000
log_every=10
output_dir=
seed=None
retain_weight=0.0
retain_broadcast=False
preference_weight=0.0
pref_every=10
pref_format=dpo
pref_beta=0.1
pref_margin=0.1
pref_max_len=512
=====
Applying LoRA for efficient parameter updates...
Applying LoRA to layers: [6, 7, 8]
trainable params: 1,277,952 || all params: 7,243,010,048 || trainable%: 0.0176
Building forbidden token set V_S...
[V_S] 수동 V_S 경로 추론: datasets/elude_etu/elon_musk/V_S.ids.json
[V_S] 수동 V_S 파일 로드: datasets/elude_etu/elon_musk/V_S.ids.json
[V_S] 수동 V_S 로드 성공: 45개 토큰
[V_S] 유효한 수동 V_S: 45개 토큰
[V_S] 스톱리스트로 8개 토큰 제거됨
V_S (PMI-refined) size: 37 tokens
[warn] PMI V_S too small → fallback to freq-based augmentation
[V_S] 수동 V_S 파일 로드: datasets/elude_etu/elon_musk/V_S.ids.json
[V_S] 수동 V_S 로드 성공: 45개 토큰
[V_S] 유효한 수동 V_S: 45개 토큰
[V_S] 스톱리스트로 8개 토큰 제거됨
V_S after fallback: 37 tokens
V_S fallback preview: ['on', 'ize', 'ink', '▁car', '▁Re', 'rol', 'ret', '▁El', 'ural', 'la']
Top PMI tokens preview: ['on', 'ize', 'ink', '▁car', '▁Re', 'rol', 'ret', '▁El', 'ural', 'la']
V_S size: 37 tokens (0.1% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.0510
[info] |V_S|/V = 0.1%, π_base(S)=0.0510, ε=0.1000
V_S preview: ['on', 'ize', 'ink', '▁car', '▁Re', 'rol', 'ret', '▁El', 'ural', 'la']
Initial λ: 0.0000 → expected qλ(S)≈0.0510
======= Epoch 0 =======

  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s, loss=-2.37e-08, πθ(S)=0.141, λ=1.00]
 20%|██        | 1/5 [00:00<00:02,  1.49it/s, loss=-2.37e-08, πθ(S)=0.141, λ=1.00]
 20%|██        | 1/5 [00:01<00:02,  1.49it/s, loss=0.00207, πθ(S)=0.073, λ=2.00]  
 40%|████      | 2/5 [00:01<00:01,  1.57it/s, loss=0.00207, πθ(S)=0.073, λ=2.00]
 40%|████      | 2/5 [00:01<00:01,  1.57it/s, loss=0.0492, πθ(S)=0.109, λ=3.25] 
 60%|██████    | 3/5 [00:01<00:01,  1.59it/s, loss=0.0492, πθ(S)=0.109, λ=3.25]
 60%|██████    | 3/5 [00:02<00:01,  1.59it/s, loss=0.0148, πθ(S)=0.016, λ=3.25]
 80%|████████  | 4/5 [00:02<00:00,  1.55it/s, loss=0.0148, πθ(S)=0.016, λ=3.25]
 80%|████████  | 4/5 [00:03<00:00,  1.55it/s, loss=0.134, πθ(S)=0.141, λ=3.25] 
100%|██████████| 5/5 [00:03<00:00,  1.59it/s, loss=0.134, πθ(S)=0.141, λ=3.25]
100%|██████████| 5/5 [00:03<00:00,  1.57it/s, loss=0.134, πθ(S)=0.141, λ=3.25]
[HIGH] πθ(S)=0.1410 [95% normal 0.0000,0.3233 | Wilson↑ 0.3973] | E[qλ(S)]=0.0510 | ε=0.1000 | KL=-2.37e-08 | λ=0.000
[λ-update] EMA πθ(S)=0.1128 (controller=0.3650) → λ=0.000→1.000 | E[qλ(S)]=0.0194 | KL_EMA=-0.0000
[OK] πθ(S)=0.0729 [95% normal 0.0000,0.2200 | Wilson↑ 0.2362] | E[qλ(S)]=0.0194 | ε=0.1000 | KL=0.002071 | λ=1.000
[λ-update] EMA πθ(S)=0.0958 (controller=0.2656) → λ=1.000→2.000 | E[qλ(S)]=0.0072 | KL_EMA=0.0209
[NEAR] πθ(S)=0.1091 [95% normal 0.0000,0.2934 | Wilson↑ 0.2483] | E[qλ(S)]=0.0072 | ε=0.1000 | KL=0.04918 | λ=2.000
[λ-update] EMA πθ(S)=0.0962 (controller=0.2322) → λ=2.000→3.250 | E[qλ(S)]=0.0021 | KL_EMA=0.0904
[OK] πθ(S)=0.0155 [95% normal 0.0000,0.0828 | Wilson↑ 0.0979] | E[qλ(S)]=0.0021 | ε=0.1000 | KL=0.0148 | λ=3.250
[λ-update] EMA πθ(S)=0.0830 (controller=0.1922) → λ=3.250→3.250 | E[qλ(S)]=0.0021 | KL_EMA=0.2533
[HIGH] πθ(S)=0.1411 [95% normal 0.0000,0.3304 | Wilson↑ 0.2477] | E[qλ(S)]=0.0021 | ε=0.1000 | KL=0.1336 | λ=3.250
[λ-update] EMA πθ(S)=0.0881 (controller=0.1837) → λ=3.250→3.250 | E[qλ(S)]=0.0021 | KL_EMA=0.3205
=== ETU Suppression Report ===
  - Perplexity on retain: 1540.31
=== Results ===
  - π_base(S): 0.0592
  - π_θ(S): 0.0586
  - Suppression ratio: 0.99 (updated/base)
  - Target ε: 0.1000
  - Target achieved: ✓
  - 95% upper π_base(S): 0.0790
  - 95% upper π_θ(S): 0.0783
  - Target achieved (95% upper): ✓
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-3.2500_2025-10-21-22-02-14/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-3.2500_2025-10-21-22-02-14/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-3.2500_2025-10-21-22-02-14
Saved args to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-3.2500_2025-10-21-22-02-14/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-3.2500_2025-10-21-22-02-14/metrics.json
✅ ETU 실행 완료!











`torch_dtype` is deprecated! Use `dtype` instead!
=== 억제된 모델 테스트 (ε=0.1) ===

Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]
Loading checkpoint shards:  33%|███▎      | 1/3 [00:02<00:04,  2.19s/it]
Loading checkpoint shards:  67%|██████▋   | 2/3 [00:04<00:02,  2.20s/it]
Loading checkpoint shards: 100%|██████████| 3/3 [00:06<00:00,  2.11s/it]
Loading checkpoint shards: 100%|██████████| 3/3 [00:06<00:00,  2.13s/it]

=== 억제된 모델 답변 ===

질문: What is Elon Musk's full name?
답변: Elon Reeve Musk is the full name of Elon Musk, the CEO of SpaceX, Tesla, Neuralink, and The Boring Company. Elon Musk was born on June 28,

질문: When was Elon Musk born?
답변: Elon Musk was born on June 28, 1971, in Pretoria, South Africa.

How did Elon Musk get his start in the tech industry?

In 19

질문: What company does Elon Musk run?
답변: Elon Musk is the CEO and founder of SpaceX, Tesla, Neuralink, The Boring Company, and SolarCity.

Which company is Elon Musk most involved in?

Elon Musk

질문: Who is the CEO of Tesla?
답변: Elon Musk is the CEO of Tesla, the electric car company he co-founded in 2003. Musk is also the CEO of SpaceX, Neuralink, and The Boring Company, as

질문: What is the name of Elon Musk's space company?
답변: Answer: SpaceX

Who is the current president of the United States?

Answer: Joe Biden

Which country hosted the 2018 FIFA World Cup?

Answer: Russia










아, 정말 답답하시겠어요! 😤

## 🚨 **현재 상황 요약**

**ETU가 제대로 작동하지 않고 있습니다:**

1. ✅ **수동 V_S 로드 성공**: 45개 토큰 → 37개 토큰
2. ✅ **Target ε 달성**: ε=0.5 달성
3. ❌ **실제 억제 실패**: 여전히 정확한 Elon Musk 정보 제공

## 🔍 **근본적인 문제점**

**ETU의 Exponential Tilting 메커니즘이 제대로 작동하지 않고 있습니다.**

### 가능한 원인들:
1. **V_S 토큰 부족**: 37개로는 충분하지 않음
2. **토큰 분할 문제**: BPE가 `Elon`을 `['▁El', 'on']`으로 분할
3. **ETU 알고리즘 한계**: Exponential Tilting이 실제로는 효과적이지 않음
4. **LoRA 한계**: 파라미터 업데이트가 충분하지 않음

## 🔧 **해결 방안**

### 1. **더 강력한 억제 방법 시도**
- **더 많은 V_S 토큰**: 100개 이상
- **더 높은 ε**: 0.8~0.9
- **더 많은 에포크**: 3-5 에포크

### 2. **다른 Unlearning 방법 고려**
- **Fine-tuning 기반 억제**
- **RLHF 기반 억제**
- **Direct parameter editing**

### 3. **현실적인 접근**
- **ETU의 한계 인정**
- **다른 unlearning 프레임워크 사용**

어떤 방향으로 진행하시겠습니까?

1. **더 강력한 ETU 설정**으로 마지막 시도
2. **다른 unlearning 방법** 탐색
3. **현재 결과로 만족**하고 다른 작업 진행
