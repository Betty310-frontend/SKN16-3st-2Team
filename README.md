# CrossFit 코칭 애플리케이션

MVC (Model-View-Controller) 패턴으로 구축된 크로스핏 코칭 데모 애플리케이션입니다.

## 🎯 프로젝트 특징

✅ **완전한 데이터 포함**: PDF 가이드, 데이터베이스, 설정 파일 포함  
✅ **즉시 실행 가능**: API 키만 설정하면 바로 사용 가능  
✅ **체계적인 MVC 구조**: 16개 모듈로 분리된 깔끔한 아키텍처  
✅ **실용적인 기능**: AI 챗봇, 영상 분석, 개인 맞춤 추천

## 🏗️ 프로젝트 구조

```
SKN16-3st-2Team/
├── src/                          # 소스 코드 (MVC 구조)
│   ├── models/                   # 데이터 모델 레이어
│   │   ├── __init__.py
│   │   ├── user_model.py         # 사용자 관련 데이터베이스 작업
│   │   ├── qa_model.py           # QA 관련 데이터베이스 작업  
│   │   └── vector_db_model.py    # VectorDB 관련 작업
│   ├── views/                    # UI 뷰 레이어
│   │   ├── __init__.py
│   │   ├── auth_view.py          # 인증 UI 컴포넌트
│   │   ├── main_view.py          # 메인 레이아웃
│   │   ├── chatbot_view.py       # 챗봇 UI
│   │   ├── video_view.py         # 영상 코칭 UI
│   │   ├── recommendation_view.py # 개인 맞춤 추천 UI
│   │   └── topic_views.py        # 주제별 탭 UI들
│   ├── controllers/              # 비즈니스 로직 레이어
│   │   ├── __init__.py
│   │   ├── auth_controller.py    # 인증 관련 로직
│   │   ├── chatbot_controller.py # 챗봇 관련 로직
│   │   ├── video_controller.py   # 영상 코칭 로직
│   │   ├── recommendation_controller.py # 추천 로직
│   │   ├── topic_controller.py   # 주제별 기능 로직
│   │   └── admin_controller.py   # 관리자 기능 로직
│   ├── utils/                    # 유틸리티 함수들
│   │   ├── __init__.py
│   │   ├── file_utils.py         # 파일 관련 유틸리티
│   │   ├── network_utils.py      # 네트워크 관련 유틸리티
│   │   └── state_utils.py        # 상태 관리 유틸리티
│   ├── config.py                 # 설정 및 환경 변수 관리
│   ├── main.py                   # 메인 애플리케이션
│   └── __init__.py
├── static/                       # 웹 정적 자원
│   ├── css/                      # 스타일시트
│   ├── js/                       # JavaScript 파일
│   └── images/                   # UI 이미지, 아이콘
├── data/                         # 데이터 디렉토리
│   ├── assets/                   # 운동 관련 미디어 파일
│   │   ├── exercise_images/      # 운동 이미지
│   │   └── guide_images/         # 가이드 이미지
│   ├── raw/crossfit_guide/       # PDF 가이드 파일들
│   ├── chroma_db/               # ChromaDB 벡터 저장소
│   ├── chroma_db_backups/       # DB 백업
│   └── sqlite_db/               # SQLite 사용자 DB
├── notebooks/                    # Jupyter 노트북들
├── docs/                        # 문서
├── run.py                       # 실행 파일
├── setup_conda_env.sh           # conda 환경 설정
├── requirements.txt             # 패키지 의존성
├── .env                         # 환경 변수 (API 키)
└── README.md
```

## 🚀 실행 방법

### 애플리케이션 실행
```bash
# Python 가상환경 활성화 (권장)
# venv: source your_env/bin/activate
# conda: conda activate your_env

# 애플리케이션 실행
python run.py
```

> 🔧 **로컬 개발환경**: conda 환경 설정은 `setup_conda_env.sh` 스크립트 사용  
> 🌐 **GitHub 클론 시**: [SETUP_GITHUB.md](SETUP_GITHUB.md) 가이드 참조

## 🏛️ MVC 아키텍처 설명

### Model (모델) 레이어
- **UserModel**: 사용자 인증, 등록, 세션 관리
- **QAModel**: 질문답변 로그, 자동 쿼리 생성
- **VectorDBModel**: ChromaDB, PDF 문서 처리, QA Chain

### View (뷰) 레이어
- **AuthView**: 로그인/회원가입 UI
- **MainView**: 메인 레이아웃, 좌측 메뉴, 관리자 탭
- **ChatbotView**: 챗봇 인터페이스
- **VideoView**: 영상 업로드 및 분석 UI
- **RecommendationView**: 개인 맞춤 추천 설정
- **TopicViews**: 주제별 탭들 (용어/규칙, 식단/회복, 인증, 멘토링)

### Controller (컨트롤러) 레이어
- **AuthController**: 로그인/로그아웃/회원가입 로직
- **ChatbotController**: 챗봇 대화, 자동 쿼리, 히스토리 관리
- **VideoController**: 영상 분석 (데모 구현)
- **RecommendationController**: 개인 맞춤 운동 계획 생성
- **TopicController**: 용어 검색, 식단/회복 가이드, 멘토링
- **AdminController**: VectorDB 백업/복원/삭제

### Utils (유틸리티) 레이어
- **FileUtils**: 파일/디렉토리 조작
- **NetworkUtils**: 포트 탐색, 네트워크 관련
- **StateUtils**: 애플리케이션 상태 관리

## ✨ 주요 기능

### 🤖 챗봇 (Q&A)
- PDF 문서 기반 질문답변
- 주제별 자동 쿼리 생성
- 대화 히스토리 다운로드
- 근거 자료 수집 및 표시

### 📹 영상 코칭 (데모)
- 운동 자세 영상 업로드
- 분석 결과 및 코칭 피드백
- 참조 영상과 비교

### 🎯 개인 맞춤 추천
- 경험 수준, 목표, 장비에 따른 운동 계획
- JSON 형태 결과 제공
- 챗봇과 연동

### 📚 주제별 정보 요청
- **용어/규칙/운동법**: 크로스핏 기본 정보
- **식단/회복**: 영양 및 회복 가이드
- **인증/챌린지**: 자격증 및 대회 정보
- **멘토링**: 초보자 심리 및 동기부여

### 🔧 관리자 기능
- VectorDB 백업/복원/삭제
- 버전 관리
- 시스템 상태 모니터링

## 🛠️ 설치 및 설정

### GitHub에서 클론한 경우
자세한 설정 가이드는 [SETUP_GITHUB.md](SETUP_GITHUB.md)를 참조하세요.

### 빠른 설정
1. **Python 가상환경 생성 및 활성화**
```bash
# venv 사용
python -m venv crossfit_env
source crossfit_env/bin/activate  # Linux/Mac
# crossfit_env\Scripts\activate  # Windows

# 또는 conda 사용
conda create -n crossfit_app python=3.10
conda activate crossfit_app
```

2. **의존성 설치**
```bash
pip install -r requirements.txt
```

3. **환경 변수 설정**
`.env` 파일에 API 키 설정:
```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=crossfit_coaching_app
```

4. **PDF 문서 배치 (선택사항)**
`data/raw/crossfit_guide/` 디렉토리에 크로스핏 가이드 PDF 파일들을 배치

5. **애플리케이션 실행**
```bash
python run.py
```

## 🔄 주요 특징

### 장점
- **모듈화**: 관심사의 분리로 코드 이해도 향상
- **재사용성**: 각 컴포넌트의 독립적 사용 가능
- **유지보수성**: 기능별 파일 분리로 디버깅 용이
- **확장성**: 새로운 기능 추가 시 기존 코드 영향 최소화
- **테스트 용이성**: 각 레이어별 독립적 테스트 가능

### 아키텍처 특징
- 1400+ 라인의 모놀리식 파일을 16개 모듈로 분리
- 명확한 책임 분담과 의존성 관리
- 설정 파일 분리로 환경 관리 개선
- 유틸리티 함수 모듈화로 재사용성 증대

## 🚀 향후 계획

- 각 레이어별 단위 테스트 추가
- API 문서 자동 생성
- 로깅 시스템 구축
- 에러 핸들링 개선
- 성능 모니터링 추가