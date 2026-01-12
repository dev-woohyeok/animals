# Mystery Reveal Pattern (미스터리 공개)

> 어둠 속 미지의 존재가 점진적으로 밝혀지는 서스펜스 패턴

## Pattern Overview

```
강도
100│                         💥 반전
 90│              정체확인  ╱  ╲ 🥺 해결
 80│     접근    ╱╲       ╱    ╲  ╱╲
 70│  ╱╲    ╱╲ ╱  ╲     ╱      ╲╱  ╲
 60│ ╱  ╲  ╱  ▽    ╲   ╱            ╲
 50│╱    ▽           ╲ ╱
   └──────────────────────────────────
    0    20    40    60    80    90초
         ↑     ↑          ↑
      "뭐지?" "저게?" "알고보니!"
```

## 미스터리 유형

| 유형 | 초기 인식 | 실제 정체 | 반전 강도 |
|------|----------|----------|----------|
| **위협→도움요청** | 무서운 존재 | 도움 필요한 동물 | ★★★★★ |
| **적→보호자** | 공격하려는 듯 | 새끼 지키는 어미 | ★★★★★ |
| **한 마리→여러** | 동물 한 마리 | 가족 전체 | ★★★★☆ |
| **야생→과거반려** | 야생 동물 | 버려진 반려동물 | ★★★★☆ |
| **소리→발견** | 이상한 소리 | 위기의 동물 | ★★★☆☆ |

## 5단계 구조

### A. 오프닝 (0-20초) - "뭔가 있다"
```yaml
trigger: 이상한 징후 감지
elements:
  - 밤/어두운 환경
  - 설명할 수 없는 소리/움직임
  - 처음엔 무시하려 함
  - 반복되는 징후, 확인하러 감
hooks:
  - 뭔 소리지?
  - 위험한가?
  - 가봐야 하나?
```

### B. 전개 (20-40초) - "접근"
```yaml
trigger: 정체 확인 시도
elements:
  - 손전등/조심스러운 접근
  - 부분적인 정보 (눈빛, 그림자)
  - 도망가거나 더 가까이 옴
  - 아직 뭔지 모름
hooks:
  - 눈빛만 보임
  - 공격하려는 건가?
  - 왜 안 도망가지?
```

### C. 클라이맥스1 (40-60초) - "정체 확인"
```yaml
trigger: 드디어 확인 + 반전
elements:
  - 정체가 드러남
  - 예상과 다름 (반전)
  - 새로운 정보 발견
  - 상황 재해석
hooks:
  - 이게 뭐야?!
  - 알고 보니...
  - 그래서 그랬구나
```

### D. 클라이맥스2 (60-80초) - "숨겨진 진실"
```yaml
trigger: 더 큰 진실 + 위기/감동
elements:
  - 첫 반전 뒤의 진짜 이유
  - 추가 발견 (새끼들, 상처)
  - 도움이 필요한 상황
  - 구조/보호 결정
hooks:
  - 이런 사정이...
  - 도와줘야 해
  - 예상 못한 전개
```

### E. 완결 (80-90초) - "해결과 연결"
```yaml
trigger: 문제 해결 + 유대 형성
elements:
  - 위기 해결
  - 동물이 신뢰 표시
  - 새로운 관계 시작
  - 미래 암시
hooks:
  - 신뢰의 순간
  - 감동적 연결
  - 다음 이야기 궁금
```

## Scenario Template

```yaml
pattern: mystery_reveal
duration: 90s

setting:
  time: "night"  # 밤이 필수
  visibility: "limited"  # 손전등만
  location: "{{LOCATION}}"  # 숲, 캠프, 집 주변

mystery_structure:
  initial_sign: "{{FIRST_CLUE}}"  # 소리, 움직임, 그림자
  partial_reveal: "{{HINT}}"  # 눈빛, 실루엣
  full_reveal: "{{IDENTITY}}"  # 실제 정체
  hidden_truth: "{{DEEPER_TRUTH}}"  # 진짜 이유

characters:
  mystery_subject:
    perceived_as: "{{THREAT}}"  # 처음 인식
    actual: "{{REALITY}}"  # 실제 정체
    motivation: "{{REASON}}"  # 왜 그랬는지

  rescuer:
    pov: "first_person"
    initial_fear: true
    equipment: "phone_flashlight"

beats:
  opening:
    duration: "0-20s"
    sign: "strange {{SOUND/MOVEMENT}}"
    reaction: "investigate reluctantly"

  development:
    duration: "20-40s"
    approach: "flashlight search"
    partial: "glimpse of {{HINT}}"
    behavior: "doesn't run away"

  climax_1:
    duration: "40-60s"
    reveal: "identity revealed"
    twist: "not what expected"
    reframe: "understand behavior"

  climax_2:
    duration: "60-80s"
    deeper: "hidden truth discovered"
    stakes: "needs help"
    decision: "must help"

  ending:
    duration: "80-90s"
    resolution: "problem solved"
    trust: "animal shows trust"
    future: "new connection"
```

## 반전 구조 유형

### Type A: 위협 → 도움 요청
```
처음: "뭔가 나를 따라온다... 무섭다"
반전1: "다친 여우였다, 도움을 원했던 거다"
반전2: "새끼들이 있는 곳으로 안내하려 했다"
```

### Type B: 적 → 보호자
```
처음: "으르렁거리며 달려온다! 공격?"
반전1: "내 뒤에 있던 포식자를 쫓는 거였다"
반전2: "날 구해준 거다"
```

### Type C: 하나 → 여럿
```
처음: "작은 동물 하나가 텐트를 긁는다"
반전1: "데려가니 자꾸 한 곳을 가리킴"
반전2: "형제들이 더 있었다"
```

### Type D: 야생 → 버려진 반려
```
처음: "야생 동물이 왜 사람을 피하지 않지?"
반전1: "목에 끊어진 목줄 흔적"
반전2: "버려진 반려동물이었다"
```

## 시각적 미스터리 연출

```
0초:   [어둠] → 소리만 들림
       ▓▓▓▓▓▓▓▓▓

10초:  [손전등] → 움직임 포착
       ▓▓▓░▓▓▓▓▓
          ↑ 뭔가 움직임

20초:  [눈빛] → 반사된 눈만 보임
       ▓▓▓●●▓▓▓▓
          ↑ 두 눈빛

40초:  [실루엣] → 형체 드러남
       ▓▓░░░░▓▓▓
          ↑ 여우 형태

60초:  [완전 공개] → 상황 파악
       ░░░░░░░░░
         ↑ 다친 여우 + 새끼들
```

## 사운드 미스터리 연출

| 단계 | 소리 | 해석 |
|------|------|------|
| 0초 | 긁는 소리 | 뭔가 접근? |
| 10초 | 작은 울음 | 동물 같은데... |
| 20초 | 발소리 + 숨소리 | 가까워진다 |
| 40초 | 약한 울음 | 공격 아님, 도움 요청 |
| 60초 | 새끼 울음 | 새끼들이 있었다 |

## 사운드 가이드

```
✅ 포함할 소리:
- 미스터리: scratching, rustling, soft crying
- 긴장: heavy breathing, cautious footsteps
- 발견: animal whimpering, babies crying
- 해결: calming sounds, first trusting sounds

❌ 제외:
- No horror movie sounds
- No jump scare effects
- No background music
```

## Prompt Style Guide

```
❌ 피해야 할 표현:
"terrifying presence lurking"
"heart-stopping revelation"
"shocking twist unfolds"

✅ 사용할 표현:
"something scratching at the tent"
"two eyes reflecting the flashlight"
"not attacking, just looking"
"following to show something"
```

## Reference Scenarios

### 어둠 속의 소리 (덫에 걸린 동물)
- 오프닝: 캠핑 중 새벽 3시, 텐트 밖 긁는 소리
- 전개: 손전등으로 풀숲 비춤, 눈빛 2개
- 클맥1: 따라가니 덫에 걸린 새끼 발견
- 클맥2: 어미가 밤새 주변 맴돌았던 것
- 완결: 새끼 구출, 어미와 함께 숲으로

### 따라오는 그림자 (길 잃은 강아지)
- 오프닝: 밤길 걷는데 뒤에서 발소리
- 전개: 멈추면 멈춤, 가면 따라옴
- 클맥1: 비춰보니 더러운 강아지
- 클맥2: 목에 끊어진 목줄, 버려진 아이
- 완결: 집에 데려감, 첫 밥

### 으르렁대는 여우
- 오프닝: 숲에서 으르렁 소리, 공격하려나?
- 전개: 갑자기 사람 쪽으로 달려옴
- 클맥1: 사람 뒤에 있던 뱀을 쫓는 거였음
- 클맥2: 여우도 다쳐있었다 (뱀에 물림)
- 완결: 서로 구한 셈, 치료 후 야생 방사

## Compatible Patterns

| 결합 패턴 | 적합도 | 활용법 |
|----------|--------|--------|
| predator_standoff | ★★★★★ | 미스터리 정체가 포식자 상황 |
| time_pressure | ★★★★☆ | 발견 후 시간 압박 |
| choice_dilemma | ★★★☆☆ | 미스터리 해결 후 선택 |
