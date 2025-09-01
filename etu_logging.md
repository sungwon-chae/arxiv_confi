# Python에서 직접 데이터셋 접근 테스트
python -c "
from datasets import load_dataset
try:
    ds = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train')
    print(f'Cyber-forget: {len(ds)} rows')
    if len(ds) > 0:
        print(f'First row: {ds[0]}')
except Exception as e:
    print(f'Error: {e}')
"
