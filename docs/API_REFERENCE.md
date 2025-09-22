# API 참조 문서

이 문서는 CrossFit 코칭 데모 애플리케이션의 주요 함수와 클래스에 대한 API 참조를 제공합니다.

## 🔧 핵심 함수

### 데이터베이스 관리

#### `init_userdb()`
사용자 데이터베이스를 초기화합니다.
- **매개변수**: 없음
- **반환값**: 없음
- **설명**: users, session_logs, qa_logs 테이블을 생성하고 기본 계정을 설정합니다.

#### `get_user(email: str)`
이메일로 사용자 정보를 조회합니다.
- **매개변수**: 
  - `email (str)`: 조회할 사용자 이메일
- **반환값**: `tuple` 또는 `None`
- **설명**: 사용자가 존재하면 (email, nickname, password_hash, role) 튜플 반환

#### `login_user(email: str, pwd: str)`
사용자 로그인을 처리합니다.
- **매개변수**:
  - `email (str)`: 사용자 이메일
  - `pwd (str)`: 비밀번호
- **반환값**: `(session_dict, message)` 튜플
- **설명**: 로그인 성공 시 세션 정보와 환영 메시지 반환

### VectorDB 관리

#### `initialize_vectordb()`
ChromaDB 벡터 데이터베이스를 초기화합니다.
- **매개변수**: 없음
- **반환값**: `Chroma` 객체 또는 `None`
- **설명**: PDF 파일들을 로드하여 임베딩을 생성하고 벡터 DB에 저장

#### `load_existing_vectordb()`
기존 벡터 데이터베이스를 로드합니다.
- **매개변수**: 없음  
- **반환값**: `Chroma` 객체 또는 `None`
- **설명**: 기존에 생성된 ChromaDB를 메모리에 로드

### 챗봇 기능

#### `send_chat(user_msg: str, qa_chain)`
사용자 질문에 대한 챗봇 응답을 생성합니다.
- **매개변수**:
  - `user_msg (str)`: 사용자 질문
  - `qa_chain`: LangChain QA 체인 객체
- **반환값**: `(chat_history, status, links_update, evidence_update)` 튜플
- **설명**: RAG를 사용하여 PDF 문서 기반 답변 생성

#### `download_history()`
챗봇 대화 기록을 JSON 파일로 다운로드합니다.
- **매개변수**: 없음
- **반환값**: `gr.update` 객체
- **설명**: 현재 세션의 대화 기록을 JSON 형태로 저장

### 영상 분석

#### `analyze_video(pose_type: str, video: str)`
업로드된 운동 영상을 분석합니다.
- **매개변수**:
  - `pose_type (str)`: 분석할 운동 자세 유형
  - `video (str)`: 업로드된 비디오 파일 경로
- **반환값**: `(user_video, ref_video, metrics, coaching, history)` 튜플
- **설명**: 현재는 모킹 데이터를 반환 (실제 AI 분석 기능은 추후 구현)

### 추천 시스템

#### `gen_recommend(level: str, goal: str, freq: int, gear: List[str])`
개인 맞춤 운동 계획을 생성합니다.
- **매개변수**:
  - `level (str)`: 운동 수준 ("초보", "중급", "상급")
  - `goal (str)`: 운동 목표
  - `freq (int)`: 주당 운동 횟수
  - `gear (List[str])`: 사용 가능한 장비 목록
- **반환값**: `(plan_json, status_message)` 튜플
- **설명**: 사용자 입력을 바탕으로 JSON 형태의 운동 계획 생성

### 검색 기능

#### `search_glossary(q: str, cat: str)`
용어집에서 키워드를 검색합니다.
- **매개변수**:
  - `q (str)`: 검색 키워드
  - `cat (str)`: 검색 카테고리 ("전체", "용어", "프로그램")
- **반환값**: `str` (마크다운 형식의 검색 결과)
- **설명**: 용어명과 설명에서 키워드를 검색하여 결과 반환

### 유틸리티 함수

#### `convert_weight(value: str, unit: str)`
무게 단위를 변환합니다.
- **매개변수**:
  - `value (str)`: 변환할 무게 값
  - `unit (str)`: 변환 방향 ("kg→lb" 또는 "lb→kg")
- **반환값**: `str` (변환 결과 문자열)
- **설명**: 킬로그램과 파운드 간의 무게 변환

#### `find_free_port(start: int = 7860, end: int = 7960)`
사용 가능한 네트워크 포트를 찾습니다.
- **매개변수**:
  - `start (int)`: 검색 시작 포트
  - `end (int)`: 검색 종료 포트
- **반환값**: `int` 또는 `None`
- **설명**: 지정된 범위에서 사용 가능한 포트 번호 반환

## 🏗️ 주요 클래스

### 전역 상태 관리
애플리케이션은 `app` 전역 딕셔너리를 사용하여 상태를 관리합니다:

```python
app = {
    "user_session": {...},      # 현재 로그인 사용자 정보
    "chat_history": [...],      # 챗봇 대화 기록
    "source_bucket": {...},     # 중복 제거된 근거 자료
    "video_history": [...],     # 영상 분석 기록
    "recommend_history": [...], # 추천 기록
    "evidence_library": [...],  # 전체 근거 자료 라이브러리
    "glossary": [...],         # 용어집
    "preset_sources": [...]    # 기본 근거 자료
}
```

## 🔒 보안 고려사항

- 비밀번호는 SHA-256 해시로 저장
- 세션 키는 UUID를 사용하여 고유성 보장
- API 키는 환경 변수로 관리
- SQLite 데이터베이스는 로컬 파일 시스템에 저장

## 🚀 확장 가능성

- 영상 분석 기능은 실제 AI 모델로 교체 가능
- 추천 시스템은 머신러닝 모델로 고도화 가능
- 멀티 사용자 지원을 위한 세션 관리 강화 가능
- RESTful API로 백엔드 분리 가능