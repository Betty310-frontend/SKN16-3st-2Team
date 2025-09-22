#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CrossFit 코칭 애플리케이션 실행 파일 (MVC 구조)
conda 3rd_project 가상환경에서 실행
"""

import sys
import os
import subprocess

def check_and_activate_conda_env():
    """conda 3rd_project 가상환경 확인 및 활성화"""
    try:
        # 현재 활성화된 conda 환경 확인 (여러 방법으로 시도)
        current_env = (
            os.environ.get('CONDA_DEFAULT_ENV') or 
            os.environ.get('CONDA_PROMPT_MODIFIER', '').strip('()') or
            'base'
        )
        
        # Python 실행 경로를 통한 환경 확인
        python_path = sys.executable
        is_3rd_project_env = (
            current_env == '3rd_project' or 
            '3rd_project' in python_path or
            '/envs/3rd_project/' in python_path
        )
        
        if is_3rd_project_env:
            print("✅ conda 3rd_project 가상환경에서 실행 중입니다.")
            print(f"📍 Python 경로: {python_path}")
            print(f"🌐 현재 환경: {current_env}")
            return True
        else:
            print(f"⚠️  현재 환경: {current_env}")
            print(f"📍 Python 경로: {python_path}")
            print("❌ 3rd_project 가상환경에서 실행되지 않고 있습니다.")
            print("다음 명령어로 환경을 활성화하고 다시 실행하세요:")
            print("conda activate 3rd_project")
            print("python run.py")
            return False
            
    except Exception as e:
        print(f"❌ 환경 확인 중 오류 발생: {e}")
        print("환경 확인을 건너뛰고 실행을 계속합니다...")
        return True

def main():
    """메인 실행 함수"""
    # conda 환경 확인
    if not check_and_activate_conda_env():
        sys.exit(1)
    
    # src 디렉토리를 Python 경로에 추가
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
    
    try:
        from src.main import main as app_main
        app_main()
    except ImportError as e:
        print(f"❌ 모듈 import 오류: {e}")
        print("필요한 패키지를 설치해주세요:")
        print("pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()