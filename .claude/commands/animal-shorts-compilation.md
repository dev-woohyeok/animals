# /animal-shorts-compilation - TikTok 컴필레이션 쇼츠

> TikTok 트렌드 기반 고양이 컴필레이션 쇼츠 생성기.
> 매 영상마다 다른 품종·장소·시추에이션의 10초 독립 클립 8개 (총 80초)를 출력.
> 사용자가 후편집(CapCut 등)으로 이어 붙임.

## 사용법

```
/animal-shorts-compilation [--mood MOOD] [--fresh] [--animal ANIMAL] [--clips N]
```

| 플래그 | 기본값 | 설명 |
|--------|------|------|
| `--mood` | `mixed` | `cute` / `dumb` / `annoying` / `mixed` |
| `--fresh` | off | 라이브러리 픽 전 웹 검색으로 새 클립 보강 |
| `--animal` | `cat` | 현재 `cat` 만 지원 |
| `--clips` | `8` | 클립 개수 (6~12 허용) |

### 예시
```
/animal-shorts-compilation                       # cat, mixed, 8개
/animal-shorts-compilation --mood dumb           # 멍청 8개
/animal-shorts-compilation --fresh --mood cute   # 검색 보강 후 귀여움 8개
/animal-shorts-compilation --mood annoying --clips 6
```

---

## ⚠️ 워크플로우 — 완전 자동, 사용자 확인 없음

**기존 `/animal-shorts` 와 달리 스토리 선택조차 없음. 명령어 한 줄 입력하면 끝까지 자동 실행.**

```
[입력] /animal-shorts-compilation --mood dumb
   ↓
Step 1. 라이브러리 로드
   ↓
Step 2. (--fresh 시) 트렌드 검색 보강
   ↓
Step 3. 다양성 제약으로 8개 픽
   ↓
Step 4. Seedance 2.0 프롬프트 8개 생성
   ↓
Step 5. 영문 제목 + 해시태그
   ↓
Step 6. 파일 저장 + used.json 갱신 + git commit & push
```

---

## Step 1: 라이브러리 로드

다음 파일을 읽어들인다:
- `library/cat_clips/catalog.json` — 전체 클립 카탈로그
- `library/cat_clips/used.json` — 사용된 clip_id 추적

검증:
- `catalog.json` 의 `clips` 배열에 mood 필터 통과 항목이 요청 개수 이상 있는지 확인
- 부족 시 `--fresh` 자동 강제 (사용자 입력 없이)

---

## Step 2: `--fresh` 시 트렌드 검색 보강

`--fresh` 플래그가 있거나 라이브러리 부족 시 실행.

### 검색 키워드 (mood별)

| mood | 키워드 |
|------|--------|
| cute | "viral kitten cute tiktok 2026", "cute cat trending reddit", "wholesome cat tiktok recent" |
| dumb | "stupid cat compilation tiktok 2026", "dumb cat moments reddit", "derpy cat tiktok viral" |
| annoying | "annoying cat tiktok viral 2026", "cats being assholes reddit", "cat menace tiktok" |
| mixed | 위 3개 카테고리 모두 |

### 검색 방법
1. **WebSearch** — TikTok / YouTube Shorts 메타데이터 검색
2. **WebFetch** — Reddit 핫 페이지 직접 조회
   - `https://www.reddit.com/r/cats/top/?t=month`
   - `https://www.reddit.com/r/CatsAreAssholes/top/?t=month`
   - `https://www.reddit.com/r/IllegallySmolCats/top/?t=month`

### LLM 정규화
검색 결과 텍스트를 읽고 catalog.json 신규 항목 형식으로 변환:
- 필수 필드: `breed`, `breed_visual`, `age_stage`, `location`, `location_category`, `location_visual`, `situation`, `point`, `tags`, `popularity`
- 미국 장소로 정규화 (외국 도시 → 미국 도시 변환)
- `id`: `cat_NNNN` 형식 (현재 최대 ID + 1부터)
- `trend_source`: 출처 URL 또는 키워드
- `added_at`: 오늘 날짜

### 중복 검출
새 항목 생성 시 기존 catalog.clips 와 다음 키 매칭으로 중복 제거:
- `breed` + `location_category` + `tags[0]` 모두 같으면 중복으로 판단

### 보강 후 파일 갱신
- `catalog.json` 의 `clips` 배열에 append, `last_updated` 갱신
- `search_log.json` 의 `entries` 배열에 한 줄 기록:
  ```json
  {
    "timestamp": "2026-05-07T14:23:00",
    "mood": "dumb",
    "queries": [...],
    "added_clip_ids": ["cat_0021", "cat_0022", ...]
  }
  ```

---

## Step 3: 픽 (8개) — 다양성 제약

알고리즘:

1. **mood 필터링**:
   - `cute` / `dumb` / `annoying`: `clip.point == mood`
   - `mixed`: 전체

2. **사용 제외**: `used.json.used_clip_ids` 에 있는 ID 제외

3. **다양성 제약** (8개 최종 풀에서):
   - 같은 `breed` 2회 이상 금지
   - 같은 `location_category` 2회 이상 금지
   - 같은 `tags[0]` 2회 이상 금지

4. **mixed 모드**: 8개 분배 — cute 3 / dumb 3 / annoying 2

5. **picks**: `popularity` 가중 랜덤. 다양성 제약 위반 시 다음 후보로.

6. **부족 시**:
   - 후보 풀 < 요청 개수 → `--fresh` 자동 실행 후 재시도
   - 그래도 부족 → 가능한 만큼만 출력 + 경고 메시지

---

## Step 4: Seedance 2.0 프롬프트 생성 (8개)

`prompts/compilation_system.md` 의 시스템 프롬프트를 따라 영어 프롬프트 8개 생성.

### 핵심 룰 (compilation_system.md 요약)
1. **10초 단일 연속 컷** — 서브샷 절대 금지 (0-5s/5-10s 분할 X)
2. **`@Image` 참조 없음** — 캐릭터 시트 없이 텍스트 묘사만
3. **`// Story:` 컴팩트** — `Compilation video — 8 {mood} cats. Clip {N}/8 — independent clip.` 한 줄
4. **`// Caption (EN, 1 line)` 포함** — TikTok 스타일 짧은 영문 1줄
5. **사운드 직접 명시** — 행동+소리 결합 (Seedance 2.0 룰)
6. **카메라 = 아마추어 핸드폰 푸티지** — 영화적 카메라워크 금지
7. **장소 = 미국/북미** — 한국 절대 금지
8. **스타일 수식어** — `Amateur phone footage quality. Slightly shaky. Natural lighting. Photorealistic. Raw, unedited feel.` 끝에 추가
9. **한국어 번역** — `> **한국어 해석:**` 블록 필수

각 프롬프트는 catalog 항목의 다음 필드를 활용:
- `breed_visual` + `age_stage` → 동물 캐릭터 묘사
- `location_visual` + `location` → 환경 묘사
- `situation` → action+sound 체인으로 확장
- `tags[0]` → 캡션 훅 키워드
- `point` → 캡션 톤 결정

---

## Step 5: 영문 제목 + 해시태그

### 제목 패턴 (mood별)

| mood | 패턴 | 예시 |
|------|------|------|
| cute | `8 [Adjective] Cat Moments That Will [Verb] Your Heart #N` | `8 Tiny Cat Moments That Will Melt Your Heart #14` |
| dumb | `8 Stupid Cats That [Verb] Their [Noun] #N` | `8 Stupid Cats That Lost Their Minds #14` |
| annoying | `Cats That Are [Verb]ing You On Purpose #N` | `Cats That Are Ruining Your Life On Purpose #14` |
| mixed | `8 Cat Moments You Won't Believe Are Real #N` | `8 Cat Moments You Won't Believe Are Real #14` |

`#N` 은 같은 mood 시리즈의 회차 번호. `used.json.videos` 에서 같은 mood 영상 개수 + 1 로 계산.

### 해시태그 (공통)
```
#cats #cattok #funnycats #catlovers #catcompilation #foryou #fyp #catsoftiktok
```

mood별 추가 태그:
- cute: `#cutecats #kittens #wholesomecats`
- dumb: `#stupidcats #derpycats #dumbcats`
- annoying: `#annoyingcats #catsbeingassholes #catmenace`

---

## Step 6: 파일 저장 + git

### 출력 폴더
```
projects/cat-{mood}-{YYYYMMDD}-{NNN}/
├── prompts.md
├── title.md
└── meta.json
```

`{NNN}` = 같은 날짜의 같은 mood 영상 시퀀스 (001부터). 폴더 존재 여부 확인 후 다음 번호 사용.

### `prompts.md`
```markdown
# {Title}

## Compilation Meta
- mood: {mood}
- clips: {N}
- video_id: cat-{mood}-{YYYYMMDD}-{NNN}

---

## Clip 1 — {breed} / {location_category} / {point}
**Caption (EN)**: "{caption}"

```
{Seedance 2.0 prompt — English}
```

> **한국어 해석:**
> {Korean translation}

---

## Clip 2 — ...
```

### `title.md`
```markdown
# {Title}

## YouTube Shorts
{Title with #N}

## TikTok / Instagram
{Same or shorter}

## Hashtags
{Hashtags}
```

### `meta.json`
```json
{
  "video_id": "cat-dumb-20260507-001",
  "mood": "dumb",
  "clips": 8,
  "clip_ids": ["cat_0009", "cat_0010", ...],
  "created_at": "2026-05-07T14:23:00"
}
```

### `used.json` 갱신
- `used_clip_ids` 에 이번 8개 ID append
- `videos` 에 새 항목 append:
  ```json
  {
    "video_id": "cat-dumb-20260507-001",
    "mood": "dumb",
    "clip_ids": [...],
    "created_at": "2026-05-07T14:23:00"
  }
  ```

### git 자동 커밋 & 푸시
```bash
git add -A
git commit -m "feat: cat compilation #{NNN} — {mood} ({YYYYMMDD})"
git push
```

---

## 참조 파일

- `prompts/compilation_system.md` — Seedance 2.0 컴필레이션 프롬프트 시스템
- `library/cat_clips/catalog.json` — 클립 카탈로그
- `library/cat_clips/used.json` — 사용 추적
- `library/cat_clips/search_log.json` — 검색 히스토리
- `docs/plans/2026-05-07-tiktok-cat-compilation-design.md` — 디자인 문서

---

## 제약사항

**허용**:
- 매 클립 다른 품종·장소·시추에이션
- 카탈로그 누적 + `--fresh` 트렌드 보강
- 시리즈 전체 중복 방지

**불허**:
- 스토리 선택 등 사용자 확인 (절대 금지)
- 한국 장소/배경
- 클립 내 서브샷 분할 (10초 단일 연속만)
- `@Image` 캐릭터 시트
- 영문 + 한글 2줄 자막 (영문 1줄만)
- 영화적 카메라워크
