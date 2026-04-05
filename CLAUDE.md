# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

**Animal Shorts Agent System** - 동물 관련 감동 쇼츠 영상 제작을 위한 Sora2 프롬프트 생성 시스템.
Claude Code 스킬 기반으로 동작하며, Max 구독만으로 사용 가능.

## 사용법

### 1. 스토리 리서치 (선택)
```
/animal-shorts-research [동물] [--viral] [--recent]
```
→ 인터넷에서 감동적인 동물 구조 스토리 검색 및 분석

### 2. 쇼츠 영상 분석 (선택)
```
/animal-shorts-analyze [YouTube Shorts URL]
```
→ 기존 쇼츠 영상을 캡처/분석하여 레퍼런스 기반 스토리 생성

### 3. 쇼츠 생성
```
/animal-shorts [동물] / [상황] / [감정] / [결말]
```
→ 90초 쇼츠 프롬프트 생성

### 예시
```
# 리서치 먼저
/animal-shorts-research 올빼미 --viral

# 직접 생성
/animal-shorts 골든 리트리버 / 버려진 후 노인을 만남 / 감동, 따뜻함
/animal-shorts 아기 고슴도치 / 골든리트리버가 입에 물고 옴 / 귀여움 / 가족이 됨
```

## Project Structure

```
animals/
├── .claude/commands/     # Claude Code 스킬
│   ├── animal-shorts.md        # 메인 워크플로우
│   ├── animal-shorts-research.md # 스토리 리서치 에이전트
│   ├── animal-shorts-analyze.md  # 쇼츠 영상 분석 (NEW)
│   ├── animal-shorts-story.md  # 스토리 생성
│   ├── animal-shorts-scene.md  # 장면 분할
│   ├── animal-shorts-prompt.md # Sora2 프롬프트
│   ├── animal-shorts-title.md  # 제목 생성
│   └── animal-shorts-export.md # 파일 출력
│
├── prompts/              # 시스템 프롬프트 (스킬에서 참조)
│   ├── research_system.md      # 리서치 에이전트 시스템 (NEW)
│   ├── story_system.md
│   ├── scene_system.md
│   ├── sora2_system.md
│   ├── translation_system.md
│   └── title_system.md
│
├── library/              # 라이브러리
│   ├── best_practices/   # Sora2 모범 사례
│   └── templates/        # 스토리 템플릿
│
├── config/styles/        # 스타일 프리셋
├── output/               # 출력 예시
└── projects/             # 생성된 프로젝트 저장
```

## 워크플로우 (완전 자동화)

```
[선택A] /animal-shorts-research 동물
    ↓ 인터넷에서 바이럴 스토리 검색/분석

[선택B] /animal-shorts-analyze [YouTube URL]
    ↓ 기존 쇼츠 캡처/분석 → 스토리 3개 제안 → 선택 후 자동 진행

/animal-shorts 입력
    ↓
Step 1: 입력 분석 → 스토리 3개 제안 (리스트)
          ↓
    [유일한 사용자 확인] 스토리 선택
          ↓
Step 2: 스토리 생성 → 자동 진행
          ↓
Step 3: 장면 분할 → 자동 진행
          ↓
Step 4: Sora2 프롬프트 → 자동 진행
          ↓
Step 5: 제목 생성 → 자동 진행
          ↓
Step 6: 파일 저장 + git commit & push → 완료
```

## 자동 진행 규칙 (영구 고정)

**스토리 선택 이후 모든 단계는 자동 진행. 중간에 절대 묻지 않는다.**

- 사용자 확인은 스토리 선택 1회만 (3가지 옵션 리스트 제안)
- 스토리 선택 후 Step 2~6은 전부 자동 실행
- 중간에 사용자에게 확인 요청 금지
- 폴더/파일 생성: 물어보지 말고 바로 생성
- 최종 저장 후 git commit & push: 자동 실행

## 🌍 타겟 시장 (영구 고정 - 절대 변경 금지)

**글로벌/북미 타겟 - 한국 아님!**

```
❌ 절대 금지: 한국, 서울, 한국 아파트, 한국 도시
✅ 필수 사용: 미국, 북미, 시애틀, 포틀랜드, 콜로라도 등 미국 도시/지역
```

### 장소 설정 규칙
- 모든 프롬프트의 장소는 **미국/북미** 기준
- 예시: "미국 시애틀 교외", "미국 콜로라도 산악지역", "미국 교외 주택가"
- 실내 장면: "미국식 주택", "미국 아파트" 사용
- 절대로 "한국"이라는 단어 사용 금지

### 제목 규칙 (영구 고정)
- **모든 제목은 반드시 영어로 작성**
- 한글 제목 절대 금지
- YouTube, TikTok, Instagram 모든 플랫폼 영어 제목
- 해시태그도 영어로 작성

## Key Concepts

1. **스킬 기반**: Claude Code 스킬로 워크플로우 실행
2. **캐릭터 일관성**: 모든 프롬프트에 동일한 캐릭터 설명 유지
3. **완전 자동화**: 스토리 선택 1회만 확인, 이후 전부 자동 진행
4. **배경음악 없음**: 모든 프롬프트에 "No background music, natural ambient sound only" 포함
5. **자막 포함**: 각 장면의 **서브샷별로** 쇼츠용 캡션 (영문 + 한글) 생성. 씬 전체에 자막 1개 금지 — 서브샷마다 해당 장면에 맞는 자막 개별 작성. 반드시 2줄 줄바꿈. `...`(말줄임표) 사용 금지.
6. **글로벌 타겟**: 모든 장소는 미국/북미 기준 (한국 절대 금지)
7. **시간순 전개**: 모든 장면 시간순 배치 (과거 회상/플래시백 절대 금지)
8. **멀티샷 (Scene 2~6)**: 최대 3개 서브샷 × 최대 5초씩 (5초 초과 절대 금지). **⚠️ Scene 1은 예외: 단일 연속 장면 (서브샷 분할 금지!)**
9. **서브샷 = 개별 미니 씬**: 서브샷은 연속 실시간이 아님! 자연스럽게 연결되지만 시간이 경과해서 구별되는 개별 장면. 같은 순간의 다른 앵글 ❌
10. **Sora2 자유도**: 카메라는 상세하게, 상황은 간결하게 (과도한 묘사 금지)
11. **1인칭 POV 촬영자 = 등장인물**: 손, 옷소매, 목소리가 보이므로 매 프롬프트에 촬영자 캐릭터 설명 필수 (절대 생략 금지)
12. **90초 이하**: 총 영상 길이 90초 이하. 장면 6개 × 15초 (고정)
13. **참조 이미지 프레임 (0-1초)**: 모든 프롬프트 시작에 `(0-1초) 참조 이미지 프레임. — 1초에 빠른 화면 전환 —` 고정. Sora2가 참조 이미지 배경으로 시작하므로 0-1초는 비워두고 후편집에서 잘라냄
14. **서브샷 간 전환 프롬프트**: 서브샷 사이에 `— 자연스러운 화면 전환 —` 필수. 영화식 전환(cut, dissolve, fade) 금지

## 🔒 프롬프트 스타일 (영구 고정 - 절대 변경 금지)

**반드시 아마추어 핸드폰 푸티지 스타일로 작성**

### 🚨 최우선 원칙: 진짜 현실처럼 보여야 한다
- **영화처럼 보이면 실패** — 이것이 프롬프트 작성의 가장 중요한 원칙
- 모든 카메라 지시는 "실제로 핸드폰을 든 사람이 이렇게 촬영할 수 있는가?"로 판단
- 영화적 카메라워크(와이드→미디엄→클로즈업, 핑퐁 편집, 로우앵글 등) 절대 금지
- 서브샷은 촬영자의 자연스러운 카메라 움직임(줌인/줌아웃, 상하좌우 이동)으로만 전환

### 촬영 시점별 규칙
- **1인칭 POV**: 한 손 촬영, 연속, 촬영자 시선/움직임 따라감
- **주변인 촬영**: 한 위치 고정, 디지털 줌, 다른 물체 뒤에서 몰래 촬영
- **홈비디오**: 바닥에 놓거나 한 손, 자연 조명

### 필수 요소
- `First person POV handheld phone footage`
- `Shaky`, `unsteady`, `amateur footage`
- `Phone flashlight only` (야간)
- `Out of focus moments`
- `Heavy breathing audible`
- 단순하고 직접적인 문장
- 실제 사람이 촬영한 것처럼 자연스럽게

### 금지되는 영화적 카메라워크
- ❌ `와이드` → `미디엄` → `클로즈업` (3단 구성)
- ❌ `핑퐁` 편집 (A↔B 교차)
- ❌ `로우앵글`, `하이앵글` (의도적 앵글 변화)
- ❌ `트래킹샷`, `돌리샷` (카메라 장비 이동)
- ❌ `여러 앵글에서 편집` (주변인 촬영인데 여러 카메라)
- ❌ `슬로우 모션`, `매치 컷`

### 사운드 규칙 (중요!)
- ❌ 배경음악(BGM)만 없앰: `No background music`
- ✅ 자연스러운 소리는 반드시 포함:
  - 동물 소리: fox crying, wolf growling 등
  - 사람 소리: heavy breathing, footsteps, yelling
  - 환경음: forest sounds, leaves crunching, tent fabric sounds

```
❌ "No background music, no sounds"
✅ "No background music, only fox crying, footsteps, heavy breathing"
```

### 금지 표현 (영화적/비현실적)
- ❌ `devastating scene`, `horrifying`, `terrifying`
- ❌ `piercing`, `anguished`, `frantically`
- ❌ `violently`, `dramatically`, `cinematic`
- ❌ `dramatic shadows`, `dramatic lighting`
- ❌ `devastating discovery moment`
- ❌ 과장된 형용사, 문학적 표현

### 대사 규칙 (영구 적용)
- ❌ 구체적인 대사 금지: `"HEY!"`, `"Come here!"`, `"Oh my god!"` 등
- ✅ 대사 가이드만 제공: Sora2가 자연스럽게 생성하도록

```
❌ "yelling 'HEY! HEY!' at the wolf"
✅ "yelling aggressively at the wolf to scare it away"

❌ "saying 'It's okay, I'm here'"
✅ "speaking softly to calm the fox down"

❌ "shouting 'Get away!'"
✅ "shouting to chase the wolves away"
```

### 올바른 예시
```
❌ "The flashlight beam cuts through the darkness and reveals a devastating scene"
✅ "Shaky flashlight beam sweeps across dark forest floor"

❌ "lets out a piercing, anguished scream"
✅ "starts crying loud"

❌ "Camera shakes violently as the man starts running"
✅ "Camera shakes badly as the man runs forward"

❌ "Devastating discovery moment. Harsh flashlight creating dramatic shadows."
✅ "Unsteady amateur footage, phone flashlight only, out of focus moments."
```

## 🔄 에이전트 시스템 동기화 규칙 (영구 고정)

**에이전트 시스템 프롬프트가 수정되면 반드시 CLAUDE.md에도 반영한다.**

- `prompts/` 디렉토리의 시스템 프롬프트 수정 시 → CLAUDE.md의 관련 섹션 업데이트
- 새로운 규칙/원칙 추가 시 → CLAUDE.md에 요약 반영
- 규칙 삭제/변경 시 → CLAUDE.md에서도 동일하게 반영
- CLAUDE.md는 에이전트 시스템의 **요약본** 역할 — 상세 내용은 `prompts/`에, 핵심 규칙은 CLAUDE.md에

### 동기화 대상
| 시스템 프롬프트 | CLAUDE.md 섹션 |
|---------------|---------------|
| `sora2_system.md` | 프롬프트 스타일, Key Concepts |
| `scene_system.md` | 프롬프트 스타일 (카메라 규칙) |
| `story_system.md` | Key Concepts (스토리 관련) |
| `title_system.md` | 제목 규칙 |
| `caption_system.md` | Key Concepts (자막 관련) |

## Git 규칙

**코드 변동사항 발생 시 자동으로 git commit & push 실행**

```bash
# 변경사항 발생 시 자동 실행
git add -A
git commit -m "feat/fix/docs: 변경 내용 요약"
git push
```

- 프로젝트 파일 생성/수정 시 즉시 push
- 스킬/프롬프트 수정 시 즉시 push
- 설정 파일 변경 시 즉시 push
