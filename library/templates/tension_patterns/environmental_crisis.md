# Environmental Crisis Pattern (환경 위기)

> 자연재해 속에서 동물을 구조하는 극한 서바이벌 패턴

## Pattern Overview

```
강도
100│               💥 구조         🥺 안전
 90│    위험감지  ╱  ╲  2차위기  ╱╲
 80│      ╱╲    ╱    ╲    ╱╲   ╱  ╲
 70│  ╱╲ ╱  ╲  ╱      ╲  ╱  ╲ ╱    ╲
 60│ ╱  ▽    ▽         ▽    ▽       ╲
   └──────────────────────────────────
    0    10    25    40    50    60초
```

## 환경 위기 유형

| 유형 | 긴장도 | 시각적 특성 | 시간 압박 |
|------|--------|------------|----------|
| **홍수** | ★★★★★ | 물살, 떠내려감 | 초 단위 |
| **산불** | ★★★★★ | 연기, 불길 | 분 단위 |
| **폭풍** | ★★★★☆ | 바람, 날아감 | 분 단위 |
| **폭설** | ★★★★☆ | 시야 제한 | 시간 단위 |
| **산사태** | ★★★☆☆ | 갇힘, 매몰 | 분 단위 |

## 5단계 구조

### A. 오프닝 (0-10초) - "위험 속 발견"
```yaml
trigger: 재해 상황에서 동물 울음
elements:
  - 재해 진행 중 (비, 연기, 바람)
  - 동물 울음소리 들림
  - 위험 무릅쓰고 찾아감
  - 위기 상황의 동물 발견
hooks:
  - 재해의 긴박함
  - 울음소리의 절박함
  - 찾을 수 있을까?
```

### B. 전개 (10-25초) - "구조 시도"
```yaml
trigger: 첫 구조 시도 + 장애물
elements:
  - 동물에게 접근
  - 장애물/위험 (물살, 불길)
  - 구조 성공 or 부분 성공
  - 더 있다! (추가 발견)
hooks:
  - 접근 가능한가?
  - 혼자가 아니었다
  - 다 구할 수 있을까?
```

### C. 클라이맥스1 (25-40초) - "선택과 위기"
```yaml
trigger: 시간 압박 + 다중 구조
elements:
  - 한 마리 구하고 안전한 곳에
  - 다시 돌아가야 함
  - 상황 악화 (물 더 불어남, 불길 가까워짐)
  - 위험한 상태에서 구조 시도
hooks:
  - 돌아갈 수 있을까?
  - 상황이 더 나빠짐
  - 시간이 없다
```

### D. 클라이맥스2 (40-50초) - "위기의 순간"
```yaml
trigger: 구조자도 위험
elements:
  - 마지막 구조 중 위기
  - 구조자 자신도 위험 (휩쓸림, 연기)
  - 거의 실패할 뻔
  - 극적으로 성공
hooks:
  - 구조자도 위험
  - 실패 직전
  - 마지막 순간 성공
```

### E. 완결 (50-60초) - "모두 안전"
```yaml
trigger: 전원 구조
elements:
  - 안전한 곳 도착
  - 모두 살았다
  - 서로 붙어있는 동물들
  - 구조자와 동물들의 교감
hooks:
  - 안도의 순간
  - 생존한 가족
  - 새로운 연결
```

## Scenario Template

```yaml
pattern: environmental_crisis
duration: 90s

setting:
  disaster: "{{DISASTER_TYPE}}"  # flood, wildfire, storm
  severity: "{{SEVERITY}}"  # moderate, severe, extreme
  progression: "worsening"  # 항상 악화

characters:
  victims:
    animal: "{{ANIMAL}}"
    count: "{{COUNT}}"  # 2-4마리 권장
    location: "trapped/stranded"

  rescuer:
    pov: "first_person"
    risk_level: "high"

crisis_escalation:
  - "situation bad"
  - "getting worse"
  - "running out of time"
  - "almost too late"
  - "barely made it"

beats:
  opening:
    duration: "0-10s"
    disaster: "ongoing {{DISASTER}}"
    discovery: "hear crying"
    approach: "go toward sound"

  development:
    duration: "10-25s"
    rescue_1: "reach first animal"
    complication: "more animals found"
    decision: "must save all"

  climax_1:
    duration: "25-40s"
    action: "carry to safety"
    return: "go back for others"
    escalation: "disaster worsens"

  climax_2:
    duration: "40-50s"
    final_rescue: "last animal"
    danger: "rescuer in trouble"
    escape: "barely make it out"

  ending:
    duration: "50-60s"
    safety: "all safe"
    together: "animals huddled"
    connection: "first trust shown"
```

## 재해별 시나리오

### 홍수 구조
```yaml
scenario: "flood_rescue"
setting:
  - 폭우, 불어난 강/계곡
  - 물에 떠내려가는/고립된 동물

escalation:
  0s:  "물에서 동물 울음"
  10s: "바위에 매달린 새끼들"
  25s: "한 마리 구하고 다시 돌아감"
  40s: "물살에 휩쓸림, 나뭇가지 잡음"
  50s: "기어서 올라옴, 다 살았다"

dangers:
  - 급류에 휩쓸림
  - 물 먹음
  - 체력 소진
  - 차가운 물
```

### 산불 구조
```yaml
scenario: "wildfire_rescue"
setting:
  - 연기 가득한 숲
  - 도망 못 가고 갇힌 동물들

escalation:
  0s:  "연기 속 울음소리"
  10s: "둥지에 갇힌 새끼들"
  25s: "2마리 안고 나감, 1마리 남음"
  40s: "다시 들어감, 숨 참음"
  50s: "마지막 찾음, 뛰어나옴"

dangers:
  - 연기 흡입
  - 불길 접근
  - 시야 제한
  - 탈출로 차단
```

### 폭풍 구조
```yaml
scenario: "storm_rescue"
setting:
  - 강한 바람, 비
  - 날아가거나 갇힌 동물

escalation:
  0s:  "폭풍 속 울음"
  10s: "무너진 구조물 아래 발견"
  25s: "잔해 치우고 구출"
  40s: "바람에 날아갈 뻔, 잡음"
  50s: "차에 도착, 안전"

dangers:
  - 날아오는 물체
  - 구조물 붕괴
  - 강한 바람
  - 체온 저하
```

## 다중 구조 전략

```
1마리만 있을 때:
[발견] → [구조] → [탈출]
긴장도: ★★★☆☆

2-3마리 있을 때 (권장):
[발견] → [1마리 구조] → [돌아감] → [나머지 구조] → [탈출]
긴장도: ★★★★★

4마리 이상:
복잡해지므로 2회 왕복으로 제한
```

## 사운드 가이드

```
✅ 포함할 소리:
- 재해: rushing water, crackling fire, howling wind
- 동물: desperate crying, whimpering
- 사람: heavy breathing, coughing, splashing
- 환경: debris falling, branches breaking

❌ 제외:
- No background music
- No dramatic orchestral sounds
```

## Prompt Style Guide

```
❌ 피해야 할 표현:
"apocalyptic scene of destruction"
"racing against the inferno"
"dramatic escape from nature's fury"

✅ 사용할 표현:
"smoke everywhere, can barely see"
"water rising fast"
"grab the last one and run"
"coughing, stumbling out"
```

## Reference Scenarios

### 홍수 속 구조 (새끼 너구리)
- 오프닝: 폭우, 강가에서 울음
- 전개: 바위 위에 2마리, 물 불어남
- 클맥1: 1마리 안고 건넴, 다시 뛰어듦
- 클맥2: 물살에 휩쓸림, 나뭇가지로 탈출
- 완결: 담요 속 2마리 서로 붙어있음

### 산불 탈출 (여우 가족)
- 오프닝: 연기 속 울음소리 2곳
- 전개: 왼쪽으로 감, 새끼 3마리
- 클맥1: 2마리 안고 나감, 불길 가까워짐
- 클맥2: 다시 들어감, 숨어있던 마지막 1마리
- 완결: 기침하며 나옴, 모두 구함

## Compatible Patterns

| 결합 패턴 | 적합도 | 활용법 |
|----------|--------|--------|
| time_pressure | ★★★★★ | 재해 + 부상 |
| choice_dilemma | ★★★★★ | 여러 동물 선택 |
| predator_standoff | ★★★☆☆ | 재해 중 포식자 등장 |
