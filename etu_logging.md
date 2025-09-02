cd ETU && python3 -c "
import os
from datasets import load_dataset
from huggingface_hub import HfApi

# 토큰 설정
token = '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'
os.environ['HUGGING_FACE_HUB_TOKEN'] = token

print('�� 토큰 설정 완료')

# 데이터셋 다운로드
datasets = [
    ('cais/wmdp-corpora', 'cyber-forget-corpus'),
    ('cais/wmdp-corpora', 'cyber-retain-corpus'),
    ('cais/wmdp-bio-forget-corpus', None),
    ('cais/wmdp-corpora', 'bio-retain-corpus'),
    ('wikitext', 'wikitext-2-raw-v1')
]

for name, config in datasets:
    try:
        if config:
            ds = load_dataset(name, config, split='train', cache_dir='./datasets')
        else:
            ds = load_dataset(name, split='train', cache_dir='./datasets')
        print(f'✅ {name}:{config or \"\"} - {len(ds)}개')
    except Exception as e:
        print(f'❌ {name}:{config or \"\"} - {e}')
"
