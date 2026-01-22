# The Cement Mixer Owl

> 건설현장 시멘트 믹서에서 발견된 큰뿔 올빼미. 시멘트로 뒤덮인 채 발견되어 구조, 3개월 후 건강하게 회복.

**총 길이:** 90초 (9개 장면)
**촬영 스타일:** Scene 1-4 관찰자 시점 / Scene 5-9 구조자 1인칭 POV
**위치:** 미국 유타주 건설현장 → Best Friends Animal Sanctuary

---

## 일관성 템플릿 (Consistency Template)

```yaml
consistency_template:
  animal:
    species: "큰뿔 올빼미 (Great Horned Owl)"
    size: "날개 펼치면 1.2m, 몸길이 약 55cm의 큰 올빼미"
    eyes: "크고 둥근 노란색 눈, 검은 동공"
    features: "특징적인 귀 깃털 (뿔처럼 보이는 깃털 다발), 갈색과 회색 깃털"

  location:
    base: "미국 유타주 사막 지역 건설현장"
    specific: "Black Desert Resort 건설 프로젝트 현장"

  human:
    worker: "30대 남성 건설 노동자, 노란색 안전모, 형광 조끼, 작업복"
    rescuer: "같은 건설 노동자, 장갑 착용"

  weather:
    base: "맑은 낮, 사막 지역의 건조한 날씨"

  sound:
    rule: "No background music"
```

---

## 장면별 프롬프트

### Scene 1: 이상한 소리 (0-10초)
**Hook Type:** A1 - Strange Discovery

```yaml
variables:
  camera: "관찰자 시점, 동료가 멀리서 촬영"
  time: "낮, 맑은 하늘"
  action: "시멘트 믹서에서 이상한 소리"
  emotion: "호기심, 의아함"

caption:
  EN: "Wait... what's that sound?"
  KR: "잠깐... 저 소리 뭐지?"
```

**Sora2 Prompt:**
```
멀리서 촬영하는 관찰자 시점의 아마추어 핸드폰 영상. 흔들리고 불안정한 푸티지.

미국 유타주 사막 지역의 대규모 건설현장. 맑은 낮, 건조한 공기. 콘크리트 믹서 트럭들, 철골 구조물, 먼지 날리는 현장.

30대 남성 건설 노동자. 노란색 안전모, 형광 조끼, 작업복 차림. 시멘트 믹서 트럭 앞에 서 있다.

믹서 드럼에서 이상한 긁는 소리가 난다. 노동자가 고개를 갸웃하며 믹서 쪽을 본다. 동료에게 손짓하며 "이리 와봐"라는 제스처.

No background music. 건설현장 소음, 멀리서 들리는 장비 소리, 믹서에서 나는 이상한 긁는 소리, 발자국 소리.
```

---

### Scene 2: 믹서 안을 들여다봄 (10-20초)
**Hook Type:** B1 - 정체 확인

```yaml
variables:
  camera: "관찰자 시점, 줌인"
  action: "믹서 안을 손전등으로 비춤"
  emotion: "긴장, 궁금"

caption:
  EN: "Is something alive in there?"
  KR: "저 안에 뭔가 살아있는 거야?"
```

**Sora2 Prompt:**
```
관찰자 시점의 아마추어 핸드폰 영상. 멀리서 촬영하다 줌인. 흔들리는 푸티지.

미국 유타주 사막 지역의 대규모 건설현장. 맑은 낮. 거대한 시멘트 믹서 트럭.

30대 남성 건설 노동자. 노란색 안전모, 형광 조끼, 작업복. 믹서 드럼 입구에 다가간다.

핸드폰 손전등을 켜고 어두운 믹서 안을 비춘다. 손전등 빛이 안쪽으로 들어간다. 노동자가 놀라서 뒤로 물러난다. 손으로 입을 막으며 충격받은 표정.

No background music. 발자국 소리, 놀라는 숨소리, 믹서 안에서 나는 퍼덕거리는 소리.
```

---

### Scene 3: 충격적 발견 (20-30초)
**Hook Type:** C1 - 반전 발견 (최강 후킹)

```yaml
variables:
  camera: "관찰자 시점 → 줌인하여 믹서 안 클로즈업"
  action: "시멘트 덩어리가 눈을 깜빡임"
  emotion: "충격, 경악"

caption:
  EN: "Oh my god... it blinked."
  KR: "세상에... 눈을 깜빡였어."
```

**Sora2 Prompt:**
```
관찰자 시점의 아마추어 핸드폰 영상. 최대 줌인. 흔들리고 불안정한 푸티지.

미국 유타주 건설현장의 시멘트 믹서 트럭 내부. 어둡고 회색빛 시멘트 잔여물로 덮인 공간.

시멘트와 먼지로 완전히 뒤덮인 덩어리. 회색 시멘트가 굳어가는 중. 갑자기 그 덩어리에서 크고 둥근 노란색 눈 두 개가 깜빡인다. 큰뿔 올빼미다. 날개 펼치면 1.2m, 몸길이 약 55cm. 특징적인 귀 깃털이 시멘트로 덮여 있다. 올빼미가 카메라를 똑바로 응시한다.

No background music. 충격받은 숨소리, 올빼미의 약한 울음소리, 시멘트 부스러지는 소리.
```

---

### Scene 4: 긴급 상황 (30-40초)
**Hook Type:** D1 - 시간 압박

```yaml
variables:
  camera: "관찰자 시점"
  action: "시멘트가 굳기 전에 꺼내야 함"
  emotion: "긴박함, 조급"

caption:
  EN: "We gotta get it out. NOW."
  KR: "지금 당장 꺼내야 해."
```

**Sora2 Prompt:**
```
관찰자 시점의 아마추어 핸드폰 영상. 흔들리고 급하게 움직이는 푸티지.

미국 유타주 사막 지역 건설현장. 맑은 낮. 시멘트 믹서 트럭 앞.

30대 남성 건설 노동자 두 명. 노란색 안전모, 형광 조끼, 작업복. 한 명이 두꺼운 작업 장갑을 끼고 있다.

노동자들이 급하게 대화하며 손짓한다. 한 명이 장갑을 끼고 믹서 안으로 팔을 뻗는다. 조심스럽지만 급한 동작. 다른 노동자가 담요를 가져온다.

No background music. 급한 목소리들, 장갑 끼는 소리, 발자국 소리, 긴장된 숨소리.
```

---

### Scene 5: 구조 시작 (40-50초)
**Hook Type:** 구조자 1인칭 POV 전환

```yaml
variables:
  camera: "1인칭 POV, 구조자의 핸드폰"
  action: "올빼미를 조심히 꺼냄"
  emotion: "긴장, 집중"

caption:
  EN: "Easy... easy... I got you."
  KR: "천천히... 천천히... 잡았어."
```

**Sora2 Prompt:**
```
1인칭 시점의 아마추어 핸드폰 영상. 흔들리고 불안정한 푸티지. 한 손으로 촬영.

미국 유타주 건설현장. 시멘트 믹서 트럭 내부를 들여다보는 시점.

시멘트와 먼지로 완전히 뒤덮인 큰뿔 올빼미. 날개 펼치면 1.2m, 몸길이 약 55cm의 큰 올빼미. 크고 둥근 노란색 눈, 검은 동공. 특징적인 귀 깃털이 시멘트로 덮여 납작해짐. 회색 시멘트가 깃털에 굳어가는 중.

장갑 낀 손이 프레임에 들어온다. 조심스럽게 올빼미 몸 아래로 손을 넣는다. 올빼미가 눈을 크게 뜨고 카메라를 본다. 천천히 들어올린다.

No background music. 긴장된 숨소리, 시멘트 부스러지는 소리, 올빼미의 약한 소리, 장갑과 깃털 스치는 소리.
```

---

### Scene 6: 물로 세척 (50-60초)
**Hook Type:** D2 - 변화 시작

```yaml
variables:
  camera: "1인칭 POV"
  action: "물로 시멘트를 씻어냄"
  emotion: "안도, 희망"

caption:
  EN: "The cement's coming off..."
  KR: "시멘트가 벗겨지고 있어..."
```

**Sora2 Prompt:**
```
1인칭 시점의 아마추어 핸드폰 영상. 흔들리지만 안정되어가는 푸티지.

미국 유타주 건설현장. 물 호스가 있는 세척 구역. 맑은 낮.

시멘트로 뒤덮인 큰뿔 올빼미. 날개 펼치면 1.2m, 몸길이 약 55cm. 크고 둥근 노란색 눈. 담요 위에 올려져 있다.

부드러운 물줄기가 올빼미의 깃털에 뿌려진다. 회색 시멘트가 씻겨 나가며 갈색과 회색의 본래 깃털 색이 드러난다. 올빼미가 눈을 깜빡이며 물을 맞는다. 특징적인 귀 깃털이 서서히 모습을 드러낸다.

No background music. 물 뿌리는 소리, 물방울 떨어지는 소리, 안도하는 숨소리, 올빼미가 몸을 터는 소리.
```

---

### Scene 7: 담요로 감쌈 (60-70초)
**Hook Type:** E1 - 신뢰의 순간

```yaml
variables:
  camera: "1인칭 POV"
  action: "따뜻한 담요로 감싸 안음"
  emotion: "따뜻함, 연결"

caption:
  EN: "You're safe now."
  KR: "이제 안전해."
```

**Sora2 Prompt:**
```
1인칭 시점의 아마추어 핸드폰 영상. 안정된 푸티지.

미국 유타주 건설현장. 트럭 그늘 아래. 맑은 낮.

대부분의 시멘트가 씻겨나간 큰뿔 올빼미. 날개 펼치면 1.2m, 몸길이 약 55cm. 크고 둥근 노란색 눈, 검은 동공. 갈색과 회색 깃털이 젖어있다. 특징적인 귀 깃털이 다시 서 있다. 아직 일부 시멘트 잔여물이 남아있다.

부드러운 담요로 올빼미를 감싼다. 올빼미가 저항하지 않고 담요 안에 안긴다. 큰 노란 눈이 천천히 감긴다. 완전한 이완. 신뢰의 순간.

No background music. 담요 스치는 소리, 부드러운 말소리, 올빼미의 편안한 숨소리.
```

---

### Scene 8: 야생동물센터 이송 (70-80초)
**Hook Type:** 전환

```yaml
variables:
  camera: "1인칭 POV → 시간 점프 텍스트"
  action: "차에 태워 센터로 이동"
  emotion: "희망, 기대"

caption:
  EN: "Hang in there, buddy."
  KR: "조금만 버텨, 친구."
```

**Sora2 Prompt:**
```
1인칭 시점의 아마추어 핸드폰 영상.

미국 유타주. 차량 내부. 낮.

담요에 싸인 큰뿔 올빼미. 날개 펼치면 1.2m, 몸길이 약 55cm. 크고 둥근 노란색 눈. 갈색과 회색 깃털. 젖은 깃털이 마르고 있다. 조수석에 조심히 놓여있다.

올빼미가 담요 안에서 카메라를 올려다본다. 큰 노란 눈이 카메라와 눈을 맞춘다. 신뢰하는 표정. 차가 출발하며 부드럽게 흔들린다.

화면 전환: "3 months later..." 텍스트.

No background music. 차 엔진 소리, 도로 위 타이어 소리, 부드러운 말소리.
```

---

### Scene 9: 3개월 후 - 완전 회복 (80-90초)
**Hook Type:** E2 - Time Skip + E4 - 감동 마무리

```yaml
variables:
  camera: "1인칭 POV, 야생동물센터"
  action: "건강하게 회복된 올빼미"
  emotion: "감동, 뿌듯함, 행복"

caption:
  EN: "Look at you now."
  KR: "지금 네 모습 좀 봐."
```

**Sora2 Prompt:**
```
1인칭 시점의 아마추어 핸드폰 영상. 안정된 푸티지.

미국 유타주 Best Friends Animal Sanctuary 야생동물 재활센터. 넓은 새장 안. 맑은 낮, 따뜻한 햇살.

완전히 회복된 큰뿔 올빼미. 날개 펼치면 1.2m, 몸길이 약 55cm의 건강한 모습. 크고 둥근 노란색 눈이 생기 있게 빛난다. 검은 동공. 깨끗하고 풍성한 갈색과 회색 깃털. 특징적인 귀 깃털이 우뚝 서 있다. 시멘트 흔적 전혀 없음.

올빼미가 횃대에 당당히 앉아있다. 카메라를 향해 고개를 천천히 돌린다. 큰 노란 눈으로 카메라를 똑바로 응시한다. 마치 "고마워"라고 말하는 듯한 눈빛. 천천히 눈을 깜빡인다.

No background music. 새소리, 바람 소리, 올빼미의 부드러운 울음소리, 감동하는 사람의 작은 웃음소리.
```

---

## 제목 옵션 (Titles)

### Main Title
```
The Cement Mixer Miracle
```

### Platform Variants

**YouTube Shorts:**
```
We Found an OWL Inside a CEMENT MIXER 🦉😱 #rescue #owl #construction
```

**TikTok:**
```
found something ALIVE in the cement mixer... 🦉💀
```

**Instagram Reels:**
```
This owl was covered in cement. 3 months later... 🦉✨
```

### Hooks

```yaml
emotional: "He was completely covered in cement. Then he opened his eyes."
curiosity: "We heard scratching inside the cement mixer..."
outcome: "From cement prison to freedom in 3 months 🦉"
```

---

## 기술 정보

```yaml
total_duration: 90초
scenes: 9개
camera_style:
  - scenes_1-4: "관찰자 시점 (제3자 촬영)"
  - scenes_5-9: "구조자 1인칭 POV"

aspect_ratio: "9:16 (vertical shorts)"
resolution: "1080x1920"

hooks:
  A_hook: "Scene 1-2 (0-20초) - 이상한 소리, 뭔가 있다"
  B_hook: "Scene 3 (20-30초) - 눈을 깜빡이는 시멘트 덩어리"
  C_hook: "Scene 4-5 (30-50초) - 긴급 구조"
  D_hook: "Scene 6-7 (50-70초) - 변화, 신뢰"
  E_hook: "Scene 8-9 (70-90초) - 3개월 후 감동"
```

---

## 참고 자료

- **원본 스토리:** [Utah Owl Rescue - KSL News](https://www.ksl.com/article/51213893/)
- **재활 센터:** Best Friends Animal Sanctuary, Kanab, Utah
- **올빼미 별명:** "Phelps" 또는 "Ledecky" (올림픽 수영선수 이름에서)
