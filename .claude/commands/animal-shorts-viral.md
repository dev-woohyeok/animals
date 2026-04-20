# /animal-shorts-viral - 바이럴 공식 쇼츠 생성

> 채널 분석 데이터 기반 검증된 바이럴 공식으로 쇼츠 프롬프트를 생성합니다.
> 두 가지 S/A티어 공식 중 선택하거나, 둘 다 제안받을 수 있습니다.

## 사용법

```
/animal-shorts-viral [동물]
/animal-shorts-viral [동물] --surprise
/animal-shorts-viral [동물] --rescue
```

### 예시
```
/animal-shorts-viral 코기                  # 두 공식 모두 제안 (6개)
/animal-shorts-viral 골든 리트리버 --surprise  # 서프라이즈 공식만 (3개)
/animal-shorts-viral 고양이 --rescue          # 분노+구조 공식만 (3개)
```

---

## ⚠️ 워크플로우 (완전 자동화)

**스토리 선택만 물어보고, 나머지는 전부 자동 진행. 중간에 절대 멈추지 않는다.**

```
Step 1: 공식별 스토리 제안
        ├── --surprise → formula1에서 3개
        ├── --rescue   → formula2에서 3개
        └── (없음)     → formula1 3개 + formula2 3개 = 6개
          ↓
    [유일한 사용자 확인] 스토리 선택
          ↓
Step 2: 스토리 생성 (/animal-shorts-story) → 자동 진행
          ↓
Step 3: 장면 분할 (/animal-shorts-scene) → 자동 진행
          ↓
Step 4: Sora2 프롬프트 (/animal-shorts-prompt) → 자동 진행
          ↓
Step 5: 제목 생성 (/animal-shorts-title) → 자동 진행
          ↓
Step 6: 파일 저장 + git commit & push (/animal-shorts-export) → 완료
```

---

## Step 1: 스토리 제안

### 플래그 없음 (기본) — 6개 제안

두 공식 스킬을 모두 호출하여 총 6개 스토리를 제안합니다.

```
📋 바이럴 공식 스토리 옵션:

━━━ 🎁 서프라이즈 공식 (S티어) ━━━
"My [개]이 [야생동물]을 데려왔다" — 놀라움+귀여움+따뜻함

🦊 1. 「[제목]」
   [시놉시스]
   📌 "[English title]"

🐺 2. 「[제목]」
   [시놉시스]
   📌 "[English title]"

🦝 3. 「[제목]」
   [시놉시스]
   📌 "[English title]"

━━━ 😡 분노+구조 공식 (A티어) ━━━
"누군가 [약한 동물]을 [잔인하게]" — 분노→구조→감동

😡 4. 「[제목]」
   [시놉시스]
   📌 "[english title]"

😢 5. 「[제목]」
   [시놉시스]
   📌 "[english title]"

💔 6. 「[제목]」
   [시놉시스]
   📌 "[english title]"

→ 번호를 선택하세요.
```

### --surprise 플래그 — 3개 제안
`/animal-shorts-formula1` 스킬의 로직으로 서프라이즈 공식 스토리 3개만 제안.

### --rescue 플래그 — 3개 제안
`/animal-shorts-formula2` 스킬의 로직으로 분노+구조 공식 스토리 3개만 제안.

---

## Step 2~6: 자동 파이프라인

**스토리 선택 후 모든 단계는 자동 실행. 중간에 절대 묻지 않는다.**

### Step 2: 스토리 생성
선택된 스토리를 기반으로 `prompts/story_system.md` 규칙에 따라 5막 구조 상세 스토리 생성.

- formula1 선택 시: `u_curve` 패턴 + `unexpected_bond` 아키타입 적용
- formula2 선택 시: `viral_abandonment` 패턴 + `rescue_adoption` 아키타입 적용

→ 완료 즉시 Step 3으로 자동 진행.

### Step 3: 장면 분할
`prompts/scene_system.md` 규칙에 따라 장면 분할.

**핵심 규칙**:
1. **Scene 1**: 단일 연속 장면 (서브샷 분할 금지)
2. **Scene 2~6**: 최대 3개 서브샷 × 최대 5초
3. **서브샷 = 개별 미니 씬** (시간 경과, 같은 순간 다른 앵글 ❌)
4. **시간순 전개만** (플래시백 금지)

→ 완료 즉시 Step 4로 자동 진행.

### Step 4: Sora2 프롬프트 생성
`prompts/sora2_system.md` 규칙에 따라 한국어 프롬프트 생성.

**핵심 규칙**:
1. 캐릭터 일관성: 모든 프롬프트에 동일 캐릭터 설명
2. Self-Contained: 각 프롬프트에 전체 맥락 포함
3. 아마추어 핸드폰 촬영 스타일 필수
4. `(0-1초) 참조 이미지 프레임` 고정
5. `No background music` + 자연음 필수

→ 완료 즉시 Step 5로 자동 진행.

### Step 5: 제목 생성
`prompts/title_system.md` 규칙 + 공식별 내장 제목 패턴 적용.

- formula1: "My [breed] [brought/found] a [wild animal]" 패턴
- formula2: "he [kicked/abandoned] a [tiny/pregnant] [animal]" 패턴 (소문자)

→ 완료 즉시 Step 6으로 자동 진행.

### Step 6: 파일 저장 + git
`projects/{slug}/prompts.md` 형식으로 저장. git commit & push 자동 실행.

---

## 📊 채널 실측 데이터 (@paw__therapy — 2026.04.20 기준)

### 채널 기본
| 항목 | 수치 |
|------|------|
| 팔로워 | 93,057 |
| 총 좋아요 | 1,925,152 |
| 총 영상 | 69개 |
| 총 조회수 | ~47,000,000 |
| 채널 개설 | 2025년 12월 |

### 공식별 성과 비교
| 공식 | 티어 | 50만+ 영상 | 평균 조회수 | 평균 좋아요율 | 강점 |
|------|------|-----------|-----------|-------------|------|
| **서프라이즈** (야생동물+3AM) | S | 4개 | ~6,300,000 | 3.1% | 조회수 폭발력 |
| **이종 보호** (강한→약한 동물) | A | 1개 | 6,200,000 | 7.1% | 조회수+인게이지먼트 둘 다 |
| **분노+구조** (학대→구출) | A | 3개 | ~2,500,000 | 7.0% | 인게이지먼트 최강 |
| **유기/충성** (버림→재회) | B | 4개 | ~1,460,000 | 5.7% | 안정적 성과 |

### 동물별 성과 랭킹
| 동물 | 평균 조회수 | 등급 | 비고 |
|------|-----------|------|------|
| **여우(Fox)** | 3,057,089 | S급 | 채널 절대 강자 |
| **핏불(Pit bull)** | 6,200,000 | S급 | 샘플 1개지만 압도적 |
| **코기(Corgi)** | 2,600,000 | S급 | |
| **허스키(Husky)** | 1,258,867 | A급 | |
| 고양이(Cat) | 602,612 | B급 | |
| 골든 리트리버 | 17,567 | D급 | ⚠️ 비추천 |

### 최적 영상 길이
| 길이 | 평균 조회수 | 판정 |
|------|-----------|------|
| **60초 전후** | 968,434 | ✅ 최적 |
| 65-70초 | 623,826 | ⚠️ 감소 |
| 75초+ | 177,954 | ❌ 급감 |

### 제목 패턴 (50만+ 영상 공통)
```
1. 1인칭 시점: "My corgi...", "Fox tackled me..." → 몰입감
2. 분노 유발: "He kicked...", "Dragged..." → 댓글 폭발
3. 시간 설정: "3 AM", "at midnight" → 긴장감+호기심
4. 강한 동사: tackled, dragged, guarded, kicked → 즉각 행동 이미지
```

---

## 공식별 참조 스킬

| 공식 | 스킬 | 감정 패턴 | 아키타입 |
|------|------|----------|---------|
| 서프라이즈 | `/animal-shorts-formula1` | `u_curve` | `unexpected_bond` |
| 이종 보호 | `/animal-shorts-formula1` (서브 공식) | `u_curve` | `unexpected_bond` |
| 분노+구조 | `/animal-shorts-formula2` | `viral_abandonment` | `rescue_adoption` |
| 유기/충성 | `/animal-shorts-formula2` (서브 공식) | `viral_abandonment` | `rescue_adoption` |

---

## 참조 파일

### 공식 스킬
- `.claude/commands/animal-shorts-formula1.md` — 서프라이즈 공식
- `.claude/commands/animal-shorts-formula2.md` — 분노+구조 공식

### 파이프라인 스킬
- `.claude/commands/animal-shorts-story.md` — 스토리 생성
- `.claude/commands/animal-shorts-scene.md` — 장면 분할
- `.claude/commands/animal-shorts-prompt.md` — Sora2 프롬프트
- `.claude/commands/animal-shorts-title.md` — 제목 생성
- `.claude/commands/animal-shorts-export.md` — 파일 출력

### 시스템 프롬프트
- `prompts/story_system.md`
- `prompts/scene_system.md`
- `prompts/sora2_system.md`
- `prompts/title_system.md`

### 템플릿
- `library/templates/emotional_patterns/u_curve.md`
- `library/templates/emotional_patterns/viral_abandonment.md`
- `library/templates/story_archetypes/unexpected_bond.md`
- `library/templates/story_archetypes/rescue_adoption.md`

---

## 제약사항

**허용**:
- 채널 분석 데이터 기반 바이럴 최적화 스토리 생성
- 두 가지 검증된 공식 활용
- 기존 파이프라인 완전 활용

**불허**:
- 스토리 선택 이후 중간에 사용자에게 확인 요청 (금지!)
- 한국 장소/배경 (미국/북미만)
- 플래시백/시간 역행
- 동물 사망/유혈 장면
