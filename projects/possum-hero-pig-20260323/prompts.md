# A Tiny Pig Saved My Entire Flock From Two Coyotes

> 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움. 코요테 2마리가 양 떼를 노림하자 Possum이 양 전부를 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬. 귀 하나를 잃고 수십 군데 물렸지만 양 전부 구함. 수술 후 회복, 다시 양 몰이 복귀.

**총 길이:** 95초 (7개 프롬프트 — Scene 1,2,4,5,6: 15초 / Scene 3a,3b: 10초)

---

## 스토리 구조

```yaml
template_used:
  archetype: "underdog_hero + sacrifice_triumph"
  emotional_pattern: "buildup_to_hero_moment"

hook_formula: "일상 침입 (Ordinary Disruption)"
hook_description: "평화로운 농장에서 작은 돼지가 양들과 걸어다니는 귀여운 일상 → 갑자기 코요테 2마리 출현"

emotional_journey:
  - position: 0.0  → 따뜻함, 귀여움 (60)
  - position: 0.17 → 자랑스러움, 웃김 (65)
  - position: 0.33 → 공포, 긴장 (90)
  - position: 0.50 → 경외, 용기 (95)
  - position: 0.67 → 슬픔, 희망 (75)
  - position: 0.83 → 감동, 자랑스러움 (95)
```

---

## 캐릭터 레퍼런스

### Possum — 미니 돼지 (Potbelly Pig)

> 수컷 미니 포트벨리 돼지 "Possum". 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 짧은 다리. 둥근 주둥이. 작은 분홍빛 눈. 뾰족한 귀 2개 (Scene 5-6에서는 왼쪽 귀 없음). 양 떼보다 훨씬 작지만 당당하게 앞장서서 걸어다님.

### 양 떼 (Sheep Flock)

> 하얀 양 8-10마리. 다양한 크기. 하얀 울 털. Possum을 따라다니며 신뢰함.

### 코요테 2마리 (Coyotes)

> 코요테(Coyote) 2마리. 회색-갈색 거친 털. 각 약 15-18kg. 날카로운 노란 눈. 뾰족한 주둥이. 야위고 날렵한 체형. Possum과 비슷한 체급이지만 이빨과 발톱이 있음.

### 촬영자/농장주 (1인칭 POV)

> 30대 초반 백인 여성. 긴 갈색 머리 포니테일. Scene 1-4: 카키색 작업 조끼, 청바지, 작업 부츠. Scene 5: 회색 스웻셔츠. Scene 6: 카키색 작업 조끼, 청바지. 한 손에 핸드폰, 소매와 손이 화면에 보임.

모든 프롬프트에서 이 캐릭터 설명을 일관되게 사용합니다.

---

## Scene 1: 꼬마 돼지와 양 떼 (The Little Pig and His Flock)

- **Duration:** 15s
- **Emotion:** 따뜻함, 귀여움
- **Camera:** 1인칭 POV 핸드폰
- **Lighting:** 아침, 따뜻한 자연광

**Caption:**

- EN: "Nobody wanted this runt pig
  Possum became the sheriff of the farm"
- KR: "아무도 원하지 않던 꼬마 돼지
  Possum이 농장의 보안관이 되었다"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: 없음 (첫 장면).
이 장면: 도입 — 아침 농장. 작은 미니 돼지 Possum이 양 떼 사이에서 당당하게 걸어다님. 양들이 Possum을 따라감.

1인칭 POV 핸드폰 영상. 한 손 촬영. 흔들리고 불안정한 아마추어 푸티지.

미국 미주리 농장. 목초지 언덕. 아침. 맑음. 따뜻한 자연광. 나무 울타리. 초록 풀밭.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 짧은 다리. 둥근 주둥이. 작은 분홍빛 눈. 뾰족한 귀 2개. 양 떼보다 훨씬 작지만 앞장서서 걸어감.

하얀 양 8-10마리. Possum 뒤를 따라감.

30대 초반 백인 여성의 손. 카키색 작업 조끼 소매 보임. (1인칭 POV 촬영자)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 아침 목초지. 초록 언덕. 작은 하얀 돼지 Possum이 양 떼 맨 앞에서 당당하게 걸어감. 양 8마리가 뒤를 줄지어 따라감. 크기 대비가 웃김. 여자 웃음소리.
— 자연스러운 화면 전환 —
(5-10초) Possum이 멈추면 양들도 멈춤. Possum이 다시 걸으면 양들도 따라감. 돼지가 목초지를 가로질러 양들을 이끌고 감.
— 자연스러운 화면 전환 —
(10-15초) 클로즈업. Possum이 풀을 뜯다가 카메라를 올려다봄. 둥근 주둥이. 작은 분홍빛 눈. 옆에 양 한 마리가 Possum 옆에 누워 있음. 여자 조용한 웃음.

No background music. 새소리, 풀 밟는 소리, 양 울음소리, Possum 코 킁킁 소리, 여자 웃음소리.
```

---

## Scene 2: 양치기 돼지 (The Pig Who Herds Sheep)

- **Duration:** 15s
- **Emotion:** 자랑스러움, 웃김, 놀라움
- **Camera:** 1인칭 POV 핸드폰
- **Lighting:** 낮, 자연광

**Caption:**

- EN: "Possum learned to herd on his own
  The sheep followed him everywhere"
- KR: "Possum이 혼자 양 몰이를 배웠다
  양들은 어디든 따라갔다"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: 아침 목초지에서 작은 돼지 Possum이 양 떼 앞에서 당당하게 걸어다녔다. 양들이 Possum을 따랐다.
이 장면: 전개 — Possum이 양 떼를 목초지에서 축사 방향으로 몰고 감. 양 뒤를 뛰어다니며 방향을 잡아줌. 작은 돼지가 양치기 역할을 함.

1인칭 POV 핸드폰 영상. 한 손 촬영. 흔들리고 불안정한 아마추어 푸티지.

미국 미주리 농장. 목초지 → 축사. 낮. 자연광.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 짧은 다리. 둥근 주둥이. 양 떼 뒤를 뛰어다니며 양 몰이.

하얀 양 8-10마리. Possum의 지시에 따라 움직임.

30대 초반 백인 여성의 손. 카키색 작업 조끼 소매 보임. (1인칭 POV 촬영자)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 목초지. Possum이 양 떼 뒤를 짧은 다리로 뛰어다님. 양 한 마리가 다른 방향으로 가자 Possum이 쫓아가서 밀어 돌려놓음.
— 자연스러운 화면 전환 —
(5-10초) 양 떼가 축사 방향으로 이동. Possum이 맨 뒤에서 왔다갔다 하며 방향을 잡아줌. 짧은 다리로 열심히 뛰는 모습.
— 자연스러운 화면 전환 —
(10-15초) 양 떼가 축사 안으로 들어감. Possum이 축사 입구에 서서 마지막 양이 들어가는 걸 확인하고 만족스럽게 코를 킁킁거림. 여자 놀란 웃음소리.

No background music. 양 울음소리, Possum 달리는 발소리, 풀 밟는 소리, 여자 웃음소리.
```

---

## Scene 3a: 침입자 (The Intruders)

- **Duration:** 10s
- **Emotion:** 공포, 긴장
- **Camera:** 1인칭 POV 핸드폰 (멀리서 촬영)
- **Lighting:** 오후, 흐린 하늘

**Caption:**

- EN: "Two coyotes came from the treeline
  Possum pushed every sheep uphill"
- KR: "코요테 두 마리가 숲에서 나타났다
  Possum이 모든 양을 언덕 위로 밀어 올렸다"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: Possum이 양 떼를 능숙하게 목초지에서 축사로 몰아넣었다. 완벽한 양치기였다.
이 장면: 위기 시작 — 오후. 숲 가장자리에서 코요테 2마리가 나타남. 양들이 패닉. Possum이 양들을 언덕 위로 몰아감.

1인칭 POV 핸드폰 영상. 한 손 촬영. 흔들리고 불안정한 아마추어 푸티지. 멀리서 촬영.

미국 미주리 농장. 목초지 언덕. 오후. 흐린 하늘.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 양들 사이를 미친듯이 뛰어다님.

하얀 양 8-10마리. 패닉 상태. 흩어지려는 양들.

코요테 2마리. 회색-갈색 거친 털. 날카로운 노란 눈. 야위고 날렵한 체형. 숲 가장자리에서 목초지로 나옴.

30대 초반 백인 여성의 손. 카키색 작업 조끼 소매 보임. (1인칭 POV 촬영자 — 집 현관에서 멀리 촬영)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 목초지. 멀리서 촬영. 숲 가장자리에서 코요테 2마리가 천천히 목초지로 나옴. 양들이 흩어지며 패닉. 카메라 흔들림. 여자 놀란 소리.
— 자연스러운 화면 전환 —
(5-10초) 작은 Possum이 흩어지는 양들 사이를 미친듯이 뛰어다니며 양들을 언덕 위로 몰아감. 짧은 다리로 전속력. 양 떼가 언덕을 올라가기 시작.

No background music. 양 울음소리, 코요테 으르렁 소리, Possum 달리는 소리, 여자 놀란 소리, 바람소리.
```

---

## Scene 3b: 첫 번째 충돌 (First Clash)

- **Duration:** 10s
- **Emotion:** 긴장, 용기
- **Camera:** 1인칭 POV 핸드폰 (멀리서 촬영)
- **Lighting:** 오후, 흐린 하늘

**Caption:**

- EN: "A coyote charged at the sheep
  Possum threw himself in the way"
- KR: "코요테가 양을 향해 달려왔다
  Possum이 몸을 던졌다"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: 코요테 2마리가 숲에서 나타났다. Possum이 양들을 언덕 위로 몰아가는 중이다.
이 장면: 첫 충돌 — 코요테 한 마리가 양을 향해 달려오자 Possum이 사이에 뛰어들어 막아섬. 머리로 코요테를 들이받아 밀어냄. 양 떼가 언덕 꼭대기로 올라감.

1인칭 POV 핸드폰 영상. 한 손 촬영. 흔들리고 불안정한 아마추어 푸티지. 멀리서 촬영.

미국 미주리 농장. 목초지 언덕 중간. 오후. 흐린 하늘.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 코요테와 양 사이에 뛰어듦.

하얀 양 8-10마리. 언덕을 올라가는 중.

코요테 2마리. 회색-갈색 거친 털. 날카로운 노란 눈. 한 마리가 양을 향해 달려옴.

30대 초반 백인 여성의 손. 카키색 작업 조끼 소매 보임. (1인칭 POV 촬영자 — 멀리서 촬영)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 코요테 한 마리가 양 한 마리를 향해 전속력으로 달려옴. Possum이 사이에 뛰어들어 몸으로 막아섬. 코요테가 멈칫.
— 자연스러운 화면 전환 —
(5-10초) Possum이 코요테를 향해 돌진하며 머리로 들이받음. 코요테가 뒤로 밀려남. 그 틈에 양 떼가 언덕 꼭대기로 올라감. 두 번째 코요테가 옆에서 다가옴. 여자가 소리를 지름.

No background music. 코요테 으르렁 소리, Possum 돌진 소리, 몸이 부딪치는 소리, 양 울음소리, 여자 소리지르는 소리.
```

---

## Scene 4: 사투 (The Fight)

- **Duration:** 15s
- **Emotion:** 경외, 용기, 긴장
- **Camera:** 1인칭 POV 핸드폰 (멀리서 촬영)
- **Lighting:** 오후, 흐린 하늘

**Caption:**

- EN: "Possum turned around and charged
  They bit him dozens of times
  Possum never backed down"
- KR: "Possum이 돌아서서 돌진했다
  수십 번을 물렸다
  Possum은 한 발짝도 물러나지 않았다"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: Possum이 코요테를 들이받아 밀어내고 양 떼를 언덕 꼭대기로 피신시켰다. 두 번째 코요테가 다가오고 있다.
이 장면: 사투 — Possum이 돌아서서 코요테 2마리를 향해 돌진. 머리로 들이받고, 물리고, 밀어붙이고, 결국 코요테를 퇴각시킴. Possum이 비틀거리며 서 있음.

1인칭 POV 핸드폰 영상. 한 손 촬영. 흔들리고 불안정한 아마추어 푸티지. 멀리서 촬영.

미국 미주리 농장. 목초지 언덕. 오후. 흐린 하늘.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 코요테에 맞서 싸움. 몸에 상처.

코요테 2마리. 회색-갈색 거친 털. 날카로운 노란 눈. 야위고 날렵한 체형.

30대 초반 백인 여성의 손. 카키색 작업 조끼 소매 보임. (1인칭 POV 촬영자 — 멀리서 촬영)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 언덕 꼭대기. Possum이 양 떼를 등지고 돌아선다. 짧은 다리로 언덕 아래 코요테를 향해 전속력 돌진. 작은 하얀 몸이 달려감. 첫 번째 코요테에 정면으로 머리를 박아 들이받음. 코요테가 옆으로 밀려남. 여자가 울면서 소리를 지름.
— 자연스러운 화면 전환 —
(5-10초) 두 번째 코요테가 Possum 옆구리를 물어 끌어당김. Possum이 몸을 비틀며 버팀. 흙먼지가 일어남. Possum이 물린 채로 코요테에 맞서 밀어붙임. 뒹굴며 격렬하게 싸움.
— 자연스러운 화면 전환 —
(10-15초) 코요테 2마리가 결국 뒤로 물러나 숲 방향으로 도망감. Possum이 비틀거리며 혼자 서 있음. 몸에 상처. 언덕 위에서 양들이 내려다봄. 카메라 심하게 흔들림. 여자 울음소리.

No background music. Possum 돌진 소리, 머리 부딪치는 소리, 코요테 으르렁 소리, 몸이 부딪치고 구르는 소리, Possum 거친 숨소리, 코요테 도망가는 발소리, 여자 울면서 소리지르는 소리.
```

---

## Scene 5: 대가 (The Price)

- **Duration:** 15s
- **Emotion:** 슬픔, 희망, 안도
- **Camera:** 1인칭 POV 핸드폰
- **Lighting:** 실내 조명

**Caption:**

- EN: "Possum kept fighting even as they tore him apart
  Every single sheep survived"
- KR: "Possum은 온몸이 찢겨도 싸움을 멈추지 않았다
  양은 전부 살았다"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: Possum이 코요테 2마리를 향해 혼자 돌진해 맞섰다.
이 장면: 대가 — 동물병원. 붕대를 감은 Possum. 왼쪽 귀가 없음. 수십 군데 상처. 하지만 양은 한 마리도 다치지 않음. 농장주가 옆에서 Possum을 쓰다듬으며 돌봄.

1인칭 POV 핸드폰 영상. 한 손 촬영. 흔들리고 불안정한 아마추어 푸티지.

동물병원 진료실. 실내 조명.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 몸 여러 곳에 붕대와 반창고. 왼쪽 귀가 없음 (수술로 제거). 피곤하지만 눈을 뜨고 있음.

30대 초반 백인 여성. 긴 갈색 머리 포니테일. 회색 스웻셔츠. 눈이 붉고 울었던 흔적. Possum 옆에 앉아 쓰다듬음. (1인칭 POV 촬영자 — 한 손으로 촬영하며 다른 손으로 Possum 쓰다듬음)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 동물병원 진료대. Possum이 옆으로 누워 있다. 몸에 붕대 여러 개. 왼쪽 귀가 없는 자리에 수술 흔적. 피곤한 눈.
— 자연스러운 화면 전환 —
(5-10초) 여자의 손이 Possum의 머리를 조심스럽게 쓰다듬음. Possum이 눈을 감고 여자 손에 주둥이를 기댐. 여자의 떨리는 숨소리.
— 자연스러운 화면 전환 —
(10-15초) Possum이 천천히 눈을 뜨고 여자를 올려다봄. 작은 분홍빛 눈. 꼬리가 아주 약하게 흔들림. 여자 울먹이는 웃음소리.

No background music. 병원 장비 소리, Possum 숨소리, 여자 떨리는 숨소리, 여자 울먹이는 웃음.
```

---

## Scene 6: 영웅의 귀환 (The Hero Returns)

- **Duration:** 15s
- **Emotion:** 감동, 자랑스러움, 사랑
- **Camera:** 홈비디오 / 1인칭 POV
- **Lighting:** 아침, 따뜻한 황금빛 자연광

**Caption:**

- EN: "Possum is back on the hill
  One ear short, twice the hero"
- KR: "Possum이 다시 언덕에 섰다
  귀 하나가 없지만 영웅은 두 배"

### Sora2 Prompt

```
// Story: 전체: 농장에서 버려진 미니 돼지 Possum이 양 몰이를 배움 → 코요테 2마리가 양 떼를 노림 → Possum이 양을 언덕 위로 피신시키고 혼자 돌아가 코요테에 맞섬 → 귀 하나를 잃지만 양 전부 구함 → 수술 후 회복 → 양 몰이 복귀.
앞 장면: 동물병원에서 붕대를 감은 Possum. 왼쪽 귀를 잃었지만 눈을 뜨고 꼬리를 약하게 흔들었다.
이 장면: 결말 — 몇 주 후. 회복한 Possum이 다시 목초지에 섬. 왼쪽 귀가 없는 모습. 양 떼가 Possum 주위에 모여듦. 다시 양 몰이를 시작. 언덕 위에서 양 떼를 이끄는 Possum.

홈비디오 스타일 핸드폰 영상. 한 손 촬영. 자연 조명.

미국 미주리 농장. 목초지 언덕. 아침. 따뜻한 황금빛 자연광.

수컷 미니 포트벨리 돼지 "Possum" 한 마리. 약 15kg. 순백색 짧은 털. 분홍색 피부가 살짝 비침. 짧은 다리. 둥근 주둥이. 왼쪽 귀가 없음. 오른쪽 귀만 뾰족하게 서 있음. 상처가 아물어 흉터. 건강하고 활발. 당당하게 걸어감.

하얀 양 8-10마리. Possum 주위에 모여들고, 뒤를 따라감.

30대 초반 백인 여성의 조용한 웃음소리. 카키색 작업 조끼 소매 보임. (1인칭 POV 촬영자)

(0-1초) 참조 이미지 프레임.
— 1초에 빠른 화면 전환 —
(1-5초) 목초지. 아침 햇빛. Possum이 축사에서 나와 목초지를 향해 걸어감. 왼쪽 귀가 없는 실루엣. 양 떼가 축사에서 하나둘 따라 나옴.
— 자연스러운 화면 전환 —
(5-10초) 양들이 Possum 주위로 모여듦. 한 마리가 Possum에게 코를 대고 킁킁거림. Possum이 앞장서서 언덕을 올라감. 양들이 줄지어 따라감.
— 자연스러운 화면 전환 —
(10-15초) 언덕 꼭대기. Possum이 양 떼 맨 앞에 서 있다. 왼쪽 귀가 없는 작은 하얀 돼지. 뒤로 하얀 양 떼. 아침 햇빛. 여자의 조용한 웃음소리.

No background music. 새소리, 풀 밟는 소리, 양 울음소리, Possum 발소리, 여자 조용한 웃음.
```

---

## 제목 (Titles)

```json
{
  "main_title": "A Tiny Pig Named Possum Saved My Entire Flock From Two Coyotes... Lost an Ear but Not a Single Sheep",
  "subtitle": "The smallest hero on the farm",
  "platform_variants": {
    "youtube_shorts": "🐷 My Tiny Pig Possum Fought Two Coyotes to Save His Sheep... Lost an Ear (Wait for His Return)",
    "instagram_reels": "A runt pig nobody wanted learned to herd sheep. When two coyotes attacked, he saved every single one 🐷🐑",
    "tiktok": "My tiny pig fought two coyotes to save his sheep... he lost an ear but saved them all 😭"
  },
  "hooks": {
    "emotional": "Possum turned around and ran straight at two coyotes... alone... to save his sheep 😭",
    "curiosity": "A runt pig nobody wanted learned to herd sheep on his own... then two coyotes came from the treeline",
    "outcome": "A tiny pig fought two coyotes alone to save his flock... lost an ear, saved every sheep, and went back to herding"
  }
}
```

---

## 자막 요약 (Captions Summary)

| Scene | EN | KR | Type |
| ----- | -- | -- | ---- |
| 1 | Nobody wanted this runt pig / Possum became the sheriff of the farm | 아무도 원하지 않던 꼬마 돼지 / Possum이 농장의 보안관이 되었다 | 반전형 |
| 2 | Possum learned to herd on his own / The sheep followed him everywhere | Possum이 혼자 양 몰이를 배웠다 / 양들은 어디든 따라갔다 | 반전형 |
| 3a | Two coyotes came from the treeline / Possum pushed every sheep uphill | 코요테 두 마리가 숲에서 나타났다 / Possum이 모든 양을 언덕 위로 밀어 올렸다 | 긴장형 |
| 3b | A coyote charged at the sheep / Possum threw himself in the way | 코요테가 양을 향해 달려왔다 / Possum이 몸을 던졌다 | 반전형 |
| 4 | Possum turned around and charged / They bit him dozens of times / Possum never backed down | Possum이 돌아서서 돌진했다 / 수십 번을 물렸다 / Possum은 한 발짝도 물러나지 않았다 | 대비형 |
| 5 | Possum kept fighting even as they tore him apart / Every single sheep survived | Possum은 온몸이 찢겨도 싸움을 멈추지 않았다 / 양은 전부 살았다 | 대비형 |
| 6 | Possum is back on the hill / One ear short, twice the hero | Possum이 다시 언덕에 섰다 / 귀 하나가 없지만 영웅은 두 배 | 반전형 |

---

*Generated by Animal Shorts Agent System*
