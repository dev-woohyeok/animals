# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

**Animal Shorts Agent System** - 동물 관련 감동 쇼츠 영상 제작을 위한 Sora2 프롬프트 생성 시스템.
Claude Code 스킬 기반으로 동작하며, Max 구독만으로 사용 가능.

## 사용법

```
/animal-shorts [동물] / [상황] / [감정] / [결말]
```

### 예시
```
/animal-shorts 골든 리트리버 / 버려진 후 노인을 만남 / 감동, 따뜻함
/animal-shorts 아기 고슴도치 / 골든리트리버가 입에 물고 옴 / 귀여움 / 가족이 됨
```

## Project Structure

```
animals/
├── .claude/commands/     # Claude Code 스킬
│   ├── animal-shorts.md        # 메인 워크플로우
│   ├── animal-shorts-story.md  # 스토리 생성
│   ├── animal-shorts-scene.md  # 장면 분할
│   ├── animal-shorts-prompt.md # Sora2 프롬프트
│   ├── animal-shorts-title.md  # 제목 생성
│   └── animal-shorts-export.md # 파일 출력
│
├── prompts/              # 시스템 프롬프트 (스킬에서 참조)
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
/animal-shorts 입력
    ↓
Step 1: 입력 분석 → 확인
    ↓
Step 2: 스토리 생성 (5막) → 확인
    ↓
Step 3: 장면 분할 (6개+) → 확인
    ↓
Step 4: Sora2 프롬프트 생성 → 확인
    ↓
Step 5: 제목 생성 → 확인
    ↓
Step 6: 파일 저장 (projects/{slug}/prompts.md)
```

## Key Concepts

1. **스킬 기반**: Claude Code 스킬로 워크플로우 실행
2. **캐릭터 일관성**: 모든 프롬프트에 동일한 캐릭터 설명 유지
3. **단계별 확인**: 각 단계에서 사용자 확인 후 진행
4. **Home Video 스타일**: 1인칭 POV 핸드헬드 촬영 기본
5. **배경음악 없음**: 모든 프롬프트에 "No background music, natural ambient sound only" 포함
6. **자막 포함**: 각 장면마다 쇼츠용 캡션 (영문 + 한글) 생성

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
