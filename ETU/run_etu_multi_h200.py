#!/usr/bin/env python3
"""
ETU 8대 H200 GPU 멀티 노드 병렬 처리 스크립트
대용량 모델 (70B+) 실험 지원
"""

import os
import sys
import torch
import argparse
import subprocess
from pathlib import Path

# 8대 H200 GPU 환경 최적화
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

class MultiH200ETU:
    def __init__(self):
        self.gpu_count = torch.cuda.device_count()
        self.device_names = []
        self.device_memories = []
        
        # GPU 정보 수집
        self._collect_gpu_info()
        
    def _collect_gpu_info(self):
        """8대 H200 GPU 정보 수집"""
        print("🚀 8대 H200 GPU 환경 분석 중...")
        
        for i in range(self.gpu_count):
            props = torch.cuda.get_device_properties(i)
            name = props.name
            memory_gb = props.total_memory / 1024**3
            
            self.device_names.append(name)
            self.device_memories.append(memory_gb)
            
            print(f"GPU {i}: {name} ({memory_gb:.1f} GB)")
        
        # H200 GPU 확인
        h200_count = sum(1 for name in self.device_names if "H200" in name)
        if h200_count != 8:
            print(f"⚠️  H200 GPU {h200_count}개 감지됨 (예상: 8개)")
        else:
            print(f"✅ 8대 H200 GPU 모두 감지됨!")
        
        total_memory = sum(self.device_memories)
        print(f"💾 총 GPU 메모리: {total_memory:.1f} GB")
        
    def setup_multi_gpu_environment(self, strategy="ddp"):
        """멀티 GPU 환경 설정"""
        print(f"🔧 멀티 GPU 환경 설정: {strategy}")
        
        if strategy == "ddp":
            # Distributed Data Parallel
            os.environ["MASTER_ADDR"] = "localhost"
            os.environ["MASTER_PORT"] = "12355"
            os.environ["WORLD_SIZE"] = str(self.gpu_count)
            os.environ["RANK"] = "0"
            
        elif strategy == "fsdp":
            # Fully Sharded Data Parallel
            os.environ["FSDP_CONFIG"] = "true"
            os.environ["FSDP_CPU_OFFLOAD"] = "false"
            
        elif strategy == "tensor_parallel":
            # Tensor Parallelism
            os.environ["TP_CONFIG"] = "true"
            os.environ["TP_SIZE"] = str(self.gpu_count)
            
        print(f"✅ {strategy.upper()} 환경 설정 완료")
        
    def get_multi_gpu_optimized_args(self):
        """8대 H200 GPU에 최적화된 인자"""
        parser = argparse.ArgumentParser(description="ETU 8대 H200 GPU 멀티 노드 실행")
        
        # GPU 전략
        parser.add_argument("--strategy", type=str, default="ddp",
                          choices=["ddp", "fsdp", "tensor_parallel"],
                          help="멀티 GPU 전략 (기본값: ddp)")
        
        # 8대 GPU 최적화 설정
        parser.add_argument("--batch_size", type=int, default=64,
                          help="전체 배치 크기 (8대 GPU 분산, 기본값: 64)")
        parser.add_argument("--batch_size_per_gpu", type=int, default=8,
                          help="GPU당 배치 크기 (기본값: 8)")
        parser.add_argument("--max_num_batches", type=int, default=200,
                          help="최대 배치 수 (8대 GPU 활용, 기본값: 200)")
        
        # 대용량 모델 지원
        parser.add_argument("--model_name_or_path", type=str,
                          default="meta-llama/Llama-2-70b-hf",
                          help="대용량 모델 경로 (기본값: Llama-2-70b)")
        parser.add_argument("--use_lora", action="store_true", default=True,
                          help="LoRA 사용 (대용량 모델 필수)")
        parser.add_argument("--lora_r", type=int, default=1024,
                          help="LoRA rank (8대 GPU 활용, 기본값: 1024)")
        parser.add_argument("--lora_alpha", type=int, default=2048,
                          help="LoRA alpha (기본값: 2048)")
        
        # ETU 핵심 파라미터
        parser.add_argument("--epsilon", type=float, default=0.05,
                          help="억제 목표 ε (기본값: 0.05)")
        parser.add_argument("--lambda_max", type=float, default=15.0,
                          help="최대 λ 값 (8대 GPU 활용, 기본값: 15.0)")
        parser.add_argument("--lambda_update_freq", type=int, default=50,
                          help="λ 업데이트 빈도 (기본값: 50)")
        
        # 데이터 설정
        parser.add_argument("--forget_corpora", type=str,
                          default="cais/wmdp-corpora:cyber-forget-corpus",
                          help="forget할 도메인 (별칭: bio:forget, cyber:forget, 또는 실제 경로)")
        parser.add_argument("--retain_corpora", type=str,
                          default="cais/wmdp-corpora:bio-retain-corpus",
                          help="retain할 도메인 (별칭: bio:retain, cyber:retain, wikitext, 또는 실제 경로)")
        
        # 성능 최적화
        parser.add_argument("--gradient_accumulation_steps", type=int, default=4,
                          help="그래디언트 누적 스텝 (기본값: 4)")
        parser.add_argument("--mixed_precision", type=str, default="bf16",
                          choices=["fp16", "bf16", "fp32"],
                          help="혼합 정밀도 (기본값: bf16)")
        parser.add_argument("--deterministic", action="store_true",
                          help="결정적 실행")
        parser.add_argument("--verbose", action="store_true", default=True,
                          help="상세 로깅")
        
        return parser.parse_args()
    
    def calculate_optimal_batch_size(self, model_size_gb):
        """모델 크기에 따른 최적 배치 크기 계산"""
        total_gpu_memory = sum(self.device_memories)
        available_memory = total_gpu_memory * 0.8  # 80% 사용
        
        # 모델 크기별 최적 배치 크기
        if model_size_gb <= 7:
            optimal_batch = 128  # 7B 모델
        elif model_size_gb <= 13:
            optimal_batch = 64   # 13B 모델
        elif model_size_gb <= 30:
            optimal_batch = 32   # 30B 모델
        elif model_size_gb <= 70:
            optimal_batch = 16   # 70B 모델
        else:
            optimal_batch = 8    # 70B+ 모델
        
        # GPU 메모리 제약 고려
        memory_constrained_batch = int(available_memory / (model_size_gb * 2))
        final_batch = min(optimal_batch, memory_constrained_batch)
        
        return final_batch
    
    def run_multi_gpu_etu(self):
        """8대 H200 GPU로 ETU 실행"""
        try:
            # 인자 파싱
            args = self.get_multi_gpu_optimized_args()
            
            # 멀티 GPU 환경 설정
            self.setup_multi_gpu_environment(args.strategy)
            
            # 모델 크기 추정 (대략적)
            if "70b" in args.model_name_or_path.lower():
                estimated_size = 70
            elif "30b" in args.model_name_or_path.lower():
                estimated_size = 30
            elif "13b" in args.model_name_or_path.lower():
                estimated_size = 13
            else:
                estimated_size = 7
            
            # 최적 배치 크기 계산
            optimal_batch = self.calculate_optimal_batch_size(estimated_size)
            args.batch_size = optimal_batch
            args.batch_size_per_gpu = optimal_batch // self.gpu_count
            
            print(f"📊 8대 H200 GPU 최적화 설정:")
            print(f"   - 전략: {args.strategy.upper()}")
            print(f"   - 전체 배치 크기: {args.batch_size}")
            print(f"   - GPU당 배치 크기: {args.batch_size_per_gpu}")
            print(f"   - LoRA rank: {args.lora_r}")
            print(f"   - 모델 크기: ~{estimated_size}B")
            print(f"   - 총 GPU 메모리: {sum(self.device_memories):.1f} GB")
            print()
            
            # ETU 실행
            from etu.unlearn import run_etu
            
            print("🚀 8대 H200 GPU로 ETU 실행 시작...")
            run_etu(args)
            
            print("✅ 8대 H200 GPU ETU 실행 완료!")
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

def main():
    """메인 함수"""
    print("=== ETU 8대 H200 GPU 멀티 노드 실행 ===")
    
    # 멀티 H200 ETU 인스턴스 생성
    multi_etu = MultiH200ETU()
    
    # 8대 GPU ETU 실행
    multi_etu.run_multi_gpu_etu()

if __name__ == "__main__":
    main() 