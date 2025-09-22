#!/bin/bash
# -*- coding: utf-8 -*-
"""
conda 3rd_project 가상환경 설정 스크립트
"""

echo "🚀 conda 3rd_project 가상환경 설정을 시작합니다..."

# conda 설치 확인
if ! command -v conda &> /dev/null; then
    echo "❌ conda가 설치되지 않았습니다. Anaconda 또는 Miniconda를 먼저 설치하세요."
    exit 1
fi

# 3rd_project 환경이 이미 존재하는지 확인
if conda env list | grep -q "3rd_project"; then
    echo "⚠️  3rd_project 환경이 이미 존재합니다."
    read -p "기존 환경을 삭제하고 새로 만들까요? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  기존 3rd_project 환경을 삭제합니다..."
        conda env remove -n 3rd_project -y
    else
        echo "기존 환경을 사용합니다."
        conda activate 3rd_project
        echo "✅ 3rd_project 환경이 활성화되었습니다."
        echo "📦 requirements.txt로 패키지를 업데이트합니다..."
        pip install -r requirements.txt
        exit 0
    fi
fi

# 새로운 환경 생성
echo "🔧 새로운 3rd_project 환경을 생성합니다..."
conda create -n 3rd_project python=3.10 -y

# 환경 활성화
echo "🔄 3rd_project 환경을 활성화합니다..."
conda activate 3rd_project

# requirements.txt가 존재하는지 확인하고 패키지 설치
if [ -f "requirements.txt" ]; then
    echo "📦 requirements.txt에서 패키지를 설치합니다..."
    pip install -r requirements.txt
else
    echo "⚠️  requirements.txt 파일이 없습니다. 수동으로 패키지를 설치하세요."
fi

echo "✅ conda 3rd_project 가상환경 설정이 완료되었습니다!"
echo ""
echo "🎯 다음 명령어로 애플리케이션을 실행하세요:"
echo "conda activate 3rd_project"
echo "python run.py"
echo ""
echo "💡 환경 정보:"
conda info --envs | grep 3rd_project
python --version
echo "설치된 패키지:"
pip list | head -10