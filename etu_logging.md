#!/usr/bin/env python3
"""
ETU H200 GPU 전용 실행 스크립트
NVIDIA H200 143GB VRAM 환경에 최적화
"""

import os
import sys
import torch
import argparse

# H200 GPU 환경 최적화
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"  # 디버깅용

# 8대 H200 GPU 환경 최적화 (run_etu_multi_h200.py에서 가져옴)
os.environ["NCCL_P2P_DISABLE"] = "0"
os.environ["NCCL_IB_DISABLE"] = "0"
os.environ["TORCH_NCCL_BLOCKING_WAIT"] = "1"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:256,expandable_segments:True"

def setup_h200_environment():
    """H200 GPU 환경 설정 및 검증"""
    print("🚀 H200 GPU 환경 설정 중...")
    
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA GPU를 찾을 수 없습니다.")
    
    gpu_count = torch.cuda.device_count()
    if gpu_count == 0:
        raise RuntimeError("사용 가능한 GPU가 없습니다.")
    
    # GPU 정보 출력
    for i in range(gpu_count):
        props = torch.cuda.get_device_properties(i)
        memory_gb = props.total_memory / 1024**3
        print(f"GPU {i}: {props.name} ({memory_gb:.1f} GB)")
    
    # H200 GPU 확인
    h200_gpus = []
    for i in range(gpu_count):
        if "H200" in torch.cuda.get_device_name(i):
            h200_gpus.append(i)
    
    if not h200_gpus:
        print("⚠️  H200 GPU를 찾을 수 없습니다. 일반 GPU 설정을 사용합니다.")
        return False
    
    print(f"✅ H200 GPU {len(h200_gpus)}개 감지됨")
    return True

def setup_multi_gpu_environment(strategy="ddp"):
    """멀티 GPU 환경 설정 (run_etu_multi_h200.py에서 가져옴)"""
    print(f"🔧 멀티 GPU 환경 설정: {strategy}")
    
    if strategy == "ddp":
        # Distributed Data Parallel
        os.environ["MASTER_ADDR"] = "localhost"
        os.environ["MASTER_PORT"] = "12355"
        os.environ["WORLD_SIZE"] = str(torch.cuda.device_count())
        os.environ["RANK"] = "0"
        
    elif strategy == "fsdp":
        # Fully Sharded Data Parallel
        os.environ["FSDP_CONFIG"] = "true"
        os.environ["FSDP_CPU_OFFLOAD"] = "false"
        
    elif strategy == "tensor_parallel":
        # Tensor Parallelism
        os.environ["TP_CONFIG"] = "true"
        os.environ["TP_SIZE"] = str(torch.cuda.device_count())
        
    print(f"✅ {strategy.upper()} 환경 설정 완료")

def get_dataset_mapping():
    """데이터셋 별칭을 실제 경로로 매핑"""
    return {
        # HuggingFace 경로
        "bio:forget": "cais/wmdp-bio-forget-corpus",
        "bio:retain": "cais/wmdp-corpora:bio-retain-corpus", 
        "cyber:forget": "cais/wmdp-corpora:cyber-forget-corpus",
        "cyber:retain": "cais/wmdp-corpora:cyber-retain-corpus",
        "wikitext": "wikitext",
        
        # 로컬 경로
        "local:cyber-forget": "./datasets/cyber-forget",
        "local:cyber-retain": "./datasets/cyber-retain",
        "local:bio-forget": "./datasets/bio-forget",
        "local:bio-retain": "./datasets/bio-retain",
        "local:wikitext": "./datasets/wikitext",
    }

def calculate_optimal_batch_size(model_name_or_path):
    """모델 크기에 따른 최적 배치 크기 계산 (run_etu_multi_h200.py에서 가져옴)"""
    gpu_count = torch.cuda.device_count()
    if gpu_count == 0:
        return 8  # 기본값
    
    # GPU 메모리 정보 수집
    device_memories = []
    for i in range(gpu_count):
        props = torch.cuda.get_device_properties(i)
        memory_gb = props.total_memory / 1024**3
        device_memories.append(memory_gb)
    
    total_gpu_memory = sum(device_memories)
    available_memory = total_gpu_memory * 0.8  # 80% 사용
    
    # 모델 크기별 최적 배치 크기
    if "70b" in model_name_or_path.lower():
        estimated_size = 70
        optimal_batch = 16   # 70B 모델
    elif "30b" in model_name_or_path.lower():
        estimated_size = 30
        optimal_batch = 32   # 30B 모델
    elif "13b" in model_name_or_path.lower():
        estimated_size = 13
        optimal_batch = 64   # 13B 모델
    elif "7b" in model_name_or_path.lower():
        estimated_size = 7
        optimal_batch = 128  # 7B 모델
    else:
        estimated_size = 7
        optimal_batch = 128  # 기본값
    
    # GPU 메모리 제약 고려
    memory_constrained_batch = int(available_memory / (estimated_size * 2))
    final_batch = min(optimal_batch, memory_constrained_batch)
    
    print(f"[batch heuristic] optimal={optimal_batch}, mem_clamp={memory_constrained_batch}, final={final_batch}")
    return final_batch

def resolve_dataset_paths(forget_corpora, retain_corpora):
    """데이터셋 별칭을 실제 경로로 변환"""
    mapping = get_dataset_mapping()
    
    def resolve_corpus(corpus):
        if corpus in mapping:
            return mapping[corpus]
        return corpus
    
    # 단일 문자열인 경우 리스트로 변환
    if isinstance(forget_corpora, str):
        if "," in forget_corpora:
            # 쉼표로 구분된 여러 데이터셋
            forget_paths = [resolve_corpus(c.strip()) for c in forget_corpora.split(",")]
        else:
            # 단일 데이터셋
            forget_paths = [resolve_corpus(forget_corpora.strip())]
    else:
        # 이미 리스트인 경우
        forget_paths = [resolve_corpus(c.strip()) for c in forget_corpora]
    
    if isinstance(retain_corpora, str):
        if "," in retain_corpora:
            # 쉼표로 구분된 여러 데이터셋
            retain_paths = [resolve_corpus(c.strip()) for c in retain_corpora.split(",")]
        else:
            # 단일 데이터셋
            retain_paths = [resolve_corpus(retain_corpora.strip())]
    else:
        # 이미 리스트인 경우
        retain_paths = [resolve_corpus(c.strip()) for c in retain_corpora]
    
    return forget_paths, retain_paths  # 리스트 반환

def get_h200_optimized_args():
    """H200 환경에 최적화된 기본 인자"""
    parser = argparse.ArgumentParser(description="ETU H200 GPU 최적화 실행")
    
    # GPU 선택 및 전략
    parser.add_argument("--gpu_id", type=int, default=0, 
                       help="사용할 GPU ID (기본값: 0)")
    parser.add_argument("--multi_gpu", action="store_true",
                       help="여러 GPU 사용 (병렬 처리)")
    parser.add_argument("--strategy", type=str, default="ddp",
                       choices=["ddp", "fsdp", "tensor_parallel"],
                       help="멀티 GPU 전략 (기본값: ddp)")
    parser.add_argument("--batch_size_per_gpu", type=int, default=8,
                       help="GPU당 배치 크기 (기본값: 8)")
    
    # H200 최적화 설정
    parser.add_argument("--batch_size", type=int, default=64,
                       help="배치 크기 (H200 권장: 64, 대규모 실험)")
    parser.add_argument("--max_num_batches", type=int, default=500,
                       help="최대 배치 수 (H200 권장: 500, 대규모 실험)")
    parser.add_argument("--frozen_on_cpu", action="store_true", default=False,
                       help="frozen 모델을 CPU에 (H200 메모리 넉넉하면 False 권장)")
    
    # LoRA 최적화
    parser.add_argument("--use_lora", action="store_true", default=True,
                       help="LoRA 사용 (H200 권장: true)")
    parser.add_argument("--lora_r", type=int, default=512,
                       help="LoRA rank (H200 권장: 512)")
    parser.add_argument("--lora_alpha", type=int, default=1024,
                       help="LoRA alpha (H200 권장: 1024)")
    
    # ETU 핵심 파라미터
    parser.add_argument("--epsilon", type=float, default=0.05,
                       help="억제 목표 ε (기본값: 0.05)")
    parser.add_argument("--lambda_max", type=float, default=30.0,
                       help="최대 λ 값 (기본값: 30.0, 강한 억제를 위해)")
    parser.add_argument("--lambda_update_freq", type=int, default=1,
                       help="λ 업데이트 빈도 (기본값: 1: 매 스텝)")
    
    # 데이터 설정
    parser.add_argument("--forget_corpora", type=str, 
                       default="./datasets/cyber-forget",
                       help="forget할 도메인 (별칭: bio:forget, cyber:forget, 또는 실제 경로)")
    parser.add_argument("--retain_corpora", type=str,
                       default="./datasets/bio-retain",
                       help="retain할 도메인 (별칭: bio:retain, cyber:retain, wikitext, 또는 실제 경로)")
    
    # 모델 설정
    parser.add_argument("--model_name_or_path", type=str,
                       default="HuggingFaceH4/zephyr-7b-beta",
                       help="사용할 모델")
    
    # 성능 최적화
    parser.add_argument("--deterministic", action="store_true",
                       help="결정적 실행 (성능 약간 하락)")
    parser.add_argument("--verbose", action="store_true", default=True,
                       help="상세 로깅")
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4,
                       help="그래디언트 누적 스텝 (기본값: 4)")
    parser.add_argument("--mixed_precision", type=str, default="bf16",
                       choices=["fp16", "bf16", "fp32"],
                       help="혼합 정밀도 (기본값: bf16)")
    parser.add_argument("--trust_remote_code", action="store_true",
                       help="원격 코드 신뢰 (대용량 모델용)")
    
    # 추가 ETU 인자들
    parser.add_argument("--lr", type=float, default=1e-5,
                       help="학습률 (기본값: 1e-5)")
    parser.add_argument("--num_epochs", type=int, default=3,
                       help="에포크 수 (기본값: 3, 수렴을 위해)")
    parser.add_argument("--min_len", type=int, default=10,
                       help="최소 시퀀스 길이 (기본값: 10)")
    parser.add_argument("--max_len", type=int, default=512,
                       help="최대 시퀀스 길이 (기본값: 512)")
    
    # LoRA 관련 인자들
    parser.add_argument("--layer_id", type=int, default=None,
                       help="단일 레이어 ID (지정 시 layer_ids를 대체)")
    parser.add_argument("--layer_ids", type=str, default="5,6,7",
                       help="쉼표로 구분된 레이어 IDs")
    parser.add_argument("--param_ids", type=str, default="",
                       help="LoRA 적용할 파라미터 ID (쉼표로 구분)")
    parser.add_argument("--name_keywords", type=str, default="q_proj,k_proj,v_proj,o_proj",
                       help="LoRA 적용할 모듈 이름 키워드 (기본값: q_proj,k_proj,v_proj,o_proj)")
    parser.add_argument("--module_str", type=str, default="{model_name}.model.layers[{layer_id}]",
                       help="LoRA 적용할 모듈 문자열 (기본값: {model_name}.model.layers[{layer_id}])")
    
    # LoRA options
    parser.add_argument("--use_lora", action=argparse.BooleanOptionalAction, default=True,
                       help="Use LoRA adapters (default: enabled). Use --no-use-lora to disable.")
    parser.add_argument("--lora_r", type=int, default=256, help="LoRA rank")
    parser.add_argument("--lora_alpha", type=int, default=512, help="LoRA scaling factor")
    parser.add_argument("--lora_dropout", type=float, default=0.1, help="LoRA dropout rate")
    parser.add_argument("--lora_target_modules", type=str, 
                       default="q_proj,k_proj,v_proj,o_proj", 
                       help="Target modules for LoRA (comma-separated)")
    
    # V_S 관련 인자들
    parser.add_argument("--use_pmi_vs", action="store_true", default=True,
                       help="PMI 기반 V_S 사용 (기본 True)")
    parser.add_argument("--vocab_top_k", type=int, default=1000,
                       help="V_S에 포함할 상위 토큰 수 (기본값: 1000)")
    parser.add_argument("--vs_freq_rate", type=float, default=0.1,
                       help="V_S 빈도 비율 (기본값: 0.1)")
    parser.add_argument("--vs_abs_cap", type=int, default=1000,
                       help="V_S 절대 상한 (기본값: 1000)")
    parser.add_argument("--pmi_top_k", type=int, default=1000,
                       help="PMI 상위 k 토큰 (기본값: 1000)")
    parser.add_argument("--pmi_min_count", type=int, default=10,
                       help="PMI 최소 카운트 (기본값: 10)")
    parser.add_argument("--pmi_smoothing", type=float, default=0.1,
                       help="PMI 스무딩 (기본값: 0.1)")
    parser.add_argument("--pmi_max_batches", type=int, default=500,
                       help="PMI 최대 배치 수 (기본값: 500, 대규모 실험)")
    parser.add_argument("--vs_preview_k", type=int, default=10,
                       help="V_S 미리보기 토큰 수 (기본값: 10)")
    
    # Span 마스킹 관련 인자들
    parser.add_argument("--span_masking", action="store_true", default=False,
                       help="V_S 토큰들의 n-gram 결합 보강 (기본값: False)")
    parser.add_argument("--span_ngram_max", type=int, default=3,
                       help="Span n-gram 최대 차수 (기본값: 3)")
    
    # Lambda 관련 인자들
    parser.add_argument("--allow_negative_lambda", action="store_true", default=False,
                       help="음수 lambda 허용")
    parser.add_argument("--lambda_eta", type=float, default=0.1,
                       help="Lambda 학습률 (기본값: 0.1)")
    parser.add_argument("--pinsker_cap", type=float, default=0.10,
                       help="Pinsker margin absolute cap (기본값: 0.10)")
    parser.add_argument("--use_upper_for_lambda", action=argparse.BooleanOptionalAction, default=True,
                       help="λ 제어에 Wilson 상한 사용(True) / EMA 사용(False)")
    
    # Wilson 관련 인자들
    parser.add_argument("--wilson_max_n", type=int, default=1000,
                       help="Wilson 최대 n (기본값: 1000)")
    
    # 로깅 관련 인자들
    parser.add_argument("--log_every", type=int, default=10,
                       help="로그 출력 빈도 (기본값: 10)")
    
    # 출력 관련 인자들
    parser.add_argument("--output_dir", type=str, default="",
                       help="출력 디렉토리")
    
    # 시드 설정
    parser.add_argument("--seed", type=int, default=None,
                       help="랜덤 시드")
    
    # Retain 관련 인자들
    parser.add_argument("--retain_weight", type=float, default=0.0,
                       help="Retain 가중치 (기본값: 0.0)")
    parser.add_argument("--retain_broadcast", action="store_true", default=False,
                       help="Retain 브로드캐스트")
    
    # Preference 관련 인자들
    parser.add_argument("--preference_weight", type=float, default=0.0,
                       help="Preference 가중치 (기본값: 0.0)")
    parser.add_argument("--pref_every", type=int, default=10,
                       help="Preference 업데이트 빈도 (기본값: 10)")
    parser.add_argument("--pref_format", type=str, default="dpo",
                       help="Preference 형식 (기본값: dpo)")
    parser.add_argument("--pref_beta", type=float, default=0.1,
                       help="Preference beta (기본값: 0.1)")
    parser.add_argument("--pref_margin", type=float, default=0.1,
                       help="Preference margin (기본값: 0.1)")
    parser.add_argument("--pref_max_len", type=int, default=512,
                       help="Preference 최대 길이 (기본값: 512)")
    
    return parser.parse_args()

def run_h200_optimized_etu():
    """H200 최적화된 ETU 실행"""
    try:
        # H200 환경 설정
        is_h200 = setup_h200_environment()
        
        # 인자 파싱
        args = get_h200_optimized_args()
        
        # 최적 배치 크기 계산 (모델 크기 기반)
        optimal_batch = calculate_optimal_batch_size(args.model_name_or_path)
        if args.batch_size == 64:  # 기본값인 경우에만 자동 조정
            args.batch_size = optimal_batch
            print(f"🔧 모델 크기 기반 최적 배치 크기: {optimal_batch}")
        else:
            print(f"🔧 사용자 지정 배치 크기 사용: {args.batch_size} (heuristic={optimal_batch})")
        
        # GPU 설정
        if args.multi_gpu:
            gpu_ids = list(range(torch.cuda.device_count()))
            os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(map(str, gpu_ids))
            print(f"🔄 멀티 GPU 모드: GPU {gpu_ids}")
            print("[note] --multi_gpu는 환경만 설정합니다. 실제 분산 실행은 torchrun으로 실행하세요. 예: \n"
                  "torchrun --nproc_per_node=<num_gpus> ETU/run_etu_h200.py --multi_gpu --strategy ddp ...")
            
            # 멀티 GPU 환경 설정
            setup_multi_gpu_environment(args.strategy)
        else:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
            print(f"🎯 단일 GPU 모드: GPU {args.gpu_id}")
        
        # H200 최적화 설정 적용
        if is_h200:
            print("🔧 H200 최적화 설정 적용:")
            strat = "ddp" if args.multi_gpu else "single"
            print(f"   - strategy: {strat}")
            print(f"   - batch_size: {args.batch_size}")
            print(f"   - batch_size_per_gpu: {args.batch_size_per_gpu}")
            print(f"   - frozen_on_cpu: {args.frozen_on_cpu}")
            print(f"   - lora_r: {args.lora_r}")
            print(f"   - lora_alpha: {args.lora_alpha}")
            print(f"   - max_num_batches: {args.max_num_batches}")
            print(f"   - mixed_precision: {args.mixed_precision}")
            print(f"   - gradient_accumulation_steps: {args.gradient_accumulation_steps}")
        
        # ETU 실행 - 올바른 방식으로 호출
        from etu.unlearn import run_etu
        from etu.utils import load_model, get_data
        
        print("🚀 ETU 실행 시작...")
        
        print("📥 모델 로딩 중...")
        # 서로 다른 인스턴스로 로드해야 함 (동일 참조 금지)
        frozen_model, tokenizer = load_model(
            args.model_name_or_path, train=False, infer_on_cpu=args.frozen_on_cpu
        )
        updated_model, _ = load_model(
            args.model_name_or_path, train=True, infer_on_cpu=False
        )
        if args.frozen_on_cpu:
            print("🔧 Frozen 모델을 CPU에 유지 (메모리 절약)")
        else:
            print("🔧 Frozen 모델을 GPU에 로드")
        
        # 데이터 로딩
        print("📊 데이터 로딩 중...")
        
        # 데이터셋 별칭 해결
        forget_paths, retain_paths = resolve_dataset_paths(
            args.forget_corpora, args.retain_corpora
        )
        print(f"🔍 Forget 데이터셋: {forget_paths}")
        print(f"🔍 Retain 데이터셋: {retain_paths}")
        
        # layer_ids를 layer_id와 동일하게 설정
        if args.layer_id is not None:
            args.layer_ids = str(args.layer_id)
            print(f"🔧 Layer 설정: layer_id={args.layer_id}, layer_ids={args.layer_ids}")
        
        # 문자열로 들어오면 리스트로 변환
        if isinstance(args.layer_ids, str):
            args.layer_ids = [int(x.strip()) for x in args.layer_ids.split(",") if x.strip()]
        
        if isinstance(args.lora_target_modules, str):
            args.lora_target_modules = [s.strip() for s in args.lora_target_modules.split(",") if s.strip()]
        
        print(f"🔧 Final layer_ids: {args.layer_ids}")
        print(f"🔧 Final lora_target_modules: {args.lora_target_modules}")
        
        # param_ids: nargs="+" 이므로 이미 List[int] 또는 None
        if args.param_ids is not None and len(args.param_ids) == 0:
            args.param_ids = None
        
        forget_data_list, retain_data_list = get_data(
            forget_paths,
            retain_paths,
            min_len=args.min_len,
            max_len=args.max_len,
            batch_size=args.batch_size,
        )
        
        # ETU 실행
        run_etu(
            updated_model,
            frozen_model,
            tokenizer,
            forget_data_list,
            retain_data_list,
            args,
        )
        
        print("✅ ETU 실행 완료!")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """메인 함수"""
    print("=== ETU H200 GPU 최적화 실행 ===")
    
    # H200 최적화된 ETU 실행
    run_h200_optimized_etu()

if __name__ == "__main__":
    main() 
