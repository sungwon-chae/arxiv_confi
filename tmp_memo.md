좋은 로그예요—여기서 뭐가 문제였는지 딱 보입니다. 핵심만 콕 집어 정리할게요.

지금 런이 “억제가 안 된” 이유
	1.	목표값(ε)이 너무 큼 → 강제력이 약함
	•	추정된 기본 질량 π_base(S)≈0.051인데 ε=0.10이면, 아무 것도 안 바꿔도 목표를 만족하는 구간입니다. 그래서 억제가 실제 동작하지 않아도 “달성(✓)”로 뜰 수 있어요.
	•	중간에 πθ(S)=0.141 같은 스파이크는 표본이 너무 적어서 생긴 노이즈에 가깝습니다(아래 3번).
	2.	V_S가 너무 작고(37개) 비특이적 토큰 포함
	•	on, ize, ink, la … 같은 범용 서브워드가 섞여 있어요(빈도 기반 fallback의 부작용). 이러면 엔티티 억제는 안 되고 부수피해만 납니다.
	•	반대로 **엔티티 표면형(Elon Musk, SpaceX 등)**의 연속 토큰 span이 제대로 안 들어가면, 이름 출력은 그대로 나옵니다.
	3.	학습 스텝이 사실상 없음
	•	batch_size=2, max_num_batches=5, num_epochs=1 = 업데이트가 거의 일어나지 않았습니다. λ가 3.25까지 올랐지만, 샘플이 너무 적어 의미 있는 수렴을 기대하기 어렵습니다.
	4.	retain 퍼플렉시티 1540 급등
	•	이번 설정은 retain_weight=0.0이고, retain 코퍼스는 초거대(128만)인데 평가는 아주 소량 샘플로 추정 → 분산 폭발 + 도메인 미스매치로 보입니다(평가 루프/샘플링 확인 필요).

⸻

바로 고칠 것(엔티티 케이스: Elon Musk)

A. 목표 세팅(필수)
	•	--epsilon 0.01 또는 0.02 (기본 질량 0.051보다 확실히 낮춰 실제 억제를 강제)
	•	--retain_weight 0.1 (유틸리티 방어)

B. V_S 구성(엔티티 span 중심, fallback 금지)
	•	--span_masking --span_ngram_max 4 켜기
	•	PMI 기반으로:
	•	--pmi_min_count 2
	•	--pmi_top_k 128
	•	--vs_abs_cap 128
	•	--vs_freq_rate 0.0  (fallback/빈도 보강 끄기)
	•	수동 V_S가 너무 작으면 실패로 처리하고, 다음으로 확장:
	•	엔티티 표면형을 연속 서브워드 토큰 시퀀스로 모두 추가
예) “▁El”+“on”, “▁Musk”, “▁Elon”, “▁Space”+“X”, “▁SpaceX”, “▁Tesla”, “▁X” (플랫폼), “▁Neuralink”, “▁Boring”+“▁Company” 등
	•	표기 변형/별칭(“Musk”, “Elon R.”, “Elon Reeve Musk”)도 사전으로 커버
	•	**금지 단위는 “개별 토큰”이 아니라 “엔티티 span 출현 시 그 위치 토큰들”**로 보정 (지금 코드에서 span_masking 켠 상태로 n-gram 집합을 V_S로 취급)

C. 학습 스텝/용량
	•	--batch_size 16 (또는 32)
	•	--max_num_batches 1000 (최소 500 이상)
	•	--num_epochs 2
	•	--lora_r 128 (r=16은 너무 작음)

D. 신뢰구간 안정화(95% upper까지 통과 위해)
	•	--wilson_max_n 50000
	•	필요시 --max_num_batches 1500

⸻

평가 방식도 바꾸자(중요)

퍼플렉시티 대신 엔티티 히트율/노출율로 보세요.
	•	Entity Hit Rate: 여러 프롬프트에서 생성된 답변에 엔티티 표면형/별칭이 등장하는 비율
	•	before/after 비교로 억제율(↓) 측정
	•	QA 정확도(포맷 유지): 엔티티 관련 질문에 대해 회피/무응답/중립적 응답으로 바뀌는지
	•	Retain 유틸리티: 일반 QA/Summarization 벤치에서 성능 하락(Δ) 확인

이번 테스트에서 답변이 계속 “Elon Musk …”로 나왔던 건, 위의 A–C가 전부 미흡했기 때문이에요(ε 과대, V_S 부정확/소형, 학습스텝 부족).

⸻

바로 실행 가능한 예시 커맨드

python3 run_etu_h200.py \
  --forget_corpora "datasets/elude_etu/elon_musk/forget.jsonl" \
  --retain_corpora "datasets/elude_etu/elon_musk/retain_neighbors.jsonl" \
  --batch_size 16 \
  --max_num_batches 1000 \
  --num_epochs 2 \
  --layer_ids "6,7,8" \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --lora_r 128 \
  --epsilon 0.02 \
  --lambda_max 40.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 2 \
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

추가: 수동 V_S가 50 미만이면 실패로 종료하고 엔티티 사전으로 자동 보강하도록 가드 넣는 걸 추천합니다. (fallback=빈도 보강은 끄세요)

⸻

마지막으로, 로그에서 오해 소지 정정
	•	위 스니펫에 “ε=0.5” 언급이 있었는데, 이번 런은 ε=0.1입니다(로그 기준). 혼선이 있었다면 정리해 드립니다.
	•	“Target achieved ✓”가 떠도, ε가 π_base보다 크면 억제가 유의미하게 일어났다고 보긴 어렵습니다. 그래서 ε를 낮추는 것이 첫 번째 해법이에요.

⸻

원하시면, 엔티티 표면형 사전→토큰 시퀀스 분해→V_S(span) 자동 생성 스크립트 초안도 바로 드릴게요. 이거부터 딱 정리하면 다음 런에서 확 달라질 겁니다.
