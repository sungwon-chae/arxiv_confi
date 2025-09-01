python -c "
import sys
sys.path.append('.')
from etu.utils import get_data

forget_data, retain_data = get_data(
    ['cais/wmdp-corpora:cyber-forget-corpus'],
    ['cais/wmdp-corpora:bio-retain-corpus'],
    min_len=1,
    max_len=1000000,
    batch_size=4
)

print('=== Forget Data ===')
for i, batch in enumerate(forget_data):
    print(f'Batch {i}: {len(batch)} items')
    if batch:
        print(f'  First item length: {len(batch[0])}')
        print(f'  First item preview: {batch[0][:100]}...')

print('\\n=== Retain Data ===')
for i, batch in enumerate(retain_data):
    print(f'Batch {i}: {len(batch)} items')
    if batch:
        print(f'  First item length: {len(batch[0])}')
        print(f'  First item preview: {batch[0][:100]}...')
"
