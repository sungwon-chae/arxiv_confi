cd ETU && \
head -50 "models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35/V_S.debug.tsv"

cd ETU && \
python3 -c "
import json, torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 모델 로드
model_path = 'models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0000_2025-09-02-20-27-35'
tokenizer = AutoTokenizer.from_pretrained('HuggingFaceH4/zephyr-7b-beta')
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map='auto')

# V_S 로드
with open(f'{model_path}/V_S.ids.json') as f:
    vs_ids = set(json.load(f))

# 간단한 프롬프트로 V_S 내 토큰 확률 확인
prompt = 'The research study focused on'
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits[0, -1, :]
    probs = torch.softmax(logits, dim=-1)

# V_S 내 토큰 중 상위 확률 순으로 출력
vs_probs = [(tid, probs[tid].item()) for tid in vs_ids if tid < len(probs)]
vs_probs.sort(key=lambda x: x[1], reverse=True)

print('V_S 내 토큰 확률 Top-20:')
for tid, prob in vs_probs[:20]:
    token = tokenizer.convert_ids_to_tokens(tid)
    print(f'{tid:>6} {token:>15} {prob:.6f}')
"
