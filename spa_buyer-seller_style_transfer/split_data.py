#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def split_file_by_separator(input_file, output_dir):
    """
    파일을 구분자(--------)로 분할하고, 각 파일 내에서 2개 이상의 엔터로 구분된 데이터를 별개로 구성
    """
    # 출력 디렉토리 생성
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # 파일 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 구분자로 분할 (--------------------------------------------)
    sections = re.split(r'-{40,}', content)
    
    print(f"총 {len(sections)}개의 섹션을 발견했습니다.")
    
    for i, section in enumerate(sections):
        if not section.strip():  # 빈 섹션 건너뛰기
            continue
            
        # 각 섹션을 2개 이상의 엔터로 분할
        # 2개 이상의 연속된 엔터(\n\n+)를 구분자로 사용
        data_blocks = re.split(r'\n\s*\n+', section.strip())
        
        # 빈 블록 제거
        data_blocks = [block.strip() for block in data_blocks if block.strip()]
        
        if not data_blocks:
            continue
            
        print(f"섹션 {i+1}: {len(data_blocks)}개의 데이터 블록")
        
        # 각 섹션을 별도 파일로 저장
        section_file = output_path / f"section_{i+1:03d}.txt"
        
        with open(section_file, 'w', encoding='utf-8') as f:
            f.write(f"=== 섹션 {i+1} ===\n\n")
            
            for j, block in enumerate(data_blocks):
                f.write(f"--- 데이터 블록 {j+1} ---\n")
                f.write(block)
                f.write("\n\n")
        
        # 각 데이터 블록을 별도 파일로도 저장
        block_dir = output_path / f"section_{i+1:03d}_blocks"
        block_dir.mkdir(exist_ok=True)
        
        for j, block in enumerate(data_blocks):
            block_file = block_dir / f"block_{j+1:03d}.txt"
            with open(block_file, 'w', encoding='utf-8') as f:
                f.write(block)
    
    print(f"분할 완료! 결과는 {output_dir} 디렉토리에 저장되었습니다.")

def main():
    input_file = "/data/aiuser3/LegalAI-DataPipeline/spa_real_data.txt"
    output_dir = "/data/aiuser3/LegalAI-DataPipeline/split_data"
    
    print("파일 분할을 시작합니다...")
    split_file_by_separator(input_file, output_dir)

if __name__ == "__main__":
    main()
