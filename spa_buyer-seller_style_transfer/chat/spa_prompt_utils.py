# Context 버전 선택을 위한 동적 import
def _get_spa_term_context(use_context_v2=False):
    """SPA_TERM_CONTEXT를 동적으로 가져오는 함수"""
    if use_context_v2:
        try:
            from spa_term_context_v2 import SPA_TERM_CONTEXT
        except ImportError:
            # spa_term_context_v2가 없으면 기본 버전 사용
            from spa_term_context import SPA_TERM_CONTEXT
    else:
        from spa_term_context import SPA_TERM_CONTEXT
    return SPA_TERM_CONTEXT

def create_enhanced_prompt(user_message, selected_options, selected_tasks=None, task_params=None, use_context_v2=False):
    """
    선택된 SPA 항목(selected_options)에 따라,
    저장된 전문가 컨텍스트(SPA_TERM_CONTEXT)를 주입하여 프롬프트를 최적화하는 함수
    
    Args:
        user_message (str): 사용자 질문
        selected_options (list): 선택된 SPA 분석 항목들
        selected_tasks (list): 선택된 작업 유형들
        task_params (dict): 작업별 파라미터 (예: style_target_orientation, tone_target_score 등)
    
    Returns:
        str: 강화된 프롬프트
    """
    # Context 버전 선택
    SPA_TERM_CONTEXT = _get_spa_term_context(use_context_v2)

    # --- 유틸: 샘플 선별 로직 ---
    def select_samples_for_style(option_context, target_orientation, k=2):
        # target_orientation: 'seller' -> 점수 4,3 / 'buyer' -> 점수 0,1 우선
        if not option_context or not option_context.get("samples"):
            return []
        samples = option_context["samples"]
        priority = [4, 3] if target_orientation == "seller" else [0, 1]
        # 인접 점수만 선택 (있다면)
        selected = [s for p in priority for s in samples if s.get("score") == p]
        return selected[:k]

    def select_samples_for_tone(option_context, target_score, k=2):
        # target_score: 0.0~4.0, 점수 차이 절대값 기준으로 가까운 것부터 k개 선택
        if not option_context or not option_context.get("samples"):
            return []
        samples = option_context["samples"]
        # 안전 처리: score 없는 샘플 제외
        scored = [s for s in samples if isinstance(s.get("score"), (int, float))]
        scored.sort(key=lambda s: abs(float(s["score"]) - float(target_score)))
        return scored[:k]

    # --- 1. 작업(Task) 지침 생성 ---
    task_instruction = ""
    if selected_tasks:
        task_instruction = f"""
        ### 수행할 작업: {', '.join(selected_tasks)}

        작업별 지침:
        """
        for task in selected_tasks:
            if task == "매수인/매도인 친화 판단":
                task_instruction += "- **매수인/매도인 친화 판단:** 각 조항이 매수인에게 유리한지 매도인에게 유리한지 분석하고 점수를 제공하세요.\n"
                task_instruction += "  - (절차) 1) 현재 점수(0~4) 평가 및 근거, 2) 핵심 리스크 요약.\n"
            elif task == "매수인 ↔ 매도인 전환":
                target = None
                k = 2
                if task_params:
                    target = task_params.get("style_target_orientation")
                    k = int(task_params.get("style_k", 2))
                human_target = "매도인 친화" if target == "seller" else ("매수인 친화" if target == "buyer" else "미지정")
                task_instruction += "- **매수인 ↔ 매도인 전환 (Style Transfer):** 입력 조항을 목표 성향으로 변환하세요.\n"
                task_instruction += f"  - (목표 성향) {human_target}. 4점(매도인) 또는 0점(매수인) 샘플을 우선 참조하세요.\n"
                task_instruction += f"  - (절차) 1) 현재 점수(0~4) 평가, 2) 핵심 쟁점 반영, 3) 목표 성향으로 재작성, 4) 변경 포인트 bullet 요약.\n"
            elif task == "Tone Up-Down":
                k = 2
                target_score = None
                if task_params:
                    target_score = task_params.get("tone_target_score")
                    k = int(task_params.get("tone_k", 2))
                task_instruction += "- **Tone Up-Down:** 조항의 강도를 조정하세요.\n"
                if target_score is not None:
                    task_instruction += f"  - (목표 점수) {target_score}점에 맞추되, 현재 점수를 평가한 뒤 필요 시 ±0.5~1.0 범위에서 조정하세요.\n"
                else:
                    task_instruction += "  - (목표 점수 미지정) 현재 점수를 평가한 뒤 ±0.5~1.0 범위에서 적정 조정하세요.\n"
                task_instruction += "  - (절차) 1) 현재 점수(0~4) 평가, 2) 조정 방향/폭 근거 제시, 3) 핵심/입장 반영해 수정, 4) 전후 비교.\n"
        task_instruction += "\n"
    else:
        # 작업이 선택되지 않은 경우 기본 분석 지침
        task_instruction = f"""
        ### 수행할 작업: 조항 분석 (Default)
        * **지침:** 사용자의 '요청 사항'과 '검토 대상'을 바탕으로, 해당 조항의 법적 위험, 협상 포인트, 매수인/매도인 친화도를 분석하세요.
        """

    # --- 2. 기본 프롬프트 구성 ---
    
    # selected_options가 없는 '단순 질문'의 경우
    if not selected_options and not selected_tasks:
        return f"""
        당신은 M&A 전문 변호사입니다.
        다음 질문에 대해 법률적 관점에서 명확하고 구체적으로 답변해주세요.

        질문: {user_message}
        """
    
    analysis_focus = "없음"
    if selected_options:
        analysis_focus = ", ".join(selected_options)

    enhanced_prompt = f"""
    당신은 M&A 주식매매계약(SPA) 전문 변호사입니다.

    {task_instruction}

    사용자 질문:
    ---
    {user_message}
    ---

    분석 시, 다음의 M&A 협상 핵심 쟁점(매도인 vs 매수인 입장)을 반드시 참고하여
    전문가적이고 실용적인 조언을 제공해주세요.
    (중점 분석 항목: {analysis_focus})
    """
    
    # --- 3. 선택된 항목(컨텍스트) 주입 + 작업별 샘플 선별 ---
    if selected_options:
        for option in selected_options:
            if option in SPA_TERM_CONTEXT:
                context = SPA_TERM_CONTEXT[option]
                enhanced_prompt += f"""

                ### 중점 분석 항목: "{option}"

                * **핵심 쟁점:** {context['핵심']}
                * **매도인(Seller) 입장:** {context['매도인 입장']}
                * **매수인(Buyer) 입장:** {context['매수인 입장']}
                """
                
                # 기본 전체 샘플 목록 (참고용)
                full_samples = context.get("samples", [])

                # 작업별로 참조할 샘플 선별
                filtered_samples = []
                if selected_tasks and task_params:
                    if "매수인 ↔ 매도인 전환" in selected_tasks and task_params.get("style_target_orientation"):
                        filtered_samples = select_samples_for_style(
                            context,
                            task_params.get("style_target_orientation"),
                            int(task_params.get("style_k", 2))
                        )
                    if "Tone Up-Down" in selected_tasks and task_params.get("tone_target_score") is not None:
                        # tone은 style과 병행 선택될 수 있으므로 누적하며 중복 제거
                        tone_selected = select_samples_for_tone(
                            context,
                            float(task_params.get("tone_target_score")),
                            int(task_params.get("tone_k", 2))
                        )
                        # 중복 제거
                        seen = set(id(s) for s in filtered_samples)
                        for s in tone_selected:
                            if id(s) not in seen:
                                filtered_samples.append(s)
                                seen.add(id(s))
                
                # 표시 우선순위: 선별 샘플이 있으면 그걸, 없으면 전체를 보여줌
                show_samples = filtered_samples if filtered_samples else full_samples

                if show_samples:
                    enhanced_prompt += "\n                * **참고 조항 샘플 (점수: 0=매수인 친화 ~ 2=중립 ~ 4=매도인 친화):**\n"
                    for sample in show_samples:
                        if sample.get("clause") is None:
                            continue
                        score = sample.get("score")
                        score_desc = "매수인 친화 (0점)" if score == 0 else \
                                     "매수인 친화 (1점)" if score == 1 else \
                                     "중립 (2점)" if score == 2 else \
                                     "매도인 친화 (3점)" if score == 3 else \
                                     "매도인 친화 (4점)"
                        clause_oneline = ' '.join(sample['clause'].split())
                        enhanced_prompt += f"                    - ({score_desc}): `{clause_oneline}`\n"

                enhanced_prompt += "                * **적용:** 위 쟁점과 참조 샘플을 바탕으로 사용자 질문의 맥락에서 법적 위험, 협상 포인트, 또는 조문 수정 방안을 분석하십시오."
            else:
                # SPA_TERM_CONTEXT에 없는 항목일 경우 (예: "기타")
                enhanced_prompt += f"""

                ### 중점 분석 항목: "{option}"
                * **적용:** "{option}"의 관점에서 사용자 질문의 맥락을 분석하십시오.
                """
    
    # --- 4. 출력 형식 및 단계 강제 ---
    steps = []
    if selected_tasks:
        if "매수인/매도인 친화 판단" in selected_tasks:
            steps.append("1) 현재 조항의 점수(0~4)를 평가하고 근거를 2~3줄로 제시")
        if "매수인 ↔ 매도인 전환" in selected_tasks:
            target = None
            if task_params:
                target = task_params.get("style_target_orientation")
            human_target = "매도인 친화(4점 근접)" if target == "seller" else ("매수인 친화(0점 근접)" if target == "buyer" else "목표 성향")
            steps.append(f"2) 목표 성향 {human_target}에 맞게 조항을 재작성")
            steps.append("3) 변경 포인트를 bullet로 3~5개 요약")
        if "Tone Up-Down" in selected_tasks:
            tgt = None
            if task_params:
                tgt = task_params.get("tone_target_score")
            if tgt is not None:
                steps.append(f"4) 목표 점수({tgt})에 맞게 표현 강도 조정")
            else:
                steps.append("4) 현재 점수를 기준으로 ±0.5~1.0 범위에서 적정 조정")
            steps.append("5) Before/After를 짧게 대비 표시")
    
    if steps:
        enhanced_prompt += "\n\n아래 단계를 순서대로 수행하세요:" + "\n" + "\n".join([f"- {s}" for s in steps])

    enhanced_prompt += "\n\n답변은 구체적이고, 매도인/매수인 중 누구의 입장에서 더 유리한지, 그리고 수정이 필요하다면 어떻게 해야 하는지 명확히 설명해주세요."
    
    return enhanced_prompt

# create_simple_prompt 함수는 create_enhanced_prompt에서 selected_options가 없을 때 동일한 기능을 제공하므로 제거

def get_available_spa_options():
    """사용 가능한 SPA 분석 옵션들을 반환"""
    return list(SPA_TERM_CONTEXT.keys()) + ["기타"]
