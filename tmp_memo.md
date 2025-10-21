(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget/data" \
  --retain_corpora "./datasets/bio-retain/bio-retain-corpus" \
  --batch_size 16 \
  --max_num_batches 500 \
  --num_epochs 2 \
  --layer_ids "6,7,8" \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --lora_r 128 \
  --epsilon 0.03 \
  --lambda_max 40.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 3 \
  --pmi_top_k 128 \
  --pmi_smoothing 1.0 \
  --pmi_max_batches 2000 \
  --vocab_top_k 300 \
  --vs_abs_cap 128 \
  --vs_freq_rate 0.0 \
  --span_masking \
  --span_ngram_max 4 \
  --retain_weight 0.1 \
  --wilson_max_n 10000 \
  --pinsker_cap 0.10 \
  --mixed_precision bf16 \
  --vs_debug \
  --vs_debug_topk 200 \
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
[batch heuristic] optimal=128, mem_clamp=55, final=55
🔧 사용자 지정 배치 크기 사용: 16 (heuristic=55)
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: single
   - batch_size: 16
   - batch_size_per_gpu: 8
   - frozen_on_cpu: False
   - lora_r: 128
   - lora_alpha: 512
   - max_num_batches: 500
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.23it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 382.58it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/bio-forget/data']
🔍 Retain 데이터셋: ['./datasets/bio-retain/bio-retain-corpus']
🔧 Final layer_ids: [6, 7, 8]
🔧 Final lora_target_modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj']
Processing corpus spec: './datasets/bio-forget/data'
Loading local dataset folder: ./datasets/bio-forget/data
Loading from actual path: ./datasets/bio-forget/data
Loaded 56 items from local dataset folder
Processing corpus spec: './datasets/bio-retain/bio-retain-corpus'
Loading local dataset folder: ./datasets/bio-retain/bio-retain-corpus
Loading from actual path: ./datasets/bio-retain/bio-retain-corpus
Loaded 4106 items from local dataset folder
Data loading complete: 1 forget splits (4 batches), 1 retain splits (257 batches)
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=16
max_num_batches=500
frozen_on_cpu=False
epsilon=0.03
lambda_max=40.0
lambda_update_freq=1
forget_corpora=./datasets/bio-forget/data
retain_corpora=./datasets/bio-retain/bio-retain-corpus
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
gradient_accumulation_steps=4
mixed_precision=bf16
trust_remote_code=False
lr=1e-05
num_epochs=2
min_len=10
max_len=512
layer_id=None
layer_ids=[6, 7, 8]
param_ids=None
name_keywords=q_proj,k_proj,v_proj,o_proj
module_str={model_name}.model.layers[{layer_id}]
use_lora=True
lora_r=128
lora_alpha=512
lora_dropout=0.1
lora_target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj']
use_pmi_vs=True
vocab_top_k=300
vs_freq_rate=0.0
vs_abs_cap=128
pmi_top_k=128
pmi_min_count=3
pmi_smoothing=1.0
pmi_max_batches=2000
vs_preview_k=10
vs_debug=True
vs_debug_topk=200
span_masking=True
span_ngram_max=4
allow_negative_lambda=False
lambda_eta=0.5
pinsker_cap=0.1
use_upper_for_lambda=True
wilson_max_n=10000
log_every=10
output_dir=
seed=None
retain_weight=0.1
retain_broadcast=False
preference_weight=0.0
pref_every=10
pref_format=dpo
pref_beta=0.1
pref_margin=0.1
pref_max_len=512
=====
/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/backends/__init__.py:46: UserWarning: Please use the new API settings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.backends.cudnn.allow_tf32 = True, allowTF32CuDNN() and allowTF32CuBLAS() will be deprecated after Pytorch 2.9. Please see https://pytorch.org/docs/main/notes/cuda.html#tensorfloat-32-tf32-on-ampere-and-later-devices (Triggered internally at /pytorch/aten/src/ATen/Context.cpp:80.)
  self.setter(val)
Applying LoRA for efficient parameter updates...
Applying LoRA to layers: [6, 7, 8]
trainable params: 10,223,616 || all params: 7,251,955,712 || trainable%: 0.1410
Building forbidden token set V_S...
[PMI] counting capped at 2000 batches per split
[PMI] split 0: used 4 batches (cap=2000)
[PMI] split 0: used 257 batches (cap=2000)
[V_S] 스톱리스트로 43개 토큰 제거됨
[V_S] token filter kept 85/128 (66.4%) after _filter_vs_tokens
V_S (PMI-refined) size: 85 tokens
Top PMI tokens preview: ['▁that', '▁with', '▁from', 'ans', '▁had', '▁they', 'ated', 'ang', '▁one', 'ov']
V_S size: 85 tokens (0.3% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.0295
[PMI] split 0: used 4 batches (cap=2000)
[PMI] split 0: used 257 batches (cap=2000)
[V_S DEBUG] |V_S|=85, π_base(S)≈0.0295, showing top 85 by PMI:
  id=  8807  tok='▁applicable'  pmi=4.129     freq=4
  id=  4504  tok='alle'        pmi=3.906     freq=3
  id=  8225  tok='▁Han'        pmi=3.906     freq=3
  id= 12936  tok='Volume'      pmi=3.906     freq=3
  id= 24606  tok='fé'          pmi=3.906     freq=3
  id= 15000  tok='▁approval'   pmi=3.619     freq=5
  id= 15134  tok='▁consent'    pmi=3.619     freq=5
  id=  6655  tok='chaft'       pmi=3.436     freq=4
  id=  7851  tok='ologie'      pmi=3.436     freq=4
  id=  6804  tok='rant'        pmi=3.213     freq=7
  id= 18952  tok='orsch'       pmi=3.213     freq=5
  id=   744  tok='▁part'       pmi=3.213     freq=3
  id=  1074  tok='ts'          pmi=3.213     freq=3
  id=  1377  tok='ces'         pmi=3.213     freq=3
  id=  5037  tok='eme'         pmi=3.213     freq=3
  id=  2601  tok='Not'         pmi=3.031     freq=4
  id=  3322  tok='sg'          pmi=3.031     freq=4
  id=  8204  tok='▁CD'         pmi=3.031     freq=4
  id=  1343  tok='▁De'         pmi=2.925     freq=5
  id=  7511  tok='▁eth'        pmi=2.808     freq=3
  id= 13242  tok='▁declare'    pmi=2.808     freq=3
  id=  1063  tok='ics'         pmi=2.771     freq=8
  id=  3069  tok='▁values'     pmi=2.743     freq=4
  id=  1165  tok='olog'        pmi=2.520     freq=4
  id= 17745  tok='▁Original'   pmi=2.520     freq=4
  id=  1126  tok='ins'         pmi=2.520     freq=6
  id=   828  tok='ev'          pmi=2.520     freq=3
  id= 10318  tok='▁conflict'   pmi=2.520     freq=3
  id= 10957  tok='CB'          pmi=2.520     freq=3
  id=   590  tok='▁they'       pmi=2.338     freq=4
  id=  7365  tok='▁obtained'   pmi=2.297     freq=3
  id=  7388  tok='▁Key'        pmi=2.297     freq=3
  id= 12043  tok='▁NS'         pmi=2.297     freq=3
  id=  2145  tok='▁interest'   pmi=2.184     freq=4
  id= 11304  tok='▁Centre'     pmi=2.184     freq=4
  id=   951  tok='ren'         pmi=2.115     freq=3
  id=  6242  tok='▁Gen'        pmi=2.050     freq=4
  id=  7379  tok='▁Text'       pmi=2.050     freq=4
  id=  8098  tok='▁Russian'    pmi=2.050     freq=4
  id=   640  tok='▁und'        pmi=1.960     freq=3
  id=  4826  tok='▁Fig'        pmi=1.827     freq=6
  id=  5745  tok='▁reported'   pmi=1.709     freq=3
  id=  7509  tok='iu'          pmi=1.709     freq=3
  id=   626  tok='ov'          pmi=1.673     freq=8
  id=  5157  tok='ya'          pmi=1.604     freq=3
  id=  7347  tok='▁Program'    pmi=1.565     freq=4
  id=   553  tok='▁had'        pmi=1.508     freq=3
  id=   849  tok='ik'          pmi=1.508     freq=3
  id= 11469  tok='▁Li'         pmi=1.508     freq=3
  id= 29000  tok='\xa0'        pmi=1.421     freq=6
  id=  5400  tok='▁Vol'        pmi=1.357     freq=4
  id=   509  tok='ans'         pmi=1.341     freq=3
  id=   624  tok='▁one'        pmi=1.341     freq=3
  id=  1770  tok='▁No'         pmi=1.296     freq=9
  id= 13154  tok='▁grant'      pmi=1.252     freq=8
  id=   771  tok='▁work'       pmi=1.198     freq=7
  id=  6615  tok='▁supported'  pmi=1.134     freq=5
  id= 28729  tok='k'           pmi=1.103     freq=7
  id=  3572  tok='elling'      pmi=1.073     freq=3
  id=  5248  tok='▁figure'     pmi=1.016     freq=3
  id=   969  tok='ung'         pmi=1.016     freq=5
  id=  4894  tok='▁shown'      pmi=0.962     freq=3
  id=  9323  tok='▁Science'    pmi=0.951     freq=4
  id=  4658  tok='▁included'   pmi=0.911     freq=3
  id= 13387  tok='▁equally'    pmi=0.871     freq=4
  id=  7982  tok='▁Research'   pmi=0.862     freq=7
  id=   707  tok='▁any'        pmi=0.862     freq=3
  id=   753  tok='ian'         pmi=0.834     freq=4
  id= 18746  tok='▁contributed'  pmi=0.834     freq=4
  id=   369  tok='▁that'       pmi=0.834     freq=9
  id=  5077  tok='▁China'      pmi=0.771     freq=3
  id=  2773  tok='ii'          pmi=0.762     freq=4
  id=  6377  tok='▁Health'     pmi=0.674     freq=5
  id=  3610  tok='▁National'   pmi=0.603     freq=4
  id= 15884  tok='▁apolog'     pmi=0.546     freq=4
  id=  3881  tok='▁study'      pmi=0.472     freq=3
  id= 11739  tok='▁authors'    pmi=0.459     freq=13
  id=   602  tok='ang'         pmi=0.441     freq=4
  id= 28775  tok='q'           pmi=0.441     freq=3
  id=  6345  tok='▁Bi'         pmi=0.410     freq=3
  id=   395  tok='▁with'       pmi=0.396     freq=10
  id=   601  tok='ated'        pmi=0.380     freq=3
  id= 11051  tok='▁Fund'       pmi=0.323     freq=3
  id=  1474  tok='▁number'     pmi=0.269     freq=5
  id=   477  tok='▁from'       pmi=0.258     freq=9
[V_S DEBUG] Top contributors by raw freq (approximation):
  '▁authors'   freq=    13  cum%= 3.50%
  '▁with'      freq=    10  cum%= 6.20%
  '▁that'      freq=     9  cum%= 8.63%
  '▁from'      freq=     9  cum%=11.05%
  '▁No'        freq=     9  cum%=13.48%
  'ov'         freq=     8  cum%=15.63%
  'ics'        freq=     8  cum%=17.79%
  '▁grant'     freq=     8  cum%=19.95%
  '▁work'      freq=     7  cum%=21.83%
  'rant'       freq=     7  cum%=23.72%
  '▁Research'  freq=     7  cum%=25.61%
  'k'          freq=     7  cum%=27.49%
  'ins'        freq=     6  cum%=29.11%
  '▁Fig'       freq=     6  cum%=30.73%
  '\xa0'       freq=     6  cum%=32.35%
  'ung'        freq=     5  cum%=33.69%
  '▁De'        freq=     5  cum%=35.04%
  '▁number'    freq=     5  cum%=36.39%
  '▁Health'    freq=     5  cum%=37.74%
  '▁supported' freq=     5  cum%=39.08%
[V_S DEBUG] PMI batch usage: forget_used=4, retain_used=257
[V_S DEBUG] Full dump saved to models/zephyr-7b-beta_etu_debug/V_S.debug.json
[V_S DEBUG] TSV dump saved to models/zephyr-7b-beta_etu_debug/V_S.debug.tsv
[info] |V_S|/V = 0.3%, π_base(S)=0.0295, ε=0.0300
V_S preview: ['▁that', '▁with', '▁from', 'ans', '▁had', '▁they', 'ated', 'ang', '▁one', 'ov']
Initial λ: 0.0000 → expected qλ(S)≈0.0295
======= Epoch 0 =======
  0%|                                                                               | 0/4 [00:00<?, ?it/s][HIGH] πθ(S)=0.0465 [95% normal 0.0330,0.0601 | Wilson↑ 0.0621] | E[qλ(S)]=0.0295 | ε=0.0300 | KL=1.685e-10 | λ=0.000
[λ-update] EMA πθ(S)=0.0380 (controller=0.0524) → λ=0.000→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.0000
 25%|█████████▌                            | 1/4 [00:02<00:07,  2.44s/it, loss=6e-07, πθ(S)=0.047, λ=0.50][NEAR] πθ(S)=0.0314 [95% normal 0.0197,0.0431 | Wilson↑ 0.0405] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.001957 | λ=0.500
[λ-update] EMA πθ(S)=0.0342 (controller=0.0437) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.0689
 50%|██████████████████                  | 2/4 [00:04<00:04,  2.32s/it, loss=0.00196, πθ(S)=0.031, λ=0.50][OK] πθ(S)=0.0214 [95% normal 0.0124,0.0303 | Wilson↑ 0.0274] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.002014 | λ=0.500
[λ-update] EMA πθ(S)=0.0313 (controller=0.0385) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.0999
 75%|███████████████████████████         | 3/4 [00:07<00:02,  2.35s/it, loss=0.00201, πθ(S)=0.021, λ=0.50][OK] πθ(S)=0.0188 [95% normal 0.0054,0.0321 | Wilson↑ 0.0241] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.002062 | λ=0.500
[λ-update] EMA πθ(S)=0.0292 (controller=0.0357) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.1262
100%|████████████████████████████████████| 4/4 [00:09<00:00,  2.47s/it, loss=0.00206, πθ(S)=0.019, λ=0.50]
======= Epoch 1 =======
  0%|                                                                               | 0/4 [00:00<?, ?it/s][HIGH] πθ(S)=0.0464 [95% normal 0.0329,0.0599 | Wilson↑ 0.0533] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.004027 | λ=0.500
[λ-update] EMA πθ(S)=0.0309 (controller=0.0367) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.1381
 25%|█████████                           | 1/4 [00:02<00:06,  2.25s/it, loss=0.00645, πθ(S)=0.046, λ=0.50][NEAR] πθ(S)=0.0307 [95% normal 0.0191,0.0423 | Wilson↑ 0.0359] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.002474 | λ=0.500
[λ-update] EMA πθ(S)=0.0307 (controller=0.0359) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.1434
 50%|██████████████████                  | 2/4 [00:04<00:04,  2.19s/it, loss=0.00458, πθ(S)=0.031, λ=0.50][OK] πθ(S)=0.0208 [95% normal 0.0119,0.0296 | Wilson↑ 0.0247] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.002376 | λ=0.500
[λ-update] EMA πθ(S)=0.0299 (controller=0.0345) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.1458
 75%|███████████████████████████         | 3/4 [00:06<00:02,  2.25s/it, loss=0.00584, πθ(S)=0.021, λ=0.50][OK] πθ(S)=0.0177 [95% normal 0.0047,0.0307 | Wilson↑ 0.0213] | E[qλ(S)]=0.0181 | ε=0.0300 | KL=0.002585 | λ=0.500
[λ-update] EMA πθ(S)=0.0290 (controller=0.0335) → λ=0.500→0.500 | E[qλ(S)]=0.0181 | KL_EMA=0.1423
100%|████████████████████████████████████| 4/4 [00:08<00:00,  2.14s/it, loss=0.00557, πθ(S)=0.018, λ=0.50]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.06
=== Results ===
  - π_base(S): 0.0295
  - π_θ(S): 0.0289
  - Suppression ratio: 0.98 (updated/base)
  - Target ε: 0.0300
  - Target achieved: ✓
  - 95% upper π_base(S): 0.0360
  - 95% upper π_θ(S): 0.0353
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.03_lambda-0.5000_2025-09-02-21-23-29/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.03_lambda-0.5000_2025-09-02-21-23-29/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.03_lambda-0.5000_2025-09-02-21-23-29
Saved args to models/zephyr-7b-beta_etu_epsilon-0.03_lambda-0.5000_2025-09-02-21-23-29/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.03_lambda-0.5000_2025-09-02-21-23-29/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
