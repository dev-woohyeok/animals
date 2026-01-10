# /animal-shorts-prompt - Sora2 프롬프트 생성

각 장면에 대한 Sora2 최적화 영어 프롬프트 + 한국어 번역 동시 생성

## 사용법

```
/animal-shorts-prompt [장면 목록 참조]
```

---

## 핵심 규칙

`prompts/sora2_system.md` 참조:

### 1. 캐릭터 일관성 (CRITICAL)

**모든 프롬프트에 동일한 캐릭터 설명 사용!**

```
A [size] [species] with [fur/feather color and texture], [eye color and expression], [distinctive features]
```

**예시**:
```
A small African pygmy hedgehog with brown and cream quills, tiny black bead eyes, and a pink nose
```

```
A golden retriever with fluffy cream-colored fur, large expressive brown eyes, slightly floppy ears, and a white patch on its chest
```

### 2. 프롬프트 구조 (순서대로)

1. **Camera/Style**: 카메라 스타일 (예: First person POV handheld home video)
2. **Character**: 캐릭터 설명 (일관되게 복사)
3. **Setting**: 환경/배경
4. **Action**: 동작/움직임
5. **Camera Movement**: 카메라 움직임
6. **Lighting**: 조명
7. **Atmosphere**: 분위기
8. **Technical Specs**: 품질 마커

### 3. 품질 마커

스타일에 따라 선택:

**Home Video (추천)**:
```
First person POV handheld footage, home video aesthetic, slightly grainy, natural imperfections, authentic amateur feel
```

**Cinematic Realistic**:
```
Photorealistic 4K cinematic quality, shallow depth of field, cinematic color grading, subtle film grain
```

**Documentary**:
```
Documentary style footage, natural lighting, observational camera, real-world authenticity
```

---

## 출력 형식

```yaml
character_reference: |
  A small African pygmy hedgehog with brown and cream quills, tiny black bead eyes, and a pink nose

prompts:
  - scene_id: 1
    english: |
      First person POV handheld home video footage. The owner films their golden retriever
      walking toward them, carefully carrying a tiny African pygmy hedgehog with brown and
      cream quills in its mouth. The dog approaches slowly with extreme gentleness.
      Natural indoor lighting, slight motion blur. Low quality home camera aesthetic,
      amateur footage feel, authentic and raw.
    korean: |
      1인칭 POV 핸드헬드 홈비디오. 주인이 골든 리트리버가 다가오는 모습을 촬영한다.
      개는 갈색과 크림색 가시가 있는 작은 아프리카 피그미 고슴도치를 조심스럽게
      입에 물고 천천히 다가온다. 자연 실내조명, 약간의 모션 블러.
      저화질 홈카메라 느낌, 아마추어 영상 분위기, 진짜 같은 느낌.
    structure:
      character: "golden retriever + African pygmy hedgehog"
      setting: "indoor, living room"
      action: "dog walking, carrying hedgehog"
      camera: "handheld POV"
      lighting: "natural indoor"
      atmosphere: "curious, gentle, warm"

  - scene_id: 2
    english: |
      ...
    korean: |
      ...
```

---

## DO / DON'T

### DO
- 구체적이고 시각적인 설명 사용
- 캐릭터 설명 **정확히 동일하게** 유지
- 카메라 움직임 방향 포함
- 조명 조건 명시
- 감정적 분위기 키워드 추가
- 품질 마커로 마무리

### DON'T
- "beautiful", "nice" 같은 모호한 표현
- 장면마다 캐릭터 설명 변경
- 오디오/사운드 설명 포함
- 부정 프롬프트 사용
- 너무 많은 요소로 복잡하게 만들기
- 200단어 초과

---

## Content Policy 검증 (필수)

프롬프트 생성 후 반드시 아래 체크리스트 확인:

### 금지 표현 자동 검사

| 금지 단어 | 대체 표현 |
|----------|----------|
| dead, death, die | motionless, still, not responding |
| corpse, body, lifeless | lying still, collapsed, fallen |
| blood, bleeding, wound | (삭제) |
| kill, attack, devour, maul | (장면 분리) |
| horrifying, terrifying, gruesome | tense, dramatic, intense |

### 검증 체크리스트

```
[ ] dead/death/die 단어 없음
[ ] blood/wound/injury 없음
[ ] attack/kill/devour 없음
[ ] 포식자가 먹이 섭취하는 장면 없음
[ ] 직접적인 폭력 묘사 없음
[ ] 동물 학대로 해석될 장면 없음
```

### 위반 발견 시

1. 해당 표현을 대체 표현으로 수정
2. 폭력 장면은 직전/직후로 분리
3. 감정은 눈물, 울음, 자세 등으로 전달

---

## 예시 프롬프트 (Home Video 스타일)

```
First person POV handheld home video. Owner crouches down filming as their golden retriever
carefully places the tiny African pygmy hedgehog with brown and cream quills onto a soft blanket.
The camera gets close, slightly shaky and out of focus momentarily as the owner adjusts.
The dog's wet nose nudges the baby hedgehog, who uncurls to reveal tiny black bead eyes.
Warm lamp lighting, grainy home video quality, slight video compression artifacts.
Authentic amateur footage aesthetic.
```

---

## 번역 가이드

`prompts/translation_system.md` 참조:

- 기술 용어는 그대로 유지 (POV, handheld 등)
- 자연스러운 한국어로 의역
- 영상 제작 용어는 업계 표준 사용
- 감정 전달 우선
