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

### 2. 쇼츠 생성
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
│   ├── animal-shorts-research.md # 스토리 리서치 에이전트 (NEW)
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

## 워크플로우

```
[선택] /animal-shorts-research 동물
    ↓
인터넷에서 바이럴 스토리 검색/분석
    ↓
추천 스토리 선택
    ↓
/animal-shorts 입력
    ↓
Step 1: 입력 분석 → 확인
    ↓
Step 2: 스토리 생성 (5막) → 확인
    ↓
Step 3: 장면 분할 (8개+) → 확인
    ↓
Step 4: Sora2 프롬프트 생성 → 확인
    ↓
Step 5: 제목 생성 → 확인
    ↓
Step 6: 파일 저장 (projects/{slug}/prompts.md)
```

## 자동 진행 규칙 (영구 고정)

**사용자가 "진행해", "ㅇㅇ" 등으로 승인하면 다음 단계로 자동 진행**

- 스킬 실행: 물어보지 말고 바로 실행
- 폴더/파일 생성: 물어보지 말고 바로 생성
- 다음 단계 진행: 물어보지 말고 바로 진행
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
3. **단계별 확인**: 각 단계에서 사용자 확인 후 진행
4. **배경음악 없음**: 모든 프롬프트에 "No background music, natural ambient sound only" 포함
5. **자막 포함**: 각 장면마다 쇼츠용 캡션 (영문 + 한글) 생성
6. **글로벌 타겟**: 모든 장소는 미국/북미 기준 (한국 절대 금지)

## 🔒 프롬프트 스타일 (영구 고정 - 절대 변경 금지)

**반드시 아마추어 핸드폰 푸티지 스타일로 작성**

### 필수 요소
- `First person POV handheld phone footage`
- `Shaky`, `unsteady`, `amateur footage`
- `Phone flashlight only` (야간)
- `Out of focus moments`
- `Heavy breathing audible`
- 단순하고 직접적인 문장
- 실제 사람이 촬영한 것처럼 자연스럽게

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
