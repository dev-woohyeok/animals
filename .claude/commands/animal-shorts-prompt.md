# /animal-shorts-prompt - Seedance 2.0 프롬프트 생성

각 장면에 대한 Seedance 2.0 최적화 **영어 프롬프트** 생성 (멀티샷)

## 사용법

```
/animal-shorts-prompt [장면 목록 참조]
```

---

## ⚠️ 핵심 원칙: Self-Contained + @ Reference + Multi-Shot

```yaml
핵심_문제: "Seedance 2.0은 각 프롬프트를 독립적으로 처리"
  - 이전 프롬프트 기억 안 함
  - 각 영상 완전히 독립 생성
  - @Image 참조로 캐릭터 시각적 일관성 확보

해결책_1: "@ 참조 + 텍스트 설명 = 완전한 일관성"
  - @Image1로 캐릭터 시각적 일관성
  - 텍스트로 상태 변화 설명 (매 씬마다)
  - 환경/스토리 컨텍스트 매 프롬프트에 포함

해결책_2: "15초 안에 최대 3개 서브샷으로 다양한 시각 자극"
```

---

## ⚠️ Seedance 2.0 자유도 원칙 (CRITICAL)

```
핵심: "카메라는 상세하게, 상황은 간결하게"

상세하게 → 카메라 앵글, 움직임, 촬영 스타일, 캐릭터 외형
간결하게 → 상황/액션(한 줄), 감정(형용사 최소), 환경(핵심만)

❌ 금지: 감정 형용사 나열, 액션 과잉 묘사, 결과 예측
✅ 지향: 카메라 지시 정확 + 상황 한 줄 + Seedance 2.0에 해석 자유도
```

**간결한 프롬프트 = 높은 영상 퀄리티**

---

## Multi-Shot 프롬프트 구조 (6단계)

### 모든 프롬프트에 반드시 포함할 요소:

```
1. 스토리 컨텍스트   → ⚠️ CRITICAL! "// Story:" 로 시작. 아래 3가지 필수:
                       [Overall] 전체 스토리 요약 1문장
                       [Previous] 직전 장면에서 무슨 일이 있었는지
                       [This scene] 이 장면의 역할과 감정 방향
2. 촬영 스타일     → 카메라 시점, 촬영 품질, 아마추어 느낌 명시
3. 환경 설정       → US 지역, 장소, 날씨, 시간, 오브젝트
4. 동물 캐릭터     → @Image1 참조 + 품종, 크기, 털 색상/상태, 눈, 액세서리 (매번!)
5. 인간 캐릭터     → 성별, 나이, 외모, 복장 (등장 시 매번 전체 설명!)
                      ⚠️ 1인칭 POV에서도 촬영자 캐릭터 필수! (손, 옷소매, 목소리 보임)
6. 서브샷 시퀀스   → 최대 3개 × 최대 5초씩. 5초 초과 금지!
                      ⚠️ 서브샷 = 개별 미니 씬 (시간 경과로 구별, 연속 실시간 ❌)
+ 오디오 지시      → No background music + 구체적 환경음/동물소리
+ 스타일 수식어    → 프롬프트 끝에 품질/분위기 키워드
```

### ⚠️ Story Context 예시

```
❌ 나쁜 예시 (이 장면만):
// Story: Cat wakes after surgery. Purring.

✅ 좋은 예시 (전체 + 앞 장면 + 이 장면):
// Story: Overall: Cat thrown from 3rd floor — rescued — surgery — happy ending 6 months later.
Previous: Wrapped in jacket, took taxi to hospital.
This scene: Cat wakes after leg fracture surgery with cast, purrs for first time — pain to trust.
```

---

## 프롬프트 작성 프로세스

### Step 1: 일관성 템플릿 정의 (프로젝트당 1회)

스토리 시작 시 **고정 요소** 정의:

```yaml
consistency_template:
  animal:
    base: "Small white Maltese, about 3kg adult"
    eyes: "Large round brown eyes"
    accessory: "Pink collar with small bell"
    reference: "@Image1's Maltese as the subject"

  location:
    base: "Suburban Seattle, Washington"

  human_rescuer:
    base: "Late 20s woman, brown ponytail, yellow rain jacket"

  audio:
    rule: "No background music"

  style:
    base: "Amateur phone footage quality. Slightly shaky. Natural lighting. Photorealistic."
```

### Step 2: 씬별 변화 요소 정의

```yaml
scene_variables:
  scene_1:
    fur: "Clean fluffy pure white fur"
    ribbon: "Pink ribbon on head"
    emotion: "Confusion"
    weather: "Late autumn evening, light rain"

  scene_4:
    fur: "White fur turned grayish and matted. Thin body"
    ribbon: "None"
    emotion: "Fear and exhaustion"
    weather: "Overcast morning after rain"
```

### Step 3: 프롬프트 조립

**템플릿 + 변화요소 + 서브샷 시퀀스 + @ 참조 = 완성된 프롬프트**

```
// Story: [context]

@Image1's [animal] as the subject.

[Shooting style - "amateur/handheld phone footage"]

[Environment: location.base + scene.weather + specific location/objects]

[Animal: animal.base + eyes + accessory + scene.fur + scene.emotion state]

[Human: human.base (when appearing)]

[Sub-shot sequence]
0-5s: [angle] [action]
— natural transition —
5-10s: [angle] [action]
— natural transition —
10-15s: [angle] [action]

[Audio: No background music. specific sounds.]

[Style modifiers]
```

---

## 프롬프트 예시

### 잘못된 예시 ❌ (정보 부족)

```
A corgi abandoned in the rain, trembling.
```

→ Seedance 2.0: "Which corgi? Where? What does it look like? What angle?"

### 잘못된 예시 ❌ (과도한 상세 - 퀄 떨어짐)

```
0-2s: Extreme close-up on puppy's eye. Raindrops streaming down face. Lightning flashes reflecting in pupils. Trembling eyes full of terror.
```

→ 감정 형용사, 액션 과잉 묘사 = 어색한 결과

### 올바른 예시 ✅ (카메라 상세 + 상황 간결)

```
// Story: Overall: White Maltese abandoned at park bench -> rescued -> recovery -> happy family.
Previous: Owner drove away leaving dog tied to bench.
This scene: Night falls. Dog still waiting. Rain starts.

@Image1's small white Maltese as the subject.

Edited amateur phone footage. Shaky, unsteady. Phone flashlight only.

Suburban park in Seattle, Washington. Night. Heavy rain. Wooden bench. Street lamp.

Small white Maltese, about 3kg adult. White fur soaked and flattened by rain. Pink collar with bell. Large round brown eyes.

0-5s: Extreme close-up. Puppy's eyes. Raindrops.
— natural transition —
5-10s: Pull back to medium shot. Full body tied to bench leg.
— natural transition —
10-15s: Slow digital zoom in. Puppy lifts head slightly.

No background music. Heavy rain, thunder, puppy breathing, collar bell clinking.

Amateur phone footage quality. Shaky. Phone flashlight only. Raw, unedited feel.
```

---

## 서브샷 시퀀스 규칙

```
⚠️ 서브샷 = 개별 미니 씬! 연속된 실시간이 아님!
  → 각 서브샷은 자연스럽게 연결되지만 시간이 경과해서 구별되는 장면

모든 Scene (Scene 2+):
  0-5s → 서브샷 1 (Mini-scene A)
  — natural transition —
  5-10s → 서브샷 2 (Mini-scene B)
  — natural transition —
  10-15s → 서브샷 3 (Mini-scene C)

Scene 1: 단일 연속 장면 (0-15s 원테이크, 서브샷 금지!)
```

### ⚠️ 서브샷 간 전환 규칙 (영구 고정)

- 서브샷 = 개별 미니 씬
- 서브샷 사이에 `— natural transition —` 필수
- 영화식 전환(cut, dissolve, fade) 금지. 같은 순간의 다른 앵글 금지

---

## @ 참조 시스템 활용

### 캐릭터 일관성
```
모든 프롬프트 시작에:
@Image1's [animal description] as the subject.

선택적으로:
@Image2 as the first frame  (장면 연속성 확보)
```

### 참조 이미지 준비 가이드
```
@Image1: 동물 캐릭터 참조 이미지 (전체 영상에서 공통 사용)
@Image2-9: 장면별 배경/환경 참조 (선택)
```

---

## 자막/캡션 규칙

**모든 장면의 서브샷별로 영문 + 한글 자막 포함!**

```yaml
caption:
  - time: "0-5s"
    EN: "He just... left her there."
    KR: "그냥... 버리고 갔어."
  - time: "5-10s"
    EN: "Tied to a bench in the rain"
    KR: "빗속 벤치에 묶인 채로"
  - time: "10-15s"
    EN: "She was still waiting"
    KR: "아직도 기다리고 있었다"
```

자막 작성 규칙:

- 1인칭 내레이션 스타일 (촬영자/구조자 시점)
- 짧고 임팩트 있게 (15자 내외)
- 서브샷마다 개별 자막 (씬 전체에 자막 1개 금지!)
- `...`(말줄임표) 사용 금지
- 반드시 2줄 줄바꿈

---

## 오디오 지시 규칙

Seedance 2.0은 음향을 자동 생성합니다. 방향만 지시:

```
❌ "No background music, no sounds"
✅ "No background music. Natural ambient sound only — rain, dog whimpering, footsteps, heavy breathing."
```

자연스러운 소리는 반드시 포함:

- 동물 소리: whimpering, growling, barking, tail wagging, collar clinking
- 사람 소리: breathing, footsteps, soft speaking, gasping
- 환경음: rain, city noise, birds, wind, door sounds

---

## 출력 형식

```yaml
# 일관성 템플릿
consistency_template:
  animal:
    base: "Small white Maltese, about 3kg adult"
    eyes: "Large round brown eyes"
    accessory: "Pink collar with small bell"
    reference: "@Image1"
  location:
    base: "Suburban Seattle, Washington"
  human_rescuer:
    base: "Late 20s woman, brown ponytail, yellow rain jacket"

# 씬별 프롬프트
prompts:
  - scene_id: 1
    title: "유기"
    is_hook: true
    duration: "15s"

    variables:
      fur: "Clean fluffy pure white fur"
      emotion: "Confusion"
      weather: "Late autumn evening, light rain"

    caption:
      - time: "0-15s"
        EN: "He just... left her there."
        KR: "그냥... 버리고 갔어."

    prompt: |
      [Full Self-Contained Seedance 2.0 Prompt in English]

  - scene_id: 2
    title: "비 속의 밤"
    is_hook: false
    duration: "15s"

    variables:
      fur: "White fur soaked and flattened by rain"
      emotion: "Fear"
      weather: "Night, heavy rain"

    caption:
      - time: "0-5s"
        EN: "She waited all night"
        KR: "밤새 기다렸다"
      - time: "5-10s"
        EN: "In the pouring rain"
        KR: "쏟아지는 빗속에서"
      - time: "10-15s"
        EN: "Alone"
        KR: "혼자서"

    prompt: |
      [Full Self-Contained Seedance 2.0 Prompt in English]
```

---

## Content Policy 검증 (필수)

### 금지 표현

| 금지           | 대체                  |
| -------------- | --------------------- |
| dead, corpse   | motionless, lying still, collapsed |
| blood, wound   | (삭제)                |
| attack, kill   | (장면 분리)           |
| horrifying, terrifying | tense, dramatic |

### 금지 표현 (영화적/비현실적)
```
No: "devastating scene", "piercing", "anguished", "frantically"
No: "violently", "dramatically", "cinematic"
Yes: "Shaky flashlight beam sweeps across dark forest floor"
Yes: "Unsteady amateur footage, phone flashlight only"
```

---

## 프롬프트 체크리스트

각 프롬프트 생성 후 확인:

```
[ ] "// Story:" 에 Overall + Previous + This scene 포함? (CRITICAL!)
[ ] @Image1 참조 포함? ("@Image1's [animal] as the subject")
[ ] 촬영 스타일에 "amateur/handheld/phone footage" 명시?
[ ] 환경/장소가 US/북미 기준 구체적?
[ ] 동물 캐릭터의 전체 설명 포함? (매번!)
[ ] 동물의 현재 상태(털, 감정)가 이전 씬과 다른가?
[ ] 인간 캐릭터(촬영자 포함!) 외모/복장 설명?
[ ] 서브샷 시퀀스가 시간 분할 형태 (0-5s, 5-10s, 10-15s)?
[ ] 서브샷 최대 3개, 각 최대 5초?
[ ] 서브샷 간 "— natural transition —" 포함?
[ ] 오디오 지시 포함 (구체적 소리 + no BGM)?
[ ] 스타일 수식어 포함? (amateur, shaky, photorealistic 등)
[ ] 서브샷별 자막(EN/KR) 포함?
[ ] Scene 1은 단일 연속 장면 (서브샷 금지)?
[ ] 프롬프트가 전부 영어?
```

---

## DO / DON'T

### DO

- **영어로 프롬프트 작성** (Seedance 2.0 최적화)
- **@Image1 참조로 캐릭터 일관성 확보**
- **매 프롬프트에 캐릭터 전체 텍스트 설명 포함** (상태 변화용)
- **매 프롬프트에 환경 설정 포함**
- **서브샷 시퀀스를 시간 분할 형태로 작성**
- **모든 서브샷에 개별 자막 포함**
- **프롬프트 끝에 스타일 수식어 추가**
- 구체적이고 시각적인 설명 사용
- 자연스러운 소리 포함

### DON'T

- 한국어로 프롬프트 작성 ❌
- "Same character as before" 같은 참조 표현 ❌
- "Continuing from previous scene" 같은 연결 표현 ❌
- 15초 동안 단일 앵글/단일 액션만 묘사 ❌
- 자막 누락 ❌
- "beautiful", "nice" 같은 모호한 표현 ❌
- 실사 인간 얼굴 참조 이미지 업로드 ❌
- 200단어 초과 ❌

---

## ⚠️ 자동 진행 (영구 고정)

**Seedance 2.0 프롬프트 생성 완료 즉시 다음 단계를 자동 실행한다. 멈추지 않는다.**

1. Seedance 2.0 프롬프트 6개 생성 완료
2. → 즉시 제목 생성 (`/animal-shorts-title`) 실행
3. → 즉시 파일 저장 + git (`/animal-shorts-export`) 실행

**중간에 사용자에게 확인을 구하거나 멈추는 것은 금지.**
