(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
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
Token: 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
HF_HOME: ./hf_cache
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|██████████████████████████████████████████████| 10.8M/10.8M [00:00<00:00, 12.5MB/s]
❌ Error: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-corpora/resolve/daf89fa9b618b63a624228061a9cebacca88009c/hf_cache/datasets/downloads/11a09952dddc72c6cb31feace763612a199bb022c59ea5d6674c4bc51930c09f
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
