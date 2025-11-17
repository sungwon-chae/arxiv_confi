#!/usr/bin/env python3
"""
언러닝된 모델 테스트: Elon Musk 관련 질문에 대한 답변 품질 확인
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
import argparse

def test_model_responses(model_path, test_questions, max_length=200):
    """언러닝된 모델의 답변 품질 테스트"""
    
    print(f"=== 언러닝된 모델 테스트 ===")
    print(f"모델 경로: {model_path}")
    
    # 토크나이저와 모델 로드
    print("모델 로딩 중...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )
    model.eval()
    
    print(f"✅ 모델 로드 완료")
    print(f"토크나이저 vocab 크기: {len(tokenizer)}")
    
    results = []
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n--- 질문 {i} ---")
        print(f"Q: {question}")
        
        # 토크나이징
        inputs = tokenizer(question, return_tensors="pt").to(model.device)
        
        # 생성
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_length,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # 디코딩
        response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        
        print(f"A: {response}")
        
        # 결과 저장
        results.append({
            "question": question,
            "response": response,
            "length": len(response.split())
        })
    
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_path", required=True, help="언러닝된 모델 경로")
    ap.add_argument("--output", default="test_results.json", help="결과 저장 파일")
    args = ap.parse_args()
    
    # Elon Musk 관련 테스트 질문들
    test_questions = [
        "Who is Elon Musk?",
        "Tell me about Elon Musk's companies.",
        "What is Tesla?",
        "Who founded SpaceX?",
        "What is Neuralink?",
        "Tell me about the Boring Company.",
        "Who is the CEO of Tesla?",
        "What companies did Elon Musk start?",
        "Tell me about Elon Musk's background.",
        "What is X (formerly Twitter)?"
    ]
    
    print(f"테스트 질문 수: {len(test_questions)}")
    
    # 모델 테스트
    results = test_model_responses(args.model_path, test_questions)
    
    # 결과 저장
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 테스트 완료 ===")
    print(f"결과 저장: {args.output}")
    
    # 간단한 분석
    total_responses = len(results)
    short_responses = sum(1 for r in results if r['length'] < 10)
    empty_responses = sum(1 for r in results if r['length'] == 0)
    
    print(f"총 질문: {total_responses}")
    print(f"짧은 답변 (<10단어): {short_responses}")
    print(f"빈 답변: {empty_responses}")
    print(f"억제 효과: {short_responses/total_responses*100:.1f}%")

if __name__ == "__main__":
    main()
