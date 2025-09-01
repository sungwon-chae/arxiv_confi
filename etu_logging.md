python -c "
from datasets import load_dataset

try:
    # cyber-forget-corpus 직접 로드
    ds = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train')
    print(f'✅ Success! cyber-forget-corpus: {len(ds)} rows')
    if len(ds) > 0:
        print(f'First row: {str(ds[0])[:200]}...')
except Exception as e:
    print(f'❌ Error loading cyber-forget-corpus: {e}')

try:
    # cyber-retain-corpus 직접 로드
    ds = load_dataset('cais/wmdp-corpora', 'cyber-retain-corpus', split='train')
    print(f'✅ Success! cyber-retain-corpus: {len(ds)} rows')
    if len(ds) > 0:
        print(f'First row: {str(ds[0])[:200]}...')
except Exception as e:
    print(f'❌ Error loading cyber-retain-corpus: {e}')
"
