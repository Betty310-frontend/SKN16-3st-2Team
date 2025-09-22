#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recommendation Controller - 개인 맞춤 추천 관련 비즈니스 로직을 처리하는 컨트롤러
"""

import json
from typing import List, Tuple, Dict, Any
from datetime import datetime


class RecommendationController:
    """개인 맞춤 추천 관련 비즈니스 로직을 처리하는 컨트롤러"""
    
    def __init__(self, app_state: Dict[str, Any]):
        """
        RecommendationController 초기화
        
        Args:
            app_state (Dict[str, Any]): 애플리케이션 상태
        """
        self.app_state = app_state

    def generate_recommendation(self, level: str, goal: str, freq: int, gear: List[str]) -> Tuple:
        """
        사용자의 운동 수준에 맞는 맞춤형 운동 계획을 생성합니다.
        
        Args:
            level (str): 경험 수준
            goal (str): 운동 목표
            freq (int): 주당 운동 횟수
            gear (List[str]): 사용 가능한 장비
            
        Returns:
            Tuple: (추천 결과 JSON, 상태 메시지)
        """
        if not self.app_state["user_session"]["auth"]:
            return "로그인 후 이용해 주세요.", ""

        summary = (
            f"{level} 수준, 목표: {goal}, 주 {int(freq)}회, "
            f"장비: {', '.join(gear) if gear else '없음'}"
        )
        
        plan = {
            "summary": summary,
            "wod": [
                "WOD A: 파워클린 테크닉 + AMRAP 10분(스윙/버피/싱글언더)",
                "WOD B: 스쿼트클린 EMOM 10분 + 코어 서킷",
                "WOD C: 파워스내치 포지션 드릴 + 컨디셔닝 인터벌"
            ],
            "stretch": ["둔근/햄스트링 스트레칭 5분", "흉추 모빌리티 3분", "발목 가동성 3분"],
            "notes": ["통증 발생 시 중단", "무게보다 기술 우선", "세트 간 충분한 휴식"]
        }
        
        # 추천 히스토리 업데이트
        self.app_state.setdefault("recommend_history", []).append({
            "ts": datetime.now().isoformat(timespec="seconds"),
            "inputs": [level, goal, int(freq), gear],
            "plan": plan
        })

        # 챗봇 히스토리에도 추가
        to_chat = (
            f"[개인추천]\n{plan['summary']}\n- " +
            "\n- ".join(plan["wod"]) +
            "\n스트레칭: " + ", ".join(plan["stretch"])
        )
        self.app_state.setdefault("chat_history", []).append({
            "role": "assistant", 
            "content": to_chat
        })

        return json.dumps(plan, ensure_ascii=False, indent=2), "챗봇 히스토리에 전송되었습니다."