# /animal-shorts-formula2 - 분노+구조 공식 스토리 생성

> **A티어 공식**: "누군가 [약한 동물]을 [잔인하게]" → 구조 → 해피엔딩
> 분노 유발 → 공유 욕구 자극. 특히 "임신한/아기/작은" 동물일수록 효과 극대화.

## 사용법

```
/animal-shorts-formula2 [동물]
```

### 예시
```
/animal-shorts-formula2 고양이
/animal-shorts-formula2 강아지
/animal-shorts-formula2 비글
```

---

## 공식 데이터 (채널 분석 기반)

### 성공 사례
| 조회수 | 제목 | 핵심 |
|---:|---|---|
| 14.4M | he kicked out a pregnant cat with a broom | 임신 고양이 + 빗자루 |
| 5.1M | Corgi abandoned by her owner | 코기 유기 |
| 3.3M | He Kicked a Tiny Kitten Begging for Food | 새끼 고양이 발로 참 |
| 2.3M | Someone Left Their Puppy With Her Bed | 강아지 침대째 버림 |
| 1.7M | I Filmed a Stray Beagle Stealing Food | 배고픈 비글 몰래 촬영 |
| 1.5M | A Starving Dog Chased From The Trash | 굶주린 개 쓰레기통에서 쫓김 |
| 1.0M | Mama Dog Stopped Eating After They Took All 3 Puppies | 새끼 빼앗긴 엄마개 |

### 핵심 성공 요인
- **분노 유발**: 가해자가 명확한 3인칭 제목 ("he kicked", "someone left")
- **약한 피해자**: "임신한", "아기", "작은", "굶주린" 수식어가 분노 극대화
- **소문자 제목**: 의도적 소문자 = 캐주얼/실제 느낌 (14.4M 영상)
- **구조 카타르시스**: 분노 → 안도 전환이 공유 행동 유발
- **Before/After**: 처음 비참한 모습 vs 마지막 행복한 모습

---

## 스토리 생성 로직

### 입력 처리
1. 입력된 동물에 **약함 수식어** 자동 부여
2. 가해 행동 자동 선택
3. 구조자 자동 설정
4. **스토리 3개 제안**

### 약함 수식어 자동 선택
```
고양이 → 임신한 / 아기 / 작은 / 한 눈이 안 보이는
강아지 → 굶주린 / 아기 / 다리 절뚝거리는 / 갓 태어난
기타 → 아기 / 작은 / 다친 / 어린
```

### 가해 행동 자동 선택
```
- 빗자루로 쫓아냄 (14.4M 검증)
- 발로 참 (3.3M 검증)
- 침대/짐째 길에 버림 (2.3M 검증)
- 쓰레기통에서 쫓아냄 (1.5M 검증)
- 새끼를 빼앗아감 (1.0M 검증)
- 비 오는 날 밖에 내쫓음
- 이사하면서 두고 감
- 상자에 넣어 도로에 버림
```

### 구조자 유형 자동 선택
```
- 지나가던 여성/남성 (가장 보편적)
- 촬영자 본인 (1인칭 POV)
- 이웃 주민
- 아이/학생
- 배달원/택배기사
```

---

## 감정 패턴 & 아키타입 (고정)

```yaml
emotional_pattern: viral_abandonment
story_archetype: rescue_adoption
```

### 감정 곡선
```
분노(100) → 안쓰러움(75) → 무력감(30) → 안도(55) → 감동/사랑(100)
```

### 5막 구조 (이 공식 전용)
```
1막 (도입): 가해 장면 목격. 시청자 분노 폭발. "이걸 누가?!"
2막 (전개): 버려진/다친 동물의 고통. 기다림, 울음, 두리번거림.
3막 (위기): 상황 악화. 날씨, 시간, 위험 요소. 아무도 도와주지 않음.
4막 (해결): 구조자 등장. 동물을 안아 올림. 안전한 곳으로 이동.
5막 (결말): 새 가족. 건강 회복. Before/After 대비. 행복한 일상.
```

---

## 제목 공식 (내장)

### 패턴 1: 소문자 3인칭 가해자 (최강 — 14.4M 검증)
```
"he [kicked/threw out/chased away] a [pregnant/tiny/starving] [animal]"
```

### 패턴 2: Someone + 유기 행동
```
"Someone [Left/Dumped/Abandoned] Their [animal] [with/at/on] [장소/물건]"
```

### 패턴 3: 동물 주어 + 피해 상태
```
"[animal] [abandoned/chased/kicked out] by [her/his] owner"
"A [Starving/Tiny/Injured] [animal] [행동]"
```

### 패턴 4: 엄마 동물 + 새끼 분리
```
"Mama [animal] [Stopped Eating/Cried] After They Took [Her Puppies/Kittens]"
```

---

## 출력 형식

**반드시 아래 형식으로 3가지 스토리 옵션 제안:**

```
📋 분노+구조 공식 스토리 옵션:

😡 1. 「[제목]」
   [가해 행동 설명]. [동물의 상태/반응].
   [2-3문장 시놉시스 — 구조~해피엔딩까지]
   📌 제목안: "[english title — 소문자 시작]"

😢 2. 「[제목]」
   [가해 행동 설명]. [동물의 상태/반응].
   [2-3문장 시놉시스 — 구조~해피엔딩까지]
   📌 제목안: "[english title — 소문자 시작]"

💔 3. 「[제목]」
   [가해 행동 설명]. [동물의 상태/반응].
   [2-3문장 시놉시스 — 구조~해피엔딩까지]
   📌 제목안: "[english title — 소문자 시작]"

→ 번호를 선택하세요.
```

### 스토리 옵션 규칙
- 3개 옵션은 서로 다른 가해 행동 사용
- 3개 옵션은 서로 다른 약함 수식어 사용
- 각 옵션에 영어 제목안 포함 (소문자 시작 필수)
- 모든 옵션에 명확한 구조+해피엔딩 포함

---

## 콘텐츠 가이드라인 (중요!)

### 분노 유발 BUT 선 넘지 않기
```
✅ 허용:
- 빗자루로 쫓아냄
- 발로 밀어냄
- 길에 두고 떠남
- 상자에 넣어 버림
- 쓰레기통에서 쫓아냄
- 새끼를 분리함

❌ 금지 (Sora2 콘텐츠 정책 위반):
- 피가 보이는 직접적 폭력
- 동물 사망 장면
- 잔인한 도구 사용 (칼, 봉 등)
- 아동 관련 학대
- 동물 간 싸움/공격
```

### 감정 밸런스
```
분노 장면: 전체의 15-20% (Scene 1만)
고통/기다림: 전체의 30% (Scene 2-3)
구조/회복: 전체의 50%+ (Scene 4-6)

→ 분노로 시작하되, 대부분은 구조와 회복에 할애
→ 해피엔딩이 반드시 전체의 절반 이상
```

---

## 제약사항

### 필수
- 감정 패턴: `viral_abandonment` 고정
- 스토리 아키타입: `rescue_adoption` 고정
- 약함 수식어 필수 (임신한/아기/작은/굶주린 등)
- 가해자 명확 (3인칭)
- 구조 + 해피엔딩 필수
- 영어 제목 (소문자 시작 권장)
- 미국/북미 배경 (한국 장소 절대 금지)
- 시간순 전개만 (플래시백 금지)

### 금지
- 동물 사망
- 직접적 유혈/폭력
- 이종 동물 조합 중심 스토리 (→ formula1의 영역)
- 해피엔딩 없는 비극
- 한국 장소/배경

---

## 참조 파일

- `library/templates/emotional_patterns/viral_abandonment.md` — 감정 곡선
- `library/templates/story_archetypes/rescue_adoption.md` — 스토리 아키타입
- `prompts/story_system.md` — 스토리 구조 가이드
