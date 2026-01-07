# /animal-shorts-scene - 장면 분할

스토리를 15초 단위 장면으로 분할

## 사용법

```
/animal-shorts-scene [스토리 참조]
```

---

## 장면 분할 규칙

`prompts/scene_system.md` 참조:

### 기본 규칙
- **총 장면 수**: 6개 이상
- **각 장면 길이**: 15초 (10-18초 허용)
- **총 영상 길이**: 90초 이상

### 장면 구성 요소
1. **제목**: 한글 + 영문
2. **설명**: 무엇이 일어나는지
3. **동작**: 구체적인 움직임
4. **감정**: 이 장면의 감정 톤
5. **카메라**: 움직임, 앵글, 전환
6. **조명**: 조명 설정 및 분위기

---

## 출력 형식

```yaml
scenes:
  - id: 1
    title: "특별한 발견"
    title_en: "A Special Discovery"
    duration: 15
    description: "골든 리트리버가 아기 고슴도치를 조심스럽게 입에 물고 집으로 들어온다"
    action: "개가 천천히 걸어오며 입에 작은 고슴도치를 물고 있다"
    emotion: "호기심, 조심스러움, 따뜻함"
    camera:
      movement: "handheld POV"
      angle: "owner perspective"
      transition: "fade in"
    lighting: "natural indoor lighting"
    key_elements:
      - "골든 리트리버의 부드러운 입"
      - "작은 고슴도치"
      - "주인의 놀란 반응"

  - id: 2
    title: "첫 만남"
    title_en: "First Meeting"
    duration: 12
    description: "..."
    action: "..."
    emotion: "..."
    camera:
      movement: "..."
      angle: "..."
      transition: "..."
    lighting: "..."
    key_elements: [...]
```

---

## 카메라 옵션

### Movement (움직임)
- `handheld POV` - 1인칭 핸드헬드 (추천)
- `slow dolly in` - 느린 접근
- `static` - 고정
- `pan` - 좌우 패닝
- `tracking` - 추적

### Angle (앵글)
- `close-up` - 클로즈업
- `wide` - 와이드
- `eye-level` - 눈높이
- `low angle` - 로우앵글
- `owner perspective` - 주인 시점

### Transition (전환)
- `fade in` - 페이드 인
- `cut` - 컷
- `dissolve` - 디졸브
- `match cut` - 매치 컷

---

## 조명 옵션

- `natural indoor lighting` - 자연 실내광
- `warm lamp light` - 따뜻한 램프
- `bright daylight` - 밝은 주광
- `soft evening light` - 부드러운 저녁빛
- `warm sunset through window` - 창문으로 들어오는 석양
- `cold blue-grey, overcast` - 차가운 흐린 날씨

---

## 장면 배치 가이드

| 스토리 단계 | 장면 수 | 권장 분위기 |
|------------|--------|------------|
| 도입 | 1-2개 | 슬픔, 고독, 차가운 조명 |
| 전개 | 1-2개 | 호기심, 따뜻한 조명 시작 |
| 위기 | 1개 | 긴장, 대비 있는 조명 |
| 해결 | 1-2개 | 안도, 따뜻한 조명 |
| 결말 | 1-2개 | 행복, 황금빛 조명 |
