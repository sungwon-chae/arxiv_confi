좋아요—이제 WMdP 대신 ELUDe로 돌릴 거라면, ETU 파이프라인을 이렇게 바꾸면 됩니다. (ELUDe 구성·지표는 업로드 문서 기준 요약 반영)  ￼

⸻

바로 적용 체크리스트
	1.	데이터 폴더 구성

	•	권장 구조:

datasets/elude/
  <entity_slug>/
    forget.jsonl        # target 엔티티 QA
    retain_neighbors.jsonl  # neighbor 엔티티 QA
    retain_world.jsonl      # world knowledge (예: Alpaca류)


	•	각 JSONL 레코드 예:

{"input": "<질문>", "output": "<정답>"}

ETU는 prompt/response도 지원하지만, 위 키를 쓰면 내부 로더에서 매핑만 맞추면 됩니다.

	2.	ETU 입력으로 변환(간단 포맷)

	•	ETU가 현재 폴더를 읽어 한 줄당 “프롬프트→정답” 쌍으로 쓰는 형태라면, 위 JSONL 그대로도 처리되게 dataset_loader 쪽 키 매핑만 확인.
	•	빠른 길: 두 retain 파일을 concat해서 하나의 retain split로 써도 됩니다.

cat retain_neighbors.jsonl retain_world.jsonl > retain_all.jsonl



	3.	V_S(금지집합) 시드 = 엔티티 표면형

	•	엔티티 기반 억제 느낌을 살리려면, 시드 토큰 리스트에 대상 엔티티의 표면형/별칭을 넣고 PMI로 확장하는 게 가장 안정적입니다.
	•	예: ["▁Elon", "▁Musk", "▁Elon▁Musk", "▁Musk’s", "▁Tesla", ...]
	•	구현 팁: --pmi_seed_files 같은 훅이 없으면, 로더에서 시드 토큰을 우선 포함하고 PMI top-k에서 중복 제거하도록 _filter_vs_tokens 앞단에 주입.

	4.	PMI/스톱리스트 세팅(ELUDe 권장값)

	•	엔티티/이름류가 잘 잡히도록 기능어를 강하게 제거하고 top-k를 타이트하게:
	•	--pmi_min_count 3
	•	--pmi_top_k 128 (필요 시 96~160 범위에서 조정)
	•	--vs_abs_cap 128
	•	--vs_freq_rate 0.0  (fallback off: freq 백필 금지)
	•	--span_masking --span_ngram_max 4
	•	스톱리스트에 기능어/타이포그래피: ▁the, ▁and, ▁to, ▁of, ▁in, ▁with, ▁from, " , © , – 등

	5.	Retain을 neighbor+world로 구성

	•	ELUDe 논리의 핵심: Neighbor retain이 유틸리티를 지탱합니다. neighbor를 반드시 retain split에 포함하세요. (논문에서도 neighbor 제거 시 RQ 급감)  ￼

	6.	평가: ELUDe 지표 맞추기(간단판)

	•	Forget Quality(FQ) / Retain Quality(RQ)를 대체 지표로 근사:
	•	FQ: (금지 응답 확률↓) + ROUGE-L(정답과의 거리↑) + Truth Ratio 등을 조화평균 → 최소한 금지 응답 확률과 ROUGE-L는 바로 계산 가능.
	•	RQ: neighbor+world QA 정확도/ROUGE, 또는 ppl 변화.
	•	가능하면 Membership Inference(≈50%), Adversarial Prompt도 간단 버전부터 추가.  ￼

⸻

실행 예시

폴더 예

datasets/elude/elon_musk/forget.jsonl
datasets/elude/elon_musk/retain_neighbors.jsonl
datasets/elude/elon_musk/retain_world.jsonl

커맨드 (현재 성공 설정을 ELUDe에 맞춰 이식)

python3 run_etu_h200.py \
  --forget_corpora "datasets/elude/elon_musk/forget.jsonl" \
  --retain_corpora "datasets/elude/elon_musk/retain_neighbors.jsonl,datasets/elude/elon_musk/retain_world.jsonl" \
  --batch_size 16 \
  --max_num_batches 1000 \
  --num_epochs 2 \
  --layer_ids "6,7,8" \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --lora_r 128 \
  --epsilon 0.03 \
  --lambda_max 40.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 3 \
  --pmi_top_k 128 \
  --pmi_smoothing 1.0 \
  --pmi_max_batches 2000 \
  --vocab_top_k 300 \
  --vs_abs_cap 128 \
  --vs_freq_rate 0.0 \
  --span_masking \
  --span_ngram_max 4 \
  --retain_weight 0.1 \
  --wilson_max_n 50000 \
  --pinsker_cap 0.10 \
  --mixed_precision bf16 \
  --vs_debug \
  --vs_debug_topk 200 \
  --verbose

	•	차이점: ELUDe는 retain이 커서 --max_num_batches, --wilson_max_n을 늘려 95% 상한 안정화.
	•	필요 시 ε=0.028~0.03 사이 미세조정으로 버퍼 확보.

⸻

주의 포인트 (ELUDe 전환 시)
	•	엔티티 표면형 다양성: 띄어쓰기/대소문자/소유격/이명(별칭)을 최대한 커버 → PMI 확장으로 관련 토큰들이 자연스럽게 들어오게 하기.
	•	Fallback 금지(vs_freq_rate=0): PMI가 충분하므로 빈도 백필이 기능어를 끌고 들어오지 않게.
	•	Neighbor Retain 필수: RQ 유지의 핵심입니다. (OPT-OUT 실험에서도 retain=neighbor가 성능을 떠받침)  ￼
	•	평가 스토리 변경: ppl만 보지 말고, FQ/RQ, MIA, Adv를 간단판이라도 반영하면 엔티티 언러닝 스토리가 직관적으로 전달됩니다.  ￼

⸻

한 줄 요약
	•	ELUDe에선 타겟 엔티티 QA를 forget, neighbor+world QA를 retain으로 넣고, 엔티티 표면형을 시드로 PMI 기반 V_S를 뽑아 ε=0.03 전후로 억제하세요.
	•	평가도 ELUDe 방식(FQ/RQ 등)으로 동행하면 논리·실험 모두 깔끔해집니다.  ￼
