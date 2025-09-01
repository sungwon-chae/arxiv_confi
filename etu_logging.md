python -c "
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
