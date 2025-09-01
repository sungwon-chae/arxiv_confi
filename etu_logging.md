(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
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
Downloading readme: 10.5kB [00:00, 35.4MB/s]
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|████████████████████████████████████████████████| 733k/733k [00:00<00:00, 1.38MB/s]
Downloading data: 100%|██████████████████████████████████████████████| 6.36M/6.36M [00:00<00:00, 9.25MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 657k/657k [00:00<00:00, 1.48MB/s]
❌ WikiText Error: Couldn't find file at https://huggingface.co/datasets/wikitext/resolve/b08601e04326c79dfdd32d625aee71d232d685c3/hf_cache/datasets/downloads/5e548f01091b2f01906ea7be35b8a1a6aa74842629dc550b7a02ca0821f1002d
Downloading readme: 7.62kB [00:00, 16.7MB/s]
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|██████████████████████████████████████████████| 14.5M/14.5M [00:02<00:00, 7.21MB/s]
Downloading data: 100%|██████████████████████████████████████████████| 1.82M/1.82M [00:00<00:00, 3.60MB/s]
❌ SQuAD Error: Couldn't find file at https://huggingface.co/datasets/squad/resolve/7b6d24c440a36b6815f21b70d25016731768db1f/hf_cache/datasets/downloads/95dd33f3715bbca0674ef4784114a00fc369050253efd3ad7d22c0c9ced6a49f
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
