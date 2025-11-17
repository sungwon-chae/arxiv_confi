#!/usr/bin/env python3
"""
ETU 기본 실행 스크립트 (H200 GPU 최적화)
"""

import os
import sys
import torch

# H200 GPU 환경 최적화
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 단일 GPU 사용 (안전)
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # 토크나이저 병렬화 비활성화

def main():
    print("=== ETU H200 GPU 최적화 실행 ===")
    
    # GPU 환경 확인
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        current_device = torch.cuda.current_device()
        device_name = torch.cuda.get_device_name(current_device)
        memory_gb = torch.cuda.get_device_properties(current_device).total_memory / 1024**3
        
        print(f"✅ GPU 환경 감지: {device_name}")
        print(f"   GPU 개수: {gpu_count}")
        print(f"   현재 GPU: {current_device}")
        print(f"   메모리: {memory_gb:.1f} GB")
        
        # H200 환경 최적화 권장사항
        if "H200" in device_name:
            print("🚀 H200 GPU 감지! 최적화된 설정을 사용합니다.")
            print("   - batch_size: 8 (권장)")
            print("   - frozen_on_cpu: false (GPU 메모리 여유)")
            print("   - lora_r: 512 (높은 성능)")
        else:
            print("⚠️  H200이 아닌 GPU입니다. 보수적인 설정을 사용합니다.")
    else:
        print("❌ CUDA GPU를 찾을 수 없습니다.")
        return
    
    try:
        from etu.unlearn import run_etu, get_args
        
        # H200 최적화된 기본 인자
        args = get_args()
        
        # H200 환경에 맞는 기본값 오버라이드
        if "H200" in device_name:
            args.batch_size = 8
            args.frozen_on_cpu = False
            args.lora_r = 512
            args.lora_alpha = 1024
            args.max_num_batches = 100
            print("🔧 H200 최적화 설정 적용됨")
        
        print(f"📊 실행 설정:")
        print(f"   - batch_size: {args.batch_size}")
        print(f"   - frozen_on_cpu: {args.frozen_on_cpu}")
        print(f"   - lora_r: {args.lora_r}")
        print(f"   - max_num_batches: {args.max_num_batches}")
        
        # ETU 실행
        run_etu(args)
        
    except ImportError as e:
        print(f"❌ ETU 모듈 import 오류: {e}")
        print("   pip install -r requirements.txt 실행 후 다시 시도하세요.")
    except Exception as e:
        print(f"❌ 실행 오류: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 