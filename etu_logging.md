(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
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
✅ Success! cyber-forget-corpus: 1000 rows
First row: {'text': '#[1]alternate [2]alternate [3]alternate\n* [4]Our Services\n* [5]Knowledge Centre\n* [6]About\n* [7]Contact\n* [8]Our Services\n+ [9]Adversary Simulation\n+ [10]Application Security\n+ [11]P...
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|██████████████████████████████████████████████| 26.4M/26.4M [00:01<00:00, 15.5MB/s]
Generating train split: 100%|███████████████████████████████| 4473/4473 [00:00<00:00, 22491.47 examples/s]
✅ Success! cyber-retain-corpus: 4473 rows
First row: {'text': '#[1]Techie Delight » Feed [2]Techie Delight » Comments Feed [3]Techie\nDelight » Implement Diff Utility Comments Feed [4]alternate\n[5]alternate\n[6]Skip to content\n[7]Techie Delight\nAce y...
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 

