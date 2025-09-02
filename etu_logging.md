#!/usr/bin/env python3
"""
HuggingFace 데이터셋 다운로드 스크립트 (수정된 버전)
"""

import os
from datasets import load_dataset
from huggingface_hub import HfApi

def download_dataset(dataset_name, config=None, split="train", local_dir="./datasets"):
    """데이터셋을 로컬에 다운로드"""
    try:
        print(f"📥 다운로드 중: {dataset_name}")
        
        if config:
            # config가 있는 경우 (예: cais/wmdp-corpora:cyber-forget-corpus)
            dataset = load_dataset(dataset_name, config, split=split, cache_dir=local_dir)
            print(f"✅ {dataset_name}:{config} 다운로드 완료 - {len(dataset)}개 항목")
        else:
            # config가 없는 경우 (예: wikitext, bio-forget-corpus)
            dataset = load_dataset(dataset_name, split=split, cache_dir=local_dir)
            print(f"✅ {dataset_name} 다운로드 완료 - {len(dataset)}개 항목")
            
        return True
        
    except Exception as e:
        print(f"❌ {dataset_name} 다운로드 실패: {e}")
        return False

def test_token():
    """토큰 유효성 테스트"""
    try:
        token = os.getenv("HUGGING_FACE_HUB_TOKEN", "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")
        api = HfApi(token=token)
        
        # 사용자 정보 확인
        user = api.whoami()
        print(f"✅ 로그인 성공: {user['name']}")
        
        # 데이터셋 접근 테스트 (generator를 list로 변환)
        datasets = list(api.list_datasets(author='cais'))
        print(f"✅ cais 데이터셋 접근 가능: {len(datasets)}개")
        
        return True
        
    except Exception as e:
        print(f"❌ 토큰 테스트 실패: {e}")
        return False

def main():
    """메인 다운로드 함수"""
    # 토큰 설정 (직접 포함)
    token = "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"
    os.environ["HUGGING_FACE_HUB_TOKEN"] = token
    
    print("🔑 HuggingFace 토큰 설정 완료")
    print(f"🔑 사용 토큰: {token[:10]}...{token[-10:]}")
    
    # 토큰 테스트
    if not test_token():
        print("❌ 토큰이 유효하지 않습니다. 토큰을 확인해주세요.")
        print("💡 토큰이 만료되었거나 권한이 변경되었을 수 있습니다.")
        return
    
    # 다운로드할 데이터셋 목록 (수정된 버전)
    datasets = [
        ("cais/wmdp-corpora", "cyber-forget-corpus"),
        ("cais/wmdp-corpora", "cyber-retain-corpus"), 
        ("cais/wmdp-bio-forget-corpus", None),  # 별도 데이터셋
        ("cais/wmdp-corpora", "bio-retain-corpus"),
        ("wikitext", "wikitext-2-raw-v1"),  # config 명시
    ]
    
    print("\n🚀 HuggingFace 데이터셋 다운로드 시작...")
    
    success_count = 0
    for dataset_name, config in datasets:
        if download_dataset(dataset_name, config):
            success_count += 1
    
    print(f"\n📊 다운로드 완료: {success_count}/{len(datasets)}")
    print("💾 데이터는 ./datasets/ 디렉토리에 저장되었습니다.")

if __name__ == "__main__":
    main() 
