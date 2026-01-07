# Implementation Roadmap
# Animal Shorts Agent System v2.0

---

## Phase 1: MVP (Core Functionality) ✅ COMPLETED

### 1.1 프로젝트 기반 설정 ✅
- [x] 디렉토리 구조 생성
- [x] requirements.txt 작성
- [x] config.yaml 기본 설정
- [x] Python 패키지 구조 설정 (`__init__.py` 파일들)
- [x] 기본 유틸리티 함수 (`utils/helpers.py` - YAML 로더, 로깅 등)

### 1.2 Core 모듈 ✅
- [x] `core/models.py` - Pydantic 데이터 모델
- [x] `core/orchestrator.py` - 메인 워크플로우 제어
- [x] `core/state_manager.py` - 세션 상태 관리

### 1.3 핵심 에이전트 (P0) ✅
- [x] `agents/base.py` - BaseAgent 추상 클래스
- [x] `agents/input_agent.py` - 사용자 입력 파싱
- [x] `agents/story_agent.py` - 스토리 생성
- [x] `agents/scene_agent.py` - 장면 분할
- [x] `agents/prompt_agent.py` - Sora2 프롬프트 생성
- [x] `agents/translation_agent.py` - 영→한 번역
- [x] `agents/title_agent.py` - 쇼츠 제목 생성 (플랫폼별)
- [x] `agents/confirm_agent.py` - 사용자 확인
- [x] `agents/output_agent.py` - 결과 출력 (Markdown)

### 1.4 시스템 프롬프트 ✅
- [x] `prompts/story_system.md`
- [x] `prompts/scene_system.md`
- [x] `prompts/sora2_system.md`
- [x] `prompts/translation_system.md`
- [x] `prompts/title_system.md` - 쇼츠 제목 생성용

### 1.5 CLI 인터페이스 ✅
- [x] `main.py` - 메인 실행 파일
- [x] Rich 기반 터미널 UI
- [x] 단계별 진행 표시
- [x] 사용자 입력 처리

### 1.6 테스트 ✅
- [x] 단위 테스트 기본 구조 (`tests/conftest.py`)
- [x] 모델 테스트 (`tests/test_models.py`)
- [x] 에이전트 테스트 (`tests/test_agents.py`)
- [x] 유틸리티 테스트 (`tests/test_utils.py`)
- [x] 상태 관리 테스트 (`tests/test_state_manager.py`)

---

## Phase 2: 품질 강화 (Enhanced Quality) ✅ COMPLETED

### 2.1 검증 시스템 ✅
- [x] `agents/validation_agent.py` - 프롬프트 검증
- [x] 일관성 검사 로직 (`check_consistency()`)
- [x] 품질 점수 계산 (specificity, sora2_compatibility, emotional_clarity, technical_accuracy)
- [x] 개선 제안 생성 (`suggest_improvements()`)

### 2.2 버전 관리 ✅
- [x] `agents/version_agent.py` - A/B 변형 생성
- [x] 버전 저장/불러오기 (`save_versions()`, `load_versions()`)
- [x] 변형 비교 로직 (`compare_versions()`, `format_comparison()`)

### 2.3 재생성 기능 ✅
- [x] `agents/regen_agent.py` - 부분 재생성
- [x] 피드백 기반 수정 (`regenerate_prompt()`, `regenerate_scene()`)
- [x] 특정 요소만 변경 (`modify_scene_element()`, `modify_prompt_element()`)

### 2.4 라이브러리 시스템 ✅
- [x] `core/library_manager.py` - 통합 라이브러리 관리
- [x] 캐릭터 라이브러리 CRUD (`create_character()`, `get_character()`, `update_character()`, `delete_character()`)
- [x] 스토리 템플릿 시스템 (`get_template()`, `create_template()`, `list_templates()`)
- [x] 모범사례 DB 활용 (`get_best_practices()`, `get_prompt_tips()`, `get_camera_suggestions()`)
- [x] 캐릭터 검색/필터 (`search_characters()`, `list_characters()`)

### 2.5 스타일 시스템 ✅
- [x] `core/style_manager.py` - 스타일 관리
- [x] 스타일 프리셋 로더 (`_load_built_in_presets()`, `_load_preset_file()`)
- [x] 커스텀 스타일 생성 (`create_preset()`, `create_custom_preset()`)
- [x] 프리셋 적용 로직 (`apply_style_to_prompt()`)
- [x] 내장 프리셋: home_video, documentary, cinematic_realistic

### 2.6 프로젝트 관리 ✅
- [x] 프로젝트 저장/불러오기 (`StateManager.save_project()`, `load_project()`)
- [x] 프로젝트 목록 관리 (`list_projects()`)
- [x] 메타데이터 관리 (`Project` model with metadata)

---

## Phase 3: 고급 기능 (Advanced Features) ✅ COMPLETED

### 3.1 비교 기능 ✅
- [x] `agents/compare_agent.py` - 비교 뷰어
- [x] 나란히 비교 출력 (`format_side_by_side()`)
- [x] 차이점 하이라이트 (`DiffResult`, `DiffType`)
- [x] 병합 기능 (`merge_prompts()`, `suggest_merge()`)

### 3.2 히스토리 관리 ✅
- [x] `core/history_manager.py`
- [x] 수정 이력 추적 (`record_change()`, 편의 메서드들)
- [x] 롤백 기능 (`rollback()`, `can_rollback()`)
- [x] 히스토리 뷰어 (`format_timeline()`, `format_entry_detail()`)

### 3.3 추가 출력 형식 ✅
- [x] `utils/exporter.py` - 통합 내보내기 모듈
- [x] JSON 내보내기 (`export_json()`, `export_prompts_json()`)
- [x] PDF/HTML 생성 (`export_pdf_html()` - 스토리보드 형식)
- [x] 클립보드 최적화 형식 (`get_clipboard_text()`)
- [x] Markdown 내보내기 (`export_markdown()`)
- [x] Sora2 전용 형식 (`export_sora2_ready()`)
- [x] 스토리보드 형식 (`export_storyboard()`)

### 3.4 고급 TUI
- [ ] Textual 기반 풀 TUI
- [ ] 인터랙티브 편집
- [ ] 실시간 미리보기

### 3.5 성능 최적화
- [ ] 프롬프트 캐싱
- [ ] 병렬 처리 (가능한 경우)
- [ ] API 호출 최적화

---

## 진행 현황

```
✅ Phase 1: MVP - 완료!
   └── 모든 핵심 기능 구현 완료
   └── 테스트 구조 완성 (64개 테스트)
   └── 시스템 프롬프트 작성 완료

✅ Phase 2: 품질 강화 - 완료!
   └── ValidationAgent: 품질 점수, 일관성 검사, 개선 제안
   └── VersionAgent: A/B 변형 생성, 버전 비교
   └── RegenAgent: 부분 재생성, 피드백 기반 수정
   └── LibraryManager: 캐릭터/템플릿 CRUD, 검색
   └── StyleManager: 스타일 프리셋, 커스텀 스타일

✅ Phase 3: 고급 기능 - 완료!
   └── CompareAgent: 나란히 비교, 차이점 하이라이트, 병합
   └── HistoryManager: 수정 이력 추적, 롤백, 타임라인 뷰어
   └── Exporter: JSON/Markdown/HTML(PDF)/Sora2/클립보드 출력

⏳ 추가 기능 (Optional)
   └── Textual 기반 풀 TUI
   └── 프롬프트 캐싱 및 성능 최적화
```

---

## 다음 단계

핵심 기능 구현 완료! 추가 가능한 기능:
1. Textual 기반 풀 TUI (인터랙티브 편집)
2. 프롬프트 캐싱 시스템
3. API 호출 최적화 (병렬 처리)
