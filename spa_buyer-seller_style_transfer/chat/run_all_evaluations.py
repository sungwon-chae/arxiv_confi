#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4가지 조합을 자동으로 평가하는 스크립트

조합:
1. utils.py + context.py
2. utils.py + context_v2.py
3. utils_v2.py + context.py
4. utils_v2.py + context_v2.py
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# 현재 디렉토리
SCRIPT_DIR = Path(__file__).parent


def run_command(cmd: List[str], description: str) -> bool:
    """명령어 실행"""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}")
    print(f"명령어: {' '.join(cmd)}")
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=False, text=True)
        print(f"✅ {description} 완료")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 실패: {e}")
        return False


def load_evaluation_result(result_path: str) -> Dict:
    """평가 결과 로드"""
    try:
        with open(result_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON 파싱 오류 ({result_path}): {e}")
        return None


def print_comparison_table(results: Dict[str, Dict]):
    """비교 테이블 출력"""
    print("\n" + "="*80)
    print("📊 4가지 조합 비교 결과")
    print("="*80)
    
    # 헤더
    print(f"\n{'조합':<30} {'ROUGE-1':>10} {'ROUGE-2':>10} {'ROUGE-L':>10} {'Accuracy':>10} {'Cat.Acc':>10}")
    print("-" * 80)
    
    # 각 조합별 결과
    for combo_name, result in results.items():
        if result:
            print(f"{combo_name:<30} "
                  f"{result.get('rouge_1', 0):>10.4f} "
                  f"{result.get('rouge_2', 0):>10.4f} "
                  f"{result.get('rouge_l', 0):>10.4f} "
                  f"{result.get('accuracy', 0):>10.4f} "
                  f"{result.get('category_accuracy', 0):>10.4f}")
        else:
            print(f"{combo_name:<30} {'N/A':>10} {'N/A':>10} {'N/A':>10} {'N/A':>10} {'N/A':>10}")
    
    print("="*80)


def main():
    """메인 실행 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='4가지 조합을 자동으로 평가하는 스크립트',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
조합:
  1. utils.py + context.py      (기본)
  2. utils.py + context_v2.py   (컨텍스트만 개선)
  3. utils_v2.py + context.py   (프롬프트만 개선)
  4. utils_v2.py + context_v2.py (둘 다 개선)

예시:
  python run_all_evaluations.py --test_data test_data/test_data_template\(손해배상\)_filled.json
        """
    )
    parser.add_argument('--test_data', type=str, required=True,
                       help='테스트 데이터 JSON 파일 경로')
    parser.add_argument('--use_local', action='store_true',
                       help='OpenAI API 사용 (로컬 테스트, generate_predictions_local.py)')
    parser.add_argument('--skip_generation', action='store_true',
                       help='예측 생성 건너뛰기 (이미 생성된 파일이 있는 경우)')
    parser.add_argument('--skip_evaluation', action='store_true',
                       help='평가 건너뛰기 (예측만 생성)')
    parser.add_argument('--output_dir', type=str, default='all_evaluation_results',
                       help='결과 저장 디렉토리 (기본값: all_evaluation_results)')
    
    args = parser.parse_args()
    
    # 테스트 데이터 경로 확인
    test_data_path = Path(args.test_data)
    if not test_data_path.exists():
        print(f"❌ 오류: 테스트 데이터 파일을 찾을 수 없습니다: {test_data_path}")
        sys.exit(1)
    
    # 출력 디렉토리 생성
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # 조합 정의
    combinations = [
        {
            "name": "utils_v1_context_v1",
            "description": "utils.py + context.py (기본)",
            "use_utils_v2": False,
            "use_context_v2": False
        },
        {
            "name": "utils_v1_context_v2",
            "description": "utils.py + context_v2.py (컨텍스트만 개선)",
            "use_utils_v2": False,
            "use_context_v2": True
        },
        {
            "name": "utils_v2_context_v1",
            "description": "utils_v2.py + context.py (프롬프트만 개선)",
            "use_utils_v2": True,
            "use_context_v2": False
        },
        {
            "name": "utils_v2_context_v2",
            "description": "utils_v2.py + context_v2.py (둘 다 개선)",
            "use_utils_v2": True,
            "use_context_v2": True
        }
    ]
    
    # 스크립트 선택
    if args.use_local:
        script_name = "generate_predictions_local.py"
    else:
        script_name = "generate_predictions.py"
    
    script_path = SCRIPT_DIR / script_name
    
    if not script_path.exists():
        print(f"❌ 오류: 스크립트를 찾을 수 없습니다: {script_path}")
        sys.exit(1)
    
    results = {}
    
    # 각 조합별로 실행
    for combo in combinations:
        combo_name = combo["name"]
        predictions_file = output_dir / f"predictions_{combo_name}.json"
        evaluation_dir = output_dir / f"evaluation_{combo_name}"
        evaluation_file = evaluation_dir / "evaluation_results.json"
        
        # 1. 예측 생성
        if not args.skip_generation:
            cmd = [
                sys.executable,
                str(script_path),
                "--test_data", str(test_data_path),
                "--output", str(predictions_file)
            ]
            
            if not combo["use_utils_v2"]:
                cmd.append("--use_utils_v1")
            if not combo["use_context_v2"]:
                cmd.append("--use_context_v1")
            
            success = run_command(cmd, f"예측 생성: {combo['description']}")
            if not success:
                print(f"⚠️ 예측 생성 실패: {combo_name}")
                continue
        else:
            if not predictions_file.exists():
                print(f"⚠️ 예측 파일이 없습니다: {predictions_file}")
                continue
        
        # 2. 평가 실행
        if not args.skip_evaluation:
            cmd = [
                sys.executable,
                str(SCRIPT_DIR / "evaluate.py"),
                "--test_data", str(test_data_path),
                "--predictions", str(predictions_file),
                "--output_dir", str(evaluation_dir)
            ]
            
            success = run_command(cmd, f"평가 실행: {combo['description']}")
            if not success:
                print(f"⚠️ 평가 실패: {combo_name}")
                continue
        
        # 3. 결과 로드
        result = load_evaluation_result(evaluation_file)
        results[combo["description"]] = result
    
    # 4. 비교 테이블 출력
    if not args.skip_evaluation:
        print_comparison_table(results)
        
        # 결과를 JSON 파일로 저장
        comparison_file = output_dir / "comparison_results.json"
        with open(comparison_file, 'w', encoding='utf-8') as f:
            json.dump({
                "generated_at": datetime.now().isoformat(),
                "test_data": str(test_data_path),
                "results": results
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 비교 결과가 저장되었습니다: {comparison_file}")
    
    print("\n" + "="*80)
    print("✅ 모든 평가 완료!")
    print("="*80)


if __name__ == "__main__":
    main()

