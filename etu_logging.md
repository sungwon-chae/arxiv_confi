# 다른 공개 데이터셋으로 테스트
python -c "
from datasets import load_dataset

try:
    # WikiText로 테스트
    ds = load_dataset('wikitext', 'wikitext-2-raw-v1', split='test')
    print(f'✅ WikiText Success: {len(ds)} rows')
except Exception as e:
    print(f'❌ WikiText Error: {e}')

try:
    # 다른 간단한 데이터셋으로 테스트
    ds = load_dataset('squad', split='train')
    print(f'✅ SQuAD Success: {len(ds)} rows')
except Exception as e:
    print(f'❌ SQuAD Error: {e}')
"
