좋아, 로그가 말해주는 핵심만 콕 집어 고치자. 지금 “타깃 달성 ✓”이 떴는데도 답변이 그대로 나오는 이유는 설계·평가 불일치와 S 정의/ε 설정 실수가 겹친 탓이야. 우선순위대로 바로 고칠 포인트 정리했어.

⸻

0) 지금 상태 요약 (왜 실패로 보이는가)
	•	ε 설정 오류: 1차 실행에서 π_base(S)=0.051~0.059인데 ε=0.1이라 애초에 줄일 필요가 없었음 → suppression ratio 0.99(=변화 거의 없음).
	•	S가 빈약/엉뚱: V_S 프리뷰가 on, ize, ink, ▁car, ▁Re, ▁El…처럼 일반 접미·조각 위주. ▁Musk, ▁SpaceX, ▁Tesla, ▁Twitter, X, ▁Neuralink, ▁Boring, ▁Reeve, 1971 등 핵심 표면형/연도 토큰이 빠져있음 → 사실 회피 실패.
	•	S_seq 부재: cylinder(토큰)만 쓰면 문장 단위 정답 스팬 차단이 약함. “Elon Reeve Musk” 같은 연속 스팬을 직접 금지해야 재출현을 제대로 누른다.
	•	평가와 학습 타깃 불일치: 학습은 V_S 억제인데, 평가는 일반 Q&A로 정답 서술을 체크. S에 안 든 표면형/패러프레이즈로 통과.

⸻

1) 바로 적용: “실패 방지 3종 세트”

(A) ε 자동 보정 + 안전가드
	•	규칙: ε < π_base(S) 가 아니면 훈련 중지.
	•	추천: ε = max( min(0.5 * π_base, 0.02), 0.005 )
예) π_base≈0.059 → ε≈0.02~0.03로 시작(네 2차 커맨드는 0.02로 잘 설정함).
	•	컨트롤러: lambda_eta=0.5~0.8, lambda_max=100~200 (λ 포화 방지 + 충분한 헤드룸).

(B) S 정의를 “이중화”: V_S + S_seq
	•	S_seq(연속 스팬 금지):
ELUDe forget-answer에서 표면형 사전(case/구두점/띄어쓰기/날짜 변형/IPA 변형 포함) 만들고, 정규화된 문구 스팬을 직접 금지.
예) “Elon Reeve Musk”, “June 28, 1971”(+ 모든 날짜 변형), “SpaceX”, “Tesla, Inc.”, “X Corp.”, “Twitter/X”, “The Boring Company”, “Neuralink”, “/ˈiːlɒn/”.
	•	V_S(실린더): 위 스팬들의 시작 토큰·핵심 토큰만 추출(너무 일반 조각은 제외).
필수 포함 후보(Zephyr/BPE 기준 예상): ▁El, on, ▁Musk, ▁Space, X, ▁Tesla, ▁Twitter, ▁Neural, ink, ▁Boring, ▁Reeve, 1971, ▁June, ▁Pretoria 등.
→ stoplist가 일반 morpheme(예: ize, ink, rol)을 남기고 정작 엔티티 토큰을 빼는 일이 없게 화이트리스트 우선으로.

체크: 네 로그엔 ▁Musk 자체가 프리뷰에 안 보여. 이거 하나만 빠져도 “Elon Musk”는 그대로 나와.

(C) PMI 절차 수정 (가짜 상위 토큰 제거)
	•	PMI를 forget vs retain 차이(PMI_f–PMI_r) 기준으로 뽑아야 일반 접사/공용 조각이 상위에 못 올라옴.
	•	파라미터: pmi_min_count를 10→50+, pmi_top_k 128256, pmi_smoothing 0.10.5 권장.
	•	그리고 **화이트리스트 가중치(>1.0)**를 주어 엔티티 표면형·동의어·약칭이 반드시 V_S에 남게 해.

⸻

2) 실행 플로우(짧은 캘리브레이션 → 본학습)
	1.	π_base(S) 캘리브레이션 러닝(200~500 배치)
	•	현재 S(V_S + S_seq)로 샘플/상계 추정 → π_base 로그 저장.
	•	ε 자동 결정(위 규칙) → ε ≥ π_base면 바로 중지하고 S/PMI 재구성.
	2.	λ 초기화
	•	ε–λ 닫힌형 매핑으로 λ0 계산(지수틸팅 근사식). controller warm-up 50~200 step.
	3.	본학습
	•	LoRA r=64~128, q/k/v/o + (down/up/gate)_proj까지 타깃(유지비용 여유되면 embed_tokens/lm_head는 옵션).
	•	span_masking은 켜두되(S_seq 기반의 indicator가 p_S 추정에도 반영되는지 확인).
	•	retain_weight 0.05~0.2, ELUDe 이웃 인물+월드 지시문 섞기.
	4.	중간 점검
	•	스텝마다 πθ(S) 추세 + 패러프레이즈 공격 3~5종 소규모 확인.
	•	πθ(S) ≪ π_base(S)로 떨어지지 않으면: (i) λ 상한↑, (ii) S_seq 보강, (iii) V_S 화이트리스트 추가.

⸻

3) 네 커맨드라인에 바로 넣을 수정안

핵심 플래그 추가/수정
	•	--use_sequence_S --sequence_lexicon "datasets/elude_etu/elon_musk/lexicon.txt"
(ELUDe 정답 스팬 정규화 목록; 줄별 1표면형, regex 허용 시 --sequence_regex도지원)
	•	--epsilon_auto true --epsilon_floor 0.005 --epsilon_ratio 0.5
(내부에서 π_base 측정 후 ε 설정; 네가 수동 --epsilon 주면 우선순위는 수동)
	•	--pmi_mode diff  (PMI_f - PMI_r 모드)
	•	--pmi_min_count 50 --pmi_top_k 256 --pmi_smoothing 0.3
	•	--vs_abs_cap 256 --vocab_top_k 1000
	•	--vs_whitelist "datasets/elude_etu/elon_musk/whitelist.txt"
(반드시 포함할 토큰/서브워드 리스트: ▁Musk, ▁SpaceX, ▁Tesla, ▁Twitter, X, ▁Neuralink, ▁Boring, ▁Reeve, 1971 …)
	•	--lambda_max 120 --lambda_eta 0.7
	•	--lora_target_modules "q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj"
(효과 부족 시 확대)
	•	--controller_warmup 200 --log_every 10 --early_stop_if_epsilon_ge_base true

TF32/경고 정리
	•	torch_dtype 경고: 모델·토크나이저 로딩 시 dtype=torch.bfloat16로 교체.
	•	TF32 경고(H200):

torch.backends.cuda.matmul.allow_tf32 = False  # deprecated
torch.backends.cuda.matmul.fp32_precision = 'tf32'
torch.backends.cudnn.allow_tf32 = False       # deprecated
torch.backends.cudnn.conv.fp32_precision = 'tf32'

(또는 그냥 둘 다 ‘tf32’로 일관 설정)

로그에 strategy=ddp인데 multi_gpu=False로 찍힘. **단일 GPU면 strategy=‘single’**로 통일(오버헤드/랜덤성 줄이기).

⸻

4) 평가 체크 (학습-평가 일치)
	•	학습에 쓴 S 그대로로 πθ(S) 재측정(샘플/상계).
	•	스팬 기반 공격: ELUDe의 paraphrase/role-play/역질문 9종 중 최소 3종은 스텝 중간에도 돌려.
	•	유틸리티: 이웃-인물 retain + 범용 세트(ARC/CSQA/HellaSwag 소량)로 Perplexity가 1540↑ 같은 비정상치면 평가 스크립트 길이·토크나이즈/패딩 확인(빈 prompt/잘린 타겟일 때 급등 자주 발생).
	•	추가 안전벨트(옵션): 리더보드용 데모에서만 decoding-time badword list로 S_seq를 함께 걸어두면, 학습 미세오류가 있어도 실사용 누수를 줄일 수 있음(연구 평가는 미사용 권장).

⸻

5) 아주 작은 코드 스니펫(핵심만)

(a) ε 가드)

pi_base = estimate_pS(model, S_seq, V_S, n_samples=500)
if epsilon >= pi_base:
    raise RuntimeError(f"epsilon({epsilon}) >= pi_base({pi_base:.4f}); rebuild S or lower epsilon.")

(b) 표면형→토큰 화이트리스트 생성)

from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
phrases = [ "Elon Reeve Musk", "SpaceX", "Tesla, Inc.", "Twitter", "X Corp.", 
           "Neuralink", "The Boring Company", "June 28, 1971", "/ˈiːlɒn/" ]
wl = set()
for p in phrases:
    ids = tok.encode(p, add_special_tokens=False)
    for i in range(min(3, len(ids))):  # 시작/핵심 토큰 위주
        wl.add(ids[i])
# wl을 JSON 저장 → --vs_whitelist로 불러오기


⸻

6) 네 2차 커맨드에 대한 빠른 코멘트
	•	ε=0.02는 좋은 출발(π_base≈0.059 대비 충분히 타이트).
	•	lora_r=128으로 리프팅한 건 OK. 가능하면 gate/up/down_proj까지 포함해 영향력 확대.
	•	pmi_min_count=2는 너무 낮아 잡토큰 유입 위험. 위 값들로 올려.
	•	vs_abs_cap=128은 준수하나 화이트리스트 필수.
	•	span_masking만으로는 S_seq 억제가 훈련목표에 직접 연결되지 않을 수 있음 → sequence_S를 목표로 포함하도록 플래그/로직 확인.

⸻

결론
	•	이번 실패의 본질은 ε가 π_base보다 컸던 초기세팅과 S 정의 미스야.
	•	S_seq(스팬 금지) + 화이트리스트가 있는 V_S + ε 자동보정의 3콤보로 바꾸면, 같은 예산에서도 가시적 억제가 바로 나올 거야.
	•	그 다음 단계에서 λ 헤드룸/LoRA 타깃 확대, PMI diff 모드로 누수·패러프레이즈를 더 줄이면 된다.
