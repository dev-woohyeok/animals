# Implementation Roadmap
# Animal Shorts Agent System v2.0

---

## Phase 1: MVP (Core Functionality)

### 1.1 프로젝트 기반 설정
- [x] 디렉토리 구조 생성
- [x] requirements.txt 작성
- [x] config.yaml 기본 설정
- [ ] Python 패키지 구조 설정 (`__init__.py` 파일들)
- [ ] 기본 유틸리티 함수 (YAML 로더, 로깅 등)

### 1.2 Core 모듈
- [ ] `core/orchestrator.py` - 메인 워크플로우 제어
- [ ] `core/state_manager.py` - 세션 상태 관리
- [ ] `core/models.py` - Pydantic 데이터 모델

### 1.3 핵심 에이전트 (P0)
- [ ] `agents/base.py` - BaseAgent 추상 클래스
- [ ] `agents/input_agent.py` - 사용자 입력 파싱
- [ ] `agents/story_agent.py` - 스토리 생성
- [ ] `agents/scene_agent.py` - 장면 분할
- [ ] `agents/prompt_agent.py` - Sora2 프롬프트 생성
- [ ] `agents/translation_agent.py` - 영→한 번역
- [ ] `agents/title_agent.py` - 쇼츠 제목 생성 (플랫폼별)
- [ ] `agents/confirm_agent.py` - 사용자 확인
- [ ] `agents/output_agent.py` - 결과 출력 (Markdown)

### 1.4 시스템 프롬프트
- [ ] `prompts/story_system.md`
- [ ] `prompts/scene_system.md`
- [ ] `prompts/sora2_system.md`
- [ ] `prompts/translation_system.md`
- [ ] `prompts/title_system.md` - 쇼츠 제목 생성용

### 1.5 CLI 인터페이스
- [ ] `main.py` - 메인 실행 파일
- [ ] Rich 기반 터미널 UI
- [ ] 단계별 진행 표시
- [ ] 사용자 입력 처리

### 1.6 테스트
- [ ] 단위 테스트 기본 구조
- [ ] 에이전트별 테스트

---

## Phase 2: 품질 강화 (Enhanced Quality)

### 2.1 검증 시스템
- [ ] `agents/validation_agent.py` - 프롬프트 검증
- [ ] 일관성 검사 로직
- [ ] 품질 점수 계산
- [ ] 개선 제안 생성

### 2.2 버전 관리
- [ ] `agents/version_agent.py` - A/B 변형 생성
- [ ] 버전 저장/불러오기
- [ ] 변형 비교 로직

### 2.3 재생성 기능
- [ ] `agents/regen_agent.py` - 부분 재생성
- [ ] 피드백 기반 수정
- [ ] 특정 요소만 변경

### 2.4 라이브러리 시스템
- [ ] 캐릭터 라이브러리 CRUD
- [ ] 스토리 템플릿 시스템
- [ ] 모범사례 DB 활용
- [ ] 캐릭터 검색/필터

### 2.5 스타일 시스템
- [ ] 스타일 프리셋 로더
- [ ] 커스텀 스타일 생성
- [ ] 프리셋 적용 로직

### 2.6 프로젝트 관리
- [ ] 프로젝트 저장/불러오기
- [ ] 프로젝트 목록 관리
- [ ] 메타데이터 관리

---

## Phase 3: 고급 기능 (Advanced Features)

### 3.1 비교 기능
- [ ] `agents/compare_agent.py` - 비교 뷰어
- [ ] 나란히 비교 출력
- [ ] 차이점 하이라이트
- [ ] 병합 기능

### 3.2 히스토리 관리
- [ ] `core/history_manager.py`
- [ ] 수정 이력 추적
- [ ] 롤백 기능
- [ ] 히스토리 뷰어

### 3.3 추가 출력 형식
- [ ] JSON 내보내기
- [ ] PDF 생성 (스토리보드 형식)
- [ ] 클립보드 최적화 형식

### 3.4 고급 TUI
- [ ] Textual 기반 풀 TUI
- [ ] 인터랙티브 편집
- [ ] 실시간 미리보기

### 3.5 성능 최적화
- [ ] 프롬프트 캐싱
- [ ] 병렬 처리 (가능한 경우)
- [ ] API 호출 최적화

---

## 구현 순서 (Recommended Order)

```
Week 1-2: Phase 1.1 - 1.3 (기반 + Core + 에이전트 시작)
    ↓
Week 3-4: Phase 1.3 - 1.5 (에이전트 완성 + CLI)
    ↓
Week 5: Phase 1.6 + 테스트 및 디버깅
    ↓
──────── MVP 완성 ────────
    ↓
Week 6-7: Phase 2.1 - 2.3 (검증 + 버전 + 재생성)
    ↓
Week 8-9: Phase 2.4 - 2.6 (라이브러리 + 프로젝트)
    ↓
──────── v1.0 릴리스 ────────
    ↓
Week 10+: Phase 3 (고급 기능)
```

---

## 즉시 시작 가능한 작업

### 오늘 할 수 있는 것:

1. **기본 모델 정의** (`core/models.py`)
   ```python
   # InputData, Story, Scene, Prompt, Character 등
   ```

2. **BaseAgent 클래스** (`agents/base.py`)
   ```python
   # 모든 에이전트의 공통 인터페이스
   ```

3. **시스템 프롬프트 작성** (`prompts/`)
   ```markdown
   # 각 에이전트용 시스템 프롬프트
   ```

4. **간단한 main.py 스켈레톤**
   ```python
   # 기본 CLI 흐름
   ```

---

## 다음 단계

구현을 시작하시겠습니까? 다음 중 선택해주세요:

1. **MVP부터 순차 구현** - Phase 1부터 차근차근
2. **특정 에이전트 먼저** - 가장 중요한 에이전트부터
3. **프로토타입 먼저** - 전체 흐름을 빠르게 연결
4. **다른 방식** - 직접 지정
