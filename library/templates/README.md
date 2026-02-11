# Story Templates Library

감동적인 동물 스토리를 만들기 위한 감정 패턴과 스토리 원형 템플릿 모음

## Quick Reference

### Emotional Patterns (감정 패턴)

| 패턴 | 특징 | 적합한 상황 |
|------|------|-------------|
| **viral_abandonment** | 분노→안쓰러움→무력감→안도→감동 | 유기 스토리, 바이럴 극대화 |
| **dual_climax** | 두 번의 절정 (비극 + 결심) | 구조 스토리, 강렬한 감정 |
| **gradual_rise** | 비극 시작 → 성장 → 재회 | 양육/성장, 세대 연결 |
| **u_curve** | 경계 → 유대 → 이별 → 재회 | 유머+감동, 다른 종 우정 |

### Story Archetypes (스토리 원형)

| 원형 | 핵심 플롯 | 추천 감정 패턴 |
|------|----------|---------------|
| **rescue_adoption** | 위기 동물 구조 → 가족 | viral_abandonment, dual_climax |
| **unexpected_bond** | 거부 → 우정 → 가족 | u_curve |
| **loss_and_reunion** | 유대 → 이별 → 재회 | gradual_rise |

---

## How to Use

### 1. 스토리 아이디어에서 시작

```
입력: "버려진 아기 고양이를 발견해서 키우다가 큰 후 방생했는데 1년 후 돌아옴"
```

### 2. 적합한 원형 선택

위 예시에 적합한 원형: **rescue_adoption** + **loss_and_reunion**

### 3. 감정 패턴 선택

성장과 재회가 핵심 → **gradual_rise** 패턴

### 4. 템플릿 적용

```yaml
archetype: rescue_adoption + loss_and_reunion
emotional_pattern: gradual_rise

opening_tragedy:
  event: "버려진 아기 고양이 발견"
  intensity: 70

growth_milestones:
  - "첫 우유 먹기"
  - "눈 뜨는 순간"
  - "첫 걸음"
  - "함께 자는 밤"

separation:
  reason: "야생 본능 발현, 방생"

reunion:
  time_gap: "1년"
  surprise: "새끼들을 데리고 옴"
```

---

## Pattern Selection Guide

### 어떤 감정을 극대화하고 싶은가?

| 원하는 효과 | 추천 패턴 |
|------------|----------|
| 바이럴 조회수 터뜨리고 싶다 | viral_abandonment |
| 최대한 울리고 싶다 | dual_climax |
| 따뜻하게 마무리하고 싶다 | gradual_rise |
| 웃음과 감동 둘 다 | u_curve |

### 스토리의 핵심 사건은?

| 핵심 사건 | 추천 패턴 |
|----------|----------|
| 유기/버림받음 | viral_abandonment |
| 비극적 발견/상실 | dual_climax |
| 성장과 독립 | gradual_rise |
| 처음엔 싫었는데 친해짐 | u_curve |

---

## Combination Examples

### Example 0: 고속도로 유기 강아지 스토리

```
원형: rescue_adoption
패턴: viral_abandonment

- 분노(Hook): CCTV에 찍힌 고속도로 유기 장면
- 안쓰러움: 차를 따라 달리다 멈춰선 강아지
- 무력감: 도로 한가운데서 지쳐 웅크림
- 안도: 다른 차가 멈추고 구조
- 감동: 새 가족과 행복한 일상
```

### Example 1: 아기 여우 스토리

```
원형: rescue_adoption
패턴: dual_climax

- 제1절정: 엄마 여우 죽음 발견
- 제2절정: "집에 가자" 결심
```

### Example 2: 캥거루 스토리

```
원형: rescue_adoption + loss_and_reunion
패턴: gradual_rise

- 시작: 어미가 아기를 맡김 (비극)
- 성장: 손바닥 → 성체
- 이별: 야생으로
- 재회: 자신의 아기와 귀환
```

### Example 3: 늑대 스토리

```
원형: unexpected_bond + loss_and_reunion
패턴: u_curve

- 시작: 침입 (유머)
- 갈등: 개집 빼앗김
- 유대: 함께 생활
- 이별: 부모가 데려감
- 재회: 1년 후 방문
```

---

## File Structure

```
library/templates/
├── README.md                    # 이 파일
├── emotional_patterns/          # 감정 곡선 패턴
│   ├── viral_abandonment.md   # 바이럴 유기 (분노→안쓰러움→무력감→안도→감동)
│   ├── dual_climax.md          # 이중 절정
│   ├── gradual_rise.md         # 점진적 상승
│   └── u_curve.md              # U자형
│
└── story_archetypes/           # 스토리 구조 원형
    ├── rescue_adoption.md      # 구조 → 입양
    ├── unexpected_bond.md      # 예상치 못한 유대
    └── loss_and_reunion.md     # 상실 → 재회
```

---

## Creating New Stories

### Step-by-Step

1. **입력 분석**: 동물, 상황, 감정, 결말 파악
2. **원형 선택**: 가장 적합한 스토리 구조 선택
3. **패턴 선택**: 감정 곡선 결정
4. **비트 작성**: 5막 구조에 맞게 장면 배치
5. **감정 확인**: 감정 강도와 전환점 확인

### Tips

- 원형은 조합 가능 (rescue + reunion)
- 패턴의 절정 위치를 핵심 사건에 맞추기
- 이별-재회 구조는 시간 경과 표현 필수
- 코믹 요소는 u_curve에서 효과적

---

## Integration with /animal-shorts-story

이 템플릿들은 `/animal-shorts-story` 스킬에서 자동 참조됩니다.

```
/animal-shorts-story 버려진 강아지 / 노인을 만남 / 감동 --pattern=gradual_rise
```

스킬이 입력을 분석하여 자동으로 적합한 템플릿을 추천합니다.
