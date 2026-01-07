# 배포 가이드 - Self-hosted Runner 설정

이 가이드에서는 GitHub Actions를 통해 로컬 PC에 자동 배포하는 방법을 설명합니다.

## Self-hosted Runner란?

Self-hosted runner는 GitHub Actions가 사용자의 로컬 PC에서 워크플로우를 실행할 수 있게 해주는 에이전트입니다. 이를 통해 GitHub Actions가 로컬 PC의 파일 시스템에 접근하여 배포할 수 있습니다.

## 설정 단계

### 1단계: GitHub 저장소에서 Runner 추가

1. GitHub 저장소로 이동
2. **Settings** → **Actions** → **Runners** 클릭
3. **New self-hosted runner** 버튼 클릭
4. 운영체제 선택 (Windows)
5. 표시되는 명령어들을 복사 (아래 예시 참고)

### 2단계: 로컬 PC에 Runner 설치

PowerShell을 **관리자 권한**으로 실행하고, GitHub에서 제공한 명령어를 실행합니다:

```powershell
# 예시 명령어 (실제 명령어는 GitHub에서 제공)
# Create a folder
mkdir actions-runner; cd actions-runner

# Download the latest runner package
Invoke-WebRequest -Uri https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-win-x64-2.311.0.zip -OutFile actions-runner-win-x64-2.311.0.zip

# Extract the installer
Add-Type -AssemblyName System.IO.Compression.FileSystem ; [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD/actions-runner-win-x64-2.311.0.zip", "$PWD")

# Create the runner and start the configuration
./config.cmd --url https://github.com/YOUR-USERNAME/YOUR-REPO --token YOUR-TOKEN

# Run it!
./run.cmd
```

**중요**: 
- `YOUR-USERNAME`과 `YOUR-REPO`를 실제 값으로 변경
- `YOUR-TOKEN`은 GitHub에서 제공하는 토큰 사용 (일회용, 빠르게 사용)

### 3단계: Runner를 서비스로 등록 (선택사항)

Runner가 항상 실행되도록 Windows 서비스로 등록할 수 있습니다:

```powershell
# Runner 디렉토리로 이동
cd actions-runner

# 서비스로 설치
./svc.cmd install

# 서비스 시작
./svc.cmd start
```

서비스로 등록하면 PC를 재시작해도 자동으로 실행됩니다.

### 4단계: 배포 디렉토리 준비

배포 디렉토리가 없으면 자동으로 생성되지만, 미리 생성해도 됩니다:

```powershell
# 배포 디렉토리 생성
New-Item -ItemType Directory -Path "$env:USERPROFILE\Desktop\test\deploy" -Force
```

## 배포 워크플로우 동작

1. **코드 푸시**: `main` 또는 `master` 브랜치에 코드를 푸시
2. **자동 트리거**: GitHub Actions가 워크플로우 실행
3. **Runner 선택**: `runs-on: self-hosted`로 인해 로컬 PC의 runner가 작업 실행
4. **배포 수행**:
   - 코드 체크아웃
   - Python 환경 설정
   - 의존성 설치
   - 배포 디렉토리에 파일 복사
   - 기존 애플리케이션 중지
   - 새 버전 실행

## 배포 위치

기본 배포 위치: `%USERPROFILE%\Desktop\test\deploy`

변경하려면 `.github/workflows/deploy.yml` 파일에서 `$deployPath` 변수를 수정하세요.

## 수동 배포

GitHub 저장소의 **Actions** 탭에서:
1. "Deploy FastAPI Application" 워크플로우 선택
2. **Run workflow** 버튼 클릭
3. 브랜치 선택 후 **Run workflow** 클릭

## 문제 해결

### Runner가 보이지 않음
- Runner가 실행 중인지 확인: `Get-Service actions.runner.*`
- Runner 디렉토리에서 `./run.cmd` 실행

### 권한 오류
- PowerShell을 관리자 권한으로 실행
- 배포 디렉토리에 쓰기 권한 확인

### 애플리케이션이 실행되지 않음
- 배포 디렉토리에서 수동 실행 테스트:
  ```powershell
  cd $env:USERPROFILE\Desktop\test\deploy
  python main.py
  ```

## 보안 주의사항

⚠️ **중요**: Self-hosted runner는 GitHub 저장소의 코드에 접근할 수 있습니다.
- 신뢰할 수 있는 저장소에서만 사용하세요
- Private 저장소에서 사용하는 것을 권장합니다
- Runner가 실행 중일 때는 PC를 안전하게 관리하세요

## Runner 제거

Runner를 제거하려면:

1. GitHub 저장소: **Settings** → **Actions** → **Runners** → Runner 제거
2. 로컬 PC: Runner 디렉토리에서 `./config.cmd remove` 실행

