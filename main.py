from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(
    title="CI/CD 학습 프로젝트 API",
    description="GitHub Actions를 활용한 CI/CD 실습을 위한 FastAPI 프로젝트",
    version="1.0.0"
)


@app.get("/")
async def root():
    """
    루트 엔드포인트 - 기본 환영 메시지
    """
    return {
        "message": "CI/CD 학습 프로젝트에 오신 것을 환영합니다!",
        "status": "running",
        "veryfy": "그냥 변경",
        "path": os.path.abspath(__file__),
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
async def health_check():
    """
    헬스 체크 엔드포인트
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/api/info")
async def get_info():
    """
    API 정보 조회
    """
    return {
        "name": "CI/CD 학습 프로젝트",
        "version": "1.0.0",
        "framework": "FastAPI",
        "description": "GitHub Actions를 활용한 CI/CD 실습 프로젝트"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

