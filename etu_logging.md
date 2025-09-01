python -c "
import os
from datasets import load_dataset

print(f'Token: {os.getenv(\"HUGGING_FACE_HUB_TOKEN\")}')
print(f'HF_HOME: {os.getenv(\"HF_HOME\")}')

try:
    ds = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train')
    print(f'✅ Success! {len(ds)} rows')
except Exception as e:
    print(f'❌ Error: {e}')
"
