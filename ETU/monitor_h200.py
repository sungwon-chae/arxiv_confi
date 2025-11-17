#!/usr/bin/env python3
"""
H200 GPU 환경 실시간 모니터링 스크립트
GPU 메모리, 온도, 전력 사용량 등을 실시간으로 추적
"""

import time
import os
import subprocess
import json
from datetime import datetime
import argparse

class H200Monitor:
    def __init__(self, log_file="h200_monitor.log", interval=5):
        self.log_file = log_file
        self.interval = interval
        self.start_time = datetime.now()
        
    def get_gpu_info(self):
        """nvidia-smi를 통해 GPU 정보 수집"""
        try:
            # GPU 상태 정보 수집
            result = subprocess.run([
                'nvidia-smi', '--query-gpu=index,name,memory.used,memory.total,utilization.gpu,temperature.gpu,power.draw,power.limit',
                '--format=csv,noheader,nounits'
            ], capture_output=True, text=True, check=True)
            
            gpu_info = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = line.split(', ')
                    if len(parts) >= 8:
                        gpu_info.append({
                            'index': int(parts[0]),
                            'name': parts[1],
                            'memory_used_mb': int(parts[2]),
                            'memory_total_mb': int(parts[3]),
                            'utilization_percent': int(parts[4]),
                            'temperature_c': int(parts[5]),
                            'power_draw_w': float(parts[6]) if parts[6] != 'N/A' else 0,
                            'power_limit_w': float(parts[7]) if parts[7] != 'N/A' else 0
                        })
            
            return gpu_info
        except subprocess.CalledProcessError as e:
            print(f"GPU 정보 수집 오류: {e}")
            return []
    
    def get_process_info(self):
        """GPU에서 실행 중인 프로세스 정보 수집"""
        try:
            result = subprocess.run([
                'nvidia-smi', '--query-compute-apps=pid,process_name,gpu_uuid,used_memory',
                '--format=csv,noheader,nounits'
            ], capture_output=True, text=True, check=True)
            
            processes = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = line.split(', ')
                    if len(parts) >= 4:
                        processes.append({
                            'pid': int(parts[0]),
                            'process_name': parts[1],
                            'gpu_uuid': parts[2],
                            'used_memory_mb': int(parts[3])
                        })
            
            return processes
        except subprocess.CalledProcessError:
            return []
    
    def format_memory(self, mb):
        """메모리를 읽기 쉬운 형태로 변환"""
        if mb >= 1024:
            return f"{mb/1024:.1f} GB"
        else:
            return f"{mb} MB"
    
    def log_info(self, gpu_info, processes):
        """정보를 로그 파일에 저장"""
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            'timestamp': timestamp,
            'uptime': str(datetime.now() - self.start_time),
            'gpu_info': gpu_info,
            'processes': processes
        }
        
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    
    def display_info(self, gpu_info, processes):
        """터미널에 정보 표시"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 80)
        print(f"🚀 H200 GPU 모니터링 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  실행 시간: {datetime.now() - self.start_time}")
        print("=" * 80)
        
        # GPU 정보 표시
        for gpu in gpu_info:
            memory_usage = (gpu['memory_used_mb'] / gpu['memory_total_mb']) * 100
            power_usage = (gpu['power_draw_w'] / gpu['power_limit_w']) * 100 if gpu['power_limit_w'] > 0 else 0
            
            print(f"GPU {gpu['index']}: {gpu['name']}")
            print(f"  💾 메모리: {self.format_memory(gpu['memory_used_mb'])} / {self.format_memory(gpu['memory_total_mb'])} ({memory_usage:.1f}%)")
            print(f"  🔥 온도: {gpu['temperature_c']}°C")
            print(f"  ⚡ 전력: {gpu['power_draw_w']:.1f}W / {gpu['power_limit_w']:.1f}W ({power_usage:.1f}%)")
            print(f"  📊 사용률: {gpu['utilization_percent']}%")
            print()
        
        # 프로세스 정보 표시
        if processes:
            print("🔄 실행 중인 프로세스:")
            for proc in processes:
                print(f"  PID {proc['pid']}: {proc['process_name']} - {self.format_memory(proc['used_memory_mb'])}")
        else:
            print("💤 실행 중인 GPU 프로세스 없음")
        
        print("=" * 80)
        print(f"📝 로그 파일: {self.log_file}")
        print(f"🔄 업데이트 간격: {self.interval}초 (Ctrl+C로 종료)")
    
    def run(self):
        """모니터링 실행"""
        print(f"🚀 H200 GPU 모니터링 시작...")
        print(f"📝 로그 파일: {self.log_file}")
        print(f"🔄 업데이트 간격: {self.interval}초")
        print("Ctrl+C로 종료할 수 있습니다.")
        print()
        
        try:
            while True:
                gpu_info = self.get_gpu_info()
                processes = self.get_process_info()
                
                self.display_info(gpu_info, processes)
                self.log_info(gpu_info, processes)
                
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print("\n\n🛑 모니터링 종료됨")
            print(f"📊 총 실행 시간: {datetime.now() - self.start_time}")
            print(f"📝 로그 파일: {self.log_file}")

def main():
    parser = argparse.ArgumentParser(description="H200 GPU 환경 모니터링")
    parser.add_argument("--log", type=str, default="h200_monitor.log",
                       help="로그 파일 경로 (기본값: h200_monitor.log)")
    parser.add_argument("--interval", type=int, default=5,
                       help="업데이트 간격(초) (기본값: 5)")
    
    args = parser.parse_args()
    
    monitor = H200Monitor(log_file=args.log, interval=args.interval)
    monitor.run()

if __name__ == "__main__":
    main() 