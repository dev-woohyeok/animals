# Time Pressure Pattern (시간 압박)

> 생존을 위해 시간과 싸우는 긴박한 구조 패턴

## Pattern Overview

```
강도
100│                    💥 위기       🥺 회복
 90│         체온저하  ╱  ╲  움직임!╱╲
 80│  발견   ╱╲      ╱    ╲      ╱  ╲
 70│    ╱╲ ╱  ╲    ╱      ╲    ╱    ╲
 60│   ╱  ▽    ╲  ╱        ╲  ╱      ╲
 50│  ╱         ▽           ▽         ╲
   └──────────────────────────────────────
    0    10    25    40     50      60초
         ↑          ↑           ↑
      "시간없다"  "안되나?"   "움직였다!"
```

## 시간 압박 유형

| 유형 | 긴장도 | 시각적 표현 | 타임라인 |
|------|--------|------------|----------|
| **저체온** | ★★★★★ | 떨림→멈춤→되살아남 | 분 단위 |
| **출혈** | ★★★★★ | 피 퍼짐, 약해짐 | 분 단위 |
| **익사** | ★★★★☆ | 물에 잠김, 힘 빠짐 | 초 단위 |
| **질식** | ★★★★☆ | 갇힘, 숨 헐떡임 | 분 단위 |
| **탈진** | ★★★☆☆ | 점점 느려짐 | 시간 단위 |

## 5단계 구조

### A. 오프닝 (0-10초) - "발견"
```yaml
trigger: 위험 상태의 동물 발견
elements:
  - 극한 환경 (폭설, 한파, 폭우)
  - 움직이지 않는 작은 덩어리
  - 가까이 가서 확인
  - 살아있지만 위험한 상태
hooks:
  - 살았나 죽었나?
  - 얼마나 버틸 수 있을까?
```

### B. 전개 (10-25초) - "시간이 없다"
```yaml
trigger: 상황 악화 + 시간 압박 인식
elements:
  - 응급 처치 시도 (체온, 지혈)
  - 상태가 더 나빠짐
  - 안전한 곳까지 거리 멂
  - 결정: 이동해야 한다
hooks:
  - 점점 약해지는 동물
  - 시간과의 싸움 시작
  - 환경 악화 (눈 더 내림 등)
```

### C. 클라이맥스1 (25-40초) - "최악의 순간"
```yaml
trigger: 이동 중 위기
elements:
  - 품에 안고 뛰기
  - 장애물/위험 (넘어짐, 길 잃음)
  - 동물 상태 확인 - 거의 안 움직임
  - 숨 쉬고 있나? 확인
hooks:
  - 넘어지면서 떨어뜨림
  - 점점 차가워지는 몸
  - 포기 직전
```

### D. 클라이맥스2 (40-50초) - "기다림"
```yaml
trigger: 안전한 곳 도착 후 기다림
elements:
  - 차/집/병원 도착
  - 따뜻하게 함 (히터, 담요)
  - 시간 경과 표현 ("10분... 20분...")
  - 움직임 없음... 포기하려는 순간
  - 작은 떨림/움직임!
hooks:
  - 되살아날까?
  - 시간 표시로 긴장감
  - 포기 직전의 희망
```

### E. 완결 (50-60초) - "살았다"
```yaml
trigger: 회복 신호
elements:
  - 눈을 뜸
  - 처음으로 반응 (핥음, 소리)
  - 안도의 순간
  - 시간 점프 (회복 후 모습)
hooks:
  - 감정 해소
  - 회복된 모습
  - 새로운 시작
```

## Scenario Template

```yaml
pattern: time_pressure
duration: 90s

setting:
  environment: "{{EXTREME_CONDITION}}"  # blizzard, flood, heatwave
  temperature: "{{TEMP}}"  # extreme cold/hot
  time_limit: "{{URGENCY}}"  # minutes, hours

characters:
  victim:
    animal: "{{ANIMAL}}"
    condition: "{{CRITICAL_STATE}}"  # hypothermia, bleeding, drowning
    age: "baby/young"  # 어릴수록 긴박

  rescuer:
    pov: "first_person"
    equipment: "basic"  # 장비 부족 = 긴장↑

crisis_elements:
  visual_decay:
    - "not moving"
    - "getting colder"
    - "barely breathing"
    - "no response"

  time_markers:
    - "10 minutes... nothing"
    - "20 minutes... still nothing"
    - "about to give up"
    - "tiny movement!"

beats:
  opening:
    duration: "0-10s"
    discovery: "barely alive {{ANIMAL}}"
    urgency: "need to act fast"

  development:
    duration: "10-25s"
    action: "first aid attempt"
    complication: "condition worsens"
    decision: "must move now"

  climax_1:
    duration: "25-40s"
    action: "running with animal"
    crisis: "falls / loses grip"
    fear: "is it still breathing?"

  climax_2:
    duration: "40-50s"
    location: "safe place"
    waiting: "time markers"
    moment: "about to give up... movement!"

  ending:
    duration: "50-60s"
    recovery: "opens eyes"
    connection: "first response"
    flash_forward: "healthy and playing"
```

## 상태 악화 시각화

```
시간 경과에 따른 동물 상태:

0초:  발견 ─── 약한 움직임, 눈 반쯤
10초: 악화 ─── 떨림, 점점 차가움
25초: 위기 ─── 거의 안 움직임
40초: 임계 ─── 반응 없음
50초: 반전 ─── 작은 떨림!
60초: 회복 ─── 눈 뜸, 반응
```

## 시간 표현 기법

| 기법 | 예시 | 효과 |
|------|------|------|
| **숫자 카운트** | "10분... 20분..." | 직접적 시간 압박 |
| **상태 변화** | "더 차가워진다" | 시각적 긴박 |
| **행동 반복** | "계속 문지름" | 무력감 표현 |
| **환경 변화** | "해가 지기 시작" | 시간 경과 암시 |

## 사운드 가이드

```
✅ 포함할 소리:
- 호흡: heavy breathing, panicked breathing
- 환경: howling wind, rain pouring, car heater
- 동물: weak whimper, first cry when waking
- 발소리: running footsteps, stumbling

❌ 제외:
- No background music
- No dramatic sound effects
```

## Prompt Style Guide

```
❌ 피해야 할 표현:
"desperately fighting against time"
"racing against death itself"
"dramatic moment of revival"

✅ 사용할 표현:
"barely moving, getting cold"
"10 minutes pass, still nothing"
"tiny movement under the blanket"
"eyes open slowly"
```

## Reference Scenarios

### 얼어붙는 시간 (새끼 여우)
- 오프닝: 영하 20도 폭설, 눈에 파묻힌 덩어리
- 전개: 거의 안 움직임, 옷으로 감쌈
- 클맥1: 품에 안고 뛰다 넘어짐
- 클맥2: 차 히터 최대, 20분 기다림... 떨림!
- 완결: 눈 뜸, 회복 후 눈밭에서 뛰어놈

### 출혈 (다친 고라니)
- 오프닝: 도로변, 피 흘리는 어린 고라니
- 전개: 지혈 시도, 계속 흘러나옴
- 클맥1: 차에 태우고 병원으로, 점점 약해짐
- 클맥2: 수술 중 기다림, 의사 나옴
- 완결: 살았다! 깁스 하고 회복

## Compatible Patterns

| 결합 패턴 | 적합도 | 활용법 |
|----------|--------|--------|
| predator_standoff | ★★★★★ | 부상 원인이 포식자 |
| environmental_crisis | ★★★★★ | 환경이 시간 압박 원인 |
| choice_dilemma | ★★★☆☆ | 여러 동물 + 시간 제한 |
