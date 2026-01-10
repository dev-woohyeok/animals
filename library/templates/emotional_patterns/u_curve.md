# U-Curve Pattern (U자형 패턴)

> 경계에서 시작해 유대를 형성하고, 이별 후 재회로 완성되는 곡선

## Pattern Overview

```
강도
100 |                                          ★ (재회/감동)
 90 |                     ★ (가족)          /
 80 |                  /                   /
 70 |               ★ (우정)            /
 60 |            /                    ★
 50 |    ★---★ (유머)               /  (그리움)
 40 | ★ (경계)                    /
 30 |                          ★ (이별/슬픔)
    |_____________________________________________
      도입    전개    전환      해결      결말
```

## Emotional Journey

| Position | Phase | Emotion | Intensity |
|----------|-------|---------|-----------|
| 0.0 | 도입 | 놀람, 경계 | 40 |
| 0.15 | 전개 | 유머, 황당함 | 60 |
| 0.25 | 전개 | 긴장 속 유머 | 55 |
| 0.40 | 전환 | 따뜻함, 우정 | 75 |
| 0.55 | 전환 | 평화, 가족애 | 90 |
| 0.70 | **해결 (저점)** | **슬픔, 이별** | **30** |
| 0.80 | 해결 | 공허, 그리움 | 50 |
| 1.0 | **결말 (정점)** | **감동, 재회** | **100** |

## Pattern Characteristics

### 핵심 특징
- **낮은 시작**: 경계심/거부에서 시작 (비극 아님)
- **코믹 요소**: 초반에 유머로 분위기 이완
- **점진적 유대**: 자연스럽게 가까워지는 과정
- **깊은 저점**: 이별에서 가장 낮은 감정
- **급상승 결말**: 재회로 한번에 최고조

### 효과
- 유머와 감동의 균형
- 이별의 슬픔이 재회의 감동 증폭
- 가벼운 시작으로 접근성 높음

## Story Structure for This Pattern

### 1. 도입 - 예상치 못한 만남 (0.0 - 0.15)
- 갑작스러운 침입/등장
- 주인공(동물 또는 인간)의 놀람/경계
- 낯선 존재와의 첫 대면

### 2. 전개 - 유머와 갈등 (0.15 - 0.40)
- 코믹한 상황 전개
- 공간/음식/관심 다툼
- 한쪽이 거부하지만 다른 쪽이 포기 안함
- 점진적 수용

### 3. 전환 - 유대 형성 (0.40 - 0.55)
- 함께하는 시간 축적
- 놀이, 식사, 수면 공유
- 진정한 가족/친구 관계

### 4. 해결 - 이별 (0.55 - 0.80)
- 원래 가족/장소로 돌아가야 함
- 피할 수 없는 이별
- 남겨진 존재의 깊은 슬픔
- 텅 빈 공간의 공허

### 5. 결말 - 재회 (0.80 - 1.0)
- 시간 경과
- 성장한 모습으로 귀환
- 변치 않은 유대 확인
- 함께하는 순간의 기쁨

## Reference Story

**개구멍으로 찾아온 겨울 손님들 (늑대)**
- 시작: 아기 늑대들이 개구멍으로 침입
- 갈등: 허스키 개집 빼앗김 (유머)
- 유대: 함께 먹고 자는 가족
- 이별: 부모 늑대가 데려감
- 재회: 1년 후 성체가 되어 방문

## When to Use This Pattern

### Best For
- 다른 종 간의 우정
- 유머와 감동의 조합
- 이별과 재회 테마
- 가벼운 시작, 감동적 마무리
- 동물-동물 또는 동물-인간 관계

### Avoid When
- 처음부터 강렬한 감정 필요시
- 비극적 분위기 유지 필요시
- 시간 경과 표현이 어려울 때

## Template Variables

```yaml
pattern: u_curve
opening:
  type: "intrusion/encounter"  # intrusion, unexpected_visit, chance_meeting
  reaction: "surprise/wariness"
  intensity: 40

comedy_phase:
  conflict: "{{COMEDIC_CONFLICT}}"  # space, food, attention
  dynamic: "{{DYNAMIC}}"  # one_pushes_other_persists

bonding:
  activities:
    - "{{BONDING_1}}"  # play together
    - "{{BONDING_2}}"  # eat together
    - "{{BONDING_3}}"  # sleep together
  peak_emotion: "family"
  intensity: 90

separation:
  reason: "{{SEPARATION_REASON}}"  # real_family_comes, must_return
  lowest_point: 30

reunion:
  time_gap: "{{TIME_GAP}}"
  how: "{{REUNION_METHOD}}"  # howling, appears_at_door, returns_to_place
  intensity: 100
```

## Comedy-to-Drama Balance

이 패턴의 핵심은 톤 전환:

### 전반부 (코믹)
- 과장된 반응
- 황당한 상황
- 반복되는 갈등의 패턴화
- 관객의 웃음 유발

### 후반부 (드라마)
- 톤 변화 신호 (조명, 음악적 분위기)
- 슬로우 모션 활용
- 감정 클로즈업
- 정적과 여백 활용

### 전환점
- "함께 잠드는 장면"이 전환점으로 효과적
- 무방비한 순간 = 진정한 신뢰
