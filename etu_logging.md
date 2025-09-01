(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
import sys
sys.path.append('.')
from etu.utils import get_data

try:
    forget_data, retain_data = get_data(
        ['cais/wmdp-corpora:cyber-forget-corpus'],
        ['cais/wmdp-corpora:bio-retain-corpus'],
        min_len=1,
        max_len=1000000,
        batch_size=4
    )
    print(f'Forget batches: {len(forget_data)}')
    print(f'Retain batches: {len(retain_data)}')
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
"
Forget batches: 1
Retain batches: 1
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
