#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPA 매수인-매도인 친화 Style Transfer 평가 코드
ROUGE + Accuracy 기반 정량 평가
"""

import json
import os
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import numpy as np
from rouge_score import rouge_scorer
from dataclasses import dataclass

# 테스트 데이터 관리 모듈 임포트
try:
    from test_data_manager import load_test_data as load_test_data_with_validation, DEFAULT_TEST_DATA_FILE
except ImportError:
    # test_data_manager가 없으면 기본 함수 사용
    load_test_data_with_validation = None
    DEFAULT_TEST_DATA_FILE = None


@dataclass
class EvaluationResult:
    """평가 결과를 담는 데이터 클래스"""
    rouge_1: float
    rouge_2: float
    rouge_l: float
    accuracy: float  # 점수 예측 정확도 (±0.5 이내 비율)
    category_accuracy: float  # 구간 기반 정확도 (매수인/중립/매도인 구간 일치 비율)
    total_samples: int


def calculate_rouge_scores(predictions: List[str], references: List[str]) -> Dict[str, float]:
    """
    ROUGE 점수 계산
    
    Args:
        predictions: 예측된 조항 리스트
        references: 참조(정답) 조항 리스트
    
    Returns:
        ROUGE-1, ROUGE-2, ROUGE-L 점수 딕셔너리
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    
    rouge_1_scores = []
    rouge_2_scores = []
    rouge_l_scores = []
    
    for pred, ref in zip(predictions, references):
        scores = scorer.score(ref, pred)
        rouge_1_scores.append(scores['rouge1'].fmeasure)
        rouge_2_scores.append(scores['rouge2'].fmeasure)
        rouge_l_scores.append(scores['rougeL'].fmeasure)
    
    return {
        'rouge_1': np.mean(rouge_1_scores),
        'rouge_2': np.mean(rouge_2_scores),
        'rouge_l': np.mean(rouge_l_scores)
    }


def get_score_category(score: float) -> str:
    """
    점수를 구간 카테고리로 분류
    
    Args:
        score: 점수 (0.0 ~ 4.0)
    
    Returns:
        'buyer' (0~1.5), 'neutral' (1.5~2.5), 'seller' (2.5~4.0)
    """
    if score < 1.5:
        return 'buyer'
    elif score < 2.5:
        return 'neutral'
    else:
        return 'seller'


def calculate_score_accuracy(predicted_scores: List[float], ground_truth_scores: List[float]) -> float:
    """
    점수 예측 정확도 계산
    
    Args:
        predicted_scores: 예측된 점수 리스트
        ground_truth_scores: 실제 점수 리스트
    
    Returns:
        Accuracy (±0.5 이내 비율)
    """
    predicted_scores = np.array(predicted_scores)
    ground_truth_scores = np.array(ground_truth_scores)
    
    # 정확도: 오차가 0.5 이내인 비율
    accuracy = np.mean(np.abs(predicted_scores - ground_truth_scores) <= 0.5)
    
    return float(accuracy)


def calculate_category_accuracy(predicted_scores: List[float], ground_truth_scores: List[float]) -> float:
    """
    구간 기반 정확도 계산
    
    구간 정의:
    - 매수인 친화: 0.0 ~ 1.5
    - 중립: 1.5 ~ 2.5
    - 매도인 친화: 2.5 ~ 4.0
    
    예측 점수와 목표 점수가 같은 구간에 속하면 정답으로 처리
    
    Args:
        predicted_scores: 예측된 점수 리스트
        ground_truth_scores: 실제 점수 리스트
    
    Returns:
        구간 일치 정확도 (0.0 ~ 1.0)
    """
    if len(predicted_scores) != len(ground_truth_scores):
        raise ValueError("예측 점수와 실제 점수의 개수가 일치하지 않습니다.")
    
    correct = 0
    for pred_score, gt_score in zip(predicted_scores, ground_truth_scores):
        pred_category = get_score_category(float(pred_score))
        gt_category = get_score_category(float(gt_score))
        if pred_category == gt_category:
            correct += 1
    
    return float(correct / len(predicted_scores)) if predicted_scores else 0.0


def evaluate_style_transfer(
    test_data: List[Dict],
    predictions: List[Dict],
    output_dir: Optional[str] = None
) -> Tuple[EvaluationResult, int]:
    """
    Style Transfer 작업 평가
    
    Args:
        test_data: 테스트 데이터 리스트 (각 항목은 'input', 'target_clause', 'target_score' 포함)
        predictions: 예측 결과 리스트 (각 항목은 'converted_sentence', 'score' 포함)
        output_dir: 결과 저장 디렉토리 (선택사항)
    
    Returns:
        (EvaluationResult 객체, 제외된 샘플 수)
    """
    if len(test_data) != len(predictions):
        raise ValueError(f"테스트 데이터({len(test_data)})와 예측 결과({len(predictions)})의 개수가 일치하지 않습니다.")
    
    # ROUGE 계산을 위한 리스트 준비
    predicted_clauses = []
    reference_clauses = []
    predicted_scores = []
    ground_truth_scores = []
    
    # 오류 항목 필터링 (로컬 테스트용)
    excluded_count = 0
    excluded_indices = []
    
    for i, (test_item, pred_item) in enumerate(zip(test_data, predictions)):
        # 오류 항목 확인 (로컬 테스트용)
        is_error = False
        converted_sentence = pred_item.get('converted_sentence', '')
        
        # 오류 패턴 확인
        if isinstance(converted_sentence, str):
            if converted_sentence.startswith('[오류:') or converted_sentence.startswith('[오류 :'):
                is_error = True
            # metadata에 error가 있는지 확인
            if not is_error and 'error' in pred_item.get('metadata', {}):
                is_error = True
            # 토큰 제한 오류 확인
            if not is_error and 'length limit was reached' in converted_sentence:
                is_error = True
        
        if is_error:
            excluded_count += 1
            excluded_indices.append(i)
            continue
        
        # 조항 비교
        if 'converted_sentence' in pred_item and 'target_clause' in test_item:
            predicted_clauses.append(pred_item['converted_sentence'])
            reference_clauses.append(test_item['target_clause'])
        
        # 점수 비교
        if 'score' in pred_item and 'target_score' in test_item:
            predicted_scores.append(float(pred_item['score']))
            ground_truth_scores.append(float(test_item['target_score']))
    
    # 제외된 항목이 있으면 경고 출력
    if excluded_count > 0:
        print(f"⚠️ 경고: {excluded_count}개 항목이 오류로 인해 평가에서 제외되었습니다.")
        print(f"   제외된 인덱스: {excluded_indices}")
    
    # ROUGE 점수 계산
    if predicted_clauses and reference_clauses:
        rouge_scores = calculate_rouge_scores(predicted_clauses, reference_clauses)
    else:
        rouge_scores = {'rouge_1': 0.0, 'rouge_2': 0.0, 'rouge_l': 0.0}
    
    # 점수 정확도 계산
    if predicted_scores and ground_truth_scores:
        accuracy = calculate_score_accuracy(predicted_scores, ground_truth_scores)
        category_accuracy = calculate_category_accuracy(predicted_scores, ground_truth_scores)
    else:
        accuracy = 0.0
        category_accuracy = 0.0
    
    # 실제 평가된 샘플 수 (오류 제외)
    valid_samples = len(predicted_clauses) if predicted_clauses else len(predicted_scores)
    
    result = EvaluationResult(
        rouge_1=rouge_scores['rouge_1'],
        rouge_2=rouge_scores['rouge_2'],
        rouge_l=rouge_scores['rouge_l'],
        accuracy=accuracy,
        category_accuracy=category_accuracy,
        total_samples=valid_samples  # 오류 제외한 실제 평가 샘플 수
    )
    
    # 결과 저장
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        result_file = os.path.join(output_dir, 'evaluation_results.json')
        
        result_dict = {
            'rouge_1': result.rouge_1,
            'rouge_2': result.rouge_2,
            'rouge_l': result.rouge_l,
            'accuracy': result.accuracy,
            'category_accuracy': result.category_accuracy,
            'total_samples': result.total_samples,
            'excluded_samples': excluded_count if excluded_count > 0 else 0
        }
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=2)
        
        print(f"평가 결과가 {result_file}에 저장되었습니다.")
    
    return result, excluded_count


def load_test_data(test_data_path: Optional[str] = None) -> List[Dict]:
    """
    테스트 데이터 로드 (검증 포함)
    
    Args:
        test_data_path: 테스트 데이터 JSON 파일 경로 (None이면 기본 경로 사용)
    
    Returns:
        검증된 테스트 데이터 리스트
    
    Note:
        test_data_manager 모듈이 있으면 자동 검증이 포함됩니다.
        없으면 기본 로드만 수행합니다.
    """
    # test_data_manager 사용 가능하면 검증 포함 로드
    if load_test_data_with_validation is not None:
        return load_test_data_with_validation(test_data_path)
    
    # 기본 로드 (하위 호환성)
    if test_data_path is None:
        raise ValueError(
            "test_data_path가 필요합니다. "
            "또는 test_data_manager 모듈을 설치하여 기본 경로를 사용할 수 있습니다."
        )
    
    with open(test_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and 'test_data' in data:
        return data['test_data']
    else:
        raise ValueError("테스트 데이터 형식이 올바르지 않습니다. 리스트 또는 {'test_data': [...]} 형식이어야 합니다.")


def load_predictions(predictions_path: str) -> List[Dict]:
    """
    예측 결과 로드
    
    Args:
        predictions_path: 예측 결과 JSON 파일 경로
    
    Returns:
        예측 결과 리스트
    """
    with open(predictions_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and 'predictions' in data:
        return data['predictions']
    else:
        raise ValueError("예측 결과 형식이 올바르지 않습니다. 리스트 또는 {'predictions': [...]} 형식이어야 합니다.")


def print_evaluation_summary(result: EvaluationResult, excluded_samples: int = 0):
    """평가 결과 요약 출력"""
    print("\n" + "="*60)
    print("평가 결과 요약")
    print("="*60)
    print(f"총 샘플 수: {result.total_samples}")
    if excluded_samples > 0:
        print(f"제외된 샘플 수 (오류): {excluded_samples}")
    print("\n[ROUGE 점수]")
    print(f"  ROUGE-1: {result.rouge_1:.4f}")
    print(f"  ROUGE-2: {result.rouge_2:.4f}")
    print(f"  ROUGE-L: {result.rouge_l:.4f}")
    print("\n[점수 예측 정확도]")
    print(f"  Accuracy (±0.5 이내): {result.accuracy:.4f} ({result.accuracy*100:.2f}%)")
    print(f"  Category Accuracy (구간 일치): {result.category_accuracy:.4f} ({result.category_accuracy*100:.2f}%)")
    print("    - 매수인 친화 (0~1.5), 중립 (1.5~2.5), 매도인 친화 (2.5~4.0)")
    print("="*60 + "\n")


def main():
    """메인 실행 함수 (예시)"""
    import argparse
    
    parser = argparse.ArgumentParser(description='SPA Style Transfer 평가')
    parser.add_argument('--test_data', type=str, default=None, 
                       help='테스트 데이터 JSON 파일 경로 (기본값: test_data/test_data.json)')
    parser.add_argument('--predictions', type=str, required=True, help='예측 결과 JSON 파일 경로')
    parser.add_argument('--output_dir', type=str, default='./evaluation_results', help='결과 저장 디렉토리')
    
    args = parser.parse_args()
    
    # 데이터 로드
    print("테스트 데이터 로드 중...")
    test_data = load_test_data(args.test_data)
    print(f"테스트 데이터 {len(test_data)}개 로드 완료")
    
    print("예측 결과 로드 중...")
    predictions = load_predictions(args.predictions)
    print(f"예측 결과 {len(predictions)}개 로드 완료")
    
    # 평가 실행
    print("\n평가 실행 중...")
    result, excluded_count = evaluate_style_transfer(test_data, predictions, args.output_dir)
    
    # 결과 출력
    print_evaluation_summary(result, excluded_count)


if __name__ == "__main__":
    main()

