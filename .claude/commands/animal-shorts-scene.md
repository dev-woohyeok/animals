# /animal-shorts-scene - 장면 분할

스토리를 15초 단위 장면으로 분할 (멀티샷 + 스타트 프레임 구조)

## 사용법

```
/animal-shorts-scene [스토리 참조]
```

---

## 핵심 변경사항

### 1. Hook First (Scene 1 = 가장 충격적 장면)

- Scene 1은 시간순 도입이 아닌, **스토리에서 가장 임팩트 있는 순간**
- 시청자 첫 3초 이탈 방지
- 나머지 장면에서 시간순으로 전개

### 2. 멀티샷 구조 (15초 = 최대 3개 서브샷)

- 쇼츠 시청자는 2-3초마다 시각 자극 필요
- 한 장면 내에서 여러 앵글/샷 전환
- 편집된 푸티지처럼 구성

### 3. 스타트 프레임 전환

- 전 씬의 마지막 프레임을 캡쳐 → 다음 씬 시작 이미지로 사용
- Scene 2부터 시작 즉시 완전히 다른 구도로 컷 전환 (스타트 프레임에 머무르면 해당 구도로 고정됨!)
- Sora2 독립 생성 간 시각적 일관성 확보

---

## 장면 분할 규칙

`prompts/scene_system.md` 참조:

### 기본 규칙

- **총 장면 수**: 4-5개
- **각 장면 길이**: 10-15초
- **총 영상 길이**: 60초 이하 (1분 이하 필수!)
- **서브샷**: 장면당 최대 3개, 각 서브샷 최대 5초 (5초 초과 금지!)
- **Scene 2+ (0-1초) 전환 beat**: 스타트 프레임에서 즉시 컷 전환 → 완전히 다른 앵글 (0-1초 별도 라인 필수! 0-5초에 합치지 말 것!)
- **Scene 1**: 반드시 Hook (가장 충격적 순간)이며 서브샷 없이 한프레임에 다담음

### 장면 구성 요소

1. **제목**: 한글 + 영문
2. **is_hook**: Scene 1이면 true
3. **story_context**: ⚠️ CRITICAL! 반드시 3가지 포함:
   - **[전체]** 전체 스토리 요약 1문장 (매 씬에 동일 반복)
   - **[앞 장면]** 직전 장면에서 무슨 일이 있었는지 (인과관계)
   - **[이 장면]** 이 장면의 역할과 감정 방향
4. **character_state**: ⚠️ CRITICAL! 매 씬마다 변화 필수:
   - physical: 물리적 상태 (이전 씬 대비 변화)
   - emotional: 감정 상태 (이전 씬 대비 변화)
   - behavioral: 행동 패턴 (이전 씬 대비 변화)
5. **human_character**: ⚠️ CRITICAL! 매 씬마다 인간 캐릭터 포함:
   - 1인칭 POV 촬영자도 등장인물 (손, 옷소매, 목소리 보임)
   - 매 씬에 성별/나이/외모/복장 전체 설명 반복
   - 촬영자가 주인공이면 절대 생략 금지
6. **자막**: 쇼츠용 짧은 캡션 (영문 + 한글)
7. **설명**: 무엇이 일어나는지
8. **감정**: 이 장면의 감정 톤
9. **서브샷(sub_shots)**: 최대 3개 beats
   - beat 번호
   - time (시간 범위)
   - shot_type (샷 타입)
   - description (설명)
10. **카메라**: 주 움직임 + 서브샷 전환 스타일
11. **조명**: 조명 설정 및 분위기
12. **end_frame**: 이 장면의 마지막 프레임 설명 (다음 장면 시작 이미지 참조용)
13. **start_frame_ref**: (Scene 2+) 전 씬 end_frame 참조

---

## 출력 형식

```yaml
scenes:
  - id: 1
    title: "폭풍 속 발견"
    title_en: "Discovery in the Storm"
    is_hook: true
    caption:
      en: "Something was tied to that bench..."
      ko: "벤치에 뭔가가 묶여있었다..."
    duration: 15
    description: "가장 충격적인 순간 - 폭풍우 속 벤치에 묶인 강아지. 서브샷 없이 단일 프레임."
    emotion: "충격, 불안"
    # ⚠️ Scene 1은 서브샷 없음 - 한 프레임에 모든 것을 담는다
    camera:
      primary_movement: "handheld POV"
      note: "단일 연속 샷 - 서브샷 없음"
    lighting: "어둠 + 번개 플래시 + 핸드폰 플래시"
    end_frame: "강아지가 카메라를 바라보는 클로즈업. 빗물에 젖은 얼굴, 크고 둥근 눈, 떨리는 몸"
    key_elements:
      - "벤치에 묶인 줄"
      - "폭풍우"
      - "떨리는 강아지"

  - id: 2
    title: "3시간 전 - 유기"
    title_en: "3 Hours Earlier - Abandoned"
    is_hook: false
    caption:
      en: "3 hours earlier... someone left her here"
      ko: "3시간 전... 누군가 여기 두고 갔다"
    duration: 15
    description: "시간을 되돌려 유기 장면"
    emotion: "분노, 슬픔"
    start_frame_ref: "Scene 1 end_frame (강아지 클로즈업)에서 시작 즉시 컷 전환 → 3시간 전 장면으로"

    sub_shots:
      - beat: 1
        time: "0-1s"
        shot_type: "transition"
        description: "전 씬 마지막(강아지 클로즈업)에서 빠르게 전환, 텍스트: '3 hours earlier'"
      - beat: 2
        time: "1-5s"
        shot_type: "wide, dashcam"
        description: "주택가 도로, 은색 세단이 멈춤"
      - beat: 3
        time: "5-9s"
        shot_type: "medium"
        description: "남자가 강아지를 벤치 다리에 묶는다"
      - beat: 4
        time: "9-13s"
        shot_type: "tracking"
        description: "남자가 차로 돌아가 떠남. 강아지가 따라가려 함"
      - beat: 5
        time: "13-15s"
        shot_type: "close-up (bridge)"
        description: "혼란스러운 표정의 강아지. 줄에 걸려 더 못 감"

    camera:
      primary_movement: "관찰 시점 → handheld"
      sub_shot_transitions: "dissolve → cut → cut → cut"
    lighting: "늦은 오후 흐린 하늘, 가로등 시작"
    end_frame: "벤치에 묶인 강아지가 떠나는 차를 바라보는 모습. 줄이 팽팽하게 당겨짐"
    key_elements:
      - "은색 세단"
      - "벤치에 묶는 행위"
      - "따라가려는 강아지"
```

---

## 서브샷 전환 패턴 가이드

| 패턴          | 서브샷 흐름                           | 적합한 장면             |
| ------------- | ------------------------------------- | ----------------------- |
| **줌인**      | wide → medium → close-up → extreme CU | 발견, 관찰, 디테일 공개 |
| **줌아웃**    | CU → medium → wide reveal             | 상황 공개, 반전, 스케일 |
| **핑퐁**      | 동물 → 사람 → 동물 → 사람             | 상호작용, 신뢰 구축     |
| **속도 변화** | 느림 → 빠름 → 느림                    | 긴장 → 액션 → 안도      |
| **POV 전환**  | 관찰자 → 1인칭 → 동물 시점            | 몰입 극대화             |

---

## 카메라 옵션

### Movement (움직임)

- `handheld POV` - 1인칭 핸드헬드 (추천)
- `slow dolly in` - 느린 접근
- `static` - 고정
- `pan` - 좌우 패닝
- `tracking` - 추적

### Shot Types (서브샷용)

- `extreme close-up` - 눈, 디테일
- `close-up` - 얼굴, 표정
- `medium` - 상반신, 상호작용
- `wide` - 환경, 전체 상황
- `POV` - 1인칭 시점
- `transition` - 전 씬 연결 (Scene 2+ 첫 beat)
- `bridge` - 다음 씬 연결 (마지막 beat)

### Transition (전환)

- `cut` - 빠른 컷 (서브샷 간 기본)
- `fade` - 시간 경과
- `dissolve` - 회상, 전환
- `match cut` - 비주얼 연속성

---

## 조명 옵션

- `natural indoor lighting` - 자연 실내광
- `warm lamp light` - 따뜻한 램프
- `bright daylight` - 밝은 주광
- `soft evening light` - 부드러운 저녁빛
- `warm sunset through window` - 창문으로 들어오는 석양
- `cold blue-grey, overcast` - 차가운 흐린 날씨
- `phone flashlight only` - 핸드폰 플래시만 (야간)
- `lightning flash` - 번개 (폭풍 장면)

---

## 장면 배치 가이드 (Hook First)

| 순서      | 역할            | 장면 수 | 서브샷 속도      | 분위기                 |
| --------- | --------------- | ------- | ---------------- | ---------------------- |
| Scene 1   | **Hook** (충격) | 1개     | 서브샷 없음 (단일 프레임) | 가장 강렬한 순간       |
| Scene 2   | 배경/맥락       | 1개     | 보통 (3 beats) | 시간순 시작, "어떻게?" |
| Scene 3   | 전개/위기       | 1개     | 빠름 (3 beats) | 긴장, 감정 고조        |
| Scene 4-5 | 해결+결말       | 1-2개   | 느림 (2-3 beats) | 안도, 감동, 행복       |
