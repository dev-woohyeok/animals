# /animal-shorts-scene - 장면 분할

스토리를 15초 단위 장면으로 분할 (멀티샷 구조, Seedance 2.0 최적화)

## 사용법

```
/animal-shorts-scene [스토리 참조]
```

---

## 핵심 변경사항

### 1. 시간순 전개 + 강한 도입 (Scene 1 = 시간순 첫 장면)

- Scene 1은 시간순 첫 장면이면서 관객의 관심을 끄는 도입
- 시청자 첫 3초 이탈 방지
- **모든 장면은 시간순(chronological)으로 전개. 과거 회상/플래시백 절대 금지**

### 2. 멀티샷 구조 (15초 = 최대 3개 서브샷 = 개별 미니 씬)

- 서브샷 = 개별 미니 씬. 자연스럽게 연결되지만 시간이 경과해서 구별되는 장면
- 같은 순간의 다른 앵글 ❌ → 시간이 흐른 뒤의 다른 장면 ✅
- 서브샷 간 전환 = 시간 경과 전환
- **⚠️ Scene 1은 예외: 단일 연속 장면으로 연출 (서브샷 분할 금지!)**

### 3. 서브샷 description은 직접 명시형 (Seedance 2.0 규칙 — 2026-05-07)

- 각 서브샷의 `description`에 **구체적 행동 + 동물 소리 + 영어 대사(있으면 따옴표)** 를 직접 작성
- ❌ 추상 표현 금지: `tense atmosphere`, `dog whimpering` (불충분), `woman reacts emotionally`
- ✅ 구체 작성: `dog lowers head and whimpers loudly`, `woman gasps and whispers "Oh my god"`
- **이유**: 다음 단계 `/animal-shorts-prompt` 에서 description을 그대로 활용 — 추상이면 Seedance 2.0이 무시함
- 자세한 규칙은 `prompts/seedance2_system.md` Dialogue + Action Rules 섹션 참조

---

## 장면 분할 규칙

`prompts/scene_system.md` 참조:

### 기본 규칙

- **총 장면 수**: 6개 (고정)
- **각 장면 길이**: 15초 (고정)
- **총 영상 길이**: 90초 (6개 x 15초 = 90초)
- **서브샷**: 장면당 최대 3개, 각 서브샷 최대 5초 (5초 초과 금지!)
- **⚠️ 서브샷 = 개별 미니 씬**: 자연스럽게 연결되지만 시간이 경과해서 구별 (연속 실시간 ❌)

### 장면 구성 요소

1. **제목**: 한글 + 영문
2. **is_hook**: Scene 1이면 true
3. **story_context**: ⚠️ CRITICAL! 반드시 3가지 포함:
   - **[Overall]** 전체 스토리 요약 1문장 (매 씬에 동일 반복)
   - **[Previous]** 직전 장면에서 무슨 일이 있었는지 (인과관계)
   - **[This scene]** 이 장면의 역할과 감정 방향
4. **character_state**: ⚠️ CRITICAL! 매 씬마다 변화 필수:
   - physical: 물리적 상태 (이전 씬 대비 변화)
   - emotional: 감정 상태 (이전 씬 대비 변화)
   - behavioral: 행동 패턴 (이전 씬 대비 변화)
5. **human_character**: ⚠️ CRITICAL! 매 씬마다 인간 캐릭터 포함:
   - 1인칭 POV 촬영자도 등장인물 (손, 옷소매, 목소리 보임)
   - 매 씬에 성별/나이/외모/복장 전체 설명 반복
   - 촬영자가 주인공이면 절대 생략 금지
6. **자막**: 서브샷별 짧은 캡션 (영문 + 한글)
7. **설명**: 무엇이 일어나는지
8. **감정**: 이 장면의 감정 톤
9. **서브샷(sub_shots)**: 최대 3개 beats
   - beat 번호
   - time (시간 범위)
   - shot_type (샷 타입)
   - description (설명)
10. **카메라**: 주 움직임 + 서브샷 전환 스타일
11. **조명**: 조명 설정 및 분위기

---

## 출력 형식

```yaml
scenes:
  - id: 1
    title: "벤치에 묶인 강아지"
    title_en: "Tied to the Bench"
    is_opening: true
    caption:
      - time: "0-15s"
        en: "Someone just left her here\nTied to a bench in the cold"
        ko: "누군가 여기 두고 갔다\n추운 벤치에 묶인 채로"
    duration: 15
    description: "시간순 도입 — 단일 연속 장면으로 촬영"
    emotion: "충격, 분노"
    camera:
      primary_movement: "handheld POV"
      note: "Scene 1 = 단일 연속 장면 (서브샷 금지)"
    lighting: "늦은 오후 흐린 하늘"
    key_elements:
      - "벤치에 묶인 줄"
      - "떨리는 강아지"

  - id: 2
    title: "다가가기"
    title_en: "Getting Closer"
    is_opening: false
    caption:
      - time: "0-5s"
        en: "She was shaking so badly"
        ko: "너무 심하게 떨고 있었다"
      - time: "5-10s"
        en: "I couldn't just walk past"
        ko: "그냥 지나칠 수 없었다"
      - time: "10-15s"
        en: "I had to help"
        ko: "도와줘야 했다"
    duration: 15
    description: "여자가 다가가서 강아지 상태를 확인"
    emotion: "연민, 걱정"

    sub_shots:
      - beat: 1
        time: "0-5s"
        shot_type: "medium"
        description: "여자가 벤치 쪽으로 천천히 다가가 무릎을 굽힌다. 강아지가 한 발 뒤로 물러나며 작게 으르렁거린다(low growl). 여자가 부드럽게 \"It's okay, sweetie. I'm here.\""
      - beat: 2
        time: "5-10s"
        shot_type: "close-up"
        description: "강아지 얼굴. 몸이 떨리고 코를 킁킁거리며 작게 낑낑거린다(whimpering). 줄이 벤치 다리에 팽팽하게 묶여 있고 비에 젖어 늘어짐."
      - beat: 3
        time: "10-15s"
        shot_type: "close-up (bridge)"
        description: "여자의 손이 매듭을 풀기 시작한다. 줄이 삐걱거린다. 여자가 깊은 숨을 쉬며 \"Come on, come on...\" 강아지가 머리를 들어 올린다."

    camera:
      primary_movement: "handheld POV"
      sub_shot_transitions: "물리적 카메라 동작"
    lighting: "늦은 오후 흐린 하늘"
    key_elements:
      - "강아지 떨림"
      - "줄 풀기"
      - "여자의 손"
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
- `static` - 고정
- `tracking` - 추적
- `digital zoom in/out` - 핸드폰 줌

### Shot Types (서브샷용)

- `extreme close-up` - 눈, 디테일
- `close-up` - 얼굴, 표정
- `medium` - 상반신, 상호작용
- `wide` - 환경, 전체 상황
- `POV` - 1인칭 시점
- `bridge` - 다음 씬 연결 (마지막 beat)

### Transition (전환) — ⚠️ 물리적 카메라 동작만!

서브샷 간 전환은 촬영자의 물리적 핸드폰 동작으로만:
- 폰을 옆으로 돌림 (화면 흔들리며 초점 나감)
- 폰을 아래로/위로 내림/올림
- 디지털 줌인/줌아웃

❌ 영화식 전환 금지: cut, fade, dissolve, match cut

---

## 조명 옵션

- `natural indoor lighting` - 자연 실내광
- `warm lamp light` - 따뜻한 램프
- `bright daylight` - 밝은 주광
- `soft evening light` - 부드러운 저녁빛
- `warm sunset through window` - 창문으로 들어오는 석양
- `cold blue-grey, overcast` - 차가운 흐린 날씨
- `phone flashlight only` - 핸드폰 플래시만 (야간)

---

## 장면 배치 가이드 (시간순 전개)

| 순서      | 역할              | 서브샷 속도              | 분위기                 |
| --------- | ----------------- | ------------------------ | ---------------------- |
| Scene 1   | **도입** (관심)   | ⚠️ 단일 연속 장면 (서브샷 금지!) | 시간순 시작, 관심 끌기  |
| Scene 2   | 전개              | 보통 (3 beats)           | 상황 전개, 감정 구축    |
| Scene 3   | 위기/전환         | 빠름 (3 beats)           | 긴장, 감정 고조        |
| Scene 4   | 해결              | 보통 (3 beats)           | 감정 전환점            |
| Scene 5   | 회복/유대         | 느림 (2-3 beats)         | 안도, 따뜻함           |
| Scene 6   | 결말/여운         | 느림 (2 beats)           | 감동, 행복             |

---

## ⚠️ 자동 진행 (영구 고정)

**장면 분할 완료 즉시 다음 단계를 자동 실행한다. 멈추지 않는다.**

1. 장면 분할 완료
2. → 즉시 Seedance 2.0 프롬프트 (`/animal-shorts-prompt`) 실행
3. → 즉시 제목 생성 (`/animal-shorts-title`) 실행
4. → 즉시 파일 저장 + git (`/animal-shorts-export`) 실행

**중간에 사용자에게 확인을 구하거나 멈추는 것은 금지.**
