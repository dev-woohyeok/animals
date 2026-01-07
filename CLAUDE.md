# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Animal Shorts Agent System** - 동물 관련 감동 쇼츠 영상 제작을 위한 AI 에이전트 시스템.
사용자가 동물 키워드와 줄거리를 제공하면 Sora2에 최적화된 일관성 있는 영상 프롬프트를 자동 생성한다.

## Repository

- GitHub: https://github.com/dev-woohyeok/animals.git
- Main branch: `main`

## Tech Stack

- **Language**: Python 3.11+
- **AI**: Claude API (Anthropic)
- **CLI**: Rich / Textual
- **Data**: YAML / JSON

## Project Structure

```
animals/
├── agents/           # 에이전트 모듈 (Input, Story, Scene, Prompt, etc.)
├── core/             # 핵심 기능 (Orchestrator, State, History)
├── library/          # 라이브러리 (캐릭터, 템플릿, 모범사례)
├── config/           # 설정 (스타일 프리셋, 검증 규칙)
├── prompts/          # 시스템 프롬프트
├── projects/         # 생성된 프로젝트들
├── docs/             # 문서 (PRD 등)
└── main.py           # 메인 실행 파일
```

## Commands

```bash
# 설치
pip install -r requirements.txt

# 실행
python main.py

# 테스트
pytest tests/
```

## Key Concepts

1. **에이전트 체인**: Input → Story → Scene → Prompt → Translation → Output
2. **일관성 관리**: 캐릭터/배경/스타일 정보가 모든 프롬프트에 포함
3. **단계별 확인**: 각 단계에서 사용자 확인 후 진행
4. **라이브러리**: 재사용 가능한 캐릭터/템플릿 저장소

## Development Notes

- 모든 에이전트는 `agents/base.py`의 `BaseAgent` 클래스를 상속
- 설정 파일은 YAML 형식 사용
- 프로젝트 데이터는 `projects/{slug}/` 디렉토리에 저장
