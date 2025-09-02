(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 -c "
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
V_S size: 192
Top 50 tokens:
262     in
263     er
264     ▁a
269     en
270     at
272     ▁the
282     al
286     ed
288     ing
297     ▁in
298     ▁to
299     et
302     ▁of
304     ▁and
317     ▁e
318     ▁S
320     ▁T
330     ▁A
334     ▁C
346     ly
347     ▁be
349     ▁is
351     ▁M
352     ation
354     ▁for
362     th
365     ▁B
367     ▁P
369     ▁that
382     ▁H
384     ▁D
390     ▁as
393     ▁L
395     ▁with
396     ▁an
399     ▁R
401     ▁F
403     ▁was
413     ▁E
415     ▁The
418     ▁N
438     ▁at
442     ▁or
451     ▁O
456     ▁this
475     ▁J
477     ▁from
486     ▁by
500     ▁U
506     ▁have
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
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
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.23it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 377.94it/s]
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
epsilon=0.1
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
vs_freq_rate=0.03
vs_abs_cap=256
pmi_top_k=256
pmi_min_count=2
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
[V_S] token filter kept 249/256 (97.3%) after _filter_vs_tokens
V_S (PMI-refined) size: 249 tokens
Top PMI tokens preview: ['er', 'en', 'at', 'ent', 'ro', '▁re', 'ad', 'se', '▁de', '▁that']
V_S size: 249 tokens (0.8% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.0549
[PMI] split 0: used 2 batches (cap=2000)
[PMI] split 0: used 129 batches (cap=2000)
[V_S DEBUG] |V_S|=249, π_base(S)≈0.0549, showing top 200 by PMI:
  id= 28809  tok='’'           pmi=4.466     freq=6
  id= 28816  tok='–'           pmi=4.312     freq=5
  id=  8807  tok='▁applicable'  pmi=4.129     freq=4
  id=  4504  tok='alle'        pmi=3.906     freq=3
  id=  8225  tok='▁Han'        pmi=3.906     freq=3
  id= 12936  tok='Volume'      pmi=3.906     freq=3
  id= 24606  tok='fé'          pmi=3.906     freq=3
  id= 15000  tok='▁approval'   pmi=3.619     freq=5
  id= 15134  tok='▁consent'    pmi=3.619     freq=5
  id=   453  tok='urn'         pmi=3.619     freq=2
  id=   981  tok='▁“'          pmi=3.619     freq=2
  id=  1819  tok='▁week'       pmi=3.619     freq=2
  id=  3629  tok='▁further'    pmi=3.619     freq=2
  id=  4146  tok='berg'        pmi=3.619     freq=2
  id=  4609  tok='iance'       pmi=3.619     freq=2
  id=  5269  tok='▁Net'        pmi=3.619     freq=2
  id=  6684  tok='▁Mit'        pmi=3.619     freq=2
  id=  7238  tok='Ke'          pmi=3.619     freq=2
  id=  7445  tok='”.'          pmi=3.619     freq=2
  id=  8154  tok='▁spl'        pmi=3.619     freq=2
  id= 10952  tok='▁Unter'      pmi=3.619     freq=2
  id= 13744  tok='itzer'       pmi=3.619     freq=2
  id= 14092  tok='▁participate'  pmi=3.619     freq=2
  id= 15417  tok='▁Ré'         pmi=3.619     freq=2
  id= 15525  tok='utschen'     pmi=3.619     freq=2
  id= 16457  tok='NI'          pmi=3.619     freq=2
  id= 16788  tok='sent'        pmi=3.619     freq=2
  id= 19643  tok='Mail'        pmi=3.619     freq=2
  id= 20059  tok='▁Interest'   pmi=3.619     freq=2
  id= 23787  tok='BAD'         pmi=3.619     freq=2
  id= 25397  tok='zung'        pmi=3.619     freq=2
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
  id=   331  tok='se'          pmi=2.925     freq=2
  id=   856  tok='Con'         pmi=2.925     freq=2
  id=  1017  tok='OR'          pmi=2.925     freq=2
  id=  1252  tok='sk'          pmi=2.925     freq=2
  id=  1289  tok='▁à'          pmi=2.925     freq=2
  id=  2294  tok='lin'         pmi=2.925     freq=2
  id=  2538  tok='▁Pol'        pmi=2.925     freq=2
  id=  4395  tok='year'        pmi=2.925     freq=2
  id=  4692  tok='atur'        pmi=2.925     freq=2
  id=  6012  tok='ika'         pmi=2.925     freq=2
  id=  6235  tok='▁Prof'       pmi=2.925     freq=2
  id=  7368  tok='▁completed'  pmi=2.925     freq=2
  id=  8828  tok='▁fellow'     pmi=2.925     freq=2
  id=  8855  tok='ells'        pmi=2.925     freq=2
  id= 10007  tok='▁Conf'       pmi=2.925     freq=2
  id= 11270  tok='üt'          pmi=2.925     freq=2
  id= 13414  tok='▁committee'  pmi=2.925     freq=2
  id= 13822  tok='▁percentage'  pmi=2.925     freq=2
  id= 14247  tok='▁Ta'         pmi=2.925     freq=2
  id= 15284  tok='▁Ali'        pmi=2.925     freq=2
  id= 16083  tok='utsche'      pmi=2.925     freq=2
  id= 16584  tok='▁supplied'   pmi=2.925     freq=2
  id= 26324  tok='▁ethical'    pmi=2.925     freq=2
  id= 28211  tok='▁institutional'  pmi=2.925     freq=2
  id=  7511  tok='▁eth'        pmi=2.808     freq=3
  id= 13242  tok='▁declare'    pmi=2.808     freq=3
  id=  1063  tok='ics'         pmi=2.771     freq=8
  id=  3069  tok='▁values'     pmi=2.743     freq=4
  id= 18675  tok='▁©'          pmi=2.743     freq=4
  id=  1165  tok='olog'        pmi=2.520     freq=4
  id= 17745  tok='▁Original'   pmi=2.520     freq=4
  id=  1126  tok='ins'         pmi=2.520     freq=6
  id=   543  tok='▁la'         pmi=2.520     freq=3
  id=   828  tok='ev'          pmi=2.520     freq=3
  id= 10318  tok='▁conflict'   pmi=2.520     freq=3
  id= 10957  tok='CB'          pmi=2.520     freq=3
  id=  1594  tok='RO'          pmi=2.520     freq=2
  id=  2117  tok='ka'          pmi=2.520     freq=2
  id=  2396  tok='▁Univers'    pmi=2.520     freq=2
  id=  2995  tok='ias'         pmi=2.520     freq=2
  id=  4752  tok='ota'         pmi=2.520     freq=2
  id=  4798  tok='ko'          pmi=2.520     freq=2
  id=  6283  tok='ischer'      pmi=2.520     freq=2
  id=  7069  tok='▁materials'  pmi=2.520     freq=2
  id=  8423  tok='LA'          pmi=2.520     freq=2
  id= 12100  tok='▁ERR'        pmi=2.520     freq=2
  id= 18267  tok='▁Basic'      pmi=2.520     freq=2
  id= 26218  tok='▁grants'     pmi=2.520     freq=2
  id=   590  tok='▁they'       pmi=2.338     freq=4
  id=   613  tok='▁i'          pmi=2.297     freq=3
  id=  7365  tok='▁obtained'   pmi=2.297     freq=3
  id=  7388  tok='▁Key'        pmi=2.297     freq=3
  id= 12043  tok='▁NS'         pmi=2.297     freq=3
  id=   559  tok='▁her'        pmi=2.232     freq=2
  id=   985  tok='▁She'        pmi=2.232     freq=2
  id=  2223  tok='▁US'         pmi=2.232     freq=2
  id=  4171  tok='UM'          pmi=2.232     freq=2
  id=  4232  tok='DR'          pmi=2.232     freq=2
  id=  7775  tok='▁Kar'        pmi=2.232     freq=2
  id=  2145  tok='▁interest'   pmi=2.184     freq=4
  id= 11304  tok='▁Centre'     pmi=2.184     freq=4
  id=   951  tok='ren'         pmi=2.115     freq=3
  id=  6242  tok='▁Gen'        pmi=2.050     freq=4
  id=  7379  tok='▁Text'       pmi=2.050     freq=4
  id=  8098  tok='▁Russian'    pmi=2.050     freq=4
  id=  8348  tok='▁pp'         pmi=2.009     freq=5
  id=   494  tok='av'          pmi=2.009     freq=2
  id=   539  tok='ich'         pmi=2.009     freq=2
  id=  1029  tok='ash'         pmi=2.009     freq=2
  id=  1238  tok='ures'        pmi=2.009     freq=2
  id=  2403  tok='link'        pmi=2.009     freq=2
  id=  2500  tok='ification'   pmi=2.009     freq=2
  id=  3843  tok='OS'          pmi=2.009     freq=2
  id=  3874  tok='▁received'   pmi=2.009     freq=2
  id=  4885  tok='▁production'  pmi=2.009     freq=2
  id=   640  tok='▁und'        pmi=1.960     freq=3
  id=   708  tok='▁no'         pmi=1.945     freq=8
  id= 28790  tok='V'           pmi=1.827     freq=8
  id=  4826  tok='▁Fig'        pmi=1.827     freq=6
  id=   408  tok='▁r'          pmi=1.827     freq=2
  id=   891  tok='▁der'        pmi=1.827     freq=2
  id=  2285  tok='ks'          pmi=1.827     freq=2
  id=  2326  tok='▁With'       pmi=1.827     freq=2
  id=  2530  tok='▁After'      pmi=1.827     freq=2
  id=  2690  tok='▁Ed'         pmi=1.827     freq=2
  id=  9199  tok='▁Spring'     pmi=1.827     freq=2
  id= 19545  tok='itutes'      pmi=1.827     freq=2
  id=   500  tok='▁U'          pmi=1.709     freq=3
  id=  5745  tok='▁reported'   pmi=1.709     freq=3
  id=  7509  tok='iu'          pmi=1.709     freq=3
  id=   626  tok='ov'          pmi=1.673     freq=8
  id=   864  tok='ise'         pmi=1.673     freq=2
  id=  1512  tok='fe'          pmi=1.673     freq=2
  id=  1565  tok='▁open'       pmi=1.673     freq=2
  id=  3133  tok='▁Inst'       pmi=1.673     freq=2
  id=  3651  tok='▁Gl'         pmi=1.673     freq=2
  id=  6505  tok='▁Av'         pmi=1.673     freq=2
  id=  6707  tok='▁Chinese'    pmi=1.673     freq=2
  id=  8894  tok='▁cells'      pmi=1.673     freq=2
  id= 10340  tok='▁Development'  pmi=1.673     freq=2
  id= 13011  tok='ailability'  pmi=1.673     freq=2
  id= 28797  tok='é'           pmi=1.673     freq=2
  id=  5157  tok='ya'          pmi=1.604     freq=3
  id=  7347  tok='▁Program'    pmi=1.565     freq=4
  id=   695  tok='ory'         pmi=1.539     freq=2
  id=  1203  tok='▁trans'      pmi=1.539     freq=2
  id=  1685  tok='iter'        pmi=1.539     freq=2
  id=  2074  tok='AP'          pmi=1.539     freq=2
  id=  5836  tok='▁Service'    pmi=1.539     freq=2
  id=  9110  tok='ceived'      pmi=1.539     freq=2
  id= 28824  tok='Q'           pmi=1.539     freq=2
  id=   553  tok='▁had'        pmi=1.508     freq=3
  id=   849  tok='ik'          pmi=1.508     freq=3
  id= 11469  tok='▁Li'         pmi=1.508     freq=3
  id=   392  tok='ist'         pmi=1.421     freq=2
  id=   962  tok='AT'          pmi=1.421     freq=2
  id=  2678  tok='▁Reg'        pmi=1.421     freq=2
  id=  4212  tok='▁June'       pmi=1.421     freq=2
  id=  7759  tok='▁Project'    pmi=1.421     freq=2
  id= 10731  tok='▁Support'    pmi=1.421     freq=2
  id= 18463  tok='▁Study'      pmi=1.421     freq=2
  id= 19013  tok='▁Nature'     pmi=1.421     freq=2
  id=   269  tok='en'          pmi=1.381     freq=7
  id=  5400  tok='▁Vol'        pmi=1.357     freq=4
  id=   509  tok='ans'         pmi=1.341     freq=3
  id=   624  tok='▁one'        pmi=1.341     freq=3
  id=   622  tok='▁will'       pmi=1.316     freq=2
  id=   736  tok='▁there'      pmi=1.316     freq=2
  id=  1380  tok='ina'         pmi=1.316     freq=2
  id=  3519  tok='▁instead'    pmi=1.316     freq=2
  id=  4271  tok='▁Public'     pmi=1.316     freq=2
  id= 28550  tok='heng'        pmi=1.316     freq=2
  id=  1770  tok='▁No'         pmi=1.296     freq=9
  id= 13154  tok='▁grant'      pmi=1.252     freq=8
  id=   308  tok='ent'         pmi=1.221     freq=2
  id=  1010  tok='▁Ar'         pmi=1.221     freq=2
  id=  2735  tok='▁access'     pmi=1.221     freq=2
  id=  5004  tok='izes'        pmi=1.221     freq=2
  id= 28758  tok='L'           pmi=1.208     freq=6
  id=   771  tok='▁work'       pmi=1.198     freq=7
  id= 28777  tok='G'           pmi=1.162     freq=8
  id= 28814  tok='X'           pmi=1.134     freq=4
  id=  6615  tok='▁supported'  pmi=1.134     freq=5
  id=   596  tok='ens'         pmi=1.134     freq=2
  id=  6064  tok='▁Center'     pmi=1.134     freq=2
  id= 21568  tok='▁publisher'  pmi=1.134     freq=2
  id= 28729  tok='k'           pmi=1.103     freq=7
  id=   451  tok='▁O'          pmi=1.093     freq=5
  id=   442  tok='▁or'         pmi=1.073     freq=3
  id=  3572  tok='elling'      pmi=1.073     freq=3
  id= 28802  tok='Y'           pmi=1.073     freq=3
  id= 28828  tok='Z'           pmi=1.073     freq=3
  id=   463  tok='iz'          pmi=1.054     freq=2
  id=   491  tok='ak'          pmi=1.054     freq=2
  id=  4624  tok='▁January'    pmi=1.054     freq=2
  id=  6476  tok='▁Foundation'  pmi=1.054     freq=2
  id=   393  tok='▁L'          pmi=1.042     freq=12
[V_S DEBUG] Top contributors by raw freq (approximation):
  '▁authors'   freq=    13  cum%= 1.68%
  '▁L'         freq=    12  cum%= 3.24%
  '▁H'         freq=    10  cum%= 4.53%
  '▁at'        freq=    10  cum%= 5.83%
  '▁that'      freq=     9  cum%= 6.99%
  '▁No'        freq=     9  cum%= 8.16%
  'ov'         freq=     8  cum%= 9.20%
  '▁no'        freq=     8  cum%=10.23%
  'ics'        freq=     8  cum%=11.27%
  '▁grant'     freq=     8  cum%=12.31%
  'G'          freq=     8  cum%=13.34%
  'V'          freq=     8  cum%=14.38%
  'en'         freq=     7  cum%=15.28%
  '▁F'         freq=     7  cum%=16.19%
  '▁work'      freq=     7  cum%=17.10%
  'rant'       freq=     7  cum%=18.01%
  '▁Research'  freq=     7  cum%=18.91%
  'k'          freq=     7  cum%=19.82%
  'ins'        freq=     6  cum%=20.60%
  '▁Fig'       freq=     6  cum%=21.37%
[V_S DEBUG] PMI batch usage: forget_used=2, retain_used=129
[V_S DEBUG] Full dump saved to models/zephyr-7b-beta_etu_debug/V_S.debug.json
[V_S DEBUG] TSV dump saved to models/zephyr-7b-beta_etu_debug/V_S.debug.tsv
[info] |V_S|/V = 0.8%, π_base(S)=0.0549, ε=0.1000
V_S preview: ['er', 'en', 'at', 'ent', 'ro', '▁re', 'ad', 'se', '▁de', '▁that']
Initial λ: 0.0000 → expected qλ(S)≈0.0549
======= Epoch 0 =======
  0%|                                                                               | 0/2 [00:00<?, ?it/s][OK] πθ(S)=0.0652 [95% normal 0.0537,0.0766 | Wilson↑ 0.0776] | E[qλ(S)]=0.0549 | ε=0.1000 | KL=-2.359e-09 | λ=0.000
[λ-update] EMA πθ(S)=0.0601 (controller=0.0721) → λ=0.000→0.000 | E[qλ(S)]=0.0549 | KL_EMA=0.0000
 50%|█████████████████▌                 | 1/2 [00:03<00:03,  3.13s/it, loss=6.01e-07, πθ(S)=0.065, λ=0.00][OK] πθ(S)=0.0450 [95% normal 0.0341,0.0559 | Wilson↑ 0.0528] | E[qλ(S)]=0.0549 | ε=0.1000 | KL=-1.68e-09 | λ=0.000
[λ-update] EMA πθ(S)=0.0551 (controller=0.0636) → λ=0.000→0.000 | E[qλ(S)]=0.0549 | KL_EMA=0.0102
100%|███████████████████████████████████| 2/2 [00:06<00:00,  3.29s/it, loss=6.08e-07, πθ(S)=0.045, λ=0.00]
======= Epoch 1 =======
  0%|                                                                               | 0/2 [00:00<?, ?it/s][OK] πθ(S)=0.0652 [95% normal 0.0537,0.0766 | Wilson↑ 0.0724] | E[qλ(S)]=0.0549 | ε=0.1000 | KL=0.0003443 | λ=0.000
[λ-update] EMA πθ(S)=0.0568 (controller=0.0636) → λ=0.000→0.000 | E[qλ(S)]=0.0549 | KL_EMA=0.0148
 50%|██████████████████                  | 1/2 [00:02<00:02,  2.81s/it, loss=0.00234, πθ(S)=0.065, λ=0.00][OK] πθ(S)=0.0451 [95% normal 0.0341,0.0560 | Wilson↑ 0.0504] | E[qλ(S)]=0.0549 | ε=0.1000 | KL=0.0003461 | λ=0.000
[λ-update] EMA πθ(S)=0.0551 (controller=0.0610) → λ=0.000→0.000 | E[qλ(S)]=0.0549 | KL_EMA=0.0165
100%|████████████████████████████████████| 2/2 [00:05<00:00,  2.95s/it, loss=0.00272, πθ(S)=0.045, λ=0.00]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.04
=== Results ===
  - π_base(S): 0.0549
  - π_θ(S): 0.0551
  - Suppression ratio: 1.00 (updated/base)
  - Target ε: 0.1000
  - Target achieved: ✓
  - 95% upper π_base(S): 0.0634
  - 95% upper π_θ(S): 0.0635
  - Target achieved (95% upper): ✓
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35
Saved args to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
