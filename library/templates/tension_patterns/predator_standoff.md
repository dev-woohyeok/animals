# Predator Standoff Pattern (포식자 대치)

> 포식자와의 긴장감 넘치는 대치 상황에서 동물을 구조하는 패턴

## Pattern Overview

```
강도
100│              💥 대치      🥺 탈출
 90│             ╱  ╲        ╱╲
 80│      발견  ╱    ╲  추격╱  ╲
 70│       ╱╲ ╱      ╲  ╱     ╲
 60│  소리╱  ▽        ▽        ╲
 50│    ╱
   └─────────────────────────────
    0   10    25    40    50   60초
```

## 5단계 구조

### A. 오프닝 (0-10초) - "무슨 소리지?"
```yaml
trigger: 이상한 소리/발견
elements:
  - 밤, 숲 속 (낮보다 밤이 긴장감↑)
  - 비명 같은 울음소리
  - 손전등 들고 뛰어감
  - 심장 뛰는 소리, 거친 숨소리
hooks:
  - 소리의 정체 불명
  - 어둠 속 시야 제한
```

### B. 전개 (10-25초) - "뭔가 이상해"
```yaml
trigger: 동물 발견 + 위협 감지
elements:
  - 피 흘리는 동물 발견
  - 동물이 이상하게 행동 (한쪽만 봄)
  - 주변에서 으르렁 소리
  - 포식자 눈빛 포착
hooks:
  - 포식자 존재 암시
  - 왜 동물이 도망 안 갔을까?
```

### C. 클라이맥스1 (25-40초) - "대치 상황"
```yaml
trigger: 포식자 등장/대치
elements:
  - 늑대/코요테 2-3마리 등장
  - 동물을 노리고 있었음
  - 사람이 소리 지르며 위협
  - 포식자가 물러나지 않음
  - 오히려 더 다가옴
hooks:
  - 포식자가 안 물러남
  - 수적 열세
  - 동물 못 움직임
```

### D. 클라이맥스2 (40-50초) - "탈출 시도"
```yaml
trigger: 동물 안고 후퇴
elements:
  - 동물을 품에 안음
  - 천천히 뒷걸음질
  - 포식자가 따라옴, 거리 좁혀짐
  - 갑자기 동물이 큰 소리를 냄
  - 포식자 멈칫 (반전)
hooks:
  - 도망갈 수 있을까?
  - 동물의 예상 못한 행동
  - 위기 탈출
```

### E. 완결 (50-60초) - "안전"
```yaml
trigger: 포식자 퇴각/안전 확보
elements:
  - 포식자들이 돌아감
  - 동물이 사람을 올려다봄
  - 품에서 힘없이 눈 감음 (서스펜스)
  - 새벽, 병원에서 눈 뜸
hooks:
  - 살았나? 죽었나?
  - 안도의 순간
  - 새로운 시작 암시
```

## Scenario Template

```yaml
pattern: predator_standoff
duration: 90s

setting:
  time: "night"  # night 권장
  location: "{{FOREST_TYPE}}"  # 숲, 설원, 황야
  weather: "{{WEATHER}}"  # clear, snowy, foggy

characters:
  victim:
    animal: "{{ANIMAL}}"
    condition: "injured"
    age: "{{AGE}}"  # baby, young, adult

  predator:
    type: "{{PREDATOR}}"  # wolf, coyote, wild_dog
    count: 2-3
    behavior: "hunting"

  rescuer:
    pov: "first_person"
    equipment: "phone_flashlight"

beats:
  opening:
    duration: "0-10s"
    sound: "distant cry"
    action: "running toward sound"

  development:
    duration: "10-25s"
    discovery: "injured {{ANIMAL}}"
    threat_reveal: "growling sounds"

  climax_1:
    duration: "25-40s"
    confrontation: "predators appear"
    tension: "won't back down"

  climax_2:
    duration: "40-50s"
    action: "retreat with animal"
    twist: "animal makes loud sound"
    resolution: "predators leave"

  ending:
    duration: "50-60s"
    location: "vet clinic / safe place"
    emotion: "relief, hope"
    flash_forward: "recovery scene"
```

## 포식자별 특성

| 포식자 | 긴장도 | 행동 패턴 | 퇴각 트리거 |
|--------|--------|----------|------------|
| 늑대 | ★★★★★ | 무리 협공, 포위 | 더 큰 소리, 불 |
| 코요테 | ★★★★☆ | 기회주의적 | 강한 위협 |
| 들개 | ★★★☆☆ | 호기심+공격 | 직접 대치 |
| 여우 | ★★☆☆☆ | 새끼 보호 | 거리 확보 |

## 사운드 가이드

```
✅ 포함할 소리:
- 포식자: growling, snarling, howling in distance
- 동물: crying, whimpering, sudden loud cry
- 사람: heavy breathing, footsteps, yelling aggressively
- 환경: leaves crunching, branches breaking

❌ 제외:
- No background music
- No dramatic sound effects
```

## Prompt Style Guide

```
❌ 피해야 할 표현:
"devastating confrontation"
"terrifying wolves emerge"
"piercing scream echoes"
"dramatically lunges"

✅ 사용할 표현:
"shaky flashlight reveals wolves"
"wolves step closer, not backing off"
"animal suddenly cries out loud"
"slowly backing away"
```

## Reference Scenarios

### 늑대와의 대치 (여우)
- 오프닝: 밤, 숲에서 비명 같은 울음
- 전개: 피 흘리는 여우 + 으르렁 소리
- 클맥1: 늑대 2마리 등장, 안 물러남
- 클맥2: 여우 안고 후퇴, 여우가 울부짖음
- 완결: 늑대 퇴각, 새벽 병원에서 회복

### 코요테 습격 (토끼)
- 오프닝: 텐트 밖 소란스러운 소리
- 전개: 구석에 몰린 토끼 발견
- 클맥1: 코요테가 덤불 사이로 보임
- 클맥2: 토끼 안고 도망, 코요테 추격
- 완결: 차에 도착, 안전 확보

## Compatible Patterns

| 결합 패턴 | 적합도 | 활용법 |
|----------|--------|--------|
| time_pressure | ★★★★★ | 동물 부상 + 포식자 |
| mystery_reveal | ★★★★☆ | 어둠 속 정체 불명 → 포식자 |
| choice_dilemma | ★★★☆☆ | 여러 동물 + 포식자 상황 |
