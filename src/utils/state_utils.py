#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
State Utils - 애플리케이션 상태 관리 유틸리티
"""

from typing import Dict, Any, List
from datetime import datetime


class StateUtils:
    """애플리케이션 상태 관리 유틸리티 기능을 제공하는 클래스"""
    
    @staticmethod
    def init_app_state() -> Dict[str, Any]:
        """애플리케이션의 초기 상태를 생성합니다."""
        return {
            "user_session": {
                "user_id": None,
                "name": None,
                "auth": False,
                "session_key": None
            },
            "chat_history": [],
            "source_bucket": {},
            "video_history": [],
            "recommend_history": [],
            "evidence_library": [],
            "glossary": StateUtils.get_default_glossary(),
            "preset_sources": StateUtils.get_default_sources()
        }

    @staticmethod
    def get_default_sources() -> List[Dict]:
        """초기 근거 자료 목록을 정의합니다."""
        return [
            {"title": "CrossFit Level 1 Training Guide (PDF)", "url": "https://example.com/cf-level1.pdf"},
            {"title": "CrossFit Journal - Movement Standards", "url": "https://journal.crossfit.com/example-standards"},
            {"title": "USAW Technique Guide", "url": "https://usaweightlifting.org/example-technique"}
        ]

    @staticmethod
    def get_default_glossary() -> List[Dict]:
        """크로스핏 관련 용어집 초기 데이터를 정의합니다."""
        return [
            {"term": "박스", "category": "용어", "desc": "크로스핏 체육관을 의미"},
            {"term": "WOD", "category": "용어", "desc": "Workout of the Day, 하루 운동 프로그램"},
            {"term": "온램프", "category": "프로그램", "desc": "초보자 적응 과정"}
        ]

    @staticmethod
    def now_iso() -> str:
        """현재 시간을 ISO 8601 형식 문자열로 반환합니다."""
        return datetime.now().isoformat(timespec="seconds")

    @staticmethod
    def reset_user_session(app_state: Dict[str, Any]):
        """사용자 세션을 초기화합니다."""
        app_state["user_session"] = {
            "user_id": None,
            "name": None,
            "auth": False,
            "session_key": None
        }
        app_state["chat_history"] = []
        app_state["source_bucket"] = {}
        app_state["video_history"] = []
        app_state["recommend_history"] = []
        app_state["evidence_library"] = []

    @staticmethod
    def is_authenticated(app_state: Dict[str, Any]) -> bool:
        """사용자가 인증되었는지 확인합니다."""
        return app_state.get("user_session", {}).get("auth", False)