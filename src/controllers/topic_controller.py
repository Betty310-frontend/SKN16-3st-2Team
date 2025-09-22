#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Topic Controller - 주제별 기능 관련 비즈니스 로직을 처리하는 컨트롤러
"""

from typing import Dict, Any, List
from ..models.qa_model import QAModel


class TopicController:
    """주제별 기능 관련 비즈니스 로직을 처리하는 컨트롤러"""
    
    def __init__(self, qa_model: QAModel, app_state: Dict[str, Any]):
        """
        TopicController 초기화
        
        Args:
            qa_model (QAModel): QA 모델 인스턴스
            app_state (Dict[str, Any]): 애플리케이션 상태
        """
        self.qa_model = qa_model
        self.app_state = app_state

    def search_glossary(self, query: str, category: str) -> str:
        """
        크로스핏 용어집에서 검색을 수행합니다.
        
        Args:
            query (str): 검색어
            category (str): 검색 카테고리
            
        Returns:
            str: 검색 결과
        """
        glossary = self.app_state.get("glossary", [])
        return self.qa_model.search_glossary(glossary, query, category)

    def get_diet_recovery_guide(self, weight_band: str, pref: str, allergy: str) -> str:
        """
        사용자 정보에 기반한 식단 및 회복 가이드라인을 제공합니다.
        
        Args:
            weight_band (str): 체중대
            pref (str): 식성 선호도
            allergy (str): 알레르기 정보
            
        Returns:
            str: 가이드 정보
        """
        if not self.app_state["user_session"]["auth"]:
            return "로그인 후 이용해 주세요."

        return "\n".join([
            f"- 체중대: {weight_band}, 선호: {pref}, 알레르기: {allergy or '없음'}",
            "- 운동 후: 유청 단백질 + 바나나 + 물 500ml 섭취",
            "- 식단 예시: 단백질 중심 식사(닭가슴살/두부), 복합탄수화물(현미/고구마), 채소 다량 섭취",
            "- 회복: 하루 7~9시간 충분한 수면, 가벼운 스트레칭으로 혈액 순환 및 근육 회복 촉진"
        ])

    def get_certification_info(self) -> str:
        """
        크로스핏 관련 인증 정보를 제공합니다.
        
        Returns:
            str: 인증 정보
        """
        return "\n".join([
            "- 온램프 프로그램: 2~4주 과정으로 크로스핏의 기초 동작, 용어, 안전 수칙 교육을 제공하여 초보자가 적응하도록 돕습니다.",
            "- 레벨 테스트: 기본적인 기술 숙련도와 기초 체력을 평가하여 현재 실력 수준을 파악합니다.",
            "- 자격 인증: 교육 수강 후 평가를 통과하면 자격을 얻게 되며, 정기적인 갱신이 필요합니다."
        ])

    def get_mentoring_preset(self, topic: str) -> str:
        """
        선택된 주제에 대한 멘토링 메시지를 제공합니다.
        
        Args:
            topic (str): 멘토링 주제
            
        Returns:
            str: 멘토링 메시지
        """
        presets = {
            "첫 수업 긴장": "호흡을 길게 가져가세요. 첫 세트는 60% 강도로 시작하고, 코치와 아이컨택으로 신호를 맞춰보세요.",
            "페이스 조절": "초반엔 70% 정도로 출발하여 체력을 아끼세요. 호흡 리듬은 4초 흡기 - 4초 호기를 유지하고, 타이머를 활용해 체크포인트를 설정하는 것이 좋습니다.",
            "목표 설정": "4주 주기로 작은 소목표를 설정하세요. 동작의 기술 습득을 우선하고, 주당 3회 이상 꾸준히 운동하여 일관성을 유지하는 것이 중요합니다."
        }
        
        msg = presets.get(topic, "필요한 주제를 선택해 주세요.")
        
        # 챗봇 히스토리에 추가
        self.app_state.setdefault("chat_history", []).append({
            "role": "assistant", 
            "content": f"[멘토링] {msg}"
        })
        
        return f"챗봇에 전송됨: {msg}"

    def convert_weight(self, value: str, unit: str) -> str:
        """
        킬로그램과 파운드 간의 무게 단위를 변환합니다.
        
        Args:
            value (str): 변환할 값
            unit (str): 변환 방향
            
        Returns:
            str: 변환 결과
        """
        try:
            v = float(value)
        except ValueError:
            return "숫자를 입력해 주세요."

        if unit == "kg→lb":
            return f"{v:.2f} kg = {v * 2.2046226218:.2f} lb"
        elif unit == "lb→kg":
            return f"{v:.2f} lb = {v / 2.2046226218:.2f} kg"
        else:
            return "올바른 단위 변환 방향을 선택해 주세요."