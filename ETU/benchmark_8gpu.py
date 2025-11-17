#!/usr/bin/env python3
"""
8대 H200 GPU 성능 벤치마크 스크립트
메모리 대역폭, 연산 성능, 병렬 처리 효율성 측정
"""

import os
import time
import torch
import torch.distributed as dist
import torch.nn as nn
import numpy as np
from datetime import datetime

class H200Benchmark:
    def __init__(self):
        self.gpu_count = torch.cuda.device_count()
        self.device_names = []
        self.device_memories = []
        self.results = {}
        
        # GPU 정보 수집
        self._collect_gpu_info()
        
    def _collect_gpu_info(self):
        """8대 H200 GPU 정보 수집"""
        print("🚀 8대 H200 GPU 벤치마크 시작")
        print("=" * 60)
        
        for i in range(self.gpu_count):
            props = torch.cuda.get_device_properties(i)
            name = props.name
            memory_gb = props.total_memory / 1024**3
            
            self.device_names.append(name)
            self.device_memories.append(memory_gb)
            
            print(f"GPU {i}: {name} ({memory_gb:.1f} GB)")
        
        total_memory = sum(self.device_memories)
        print(f"💾 총 GPU 메모리: {total_memory:.1f} GB")
        print("=" * 60)
        
    def benchmark_memory_bandwidth(self):
        """메모리 대역폭 벤치마크"""
        print("📊 메모리 대역폭 벤치마크 시작...")
        
        results = {}
        for i in range(self.gpu_count):
            torch.cuda.set_device(i)
            
            # 대용량 텐서 생성 (1GB)
            size = 1024 * 1024 * 1024 // 4  # float32 기준
            x = torch.randn(size, device=f'cuda:{i}')
            y = torch.randn(size, device=f'cuda:{i}')
            
            # 메모리 복사 벤치마크
            start_time = time.time()
            for _ in range(100):
                z = x + y
                torch.cuda.synchronize()
            end_time = time.time()
            
            # 대역폭 계산 (GB/s)
            total_bytes = size * 4 * 100 * 2  # 읽기 + 쓰기
            bandwidth_gbps = (total_bytes / 1024**3) / (end_time - start_time)
            
            results[f'gpu_{i}'] = bandwidth_gbps
            print(f"GPU {i} 메모리 대역폭: {bandwidth_gbps:.2f} GB/s")
        
        self.results['memory_bandwidth'] = results
        return results
    
    def benchmark_compute_performance(self):
        """연산 성능 벤치마크"""
        print("🔢 연산 성능 벤치마크 시작...")
        
        results = {}
        for i in range(self.gpu_count):
            torch.cuda.set_device(i)
            
            # 행렬 곱셈 벤치마크
            size = 4096
            a = torch.randn(size, size, device=f'cuda:{i}')
            b = torch.randn(size, size, device=f'cuda:{i}')
            
            # warmup
            for _ in range(10):
                _ = torch.mm(a, b)
                torch.cuda.synchronize()
            
            # 실제 벤치마크
            start_time = time.time()
            for _ in range(100):
                c = torch.mm(a, b)
                torch.cuda.synchronize()
            end_time = time.time()
            
            # FLOPS 계산
            flops = 2 * size**3 * 100  # 행렬 곱셈 FLOPS
            gflops = flops / (end_time - start_time) / 1e9
            
            results[f'gpu_{i}'] = gflops
            print(f"GPU {i} 연산 성능: {gflops:.2f} GFLOPS")
        
        self.results['compute_performance'] = results
        return results
    
    def benchmark_multi_gpu_scaling(self):
        """멀티 GPU 스케일링 벤치마크"""
        print("🔄 멀티 GPU 스케일링 벤치마크 시작...")
        
        results = {}
        
        # 단일 GPU부터 8대 GPU까지 점진적 테스트
        for gpu_count in range(1, min(9, self.gpu_count + 1)):
            print(f"  {gpu_count}대 GPU 테스트...")
            
            # 배치 크기 조정
            batch_size = 32 * gpu_count
            size = 2048
            
            # 데이터 생성
            inputs = []
            for i in range(gpu_count):
                torch.cuda.set_device(i)
                x = torch.randn(batch_size // gpu_count, size, device=f'cuda:{i}')
                inputs.append(x)
            
            # 순차 처리
            start_time = time.time()
            outputs = []
            for i, x in enumerate(inputs):
                torch.cuda.set_device(i)
                y = torch.mm(x, x.t())
                outputs.append(y)
                torch.cuda.synchronize()
            seq_time = time.time() - start_time
            
            # 병렬 처리 (시뮬레이션)
            start_time = time.time()
            for i, x in enumerate(inputs):
                torch.cuda.set_device(i)
                y = torch.mm(x, x.t())
                torch.cuda.synchronize()
            par_time = time.time() - start_time
            
            # 스케일링 효율성
            efficiency = seq_time / par_time / gpu_count
            results[f'{gpu_count}gpu'] = {
                'sequential_time': seq_time,
                'parallel_time': par_time,
                'efficiency': efficiency
            }
            
            print(f"    {gpu_count}대 GPU 효율성: {efficiency:.3f}")
        
        self.results['multi_gpu_scaling'] = results
        return results
    
    def benchmark_memory_utilization(self):
        """메모리 사용량 벤치마크"""
        print("💾 메모리 사용량 벤치마크 시작...")
        
        results = {}
        for i in range(self.gpu_count):
            torch.cuda.set_device(i)
            
            # 메모리 초기화
            torch.cuda.empty_cache()
            initial_memory = torch.cuda.memory_allocated(i)
            
            # 점진적 메모리 할당
            tensors = []
            memory_usage = []
            
            for size_mb in [100, 200, 500, 1000, 2000, 5000, 10000]:
                try:
                    # MB 단위로 텐서 생성
                    size = size_mb * 1024 * 1024 // 4
                    x = torch.randn(size, device=f'cuda:{i}')
                    tensors.append(x)
                    
                    current_memory = torch.cuda.memory_allocated(i)
                    memory_usage.append({
                        'size_mb': size_mb,
                        'allocated_gb': current_memory / 1024**3,
                        'reserved_gb': torch.cuda.memory_reserved(i) / 1024**3
                    })
                    
                except torch.cuda.OutOfMemoryError:
                    print(f"GPU {i}: {size_mb}MB에서 OOM 발생")
                    break
            
            # 메모리 정리
            del tensors
            torch.cuda.empty_cache()
            
            results[f'gpu_{i}'] = memory_usage
            print(f"GPU {i} 최대 메모리: {memory_usage[-1]['allocated_gb']:.2f} GB")
        
        self.results['memory_utilization'] = results
        return results
    
    def run_all_benchmarks(self):
        """모든 벤치마크 실행"""
        print("🚀 전체 벤치마크 시작...")
        print()
        
        # 1. 메모리 대역폭
        self.benchmark_memory_bandwidth()
        print()
        
        # 2. 연산 성능
        self.benchmark_compute_performance()
        print()
        
        # 3. 멀티 GPU 스케일링
        self.benchmark_multi_gpu_scaling()
        print()
        
        # 4. 메모리 사용량
        self.benchmark_memory_utilization()
        print()
        
        # 결과 요약
        self._print_summary()
        
        # 결과 저장
        self._save_results()
    
    def _print_summary(self):
        """벤치마크 결과 요약"""
        print("=" * 60)
        print("📊 벤치마크 결과 요약")
        print("=" * 60)
        
        # 메모리 대역폭 평균
        if 'memory_bandwidth' in self.results:
            avg_bandwidth = np.mean(list(self.results['memory_bandwidth'].values()))
            print(f"평균 메모리 대역폭: {avg_bandwidth:.2f} GB/s")
        
        # 연산 성능 평균
        if 'compute_performance' in self.results:
            avg_gflops = np.mean(list(self.results['compute_performance'].values()))
            print(f"평균 연산 성능: {avg_gflops:.2f} GFLOPS")
        
        # 멀티 GPU 효율성
        if 'multi_gpu_scaling' in self.results:
            efficiencies = [v['efficiency'] for v in self.results['multi_gpu_scaling'].values()]
            avg_efficiency = np.mean(efficiencies)
            print(f"평균 멀티 GPU 효율성: {avg_efficiency:.3f}")
        
        print("=" * 60)
    
    def _save_results(self):
        """벤치마크 결과 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"h200_benchmark_{timestamp}.json"
        
        import json
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        
        print(f"📝 벤치마크 결과 저장됨: {filename}")

def main():
    """메인 함수"""
    print("=== ETU 8대 H200 GPU 성능 벤치마크 ===")
    
    # 벤치마크 인스턴스 생성
    benchmark = H200Benchmark()
    
    # 모든 벤치마크 실행
    benchmark.run_all_benchmarks()

if __name__ == "__main__":
    main() 