cd ETU && python -c "
import os
from datasets import load_dataset

# 토큰 설정
token = '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'

try:
    # bio-forget 데이터셋 로드
    ds = load_dataset('cais/wmdp-bio-forget-corpus', 
                     split='train', 
                     token=token,
                     cache_dir='./data_cache')
    print(f'✅ Success! Loaded {len(ds)} rows')
    print(f'Features: {ds.features}')
    if len(ds) > 0:
        print(f'First row preview: {str(ds[0])[:200]}...')
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
"
