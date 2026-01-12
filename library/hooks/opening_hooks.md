# Opening Hooks (A단계: 0-20초)

> 첫 3초 안에 시청자를 멈추게 하고, 20초까지 붙잡는 기법

## 목표

```
"이게 뭐지?" → 스크롤 멈춤 → 계속 시청
```

## Hook Types

### A1. 이상한 발견 (Strange Discovery)
```yaml
type: strange_discovery
strength: ★★★★☆
description: 평범한 상황에서 뭔가 이상함 감지

examples:
  - "숲에서 이상한 소리가 들린다"
  - "눈 위에 이상한 발자국"
  - "텐트 밖에서 긁는 소리"
  - "차 밑에서 움직임"

visual:
  - 어둠/제한된 시야
  - 손전등으로 찾는 모습
  - 정체 불명의 형체

sound:
  - strange crying
  - scratching sounds
  - rustling in bushes
```

### A2. 위기 상황 시작 (Crisis Start)
```yaml
type: crisis_start
strength: ★★★★★
description: 긴급한 상황으로 바로 진입

examples:
  - "피 흘리는 동물 발견"
  - "물에 떠내려가는 상자"
  - "도로 한가운데 쓰러진 동물"
  - "포식자에게 쫓기는 동물"

visual:
  - 즉각적인 위기 상황
  - 움직여야 하는 긴박함
  - 위험 요소 가시화

sound:
  - panicked crying
  - rushing water
  - growling/howling
```

### A3. 미스터리 제시 (Mystery Setup)
```yaml
type: mystery_setup
strength: ★★★★☆
description: 설명 없이 궁금증 유발

examples:
  - "이걸 발견했을 때..."
  - "왜 이 동물이 나를 따라오는지 몰랐다"
  - "처음엔 무서웠다"
  - "이상한 상자가 있었다"

visual:
  - 의문의 물체/존재
  - 설명 없는 시작
  - 힌트만 보여줌

sound:
  - ambient tension
  - mysterious sounds
```

### A4. 반전 예고 (Flash Forward)
```yaml
type: flash_forward
strength: ★★★★★
description: 결말을 암시하며 시작

examples:
  - "3개월 후 이렇게 될 줄 몰랐다"
  - "이 아이가 내 가족이 될 줄..."
  - "그때 그 선택이..."
  - "지금은 이렇게 됐다" (미래 보여주고 과거로)

visual:
  - 행복한 결말 먼저 보여줌
  - "○개월 전" 텍스트
  - 과거로 회귀

sound:
  - calm/happy sounds (future)
  - transition to past
```

### A5. 행동 중간 시작 (In Media Res)
```yaml
type: in_media_res
strength: ★★★★☆
description: 이미 진행 중인 상황

examples:
  - "뛰어가는 중 (왜인지 모름)"
  - "이미 구조하고 있는 중"
  - "무언가를 쫓는 중"
  - "도망가는 중"

visual:
  - 흔들리는 카메라
  - 달리는 발
  - 급한 호흡

sound:
  - running footsteps
  - heavy breathing
  - urgent sounds
```

## Best Practices

### 첫 3초 필수 요소
```
✅ 움직임 (정적 화면 금지)
✅ 소리 (무음 시작 금지)
✅ 질문 유발 (왜? 뭐지?)
✅ 긴박함 or 호기심
```

### 오프닝 구조
```
0-3초:  시선 잡기 (움직임/소리)
3-10초: 상황 제시 (뭔 일인지)
10-20초: 첫 액션 (접근/결정)
```

## Prompt Examples

### A1 - 이상한 발견
```
First person POV handheld phone footage at night.
Camping in forest, hearing strange crying sound from outside.
Shaky flashlight beam sweeps across dark trees.
Heavy breathing, footsteps on leaves.
No background music, only distant animal crying, forest sounds.
```

### A2 - 위기 상황
```
First person POV handheld phone footage.
Running toward something on snowy road.
Shaky camera, heavy breathing, panicked voice.
Discovers small fox lying in snow, barely moving.
No background music, only breathing, footsteps crunching snow.
```

### A4 - 반전 예고
```
First person POV phone footage.
Happy healthy fox playing in living room.
Cut to text: "3 months ago"
Cut to: running through dark forest with flashlight.
No background music, transition from happy sounds to tense atmosphere.
```

## 안티 패턴 (피해야 할 것)

```
❌ 느린 시작 (풍경 보여주기)
❌ 설명부터 시작 ("오늘 캠핑을 갔는데...")
❌ 정적인 화면
❌ 무음 시작
❌ 결과 먼저 스포일러 (반전예고와 다름)
```

## 연결 가이드

| 오프닝 유형 | 추천 전개 (B) | 추천 클맥 (C) |
|------------|--------------|--------------|
| 이상한 발견 | 정체 확인 | 반전 발견 |
| 위기 상황 | 상황 악화 | 최악의 순간 |
| 미스터리 | 점진적 공개 | 진실 폭로 |
| 반전 예고 | 과거 위기 | 결정적 순간 |
| 행동 중간 | 이유 밝혀짐 | 목표 달성/실패 |
