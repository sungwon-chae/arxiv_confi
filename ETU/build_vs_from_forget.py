#!/usr/bin/env python3
"""
브루트포스 V_S 생성: forget 정답 텍스트의 모든 토큰을 V_S에 포함
Lo-Fi 검증용 - 억제 메커니즘 작동 여부만 확인
"""
import json
import argparse
import re
from collections import Counter
from transformers import AutoTokenizer

# 너무 일반적인 구두점/기호들
STOP_PIECES = {
    ".", ",", ":", ";", "!", "?", "(", ")", "[", "]", "{", "}", "'", '"',
    "-", "—", "–", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "~",
    "▁", " ", "\n", "\t"  # BPE 특수 토큰들
}

def too_generic(piece):
    """너무 일반적인 서브워드 조각인지 판단"""
    p = piece.replace("▁", "")
    return (p in STOP_PIECES) or (len(p) <= 1 and p.isalpha())

def main():
    ap = argparse.ArgumentParser(description="브루트포스 V_S 생성 (forget 정답 기반)")
    ap.add_argument("--model", default="HuggingFaceH4/zephyr-7b-beta", help="토크나이저 모델")
    ap.add_argument("--forget_jsonl", required=True, help="forget 데이터 JSONL 파일")
    ap.add_argument("--out", required=True, help="출력 V_S.ids.json 파일")
    ap.add_argument("--cap", type=int, default=2000, help="V_S 최대 크기")
    ap.add_argument("--min_freq", type=int, default=1, help="최소 등장 빈도")
    args = ap.parse_args()

    print(f"=== 브루트포스 V_S 생성 ===")
    print(f"모델: {args.model}")
    print(f"입력: {args.forget_jsonl}")
    print(f"출력: {args.out}")
    print(f"최대 크기: {args.cap}")
    print(f"최소 빈도: {args.min_freq}")

    # 토크나이저 로드
    print("토크나이저 로딩 중...")
    tok = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    
    # forget 정답 텍스트에서 토큰 빈도 계산
    print("forget 정답 텍스트 토크나이징 중...")
    freq = Counter()
    total_lines = 0
    
    with open(args.forget_jsonl, "r", encoding="utf-8") as f:
        for line in f:
            try:
                ex = json.loads(line.strip())
                # 정답 텍스트만 사용 (진짜 Lo-Fi)
                txt = ex.get("output", "")
                if txt:
                    ids = tok.encode(txt, add_special_tokens=False)
                    freq.update(ids)
                    total_lines += 1
            except json.JSONDecodeError:
                continue
    
    print(f"처리된 라인 수: {total_lines}")
    print(f"총 토큰 수: {sum(freq.values())}")
    print(f"고유 토큰 수: {len(freq)}")

    # 빈도순으로 정렬하여 V_S 구성
    print("V_S 구성 중...")
    vs = []
    skipped_generic = 0
    skipped_low_freq = 0
    
    for tid, count in freq.most_common():
        # 최소 빈도 체크
        if count < args.min_freq:
            skipped_low_freq += 1
            continue
            
        # 일반적인 토큰 체크
        piece = tok.convert_ids_to_tokens(tid)
        if too_generic(piece):
            skipped_generic += 1
            continue
            
        vs.append(tid)
        if len(vs) >= args.cap:
            break

    print(f"V_S 크기: {len(vs)}")
    print(f"제외된 일반 토큰: {skipped_generic}")
    print(f"제외된 저빈도 토큰: {skipped_low_freq}")

    # V_S 저장
    result = {
        "token_ids": vs,
        "size": len(vs),
        "total_tokens": sum(freq.values()),
        "unique_tokens": len(freq),
        "skipped_generic": skipped_generic,
        "skipped_low_freq": skipped_low_freq,
        "model": args.model,
        "source": args.forget_jsonl
    }
    
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # 미리보기
    print(f"\n=== V_S 미리보기 (상위 50개) ===")
    preview = []
    for i, tid in enumerate(vs[:50]):
        piece = tok.convert_ids_to_tokens(tid)
        freq_count = freq[tid]
        preview.append(f"{tid}:{piece}({freq_count})")
        if i < 10:  # 처음 10개만 자세히
            print(f"  {tid:5d}: '{piece}' (빈도: {freq_count})")
    
    print(f"\n✅ V_S 저장 완료: {args.out}")
    print(f"   크기: {len(vs)}개 토큰")
    print(f"   상위 토큰: {preview[:10]}")

if __name__ == "__main__":
    main()
