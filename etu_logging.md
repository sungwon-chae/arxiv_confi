# 다른 접근 방식 시도
python -c "
from datasets import load_dataset

try:
    # 다른 config로 시도
    ds = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train', cache_dir='./hf_cache')
    print(f'✅ Success with hf_cache: {len(ds)} rows')
except Exception as e:
    print(f'❌ Error with hf_cache: {e}')
    
    try:
        # 기본 캐시로 시도
        ds = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train')
        print(f'✅ Success with default cache: {len(ds)} rows')
    except Exception as e2:
        print(f'❌ Error with default cache: {e2}')
"
