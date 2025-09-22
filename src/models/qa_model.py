#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA Model - 질문답변 관련 데이터베이스 작업과 로직을 담당하는 모델
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Any, Optional


class QAModel:
    """QA 관련 데이터베이스 작업을 처리하는 모델 클래스"""
    
    def __init__(self, db_path: str):
        """
        QAModel 초기화
        
        Args:
            db_path (str): SQLite 데이터베이스 파일 경로
        """
        self.db_path = db_path
        self.init_tables()
    
    def init_tables(self):
        """QA 관련 테이블을 초기화합니다."""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()

            # QA 로그
            cur.execute("""
            CREATE TABLE IF NOT EXISTS qa_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                question TEXT,
                answer TEXT,
                ts TEXT
            )
            """)
            
            conn.commit()

    def log_qa(self, email: str, question: str, answer: str):
        """
        사용자 QA 로그를 기록합니다.
        
        Args:
            email (str): 사용자 이메일
            question (str): 질문
            answer (str): 답변
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO qa_logs (email, question, answer, ts) VALUES (?, ?, ?, ?)",
                (email, question, answer, datetime.now().isoformat())
            )
            conn.commit()

    def get_user_qa_history(self, email: str, limit: int = 50) -> List[Dict[str, Any]]:
        """
        사용자의 QA 히스토리를 조회합니다.
        
        Args:
            email (str): 사용자 이메일
            limit (int): 조회할 최대 개수
            
        Returns:
            List[Dict[str, Any]]: QA 히스토리 리스트
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT question, answer, ts FROM qa_logs WHERE email=? ORDER BY ts DESC LIMIT ?",
                (email, limit)
            )
            rows = cur.fetchall()
            
            return [
                {
                    "question": row[0],
                    "answer": row[1],
                    "timestamp": row[2]
                }
                for row in rows
            ]

    @staticmethod
    def generate_topic_query(topic: str) -> str:
        """
        주제에 따른 자동 쿼리를 생성합니다.
        
        Args:
            topic (str): 주제명
            
        Returns:
            str: 생성된 쿼리
        """
        import random
        
        topic_queries = {
            "용어/규칙/운동법": [
                "크로스핏의 기본 용어와 규칙에 대해 설명해주세요.",
                "크로스핏 운동법의 기본 원리와 주요 운동들을 알려주세요.",
                "WOD(Workout of the Day)의 구성과 스케일링 방법을 설명해주세요.",
                "크로스핏 박스에서 지켜야 할 안전 규칙과 에티켓을 알려주세요."
            ],
            "식단/회복": [
                "크로스핏 운동 후 효과적인 식단과 회복 방법을 알려주세요.",
                "운동 전후 영양 섭취 가이드라인을 제공해주세요.",
                "근육 회복을 위한 수면과 휴식의 중요성을 설명해주세요.",
                "크로스핏 선수들의 일반적인 식단 패턴과 보충제 사용법을 알려주세요."
            ],
            "인증/챌린지 안내": [
                "크로스핏 레벨 1 인증 과정과 자격요건을 설명해주세요.",
                "크로스핏 오픈(CrossFit Open) 참가 방법과 준비 과정을 알려주세요.",
                "크로스핏 박스에서 진행하는 챌린지와 대회 정보를 제공해주세요.",
                "크로스핏 코치 자격증 취득 과정과 커리어 패스를 설명해주세요."
            ],
            "멘토링(초보 심리/동기)": [
                "크로스핏 초보자가 겪는 심리적 어려움과 극복 방법을 알려주세요.",
                "운동 동기를 유지하고 지속적으로 발전하는 방법을 제공해주세요.",
                "크로스핏 커뮤니티에 적응하고 관계를 형성하는 팁을 알려주세요.",
                "운동 목표 설정과 달성을 위한 체계적인 접근법을 설명해주세요."
            ]
        }
        
        queries = topic_queries.get(topic, ["크로스핏에 대해 알려주세요."])
        return random.choice(queries)

    @staticmethod
    def search_glossary(glossary: List[Dict], query: str, category: str) -> str:
        """
        크로스핏 용어집에서 검색을 수행합니다.
        
        Args:
            glossary (List[Dict]): 용어집 데이터
            query (str): 검색어
            category (str): 검색 카테고리
            
        Returns:
            str: 검색 결과
        """
        q_norm = (query or "").strip().lower()
        cat_str = str(category or "전체")
        if cat_str not in {"전체", "용어", "프로그램"}:
            cat_str = "전체"

        rows = []
        for item in glossary:
            ok_q = (not q_norm) or (q_norm in item["term"].lower()) or (q_norm in item["desc"].lower())
            ok_c = (cat_str == "전체") or (item["category"] == cat_str)

            if ok_q and ok_c:
                rows.append(f"- {item['term']} ({item['category']}): {item['desc']}")

        return "\n".join(rows) if rows else "결과가 없습니다."