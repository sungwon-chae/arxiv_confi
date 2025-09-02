(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget/data" \
  --retain_corpora "./datasets/bio-retain/bio-retain-corpus" \
  --batch_size 32 \
  --max_num_batches 500 \
  --num_epochs 2 \
  --layer_ids "6,7,8" \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --lora_r 128 \
  --epsilon 0.05 \
  --lambda_max 40.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 3 \
  --pmi_top_k 192 \
  --pmi_smoothing 1.0 \
  --pmi_max_batches 2000 \
  --vocab_top_k 300 \
  --vs_abs_cap 256 \
  --vs_freq_rate 0.02 \
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
🔧 사용자 지정 배치 크기 사용: 32 (heuristic=55)
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: single
   - batch_size: 32
   - batch_size_per_gpu: 8
   - frozen_on_cpu: False
   - lora_r: 128
   - lora_alpha: 512
   - max_num_batches: 500
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:07<00:00,  1.09it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 379.59it/s]
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
Data loading complete: 1 forget splits (2 batches), 1 retain splits (129 batches)
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=32
max_num_batches=500
frozen_on_cpu=False
epsilon=0.05
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
vs_freq_rate=0.02
vs_abs_cap=256
pmi_top_k=192
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
[PMI] split 0: used 2 batches (cap=2000)
[PMI] split 0: used 129 batches (cap=2000)
[V_S] 스톱리스트로 65개 토큰 제거됨
[V_S] token filter kept 127/192 (66.1%) after _filter_vs_tokens
V_S (PMI-refined) size: 127 tokens
Top PMI tokens preview: ['er', 'en', 'at', '▁the', 'al', 'ing', 'et', '▁and', 'ly', 'ation']
V_S size: 127 tokens (0.4% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.0640
[PMI] split 0: used 2 batches (cap=2000)
[PMI] split 0: used 129 batches (cap=2000)
[V_S DEBUG] |V_S|=127, π_base(S)≈0.0640, showing top 127 by PMI:
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
  id=   269  tok='en'          pmi=1.381     freq=7
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
  id=   263  tok='er'          pmi=0.492     freq=4
  id=  3881  tok='▁study'      pmi=0.472     freq=3
  id= 11739  tok='▁authors'    pmi=0.459     freq=13
  id=   602  tok='ang'         pmi=0.441     freq=4
  id= 28775  tok='q'           pmi=0.441     freq=3
  id=   270  tok='at'          pmi=0.416     freq=4
  id=  6345  tok='▁Bi'         pmi=0.410     freq=3
  id=   395  tok='▁with'       pmi=0.396     freq=10
  id=   601  tok='ated'        pmi=0.380     freq=3
  id= 11051  tok='▁Fund'       pmi=0.323     freq=3
  id=  1474  tok='▁number'     pmi=0.269     freq=5
  id=   477  tok='▁from'       pmi=0.258     freq=9
  id=   299  tok='et'          pmi=0.189     freq=6
  id=   362  tok='th'          pmi=0.153     freq=5
  id=  4775  tok='▁published'  pmi=0.104     freq=9
  id=  3260  tok='This'        pmi=0.100     freq=3
  id= 28718  tok='u'           pmi=0.100     freq=3
  id=   506  tok='▁have'       pmi=0.069     freq=4
  id=  2985  tok='▁Dr'         pmi=0.052     freq=4
  id=  4211  tok='▁section'    pmi=0.035     freq=3
  id=  4058  tok='▁review'     pmi=0.014     freq=3
  id= 14098  tok='▁publication'  pmi=0.004     freq=7
  id=   851  tok='▁This'       pmi=-0.036    freq=8
  id=   403  tok='▁was'        pmi=-0.045    freq=16
  id=   354  tok='▁for'        pmi=-0.099    freq=17
  id=  2432  tok='do'          pmi=-0.137    freq=3
  id=  3493  tok='▁original'   pmi=-0.145    freq=7
  id=  1014  tok='The'         pmi=-0.181    freq=8
  id=  1298  tok='▁Re'         pmi=-0.188    freq=3
  id=   272  tok='▁the'        pmi=-0.253    freq=74
  id=  5447  tok='▁article'    pmi=-0.263    freq=17
  id=   288  tok='ing'         pmi=-0.266    freq=8
  id=   282  tok='al'          pmi=-0.277    freq=4
  id=  2900  tok='▁University'  pmi=-0.283    freq=3
  id= 28709  tok='o'           pmi=-0.313    freq=3
  id=  1023  tok='▁should'     pmi=-0.342    freq=5
  id=   456  tok='▁this'       pmi=-0.392    freq=14
  id=   304  tok='▁and'        pmi=-0.418    freq=30
  id=  2118  tok='▁error'      pmi=-0.424    freq=5
  id=   352  tok='ation'       pmi=-0.615    freq=3
  id=  4714  tok='▁correct'    pmi=-0.625    freq=8
  id=   415  tok='▁The'        pmi=-0.691    freq=15
  id= 16390  tok='▁incorrect'  pmi=-0.732    freq=5
  id=  4527  tok='▁October'    pmi=-0.757    freq=3
  id= 20108  tok='▁Article'    pmi=-0.785    freq=3
  id= 27840  tok='▁corrected'  pmi=-0.812    freq=3
  id=  3227  tok='▁author'     pmi=-0.853    freq=5
  id=   346  tok='ly'          pmi=-0.856    freq=3
  id= 28710  tok='i'           pmi=-0.856    freq=14
  id=  2751  tok='▁version'    pmi=-0.927    freq=4
  id=   560  tok='▁In'         pmi=-0.961    freq=3
[V_S DEBUG] Top contributors by raw freq (approximation):
  '▁the'       freq=    74  cum%=10.18%
  '▁and'       freq=    30  cum%=14.31%
  '▁for'       freq=    17  cum%=16.64%
  '▁article'   freq=    17  cum%=18.98%
  '▁was'       freq=    16  cum%=21.18%
  '▁The'       freq=    15  cum%=23.25%
  '▁this'      freq=    14  cum%=25.17%
  'i'          freq=    14  cum%=27.10%
  '▁authors'   freq=    13  cum%=28.89%
  '▁with'      freq=    10  cum%=30.26%
  '▁that'      freq=     9  cum%=31.50%
  '▁from'      freq=     9  cum%=32.74%
  '▁No'        freq=     9  cum%=33.98%
  '▁published' freq=     9  cum%=35.21%
  'ing'        freq=     8  cum%=36.31%
  'ov'         freq=     8  cum%=37.41%
  '▁This'      freq=     8  cum%=38.51%
  'The'        freq=     8  cum%=39.61%
  'ics'        freq=     8  cum%=40.72%
  '▁correct'   freq=     8  cum%=41.82%
[V_S DEBUG] PMI batch usage: forget_used=2, retain_used=129
[V_S DEBUG] Full dump saved to models/zephyr-7b-beta_etu_debug/V_S.debug.json
[V_S DEBUG] TSV dump saved to models/zephyr-7b-beta_etu_debug/V_S.debug.tsv
[info] |V_S|/V = 0.4%, π_base(S)=0.0640, ε=0.0500
V_S preview: ['er', 'en', 'at', '▁the', 'al', 'ing', 'et', '▁and', 'ly', 'ation']
Initial λ: 0.2611 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/2 [00:00<?, ?it/s][HIGH] πθ(S)=0.0651 [95% normal 0.0536,0.0765 | Wilson↑ 0.0775] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.001465 | λ=0.261
[λ-update] EMA πθ(S)=0.0646 (controller=0.0770) → λ=0.261→0.261 | E[qλ(S)]=0.0500 | KL_EMA=0.0475
 50%|██████████████████                  | 1/2 [00:03<00:03,  3.12s/it, loss=0.00147, πθ(S)=0.065, λ=0.26][HIGH] πθ(S)=0.0632 [95% normal 0.0504,0.0760 | Wilson↑ 0.0722] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.001529 | λ=0.261
[λ-update] EMA πθ(S)=0.0636 (controller=0.0726) → λ=0.261→0.261 | E[qλ(S)]=0.0500 | KL_EMA=0.0985
100%|████████████████████████████████████| 2/2 [00:06<00:00,  3.26s/it, loss=0.00153, πθ(S)=0.063, λ=0.26]
======= Epoch 1 =======
  0%|                                                                               | 0/2 [00:00<?, ?it/s][HIGH] πθ(S)=0.0641 [95% normal 0.0527,0.0754 | Wilson↑ 0.0712] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.002565 | λ=0.261
[λ-update] EMA πθ(S)=0.0636 (controller=0.0707) → λ=0.261→0.261 | E[qλ(S)]=0.0500 | KL_EMA=0.1214
 50%|██████████████████                  | 1/2 [00:02<00:02,  2.80s/it, loss=0.00544, πθ(S)=0.064, λ=0.26][HIGH] πθ(S)=0.0619 [95% normal 0.0492,0.0746 | Wilson↑ 0.0681] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.002748 | λ=0.261
[λ-update] EMA πθ(S)=0.0633 (controller=0.0695) → λ=0.261→0.261 | E[qλ(S)]=0.0500 | KL_EMA=0.1191
100%|████████████████████████████████████| 2/2 [00:05<00:00,  2.92s/it, loss=0.00762, πθ(S)=0.062, λ=0.26]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.04
=== Results ===
  - π_base(S): 0.0640
  - π_θ(S): 0.0630
  - Suppression ratio: 0.98 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.0730
  - 95% upper π_θ(S): 0.0720
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.2611_2025-09-02-21-03-08/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.2611_2025-09-02-21-03-08/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.2611_2025-09-02-21-03-08
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.2611_2025-09-02-21-03-08/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.2611_2025-09-02-21-03-08/metrics.json
✅ ETU 실행 완료!
