(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
import sys
sys.path.append('.')
from etu.utils import get_data

print('=== 단계별 데이터 확인 ===')

# 1. 원본 데이터셋 확인
from datasets import load_dataset
cyber_forget = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train')
bio_retain = load_dataset('cais/wmdp-corpora', 'bio-retain-corpus', split='train')

print(f'1. 원본 데이터:')
print(f'   Cyber-forget: {len(cyber_forget)} rows')
print(f'   Bio-retain: {len(bio_retain)} rows')

# 2. load_corpus 함수 직접 테스트
from etu.utils import load_corpus
cyber_data = load_corpus('cais/wmdp-corpora:cyber-forget-corpus')
bio_data = load_corpus('cais/wmdp-corpora:bio-retain-corpus')

print(f'\\n2. load_corpus 결과:')
print(f'   Cyber-forget: {len(cyber_data)} items')
print(f'   Bio-retain: {len(bio_data)} items')

# 3. to_batches 함수 직접 테스트
from etu.utils import to_batches
cyber_batches = to_batches(cyber_data)
bio_batches = to_batches(bio_data)

print(f'\\n3. to_batches 결과:')
print(f'   Cyber-forget: {len(cyber_batches)} batches')
for i, batch in enumerate(cyber_batches):
    print(f'     Batch {i}: {len(batch)} items')
print(f'   Bio-retain: {len(bio_batches)} batches')
for i, batch in enumerate(bio_batches):
    print(f'     Batch {i}: {len(batch)} items')
"
=== 단계별 데이터 확인 ===
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|████████████████████████████████████████████████| 222M/222M [00:15<00:00, 14.1MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 220M/220M [00:16<00:00, 13.3MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 222M/222M [00:12<00:00, 17.7MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 221M/221M [00:16<00:00, 13.8MB/s]
Generating train split: 100%|█████████████████████████████| 60887/60887 [00:05<00:00, 10758.13 examples/s]
1. 원본 데이터:
   Cyber-forget: 1000 rows
   Bio-retain: 60887 rows
Traceback (most recent call last):
  File "<string>", line 18, in <module>
ImportError: cannot import name 'load_corpus' from 'etu.utils' (/data/aiuser3/ETU/etu/utils.py)
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
