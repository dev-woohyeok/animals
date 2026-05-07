# TikTok Cat Compilation Generator — Design

**Date**: 2026-05-07
**Author**: dev_woo (with Claude)
**Status**: Approved → implementation

---

## 1. Overview & Goals

TikTok 트렌드 기반 고양이 컴필레이션 쇼츠 프롬프트 자동 생성. 매 영상마다 다른 품종·장소·시추에이션의 10초 독립 클립 8개 (총 80초)를 출력해, 사용자가 후편집(CapCut 등)으로 이어 붙임.

### vs. 기존 감동 쇼츠

| 항목 | 기존 감동 쇼츠 | 신규 컴필레이션 |
|------|--------------|---------------|
| 스토리 | 1개 동물 6씬 연속 서사 | 8개 독립 클립 (서사 없음) |
| 클립 길이 | 15초 (서브샷 가능) | 10초 단일 연속 |
| 캐릭터 시트 | `@ImageN` 자동 생성 필수 | 없음 (텍스트 묘사만) |
| 자막 | 영문 + 한글 2줄 | 영문 1줄 |
| 톤 | 감동·따뜻함 | 귀여움·멍청함·짜증나는 (mood 선택) |
| 데이터 소스 | 매번 새 스토리 작성 | 누적 카탈로그 + `--fresh` 검색 보강 |

### 성공 기준
1. **중복 방지**: 한 영상 내, 영상 시리즈 전체에서 같은 클립 두 번 등장 금지
2. **다양성**: 한 영상 8개 클립이 품종·장소·시추에이션 모두 다름
3. **트렌드 반영**: `--fresh` 실행 시 최신 TikTok/Reddit 트렌드 자동 수집
4. **확장성**: `--animal dog` 등 다른 동물도 같은 워크플로우
5. **자동화**: 명령어 한 줄로 끝까지 자동 실행

### Out of Scope (YAGNI)
- 영상 자체 생성 (사용자가 Seedance 2.0에 직접 투입)
- 자동 후편집/이어붙이기 (CapCut 등에서 처리)
- BGM 자동 추천 (자연 사운드만, 사용자가 후편집에서 트렌딩 BGM 추가)

---

## 2. CLI Interface & Workflow

### 명령어 시그니처
```
/animal-shorts-compilation [--mood MOOD] [--fresh] [--animal ANIMAL] [--clips N]
```

| 플래그 | 기본값 | 설명 |
|--------|------|------|
| `--mood` | `mixed` | `cute` / `dumb` / `annoying` / `mixed` |
| `--fresh` | off | 라이브러리 픽 전에 웹 검색으로 새 클립 보강 |
| `--animal` | `cat` | `cat` (현재) / `dog` 등 (향후) |
| `--clips` | `8` | 클립 개수 (6~12 허용) |

### 워크플로우 (완전 자동, 사용자 확인 없음)
```
[입력] /animal-shorts-compilation --mood dumb
   ↓
Step 1. 라이브러리 로드 (catalog.json + used.json)
   ↓
Step 2. (--fresh 시) 트렌드 검색 보강
   - WebSearch + Reddit 다중 출처 → catalog.json append
   ↓
Step 3. 픽 (8개)
   - mood 필터 + used 제외 + 다양성 제약 + popularity 가중 랜덤
   ↓
Step 4. Seedance 2.0 프롬프트 8개 (10초 단일 연속)
   ↓
Step 5. 영문 제목 (e.g. "8 Stupid Cats That Made Me Lose Faith #14")
   ↓
Step 6. 파일 저장 + used.json 업데이트 + git auto-commit/push
```

### 실패 처리
- `--fresh` 검색 실패 → 라이브러리에서 픽 (graceful fallback)
- 라이브러리 클립 < 요청 개수 → 자동 `--fresh` 강제 실행 후 재시도
- 그래도 부족 → 에러 메시지 + 수집된 N개라도 출력

---

## 3. Data Layer

### 디렉토리
```
library/cat_clips/
├── catalog.json          # 전체 클립 카탈로그 (누적)
├── used.json             # 사용된 clip_id 추적
└── search_log.json       # --fresh 실행 히스토리
```

### `catalog.json` 스키마
```json
{
  "version": 1,
  "last_updated": "2026-05-07",
  "clips": [
    {
      "id": "cat_0001",
      "breed": "British Shorthair",
      "breed_visual": "round face, gray fur, copper eyes, plush coat",
      "age_stage": "adult",
      "location": "American suburban kitchen",
      "location_category": "kitchen",
      "location_visual": "white cabinets, stainless fridge, hardwood floor",
      "situation": "Cat opens fridge with paw, climbs in, refuses to come out",
      "point": "annoying",
      "tags": ["fridge", "stuck", "stubborn", "indoor"],
      "trend_source": "reddit r/CatsAreAssholes",
      "added_at": "2026-05-07",
      "popularity": 0.8
    }
  ]
}
```

### `used.json` 스키마
```json
{
  "used_clip_ids": ["cat_0001"],
  "videos": [
    {
      "video_id": "cat-dumb-20260507-001",
      "mood": "dumb",
      "clip_ids": ["cat_0003", "cat_0008"],
      "created_at": "2026-05-07T14:23:00"
    }
  ]
}
```

### 다양성 제약 (Step 3 픽)
1. mood 필터 → 후보 풀
2. `used_clip_ids` 제외
3. 후보 < 요청 → `--fresh` 강제
4. 다양성:
   - 같은 `breed` 2회 이상 금지
   - 같은 `location_category` 2회 이상 금지
   - 같은 `tags[0]` 2회 이상 금지
5. `popularity` 가중 랜덤 픽
6. mixed 모드: cute 3 / dumb 3 / annoying 2 균등

### 카탈로그 고갈
- 거의 발생 안 함 (`--fresh` 보강 가능)
- 발생 시: `library/cat_clips/used.json` 수동 리셋 안내

---

## 4. Search & Refresh Strategy

### `--fresh` 동작
1. **검색 키워드 생성** (mood 기반)
   - `cute`: "viral kitten cute tiktok 2026", "cute cat trend reddit"
   - `dumb`: "stupid cat compilation tiktok", "dumb cat reddit"
   - `annoying`: "annoying cat tiktok viral", "cats being assholes reddit"
   - `mixed`: 위 3개 카테고리 모두 검색

2. **다중 출처 검색**
   - WebSearch (TikTok 메타, YouTube Shorts 메타)
   - WebFetch on Reddit URLs (`reddit.com/r/cats/top/?t=month` 등)

3. **LLM 정규화**
   - 검색 결과 텍스트 읽고 catalog.json 항목 형식으로 변환
   - 필수 필드 채우기 (breed, location, situation, point, tags, popularity)
   - 기존 catalog.clips와 중복 검출 (breed + location_category + tags[0] 매칭)

4. **append**
   - 1회 `--fresh` 시 5~15개 신규 항목 추가
   - `search_log.json` 에 검색어/시각/추가 ID 기록

### 검색 빈도
- 사용자가 직접 `--fresh` 줄 때만 (자동 트리거 X)
- 예외: 라이브러리 부족 시 자동 강제

---

## 5. Prompt Generation (Seedance 2.0)

### 1개 클립 = 1개 프롬프트 (한국어 작성, 미국 장소 기준)

### 프롬프트 구조
```
// Story: Compilation video — 8 [mood] cats. Clip {N}/8 — independent clip.
// Caption (EN, 1 line): "..."

10-second single continuous shot.

[breed_visual] cat in [location_visual]. [situation in detail with action+sound].

[Specific sounds — action+sound paired]
- Animal: [breed] [action], [sound], then [next action].
- Environment: [ambient sounds tied to visible cause]
- Filmmaker (if applicable): [breathing, gasps, brief words in quotes]

Camera: [first-person POV handheld phone footage / fixed phone on counter / etc.]

No background music. Amateur phone footage quality. Slightly shaky. Natural lighting. Photorealistic. Raw, unedited feel.

> **한국어 해석:**
> [전체 한국어 번역]
```

### 핵심 룰
- **클립 간 컨텍스트 없음** — 각 클립은 독립적. `// Story:` 는 컴필레이션 컨셉 + 클립 번호만
- **사운드**: 행동+소리 결합 직접 명시 (CLAUDE.md 룰)
- **카메라**: 1인칭 POV 또는 고정 핸드폰 푸티지. 영화적 카메라워크 금지
- **자막 (영문 1줄)**: 클립 시작에 `// Caption (EN, 1 line):` 으로 명시
- **캐릭터 시트 없음**: `@Image` 참조 사용 안 함. 텍스트 묘사만
- **장소**: 미국/북미 기준 (CLAUDE.md 글로벌 타겟 룰)
- **금지 표현**: cinematic, dramatic, devastating 등 (CLAUDE.md 룰 따름)

### 캡션 스타일
- TikTok 컴필레이션 표준: 짧은 wit 있는 영문 1줄
- 예시:
  - cute: `"When she finally falls asleep on me"`
  - dumb: `"He's been staring at this wall for 20 minutes"`
  - annoying: `"3 AM. Every. Single. Night."`

---

## 6. Output Structure & 동기화

### 출력 폴더
```
projects/cat-{mood}-{YYYYMMDD}-{NNN}/
├── prompts.md          # 8개 클립 Seedance 2.0 프롬프트
├── title.md            # 영문 제목 + 해시태그
└── meta.json           # clip_ids, mood, created_at, video_id
```

### `prompts.md` 구조
```markdown
# {Title}

## Compilation Meta
- mood: dumb
- clips: 8
- video_id: cat-dumb-20260507-001

## Clip 1 — [breed] / [location_category] / [point]
**Caption (EN)**: "He's been staring at this wall for 20 minutes"

```
[Seedance 2.0 prompt — 영어]
```

> **한국어 해석:** [번역]

---

## Clip 2 — ...
```

### `title.md` 구조
```markdown
# Title (English Only)

## YouTube Shorts
{Title with #N}

## TikTok / Instagram
{Same or shorter variant}

## Hashtags
#cats #cattok #funnycats #stupidcats #catlovers #catcompilation
```

### CLAUDE.md 업데이트
- "사용법" 섹션에 `/animal-shorts-compilation` 추가
- "Project Structure" 의 `.claude/commands/` 트리에 추가
- 컴필레이션 전용 규칙 (10초 단일 / 캐릭터 시트 없음 / 영문 1줄 자막) 명시

### 시드 데이터
- `library/cat_clips/catalog.json` 시드: 20개 (cute 8 / dumb 8 / annoying 4)
- 첫 실행 mixed 모드 (cute 3 / dumb 3 / annoying 2) 무리없이 가능
- 두 번째 실행부터 `--fresh` 권장

### git
- 출력 후 자동 commit & push (CLAUDE.md 룰)
- 커밋 메시지: `feat: cat compilation #{NNN} — {mood} ({YYYYMMDD})`

---

## 7. File Manifest (구현 산출물)

| 파일 | 목적 |
|------|------|
| `.claude/commands/animal-shorts-compilation.md` | 명령어 진입점 |
| `prompts/compilation_system.md` | 컴필레이션 전용 시스템 프롬프트 |
| `library/cat_clips/catalog.json` | 시드 카탈로그 (20개) |
| `library/cat_clips/used.json` | 사용 추적 (빈 초기 상태) |
| `library/cat_clips/search_log.json` | 검색 히스토리 (빈 초기 상태) |
| `CLAUDE.md` | 사용법/구조 섹션 업데이트 |
| `docs/plans/2026-05-07-tiktok-cat-compilation-design.md` | 본 디자인 문서 |
