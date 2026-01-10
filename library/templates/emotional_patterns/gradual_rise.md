# Gradual Rise Pattern (점진적 상승 패턴)

> 초반 비극에서 시작해 점진적으로 상승하는 희망의 곡선

## Pattern Overview

```
강도
100 |                                          ★ (감동/완전함)
 90 |                           ★ (행복)    /
 80 |                        /           ★
 70 |        ★ (비극)    ★ (희망)    /   (이별)
 60 |      /           /          \    /
 50 |    /         /              ★
 40 | ★ (슬픔) ★ (결심)
 30 |
    |_____________________________________________
      도입    전개    성장      해결      결말
```

## Emotional Journey

| Position | Phase | Emotion | Intensity |
|----------|-------|---------|-----------|
| 0.0 | **도입 (비극)** | **충격, 슬픔** | **70** |
| 0.15 | 전개 | 걱정, 결심 | 50 |
| 0.30 | 전개→성장 | 희망, 유대 | 65 |
| 0.50 | 성장 | 기쁨, 성취감 | 75 |
| 0.65 | 성장 | 행복, 가족애 | 85 |
| 0.75 | 해결 (이별) | 슬픔, 놓아줌 | 40 |
| 0.85 | 해결 | 공허, 그리움 | 50 |
| 1.0 | **결말 (재회)** | **감동, 완전함** | **100** |

## Pattern Characteristics

### 핵심 특징
- **강렬한 시작**: 초반에 비극적 사건으로 시작 (주의 집중)
- **점진적 회복**: 돌봄과 성장 과정에서 희망 상승
- **일시적 하락**: 이별/독립 순간에 감정 하락
- **감동적 마무리**: 예상치 못한 재회로 최고조

### 효과
- 관객이 캐릭터와 함께 성장 경험
- 시간 경과를 통한 감정 투자 축적
- 이별 후 재회가 주는 큰 보상감

## Story Structure for This Pattern

### 1. 도입 - 비극 (0.0 - 0.15)
- 충격적인 비극으로 시작 (죽음, 버림받음)
- 도움이 필요한 아기 동물
- 인간과의 첫 만남

### 2. 전개 - 결심 (0.15 - 0.30)
- 인간이 돌보기로 결심
- 서툴지만 정성스러운 양육
- 불안과 희망의 공존

### 3. 성장 (0.30 - 0.65)
- **몽타주**: 시간 경과와 성장
- 중요한 이정표 (첫 걸음, 첫 먹이 등)
- 가족으로서의 유대 심화
- 행복한 일상의 축적

### 4. 해결 - 이별 (0.65 - 0.85)
- 동물의 본능/야생 발현
- 떠나보내야 하는 결심
- 쓸쓸한 이별
- 텅 빈 공간의 공허함

### 5. 결말 - 재회 (0.85 - 1.0)
- 시간 경과 (1년, 2년)
- **예상치 못한 귀환**
- 세대를 잇는 연결 (아기 데려옴)
- 사랑이 돌아온다는 메시지

## Reference Story

**엄마가 남긴 선물 (캥거루)**
- 시작: 죽어가는 어미 캥거루가 아기를 맡김
- 성장: 손바닥 위 조이 → 성체 캥거루
- 이별: 야생 무리에 합류
- 재회: 2년 후 자신의 아기를 데리고 돌아옴

## When to Use This Pattern

### Best For
- 양육/성장 스토리
- 시간 경과가 중요한 스토리
- 세대 간 연결 테마
- 독립과 귀환의 순환
- 따뜻하고 감동적인 마무리

### Avoid When
- 짧은 시간 내 사건 스토리
- 액션/긴장 중심 콘텐츠
- 비극적 결말 필요시

## Template Variables

```yaml
pattern: gradual_rise
opening_tragedy:
  type: "death/abandonment"
  intensity: 70
  event: "{{OPENING_EVENT}}"

growth_milestones:
  - milestone: "{{FIRST_MILESTONE}}"
    emotion: "hope"
  - milestone: "{{SECOND_MILESTONE}}"
    emotion: "joy"
  - milestone: "{{THIRD_MILESTONE}}"
    emotion: "family_bond"

separation:
  reason: "{{SEPARATION_REASON}}"  # wild_instinct, independence, must_leave
  intensity: 40

reunion:
  time_gap: "{{TIME_GAP}}"  # 1년, 2년
  surprise: "{{REUNION_SURPRISE}}"  # brings_baby, brings_gift
  intensity: 100
```

## Montage Techniques

이 패턴에서 성장 몽타주는 필수:

### 시간 경과 표현
- 빠른 컷 전환
- 계절 변화 (눈 → 꽃 → 단풍)
- 크기 변화 (손바닥 → 무릎높이 → 어른)
- 반복 행동의 진화 (서툰 걸음 → 능숙한 움직임)

### 감정 누적
- 같은 장소, 다른 시간
- 같은 행동, 성장한 모습
- 일상의 반복이 주는 따뜻함
