#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
테스트 데이터 관리 유틸리티
테스트 데이터의 (생성,) 검증, 로드를 담당
"""

import json
import os
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime


# 기본 테스트 데이터 디렉토리
DEFAULT_TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
DEFAULT_TEST_DATA_FILE = os.path.join(DEFAULT_TEST_DATA_DIR, "test_data.json")


def ensure_test_data_dir(test_data_dir: Optional[str] = None) -> str:
    """
    테스트 데이터 디렉토리 생성 (불미스러운 이슈로 날아가서 없으면)
    
    Args:
        test_data_dir: 테스트 데이터 디렉토리 경로 (None이면 기본값 사용)
    
    Returns:
        테스트 데이터 디렉토리 경로
    """
    if test_data_dir is None:
        test_data_dir = DEFAULT_TEST_DATA_DIR
    
    os.makedirs(test_data_dir, exist_ok=True)
    return test_data_dir


def validate_test_data_item(item: Dict, index: int = None) -> Tuple[bool, List[str]]:
    """
    테스트 데이터 항목 검증
    
    Args:
        item: 검증할 테스트 데이터 항목
        index: 항목 인덱스 (에러 메시지용)
    
    Returns:
        (is_valid, error_messages) 튜플
    """
    errors = []
    prefix = f"[항목 {index}] " if index is not None else ""
    
    # 필수 필드 확인
    required_fields = ['input', 'target_clause', 'target_score']
    for field in required_fields:
        if field not in item:
            errors.append(f"{prefix}필수 필드 '{field}'가 없습니다.")
    
    # target_score 타입 및 범위 확인
    if 'target_score' in item:
        try:
            score = float(item['target_score'])
            if not (0.0 <= score <= 4.0):
                errors.append(f"{prefix}target_score는 0.0~4.0 범위여야 합니다. (현재: {score})")
        except (ValueError, TypeError):
            errors.append(f"{prefix}target_score는 숫자여야 합니다. (현재: {item['target_score']})")
    
    # 선택 필드 검증
    optional_fields = ['spa_term', 'description', 'metadata']
    for field in optional_fields:
        if field in item and item[field] is None:
            errors.append(f"{prefix}선택 필드 '{field}'가 None입니다.")
    
    return len(errors) == 0, errors


def validate_test_data(test_data: List[Dict]) -> Tuple[bool, List[str]]:
    """
    전체 테스트 데이터 검증
    
    Args:
        test_data: 검증할 테스트 데이터 리스트
    
    Returns:
        (is_valid, error_messages) 튜플
    """
    if not isinstance(test_data, list):
        return False, ["테스트 데이터는 리스트 형식이어야 합니다."]
    
    if len(test_data) == 0:
        return False, ["테스트 데이터가 비어있습니다."]
    
    all_errors = []
    for i, item in enumerate(test_data):
        is_valid, errors = validate_test_data_item(item, index=i)
        if not is_valid:
            all_errors.extend(errors)
    
    return len(all_errors) == 0, all_errors


def load_test_data(test_data_path: Optional[str] = None) -> List[Dict]:
    """
    테스트 데이터 로드 (검증 포함)
    
    Args:
        test_data_path: 테스트 데이터 JSON 파일 경로 (None이면 기본 경로 사용)
    
    Returns:
        검증된 테스트 데이터 리스트
    
    Raises:
        ValueError: 데이터 형식이 올바르지 않거나 검증 실패 시
        FileNotFoundError: 파일이 없을 때
    """
    if test_data_path is None:
        test_data_path = DEFAULT_TEST_DATA_FILE
    
    if not os.path.exists(test_data_path):
        raise FileNotFoundError(
            f"테스트 데이터 파일을 찾을 수 없습니다: {test_data_path}\n"
            f"기본 경로: {DEFAULT_TEST_DATA_FILE}\n"
            f"테스트 데이터를 생성하려면 create_test_data() 함수를 사용하세요."
        )
    
    with open(test_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 데이터 형식 변환
    if isinstance(data, list):
        test_data = data
    elif isinstance(data, dict):
        if 'test_data' in data:
            test_data = data['test_data']
        elif 'samples' in data:
            test_data = data['samples']
        else:
            raise ValueError(
                "테스트 데이터 형식이 올바르지 않습니다. "
                "리스트 또는 {'test_data': [...]} 또는 {'samples': [...]} 형식이어야 합니다."
            )
    else:
        raise ValueError("테스트 데이터는 리스트 또는 딕셔너리 형식이어야 합니다.")
    
    # 검증
    is_valid, errors = validate_test_data(test_data)
    if not is_valid:
        error_msg = "테스트 데이터 검증 실패:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)
    
    return test_data


def save_test_data(
    test_data: List[Dict],
    test_data_path: Optional[str] = None,
    backup: bool = True
) -> str:
    """
    테스트 데이터 저장 (검증 포함)
    
    Args:
        test_data: 저장할 테스트 데이터 리스트
        test_data_path: 저장할 파일 경로 (None이면 기본 경로 사용)
        backup: 기존 파일이 있으면 백업할지 여부
    
    Returns:
        저장된 파일 경로
    
    Raises:
        ValueError: 데이터 검증 실패 시
    """
    # 검증
    is_valid, errors = validate_test_data(test_data)
    if not is_valid:
        error_msg = "테스트 데이터 검증 실패:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)
    
    if test_data_path is None:
        test_data_path = DEFAULT_TEST_DATA_FILE
    
    # 디렉토리 생성
    os.makedirs(os.path.dirname(test_data_path), exist_ok=True)
    
    # 백업
    if backup and os.path.exists(test_data_path):
        backup_path = f"{test_data_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        import shutil
        shutil.copy2(test_data_path, backup_path)
        print(f"기존 파일 백업: {backup_path}")
    
    # 저장
    output_data = {
        "version": "1.0",
        "created_at": datetime.now().isoformat(),
        "total_samples": len(test_data),
        "test_data": test_data
    }
    
    with open(test_data_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"테스트 데이터 저장 완료: {test_data_path} ({len(test_data)}개 샘플)")
    return test_data_path


def create_test_data_template() -> List[Dict]:
    """
    테스트 데이터 템플릿 생성 (예시)
    
    Returns:
        예시 테스트 데이터 리스트
    """
    return [
        {
            "input": "매도인이 알고 있는 한이라 함은 매도인 또는 대상회사의 등기이사가 실제로 알고 있는 경우를 의미한다.",
            "target_clause": "\"매도인이 알고 있는 한\"이라 함은 매도인, 대상회사에 소속된 상무급 이상의 임원 및/또는 해외 종속회사(이하에서 정의함) 소속 팀장급 이상의 임직원이 실제로 알고 있거나 합리적인 주의의무(해당 임직원의 직위, 직책, 업무분장, 위임전결규정 기타 내규에 따라 판단함)를 다 하였다면 알 수 있었던 것을 의미한다.",
            "target_score": 0.0,
            "spa_term": "매도인이 알고 있는 한",
            "description": "매수인 친화로 변환 (0점 목표)",
            "metadata": {
                "source": "spa_term_context.py",
                "original_score": 4.0
            }
        },
        {
            "input": "부담은 소유권, 수익권, 사용권, 의결권, 처분권 등 각종 권리에 대한 (근)저당권, 질권, 유치권 등의 담보권 및 용익물권, 옵션, 우선권, 우선매수권, 동반매각요구권(drag-along right), 동반매각참여권(tag-along right) 기타 이와 유사한 법률상 또는 계약상 제약 또는 제한을 의미한다.",
            "target_clause": "\"부담\"은 (근)저당권, 질권, 유치권 등의 담보권을 의미한다.",
            "target_score": 4.0,
            "spa_term": "부담",
            "description": "매도인 친화로 변환 (4점 목표)",
            "metadata": {
                "source": "spa_term_context.py",
                "original_score": 0.0
            }
        }
    ]


def get_test_data_info(test_data_path: Optional[str] = None) -> Dict:
    """
    테스트 데이터 정보 조회
    
    Args:
        test_data_path: 테스트 데이터 파일 경로 (None이면 기본 경로 사용)
    
    Returns:
        테스트 데이터 정보 딕셔너리
    """
    if test_data_path is None:
        test_data_path = DEFAULT_TEST_DATA_FILE
    
    if not os.path.exists(test_data_path):
        return {
            "exists": False,
            "path": test_data_path,
            "message": "테스트 데이터 파일이 없습니다."
        }
    
    with open(test_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        test_data = data.get('test_data', data.get('samples', []))
        info = {
            "exists": True,
            "path": test_data_path,
            "version": data.get('version', 'unknown'),
            "created_at": data.get('created_at', 'unknown'),
            "total_samples": len(test_data),
            "score_distribution": {}
        }
        
        # 점수 분포 계산
        scores = [float(item.get('target_score', 0)) for item in test_data if 'target_score' in item]
        if scores:
            info["score_distribution"] = {
                "min": min(scores),
                "max": max(scores),
                "mean": sum(scores) / len(scores),
                "samples_by_score": {
                    "0.0": sum(1 for s in scores if s == 0.0),
                    "1.0": sum(1 for s in scores if s == 1.0),
                    "2.0": sum(1 for s in scores if s == 2.0),
                    "3.0": sum(1 for s in scores if s == 3.0),
                    "4.0": sum(1 for s in scores if s == 4.0),
                }
            }
    else:
        test_data = data if isinstance(data, list) else []
        info = {
            "exists": True,
            "path": test_data_path,
            "total_samples": len(test_data)
        }
    
    return info


def main():
    """테스트 데이터 관리 CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description='테스트 데이터 관리 유틸리티')
    parser.add_argument('command', choices=['create', 'validate', 'info', 'list'], 
                       help='실행할 명령어')
    parser.add_argument('--path', type=str, default=None, 
                       help='테스트 데이터 파일 경로 (기본값: test_data/test_data.json)')
    
    args = parser.parse_args()
    
    if args.command == 'create':
        # 템플릿 생성
        template = create_test_data_template()
        save_test_data(template, args.path)
        print("\n템플릿 테스트 데이터가 생성되었습니다. 필요에 따라 수정하세요.")
    
    elif args.command == 'validate':
        # 검증
        try:
            test_data = load_test_data(args.path)
            print(f"✅ 테스트 데이터 검증 성공: {len(test_data)}개 샘플")
        except Exception as e:
            print(f"❌ 검증 실패: {e}")
    
    elif args.command == 'info':
        # 정보 조회
        info = get_test_data_info(args.path)
        print(json.dumps(info, ensure_ascii=False, indent=2))
    
    elif args.command == 'list':
        # 목록 조회
        try:
            test_data = load_test_data(args.path)
            print(f"\n총 {len(test_data)}개 샘플:\n")
            for i, item in enumerate(test_data, 1):
                print(f"{i}. {item.get('spa_term', 'N/A')} (점수: {item.get('target_score', 'N/A')})")
                print(f"   입력: {item.get('input', '')[:50]}...")
        except Exception as e:
            print(f"❌ 오류: {e}")


if __name__ == "__main__":
    main()

