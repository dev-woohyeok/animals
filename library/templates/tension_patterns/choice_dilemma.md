# Choice Dilemma Pattern (선택 딜레마)

> 여러 동물 중 선택해야 하는 갈등과 결국 모두 구하는 패턴

## Pattern Overview

```
강도
100│                    💥 마지막    🥺 전부
 90│       선택1      ╱  ╲    구조 ╱╲
 80│    ╱╲    돌아감╱    ╲     ╱  ╲
 70│   ╱  ╲      ╱        ╲   ╱    ╲
 60│  ╱    ╲    ╱          ╲ ╱      ╲
 50│ ╱      ╲  ╱            ▽        ╲
   └──────────────────────────────────
    0    20    40    60    80    90초
```

## 딜레마 유형

| 유형 | 갈등 구조 | 감정 강도 |
|------|----------|----------|
| **공간 분리** | 다른 위치에 있는 동물들 | ★★★★★ |
| **시간 제한** | 한번에 못 데려감 | ★★★★★ |
| **위험 선택** | 더 위험한 쪽 vs 안전한 쪽 | ★★★★☆ |
| **종류 선택** | 다른 종의 동물들 | ★★★☆☆ |

## 5단계 구조

### A. 오프닝 (0-20초) - "두 곳에서 소리"
```yaml
trigger: 동시에 여러 곳에서 울음
elements:
  - 위기 상황 (재해, 위험)
  - 울음소리가 두 곳에서
  - 왼쪽? 오른쪽?
  - 시간이 없다, 결정해야 함
hooks:
  - 양쪽 다 급하다
  - 어디로 먼저?
  - 선택의 무게
```

### B. 전개 (20-40초) - "첫 번째 선택"
```yaml
trigger: 한쪽 선택 + 구조
elements:
  - 한쪽으로 결정 (더 급해 보이는 쪽)
  - 첫 번째 동물 발견
  - 빠르게 구조
  - 안전한 곳에 두고 다시 출발
hooks:
  - 다른 쪽은 괜찮을까?
  - 시간 촉박
  - 돌아갈 수 있을까?
```

### C. 클라이맥스1 (40-60초) - "상황 악화"
```yaml
trigger: 돌아가는 중 + 악화
elements:
  - 다른 쪽으로 달려감
  - 상황이 더 나빠짐
  - 여러 마리 발견
  - 한번에 다 못 데려감
hooks:
  - 더 많았다
  - 상황 악화
  - 또 선택해야 함
```

### D. 클라이맥스2 (60-80초) - "마지막 하나"
```yaml
trigger: 반복 구조 + 마지막 위기
elements:
  - 대부분 구함
  - 마지막 한 마리 남음
  - 가장 위험한 상황
  - 포기 직전 발견/구출
hooks:
  - 마지막 한 마리
  - 가장 힘든 구조
  - 포기할 수 없다
```

### E. 완결 (80-90초) - "모두 구했다"
```yaml
trigger: 전원 구조 성공
elements:
  - 모든 동물이 안전
  - 함께 모여있는 모습
  - 구조자 탈진/감정
  - 모두 살았다는 안도
hooks:
  - 하나도 포기 안 함
  - 완전한 성공
  - 감동의 순간
```

## Scenario Template

```yaml
pattern: choice_dilemma
duration: 90s

setting:
  crisis: "{{CRISIS_TYPE}}"  # fire, flood, predator
  locations: 2-3  # 분산된 위치
  urgency: "extreme"

characters:
  victims:
    type: "{{ANIMAL}}"
    total_count: 3-5  # 총 구조 대상
    distribution:
      - location_1: 1-2
      - location_2: 2-3

  rescuer:
    pov: "first_person"
    capacity: 1-2  # 한번에 데려갈 수 있는 수

dilemma_structure:
  first_choice: "which direction?"
  second_choice: "who first?"
  final_choice: "go back for last one?"

beats:
  opening:
    duration: "0-20s"
    sounds: "crying from two directions"
    decision: "which way first?"
    urgency: "no time to think"

  development:
    duration: "20-40s"
    first_rescue: "save 1-2"
    place_safe: "put in safe spot"
    return: "run back for others"

  climax_1:
    duration: "40-60s"
    discovery: "more than expected"
    complication: "can't carry all"
    trips: "multiple rescue runs"

  climax_2:
    duration: "60-80s"
    last_one: "one still missing"
    danger: "situation critical"
    rescue: "almost give up, then find"

  ending:
    duration: "80-90s"
    count: "all accounted for"
    together: "huddled together"
    relief: "exhausted but happy"
```

## 선택 시나리오 변형

### 변형 1: 방향 선택
```
   [왼쪽 울음] ←──── 나 ────→ [오른쪽 울음]
        ↓                         ↓
   더 가깝다                  더 급해 보인다
        ↓                         ↓
   먼저 갈까?               먼저 갈까?
```

### 변형 2: 위험도 선택
```
   [안전한 위치] ←─ 나 ─→ [위험한 위치]
   1마리, 덜 급함         3마리, 매우 급함
        ↓                      ↓
   나중에 가도 됨         지금 안 가면 늦음
```

### 변형 3: 운반 한계
```
   새끼 3마리 발견
        ↓
   한번에 2마리만 가능
        ↓
   2마리 먼저 → 다시 돌아옴 → 1마리 구조
```

## 감정 설계

| 단계 | 구조자 감정 | 관객 감정 |
|------|-----------|----------|
| 오프닝 | 혼란, 압박 | 긴장, 조급 |
| 첫 선택 | 죄책감, 급함 | 다른 쪽 걱정 |
| 돌아감 | 불안, 희망 | 제발... |
| 마지막 | 절박, 지침 | 포기하지 마 |
| 성공 | 탈진, 안도 | 감동, 안도 |

## 숫자별 구조

### 2마리 (기본)
```
0초:  두 방향에서 소리
20초: A 구조 완료
40초: B 찾아감
60초: B 구조 중 위기
80초: B 구조 완료
90초: 둘 다 안전
```

### 3마리 (권장)
```
0초:  두 방향에서 소리
20초: A 구조 (1마리)
40초: B 찾아감, 2마리 있음!
60초: B-1 구조, B-2 남음
70초: 다시 돌아감
80초: B-2 구조 (가장 힘듦)
90초: 3마리 모두 안전
```

### 4-5마리 (고급)
```
복잡해지므로:
- 2개 위치로 제한
- 한 위치에 여러 마리
- 2-3회 왕복
```

## 사운드 가이드

```
✅ 포함할 소리:
- 분산된 울음: crying from left, crying from right
- 호흡: panting, exhausted breathing
- 발소리: running footsteps, stumbling
- 환경: relevant disaster sounds

❌ 제외:
- No background music
- No countdown timers
```

## Prompt Style Guide

```
❌ 피해야 할 표현:
"agonizing choice between life and death"
"heart-wrenching decision"
"dramatic race against time"

✅ 사용할 표현:
"crying from two directions"
"grab first one, run back"
"one more still there"
"finally got the last one"
```

## Reference Scenarios

### 산불 속 선택 (여우 새끼들)
- 오프닝: 연기 속 울음 두 곳
- 전개: 왼쪽 먼저 (다친 사슴), 안전한 곳에
- 클맥1: 오른쪽 갔더니 여우 새끼 3마리
- 클맥2: 2마리 데려가고 마지막 숨은 1마리
- 완결: 사슴 + 여우 3마리, 모두 구함

### 홍수 선택 (강아지들)
- 오프닝: 물에 떠내려가는 상자 2개
- 전개: 가까운 상자 먼저 (1마리)
- 클맥1: 멀리 떠내려가는 상자 수영
- 클맥2: 상자에 2마리, 물살에 휩쓸릴 뻔
- 완결: 3마리 모두 담요에 붙어있음

## Compatible Patterns

| 결합 패턴 | 적합도 | 활용법 |
|----------|--------|--------|
| environmental_crisis | ★★★★★ | 재해 + 분산된 동물 |
| time_pressure | ★★★★★ | 시간 제한 + 선택 |
| predator_standoff | ★★★★☆ | 포식자 피하며 구조 |
