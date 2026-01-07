# GitHub CI/CD 학습 프로젝트

이 프로젝트는 GitHub Actions를 활용한 CI/CD(Continuous Integration/Continuous Deployment)를 이해하고 실습하기 위한 프로젝트입니다.

## 🚀 프로젝트 개요

FastAPI를 사용한 간단한 REST API 프로젝트로, GitHub Actions를 통해 자동 배포 파이프라인을 구축합니다.

### 주요 기능
- FastAPI 기반 REST API
- GitHub Actions를 통한 자동 배포
- 로컬 환경 자동 배포 (같은 PC의 다른 디렉토리)

### 프로젝트 구조
```
.
├── .github/
│   └── workflows/
│       └── deploy.yml      # 배포 워크플로우
├── main.py                 # FastAPI 애플리케이션
├── requirements.txt        # Python 의존성
├── .gitignore
└── README.md
```

## 📦 설치 및 실행

### 1. 로컬 개발 환경 설정

```bash
# 가상 환경 생성 (선택사항)
python -m venv venv

# 가상 환경 활성화
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt

# 애플리케이션 실행
python main.py
```

### 2. API 테스트

애플리케이션이 실행되면 다음 엔드포인트를 사용할 수 있습니다:

- **루트**: http://localhost:8000/
- **헬스 체크**: http://localhost:8000/health
- **API 정보**: http://localhost:8000/api/info
- **API 문서**: http://localhost:8000/docs (Swagger UI)
- **대체 문서**: http://localhost:8000/redoc (ReDoc)

### 3. GitHub에 업로드

```bash
# Git 저장소 초기화
git init

# 파일 추가
git add .

# 커밋
git commit -m "Initial commit: FastAPI CI/CD 프로젝트"

# GitHub 저장소 연결 (원격 저장소 URL로 변경)
git remote add origin https://github.com/your-username/your-repo.git

# 메인 브랜치로 푸시
git branch -M main
git push -u origin main
```

### 4. 자동 배포

`main` 또는 `master` 브랜치에 코드를 푸시하면 자동으로 배포 워크플로우가 실행됩니다.

배포 위치: `%USERPROFILE%\Desktop\test\deploy`

워크플로우는 다음 작업을 수행합니다:
1. 코드 체크아웃
2. Python 환경 설정
3. 의존성 설치
4. 배포 디렉토리에 파일 복사
5. 기존 애플리케이션 중지 (실행 중인 경우)
6. 새 버전 실행

### 5. 수동 배포 실행

GitHub 저장소의 Actions 탭에서 "Deploy FastAPI Application" 워크플로우를 선택하고 "Run workflow" 버튼을 클릭하여 수동으로 배포할 수 있습니다.

## 목차

1. [CI/CD란?](#cicd란)
2. [GitHub Actions 소개](#github-actions-소개)
3. [기본 개념](#기본-개념)
4. [실습 예제](#실습-예제)
5. [고급 활용](#고급-활용)
6. [참고 자료](#참고-자료)

---

## CI/CD란?

### CI (Continuous Integration) - 지속적 통합

- **정의**: 개발자들이 코드를 자주 병합하고, 각 병합마다 자동화된 빌드와 테스트를 실행하는 개발 관행
- **목적**: 
  - 버그 조기 발견
  - 통합 문제 최소화
  - 코드 품질 향상
  - 배포 속도 향상

### CD (Continuous Deployment/Delivery) - 지속적 배포/전달

- **Continuous Delivery**: 코드 변경사항을 자동으로 테스트하고 스테이징 환경에 배포
- **Continuous Deployment**: 자동화된 테스트를 통과하면 프로덕션 환경에 자동 배포

### CI/CD 파이프라인

```
코드 작성 → Git Push → 자동 빌드 → 자동 테스트 → 자동 배포
```

---

## GitHub Actions 소개

GitHub Actions는 GitHub에서 제공하는 CI/CD 플랫폼으로, 코드 저장소에서 직접 워크플로우를 자동화할 수 있습니다.

### 주요 특징

- **무료**: Public 저장소는 무제한 무료, Private 저장소는 월 2,000분 무료
- **통합**: GitHub과 완벽하게 통합
- **유연성**: 다양한 언어와 플랫폼 지원
- **커뮤니티**: 수천 개의 재사용 가능한 액션

### 기본 구조

GitHub Actions 워크플로우는 `.github/workflows/` 디렉토리에 YAML 파일로 작성됩니다.

---

## 기본 개념

### 1. Workflow (워크플로우)

- **정의**: 자동화된 프로세스를 정의하는 YAML 파일
- **위치**: `.github/workflows/` 디렉토리
- **확장자**: `.yml` 또는 `.yaml`

### 2. Event (이벤트)

워크플로우를 트리거하는 GitHub 이벤트:
- `push`: 코드가 푸시될 때
- `pull_request`: PR이 생성/업데이트될 때
- `schedule`: 스케줄에 따라 (cron 형식)
- `workflow_dispatch`: 수동 실행
- `release`: 릴리스가 생성될 때

### 3. Job (작업)

- 하나의 워크플로우는 여러 Job을 포함할 수 있음
- Job은 병렬 또는 순차적으로 실행 가능
- 각 Job은 독립적인 가상 환경에서 실행

### 4. Step (단계)

- Job 내에서 실행되는 개별 작업 단위
- 각 Step은 명령어 실행 또는 Action 사용

### 5. Action (액션)

- 재사용 가능한 워크플로우 단위
- GitHub Marketplace에서 수천 개의 액션 제공
- 커스텀 액션도 작성 가능

---

## 실습 예제

### 예제 1: 기본 Hello World 워크플로우

`.github/workflows/hello-world.yml` 파일 생성:

```yaml
name: Hello World

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Say Hello
        run: echo "Hello, GitHub Actions!"
```

### 예제 2: Node.js 프로젝트 빌드 및 테스트

`.github/workflows/nodejs-ci.yml` 파일 생성:

```yaml
name: Node.js CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [14.x, 16.x, 18.x]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Build
        run: npm run build
```

### 예제 3: Python 프로젝트 CI/CD

`.github/workflows/python-ci.yml` 파일 생성:

```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run tests
        run: pytest
      
      - name: Check code style
        run: |
          pip install flake8
          flake8 .
```

### 예제 4: Docker 이미지 빌드 및 푸시

`.github/workflows/docker.yml` 파일 생성:

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: |
            your-username/your-image:latest
            your-username/your-image:${{ github.sha }}
```

### 예제 5: 자동 릴리스 생성

`.github/workflows/release.yml` 파일 생성:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false
```

---

## 고급 활용

### 1. 환경 변수 및 시크릿

**환경 변수 설정:**
```yaml
env:
  NODE_ENV: production
  API_URL: https://api.example.com
```

**시크릿 사용:**
- GitHub 저장소 Settings → Secrets and variables → Actions에서 설정
- 워크플로우에서 `${{ secrets.SECRET_NAME }}` 형식으로 사용

### 2. 조건부 실행

```yaml
steps:
  - name: Deploy to production
    if: github.ref == 'refs/heads/main'
    run: echo "Deploying to production"
```

### 3. 의존성 있는 Job

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building..."
  
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing..."
  
  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
```

### 4. 아티팩트 저장 및 다운로드

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build
        run: npm run build
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-files
          path: dist/
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Download artifacts
        uses: actions/download-artifact@v3
        with:
          name: build-files
```

### 5. 매트릭스 전략

여러 버전/환경에서 동시 테스트:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [14.x, 16.x, 18.x]
```

### 6. 캐싱

빌드 속도 향상을 위한 캐싱:

```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

---

## 워크플로우 작성 체크리스트

- [ ] 워크플로우 파일이 `.github/workflows/` 디렉토리에 있는가?
- [ ] 적절한 이벤트 트리거가 설정되어 있는가?
- [ ] 적절한 러너(OS)가 선택되었는가?
- [ ] 필요한 시크릿이 설정되어 있는가?
- [ ] 에러 처리가 포함되어 있는가?
- [ ] 불필요한 단계가 없는가? (비용 최적화)

---

## 일반적인 문제 해결

### 1. 권한 오류
- 시크릿이 올바르게 설정되었는지 확인
- GitHub Token 권한 확인

### 2. 빌드 실패
- 로그를 자세히 확인
- 로컬에서 동일한 명령어가 작동하는지 테스트

### 3. 느린 실행 속도
- 캐싱 활용
- 불필요한 단계 제거
- 매트릭스 전략 최적화

---

## 참고 자료

### 공식 문서
- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [GitHub Actions 워크플로우 문법](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

### 학습 리소스
- [GitHub Actions 시작하기](https://docs.github.com/en/actions/quickstart)
- [GitHub Marketplace](https://github.com/marketplace?type=actions)

### 유용한 액션
- `actions/checkout@v3` - 코드 체크아웃
- `actions/setup-node@v3` - Node.js 설정
- `actions/setup-python@v4` - Python 설정
- `actions/cache@v3` - 캐싱
- `actions/upload-artifact@v3` - 아티팩트 업로드
- `actions/download-artifact@v3` - 아티팩트 다운로드

---

## 실습 과제

1. **기본 워크플로우 생성**
   - 간단한 Hello World 워크플로우 작성
   - 수동 실행 기능 추가

2. **CI 파이프라인 구축**
   - 프로젝트에 맞는 빌드 및 테스트 워크플로우 작성
   - 여러 브랜치에서 실행되도록 설정

3. **CD 파이프라인 구축**
   - 자동 배포 워크플로우 작성
   - 환경별 배포 전략 구현

4. **고급 기능 활용**
   - 매트릭스 전략으로 여러 버전 테스트
   - 캐싱을 활용한 빌드 속도 개선
   - 아티팩트 저장 및 활용

---

## 프로젝트 구조 예시

```
.
├── .github/
│   └── workflows/
│       ├── ci.yml          # CI 워크플로우
│       ├── cd.yml          # CD 워크플로우
│       └── release.yml     # 릴리스 워크플로우
├── src/                    # 소스 코드
├── tests/                  # 테스트 코드
├── .gitignore
└── README.md
```

---

## 주의사항

1. **비용 관리**: Private 저장소는 월 2,000분 무료이므로 사용량 모니터링 필요
2. **보안**: 시크릿 정보는 절대 코드에 하드코딩하지 않기
3. **성능**: 불필요한 워크플로우 실행 방지 (브랜치 필터링 등)
4. **테스트**: 워크플로우 변경 시 로컬에서 먼저 테스트

---

## 마무리

이 프로젝트를 통해 GitHub Actions를 활용한 CI/CD의 기본부터 고급 활용까지 학습할 수 있습니다. 각 예제를 직접 실행해보고, 자신의 프로젝트에 맞게 커스터마이징해보세요!

**Happy Coding! 🚀**

