아하 그 말이었구나 😆
“거기(폐쇄망) 들어가서 뭘 체크해서, 뭘 나한테 가져오면 이쪽 맥북에서 실험 설계/튜닝할 때 도움이 되냐” 그 질문인 거지.

그럼 아예 **“폐쇄망에서 한 번만 돌려보고 결과를 복붙해오면 좋은 체크리스트 + 스크립트”**로 정리해줄게.

⸻

1. 꼭 알고 오면 좋은 핵심 스펙들

(1) GPU 관련

이건 무조건:
	•	GPU 모델명 (A100 / H100 / V100 / L40 / RTX 등)
	•	GPU 개수
	•	각 GPU 메모리 용량 (GB)
	•	NVLink / PCIe 여부(있으면 좋음, 없으면 그냥 그렇구나)

→ 이 정보 있으면:
	•	한 번에 몇 개 prompt 넣을 수 있을지 (batch / max_new_tokens)
	•	Mixtral / Qwen-MoE 같은 거 몇 개까지 동시에 돌릴 수 있을지
	•	모델을 한 GPU에 얹을지, FSDP / tensor parallel 해야 할지 감 잡을 수 있음.

명령어 (폐쇄망에서):

nvidia-smi

여기 출력 전체를 그냥 복붙해서 보내주면 제일 좋아.

⸻

(2) CUDA / 드라이버 / PyTorch

DROP 실험에서 mixed precision, bfloat16 쓸 수 있는지가 중요해서:
	•	CUDA 버전
	•	NVIDIA Driver 버전
	•	PyTorch 버전
	•	torch.cuda.is_available() / torch.cuda.get_device_capability()
	•	bfloat16 지원 여부 (A100 이상이면 보통 됨)

파이썬 원라이너 (폐쇄망에서):

python - << 'EOF'
import torch, platform
print("Python:", platform.python_version())
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA device count:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print(f"[GPU {i}] name:", torch.cuda.get_device_name(i))
        print(f"[GPU {i}] capability:", torch.cuda.get_device_capability(i))
        print(f"[GPU {i}] total memory (GB):", round(torch.cuda.get_device_properties(i).total_memory / (1024**3), 2))
EOF

이 출력 전체 가져오면,
내가 **“여기선 bf16 써도 됨 / fp16만 써라 / 이 정도면 Mixtral 여러 개 가능/불가”**까지 구체적으로 말해줄 수 있음.

⸻

(3) CPU / RAM / 디스크

LLM은 GPU도 중요하지만:
	•	CPU 코어 수
	•	시스템 RAM (메모리)
	•	디스크 용량(남은 용량)

도 실험 돌리는 데 영향 있음.

파이썬으로 대충:

python - << 'EOF'
import psutil, shutil, platform
print("Machine:", platform.node(), platform.platform())
print("CPU cores (logical):", psutil.cpu_count())
print("RAM (GB):", round(psutil.virtual_memory().total / (1024**3), 2))
total, used, free = shutil.disk_usage(".")
print("Disk total (GB):", round(total / (1024**3), 2))
print("Disk free (GB):", round(free / (1024**3), 2))
EOF

이 정도만 알아도:
	•	결과 jsonl / 로그를 어느 정도 쌓을 수 있는지
	•	dataset을 한 번에 메모리에 올릴 수 있는지
	•	dataloader를 어떻게 짤지
대략 감 옴.

⸻

(4) 파이썬 / 라이브러리 버전

특히:
	•	Python 버전
	•	transformers
	•	accelerate (있으면)
	•	bitsandbytes (쓸 거면)
	•	datasets (MMLU 로드할 경우)

예:

python - << 'EOF'
import platform
print("Python:", platform.python_version())

def safe_import(name):
    try:
        m = __import__(name)
        print(f"{name}:", getattr(m, "__version__", "no __version__ attr"))
    except ImportError:
        print(f"{name}: NOT INSTALLED")

for pkg in ["torch", "transformers", "accelerate", "datasets", "bitsandbytes"]:
    safe_import(pkg)
EOF

결과 가져오면,
내가 너 코드베이스를 **그 버전에 맞춰서 수정해야 할 부분(예: generate 인자, device_map 동작, MoE 구조 등)**을 미리 예상할 수 있음.

⸻

(5) 모델/가중치 경로

폐쇄망이면 huggingface hub 접속이 안 될 가능성이 크니까:
	•	이미 올려둔 모델들 목록 (예: /mnt/models/mixtral-8x7b/, /models/qwen2-moe-14b/ 같은 거)
	•	그 경로 구조
	•	예:
	•	/models/mixtral-8x7b/
	•	config.json
	•	pytorch_model-*.bin or model.safetensors
	•	tokenizer.json, tokenizer.model 등

이걸 알아야:
	•	AutoModelForCausalLM.from_pretrained("/models/mixtral-8x7b") 이런 식으로 불러올지
	•	아니면 로컬에서 경로를 하드코딩해서 넘겨줄지

를 안정적으로 맞출 수 있음.

단순 ls 만으로도 좋아:

ls -R /models

출력 전체까지는 필요 없고,
“어떤 모델이 있고, 각 모델 디렉토리에 뭐 들어 있는지”만 텍스트로 적어와도 충분.

⸻

(6) 인터넷/네트워크 정책

이건 숫자가 아니라 정책 정보:
	•	인터넷 완전 차단인지,
	•	내부 PyPI mirror만 되는지,
	•	pip install이 가능한지 (사설 미러라도),
	•	외부 git clone 가능한지 불가한지.

→ 이걸 알아야:
	•	**“requirements.txt 넘겨줄지” vs “wheel 파일/zip을 만들어서 던져야 할지”
	•	HF 모델/데이터셋을 아예 로컬에 tar로 싸서 가져가야 하는지

를 결정할 수 있음.

이건 그냥 메모로:

예)
	•	외부 인터넷 완전 차단
	•	내부 PyPI mirror 있음 (URL: …)
	•	git clone 안 됨
	•	/home/$USER 아래에만 쓰기 권한 있음

이런 식으로 적어오면 돼.

⸻

2. “환경 진단 스크립트” 하나로 묶어줄까?

폐쇄망에서 아래 스크립트 하나 저장해서 실행하고,
출력만 텍스트로 가져오면 거의 내가 필요한 건 다 알 수 있음.

# env_probe.py 로 저장해서 실행해도 됨
python - << 'EOF'
import platform, shutil, psutil, json, os

report = {}

# Python
report["python"] = platform.python_version()
report["platform"] = platform.platform()
report["node"] = platform.node()

# CPU / RAM / Disk
report["cpu_cores_logical"] = psutil.cpu_count()
report["ram_gb"] = round(psutil.virtual_memory().total / (1024**3), 2)
total, used, free = shutil.disk_usage(".")
report["disk_total_gb"] = round(total / (1024**3), 2)
report["disk_free_gb"] = round(free / (1024**3), 2)

# GPU / Torch
try:
    import torch
    report["torch_version"] = torch.__version__
    report["cuda_available"] = torch.cuda.is_available()
    if torch.cuda.is_available():
        gpus = []
        for i in range(torch.cuda.device_count()):
            p = torch.cuda.get_device_properties(i)
            gpus.append({
                "index": i,
                "name": p.name,
                "total_memory_gb": round(p.total_memory / (1024**3), 2),
                "capability": list(p.major, p.minor) if hasattr(p, "major") else None,
            })
        report["gpus"] = gpus
except ImportError:
    report["torch_version"] = None
    report["cuda_available"] = False

# Key libs
def safe_import(name):
    try:
        m = __import__(name)
        return getattr(m, "__version__", "no __version__ attr")
    except ImportError:
        return None

for pkg in ["transformers", "accelerate", "datasets", "bitsandbytes"]:
    report[f"{pkg}_version"] = safe_import(pkg)

print(json.dumps(report, indent=2))
EOF

이거 출력 그대로 복붙해서 보내주면,
	•	어느 모델까지 무리 없이 올릴 수 있는지
	•	fp16 / bf16 / int8 어느 정도까지 가능한지
	•	batch & max_new_tokens 대략 얼마까지 잡을지
	•	experiment_runner 쪽에서 병렬도를 어떻게 잡을지

전부 현실적인 숫자로 같이 잡아줄 수 있음.

⸻

3. 내가 특히 보고 싶은 것만 요약해주면 베스트
	1.	nvidia-smi 출력
	2.	위 env_probe 결과 JSON
	3.	“폐쇄망에 이미 올라간 모델 디렉토리 구조”(대략 어떤 모델들 들어와 있는지)
	4.	인터넷/패키지 설치 정책(말로 요약)

이 네 개 정도만 가져오면,
이제부터는 진짜 “코드 튜닝 + 실험 설계”만 하면 되는 상태라고 보면 돼.

원하면 env_probe 결과 가져오면,
내가 거기에 맞춰서 experiment_runner의 batch/알파-grid/모델 수/병렬 전략 추천 세트까지 같이 짜줄게.
