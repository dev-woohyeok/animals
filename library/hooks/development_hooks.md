# Development Hooks (B단계: 20-40초)

> 첫 후킹 후 기대감을 높이고 다음 전개를 궁금하게 만드는 기법

## 목표

```
"설마...?" → 예상 형성 → 뒤집을 준비
```

## Hook Types

### B1. 예상 뒤집기 (Expectation Flip)
```yaml
type: expectation_flip
strength: ★★★★★
description: 시청자가 생각한 것과 다른 전개

examples:
  - "공격적일 줄 알았는데 다가옴"
  - "도망갈 줄 알았는데 가만히 있음"
  - "한 마리인 줄 알았는데 여러 마리"
  - "야생인 줄 알았는데 목줄 흔적"

visual:
  - 예상과 다른 행동
  - 새로운 정보 등장
  - 상황 재해석 필요

application:
  - 오프닝에서 설정한 예상을 뒤집음
  - 너무 빨리 다 공개하지 말 것
```

### B2. 새로운 발견 (New Discovery)
```yaml
type: new_discovery
strength: ★★★★☆
description: 추가 정보/존재 등장

examples:
  - "새끼가 더 있었다"
  - "상처가 있었다"
  - "다른 동물도 있었다"
  - "둥지/집을 발견"

visual:
  - 화면 안에 새로운 요소
  - 관점 이동
  - 범위 확대

application:
  - 상황을 더 복잡하게 만듦
  - 스테이크 상승
```

### B3. 동물의 반응 (Animal Response)
```yaml
type: animal_response
strength: ★★★★★
description: 예상 못한 동물 행동

examples:
  - "도망 안 감"
  - "따라옴"
  - "특정 방향을 가리킴"
  - "처음으로 눈 마주침"
  - "울음소리 냄"

visual:
  - 동물 클로즈업
  - 행동 변화
  - 교감 순간

application:
  - 동물의 의도 암시
  - 인간-동물 연결 시작
```

### B4. 상황 악화 (Situation Worsens)
```yaml
type: situation_worsens
strength: ★★★★★
description: 더 심각해지는 상황

examples:
  - "날씨가 더 나빠짐"
  - "다른 위험 요소 등장"
  - "시간이 촉박해짐"
  - "상태가 더 안 좋아짐"

visual:
  - 환경 변화
  - 긴박한 상황 요소
  - 시계/시간 암시

application:
  - 긴장감 상승
  - 행동 촉구
```

### B5. 첫 교감 순간 (First Connection)
```yaml
type: first_connection
strength: ★★★★☆
description: 동물이 마음을 여는 순간

examples:
  - "처음 눈 마주침"
  - "첫 접촉 허용"
  - "도망가지 않음"
  - "쪽으로 다가옴"

visual:
  - 눈 클로즈업
  - 거리 좁혀짐
  - 조심스러운 접촉

application:
  - 감정적 연결
  - 신뢰 형성 시작
```

### B6. 선택의 순간 (Decision Point)
```yaml
type: decision_point
strength: ★★★★☆
description: 갈등/결정 필요

examples:
  - "데려갈까 말까"
  - "도와줄까 말까"
  - "어느 쪽으로 갈까"
  - "계속할까 포기할까"

visual:
  - 망설이는 모습
  - 양쪽 옵션 보여줌
  - 결정의 순간

application:
  - 서스펜스 생성
  - 관객 참여 유도
```

## Best Practices

### 20-40초 구조
```
20-25초: 첫 발견/반응
25-30초: 상황 이해
30-35초: 새로운 정보
35-40초: 다음 단계로 연결
```

### 연결 원칙
```
A(오프닝)에서 던진 질문에 부분 답변
+ 새로운 질문 추가
= C(클라이맥스)로의 기대감
```

## Prompt Examples

### B1 - 예상 뒤집기
```
The small fox doesn't run away.
Instead, it looks up and slowly walks closer.
Shaky phone footage, heavy breathing slows down.
Fox stops right in front, looking up with pleading eyes.
No background music, only soft whimpering from fox.
```

### B3 - 동물의 반응
```
The fox keeps looking at one direction.
Camera follows its gaze, nothing visible yet.
Fox starts walking that way, looking back.
Seems like it wants to be followed.
No background music, fox crying softly, footsteps.
```

### B4 - 상황 악화
```
Snow starts falling harder.
The small fox is shivering more.
Flashlight flickers, battery low.
Need to move fast, no time to wait.
No background music, howling wind, urgent breathing.
```

## 안티 패턴 (피해야 할 것)

```
❌ 오프닝 반복 (같은 정보)
❌ 너무 빨리 다 공개
❌ 긴장감 떨어뜨림
❌ 불필요한 설명
❌ 액션 없는 대기
```

## C단계 연결 가이드

| B 유형 | → C 추천 전개 |
|--------|--------------|
| 예상 뒤집기 | 더 큰 반전 |
| 새로운 발견 | 발견의 의미 폭발 |
| 동물 반응 | 이유가 밝혀짐 |
| 상황 악화 | 최악의 순간 |
| 첫 교감 | 신뢰 테스트 |
| 선택 순간 | 선택의 결과 |
