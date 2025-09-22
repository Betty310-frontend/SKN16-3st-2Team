# CrossFit 코### 2. 환경 변수 설정

#### 방법 1: .env 파일 사용 (권장)

1. `.env.example` 파일을 `.env`로 복사:
```bash
cp config/.env.example .env
```

2. `.env` 파일을 열어 실제 API 키로 수정:
```bash
# .env 파일 내용
OPENAI_API_KEY=your_actual_openai_api_key_here
LANGCHAIN_API_KEY=your_actual_langchain_api_key_here
LANGCHAIN_PROJECT=ai_camp_3rd_project
```이드

이 가이드는 Jupyter 노트북에서 로컬 Python 환경으로 변환된 CrossFit 코칭 데모 애플리케이션(MVC 구조)의 설치 및 실행 방법을 안내합니다.

## 🚀 빠른 시작

### 1. 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

#### 방법 1: .env 파일 사용 (권장)

1. `.env.example` 파일을 `.env`로 복사:
```bash
cp .env.example .env
```

2. `.env` 파일을 열어 실제 API 키로 수정:
```bash
# .env 파일 내용
OPENAI_API_KEY=your_actual_openai_api_key_here
LANGCHAIN_API_KEY=your_actual_langchain_api_key_here
LANGCHAIN_PROJECT=ai_camp_3rd_project
```

#### 방법 2: 환경 변수로 직접 설정

##### Linux/Mac/WSL:
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
export LANGCHAIN_API_KEY="your_langchain_api_key_here"
```

##### Windows Command Prompt:
```cmd
set OPENAI_API_KEY=your_openai_api_key_here
set LANGCHAIN_API_KEY=your_langchain_api_key_here
```

##### Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="your_openai_api_key_here"
$env:LANGCHAIN_API_KEY="your_langchain_api_key_here"
```

### 3. PDF 가이드 파일 배치 (선택사항)

CrossFit 가이드 PDF 파일들을 다음 경로에 배치하세요:

```
data/raw/crossfit_guide/
├── 12_03_Anatomy_Physiology.pdf
├── 13_03_Benchmark_Workouts.pdf
├── 31_05_fooling_with_fran.pdf
└── ... (기타 PDF 파일들)
```

### 4. 애플리케이션 실행

```bash
python run.py
```

브라우저에서 출력된 URL (예: `http://localhost:7860`)로 접속하세요.

## 📋 주요 변경사항 (Colab → 로컬)

### 제거된 기능들
- Google Colab 관련 imports (`google.colab`, `drive.mount`)
- `!pip install` 명령어들 → `requirements.txt`로 대체
- Google Drive 연동 → 로컬 파일 시스템 사용

### 수정된 경로들
- 메인 애플리케이션: 루트 → `run.py` (MVC 구조)
- MVC 소스 코드: `src/` 디렉토리 (models, views, controllers, utils)
- 환경 변수: 루트 → `.env` 파일 
- 문서: 루트 → `docs/` 디렉토리
- 데이터베이스: `/content/drive/MyDrive/...` → `./data/sqlite_db/`
- ChromaDB: `/content/drive/MyDrive/...` → `./data/chroma_db/`
- PDF 가이드: `/content/drive/MyDrive/...` → `./data/raw/crossfit_guide/`

### 추가된 기능들
- `.env` 파일 자동 로드 기능 추가
- 체계적인 폴더 구조 적용
- 실행 스크립트 분리 (`run.py`)
- 설정 파일 분리 (`config/settings.py`)
- API 참조 문서 추가

## 🔧 기능 설명

### 1. 챗봇 Q&A
- **작동 조건**: OpenAI API 키 + PDF 파일들
- **없을 경우**: 기본 응답 메시지 표시
- **기능**: PDF 문서 기반 질의응답, 대화 히스토리 저장

### 2. 영상 코칭 (데모)
- **상태**: 모킹 데이터 사용 (실제 영상 분석 X)
- **기능**: 영상 업로드, 가상의 분석 결과 표시

### 3. 개인 맞춤 추천
- **기능**: 사용자 입력 기반 운동 계획 생성
- **출력**: JSON 형태의 상세 추천

### 4. 기타 기능들
- 용어/규칙 검색
- 식단/회복 가이드
- 단위 변환기 (kg ↔ lb)
- 관리자 VectorDB 관리

## 🔑 로그인 정보

### 관리자 계정
- **이메일**: `admin@crossfit.com`
- **비밀번호**: `admin123`
- **권한**: VectorDB 관리 탭 접근 가능

### 데모 계정
- **이메일**: `demo@demo.com`
- **비밀번호**: `x`
- **권한**: 일반 사용자

## ⚠️ 문제 해결

### API 키 관련
```
Warning: OPENAI_API_KEY environment variable not set!
```
→ `.env` 파일에 API 키를 설정하거나 환경 변수를 직접 설정하고 애플리케이션을 재시작하세요.

#### .env 파일 확인 방법:
1. 프로젝트 루트에 `.env` 파일이 있는지 확인
2. `.env` 파일에 `OPENAI_API_KEY=실제키값` 형태로 설정되어 있는지 확인
3. API 키에 따옴표나 불필요한 공백이 없는지 확인

### PDF 파일 관련
```
Warning: No PDF files found in data/raw/crossfit_guide/
```
→ PDF 파일을 해당 디렉토리에 배치하고 재시작하세요.

### 포트 충돌
→ 애플리케이션이 자동으로 사용 가능한 포트를 찾습니다 (7860-7960 범위).

### 데이터베이스 문제
→ `data/` 디렉토리의 하위 폴더들이 자동으로 생성됩니다.

## 📁 생성된 파일 구조

```
SKN16-3st-2Team/
├── run.py                       # 애플리케이션 실행 스크립트
├── requirements.txt             # 패키지 의존성
├── .env                        # 환경 변수 설정 파일 (사용자가 생성)
├── README.md                   # 프로젝트 개요
├── .gitignore                  # Git 무시 파일
├── setup_conda_env.sh          # conda 환경 설정 스크립트
│
├── src/                        # MVC 소스 코드
│   ├── main.py                 # 메인 애플리케이션
│   ├── config.py               # 설정 관리
│   ├── models/                 # 데이터 모델 레이어
│   ├── views/                  # UI 뷰 레이어
│   ├── controllers/            # 비즈니스 로직 레이어
│   └── utils/                  # 유틸리티 함수들
│
├── docs/                       # 문서
│   ├── SETUP_GUIDE.md         # 이 파일
│   └── API_REFERENCE.md       # API 참조 문서
│
├── data/                       # 자동 생성되는 데이터 디렉토리
│   ├── sqlite_db/             # 사용자 데이터베이스
│   ├── chroma_db/             # 벡터 데이터베이스
│   ├── chroma_db_backups/     # DB 백업
│   └── raw/
│       └── crossfit_guide/    # PDF 파일 배치 위치
│
├── notebooks/                  # Jupyter 노트북
│   ├── index.ipynb            # 원본 메인 노트북
│   ├── AI_평가_코드.ipynb      # AI 평가 관련 노트북
│   ├── Basic_Pipeline.ipynb   # 기본 파이프라인 노트북
│   └── py/                    # Python 모듈들
│       ├── coaching_llm.py    # 코칭 LLM 모듈
│       ├── pose2d_yolo.py     # 2D 자세 분석
│       ├── pose3d_vpose.py    # 3D 자세 분석
│       └── ... (기타 모듈들)
```

## 🔄 개발 워크플로우

1. **로컬 개발**: `python run.py`
2. **의존성 추가**: `requirements.txt` 업데이트
3. **설정 변경**: `config/settings.py` 수정
4. **문서 업데이트**: `docs/` 디렉토리에서 문서 관리
5. **데이터 백업**: 관리자 탭에서 DB 백업
6. **버전 관리**: Git으로 코드 변경사항 추적

## 📚 추가 문서

- **[API 참조](API_REFERENCE.md)**: 함수 및 클래스 상세 문서
- **[프로젝트 개요](../README.md)**: 전체 프로젝트 설명

---

추가 질문이나 문제가 있으면 이슈를 생성해주세요.