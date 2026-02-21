# /animal-shorts-story - 스토리 생성

동물 감동 스토리 5막 구조 생성

## 사용법

```
/animal-shorts-story [동물] / [상황] / [감정] / [결말]
```

---

## 스토리 구조 (5막)

`prompts/story_system.md` 참조하여 다음 구조로 생성:

### 1. 도입 (Introduction)
- 동물 캐릭터의 초기 상황 설정
- 관객의 공감과 감정 이입 유도
- 감정: 슬픔, 고독, 불안, 외로움

### 2. 전개 (Development)
- 주요 캐릭터/상황 등장
- 감정적 연결 구축 시작
- 감정: 호기심, 연민, 희망의 시작

### 3. 위기 (Crisis)
- 긴장감 조성, 갈등 또는 결정의 순간
- 스토리의 전환점
- 감정: 긴장, 갈등, 망설임, 불확실

### 4. 해결 (Resolution)
- 상황 반전, 희망 또는 구원
- 감정적 전환
- 감정: 안도, 따뜻함, 기쁨, 결심

### 5. 결말 (Conclusion)
- 감정적 보상, 따뜻한 마무리
- 시청자 기억에 남는 장면
- 감정: 행복, 감동, 치유, 사랑

---

## 출력 형식

```yaml
title: "스토리 제목 (한글)"
synopsis: "1-2문장 요약"

arc:
  - phase: "도입"
    description: "장면 설명 (구체적으로)"
    beats:
      - "세부 비트 1"
      - "세부 비트 2"
    emotion: "슬픔, 고독"

  - phase: "전개"
    description: "..."
    beats: [...]
    emotion: "호기심, 희망"

  - phase: "위기"
    description: "..."
    beats: [...]
    emotion: "긴장, 불확실"

  - phase: "해결"
    description: "..."
    beats: [...]
    emotion: "안도, 따뜻함"

  - phase: "결말"
    description: "..."
    beats: [...]
    emotion: "행복, 감동"

character_development: "캐릭터가 어떻게 변화하는지"

emotional_journey:
  - position: 0.0
    emotion: "슬픔"
    intensity: 80
  - position: 0.3
    emotion: "희망"
    intensity: 50
  - position: 0.5
    emotion: "긴장"
    intensity: 70
  - position: 0.8
    emotion: "안도"
    intensity: 60
  - position: 1.0
    emotion: "행복"
    intensity: 90

total_duration: 60
```

---

## 감정 트리거 (효과적인 요소)

- 다른 종 간의 예상치 못한 우정
- 구조와 재활 여정
- 동물의 충성심과 무조건적 사랑
- 부모-자녀 유대
- 역경 극복
- 신뢰를 얻어가는 순간

---

## 가이드라인

### DO
- 보편적 감정에 집중: 사랑, 희망, 치유, 가족, 구원
- 슬픔/외로움에서 따뜻함/행복으로 명확한 감정 아크
- 시각적 스토리텔링을 위한 구체적인 감각 디테일
- 각 단계는 간결하지만 감정적으로 임팩트 있게
- 4-5개 짧은 비디오 클립(각 10-15초)으로 표현 가능하도록
- 실제 카메라로 포착한 진짜 순간처럼 느껴지도록

### DON'T
- 너무 복잡한 플롯
- 추상적인 개념
- 비현실적인 동물 행동
- 과도한 의인화
