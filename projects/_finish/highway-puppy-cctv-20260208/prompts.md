# The Car That Stopped

> 미국 펜실베이니아주 고속도로 CCTV 영상. 남자가 골든 리트리버 강아지를 갓길에 내려놓고 차를 몰고 떠난다. 강아지가 차를 쫓아 도로로 뛰어들지만 차들 사이에서 오도가도 못한다. 반대편에서 한 여자가 도로를 건너 강아지를 안아 올린다. 이후 다양한 CCTV 영상 속에서 둘의 행복한 일상이 펼쳐진다 — 해변 산책, 터그놀이, 고양이 친구, 그리고 사랑.

**총 길이:** 90초 (6개 장면)

---

## 캐릭터 레퍼런스

### Puppy (강아지)

> 골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털, 약간 웨이브. 큰 갈색 눈. 큰 발. 접힌 귀. 빨간 목줄.

### Man (남자 - 유기자)

> 30대 남자. 어두운 후디. 청바지. 검은 SUV.

### Woman (여자 - 구조자)

> 20대 후반 여자. 갈색 포니테일. 회색 후디. 청바지. 흰색 세단.

### Cat (고양이)

> 회색 줄무늬 고양이. 녹색 눈.

### Location (장소)

> 미국 펜실베이니아주 필라델피아 교외 편도 3차선 고속도로 → 여자의 미국식 주택 / 해변

---

## Scene 1: 도로 한가운데 (Frozen in Traffic)

- **Duration:** 15s
- **is_hook:** true
- **Emotion:** 충격, 공포, 긴장
- **Camera:** 고속도로 CCTV 고정 앵글, 높은 위치
- **Lighting:** 낮, 흐린 하늘, 회색 아스팔트

**Caption:**

- EN: "A golden retriever puppy... in the middle of a highway"
- KR: "골든 리트리버 강아지가... 고속도로 한가운데에"

### Sora2 Prompt

```
고속도로 CCTV 감시 카메라 영상. 높은 위치에서 내려다보는 고정 앵글. 와이드. 약간 거친 화질.

미국 펜실베이니아주 필라델피아 교외 편도 3차선 고속도로. 낮. 흐린 하늘. 차들이 양방향으로 달리고 있다.

골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털, 약간 웨이브. 큰 갈색 눈. 큰 발. 접힌 귀. 빨간 목줄.

(0-3초) 와이드 고정. 고속도로 전체. 차들이 빠르게 지나간다. 도로 중앙에 금색 형체.
(3-7초) 같은 앵글. 골든 리트리버 강아지가 도로 중앙에서 왔다갔다 움직인다. 차들이 클랙슨을 울리며 비켜간다.
(7-11초) 같은 앵글. 강아지가 멈춰 서서 움직이지 못한다. 양쪽으로 차들이 지나간다.
(11-15초) 같은 앵글. 강아지가 몸을 낮추고 도로에 납작 엎드린다. 차들이 계속 지나간다.

No background music. 멀리서 들리는 차 소리, 클랙슨, 타이어 소리, 바람 소리.
```

**end_frame:** 고속도로 CCTV 앵글. 도로 중앙에 납작 엎드린 골든 리트리버 강아지. 금색 털. 양쪽으로 차들이 지나감.

---

## Scene 2: 갓길의 SUV (The Drop-Off)

- **Duration:** 15s
- **is_hook:** false
- **Emotion:** 분노, 충격
- **Camera:** 고속도로 CCTV 고정 앵글
- **Lighting:** 낮, 흐린 하늘

**Caption:**

- EN: "Minutes earlier... caught on camera"
- KR: "몇 분 전... 카메라에 잡혔다"

**start_frame_ref:** Scene 1 end_frame (도로 중앙에 엎드린 골든 리트리버 강아지)

### Sora2 Prompt

```
(스타트 프레임: 고속도로 CCTV, 도로 중앙에 엎드린 골든 리트리버 강아지, 차들이 지나감) 에서 시작. 빠르게 전환. 몇 분 전 장면.

고속도로 CCTV 감시 카메라 영상. 높은 위치에서 내려다보는 고정 앵글. 와이드. 약간 거친 화질.

미국 펜실베이니아주 필라델피아 교외 편도 3차선 고속도로 갓길. 낮. 흐린 하늘.

골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털, 약간 웨이브. 큰 갈색 눈. 큰 발. 접힌 귀. 빨간 목줄.

30대 남자. 어두운 후디. 청바지. 검은 SUV.

(0-1초) 전 씬에서 빠르게 전환.
(1-5초) 와이드 고정. 검은 SUV가 갓길에 멈춰있다. 남자가 운전석에서 내린다.
(5-9초) 같은 앵글. 남자가 뒷좌석 문을 열고 골든 리트리버 강아지를 갓길에 내려놓는다.
(9-12초) 같은 앵글. 남자가 빠르게 차에 타고 문을 닫는다.
(12-15초) 같은 앵글. SUV가 출발한다. 골든 리트리버 강아지가 갓길에 서서 차를 바라본다.

No background music. 차 엔진 소리, 문 닫히는 소리, 고속도로 차량 소음.
```

**end_frame:** CCTV 앵글. 갓길에 혼자 서있는 골든 리트리버 강아지. 금색 털. SUV가 멀어지고 있다.

---

## Scene 3: 쫓아가는 강아지 (The Chase)

- **Duration:** 15s
- **is_hook:** false
- **Emotion:** 절박함, 공포, 긴장
- **Camera:** 고속도로 CCTV 고정 앵글 (다른 카메라)
- **Lighting:** 낮, 흐린 하늘

**Caption:**

- EN: "He ran after the car... into traffic"
- KR: "차를 쫓아 달렸다... 도로 한가운데로"

**start_frame_ref:** Scene 2 end_frame (갓길에 혼자 서있는 골든 리트리버 강아지)

### Sora2 Prompt

```
(스타트 프레임: CCTV 앵글, 갓길에 혼자 서있는 골든 리트리버 강아지, SUV가 멀어짐) 에서 시작. 빠르게 전환.

고속도로 CCTV 감시 카메라 영상. 높은 위치에서 내려다보는 고정 앵글. 와이드. 약간 거친 화질.

미국 펜실베이니아주 필라델피아 교외 편도 3차선 고속도로. 낮. 흐린 하늘. 차들이 양방향으로 달린다.

골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털, 약간 웨이브. 큰 갈색 눈. 큰 발. 접힌 귀. 빨간 목줄.

(0-1초) 전 씬에서 빠르게 전환.
(1-5초) 와이드 고정. 골든 리트리버 강아지가 갓길에서 도로쪽으로 뛰기 시작한다. SUV를 쫓아간다.
(5-9초) 같은 앵글. 강아지가 1차선을 가로질러 달린다. 차 한 대가 급하게 피한다.
(9-12초) 같은 앵글. 강아지가 도로 중앙에서 멈춘다. 양쪽에서 차들이 지나간다.
(12-15초) 같은 앵글. 강아지가 이리저리 움직이다 결국 몸을 낮추고 멈춘다.

No background music. 차 소리, 급브레이크 소리, 클랙슨, 타이어 소리.
```

**end_frame:** CCTV 앵글. 도로 중앙에 몸을 낮추고 멈춘 골든 리트리버 강아지. 금색 털. 차들이 양쪽으로 지나감.

---

## Scene 4: 도로를 건너는 여자 (The Crossing)

- **Duration:** 15s
- **is_hook:** false
- **Emotion:** 긴장, 안도, 따뜻함
- **Camera:** 고속도로 CCTV 고정 앵글
- **Lighting:** 낮, 흐린 하늘

**Caption:**

- EN: "Then one car stopped"
- KR: "그때 한 대가 멈췄다"

**start_frame_ref:** Scene 3 end_frame (도로 중앙에 엎드린 골든 리트리버 강아지)

### Sora2 Prompt

```
(스타트 프레임: CCTV 앵글, 도로 중앙에 엎드린 골든 리트리버 강아지, 차들이 양쪽으로 지나감) 에서 시작.

고속도로 CCTV 감시 카메라 영상. 높은 위치에서 내려다보는 고정 앵글. 와이드. 약간 거친 화질.

미국 펜실베이니아주 필라델피아 교외 편도 3차선 고속도로. 낮. 흐린 하늘.

골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털, 약간 웨이브. 큰 갈색 눈. 큰 발. 접힌 귀. 빨간 목줄.

20대 후반 여자. 갈색 포니테일. 회색 후디. 청바지. 흰색 세단.

(0-1초) 전 씬에서 이어짐.
(1-5초) 와이드 고정. 반대편 갓길에 흰색 세단이 비상등을 켜고 멈춘다. 여자가 내린다.
(5-9초) 같은 앵글. 여자가 차들 사이를 가로질러 도로 중앙으로 다가간다.
(9-12초) 같은 앵글. 여자가 골든 리트리버 강아지 앞에 쪼그려 앉아 안아 올린다.
(12-15초) 같은 앵글. 여자가 강아지를 안고 도로를 건너 자기 차로 돌아간다.

No background music. 차 소리, 비상등 틱틱 소리, 차량 소음, 바람 소리.
```

**end_frame:** CCTV 앵글. 여자가 골든 리트리버 강아지를 안고 흰색 세단으로 돌아가는 모습. 비상등이 깜빡임.

---

## Scene 5: 새로운 세상 (A New World)

- **Duration:** 15s
- **is_hook:** false
- **Emotion:** 기쁨, 자유, 치유
- **Camera:** 다양한 CCTV/보안카메라 몽타주
- **Lighting:** 밝은 햇살, 따뜻한 톤

**Caption:**

- EN: "She gave him a world bigger than a highway"
- KR: "그녀는 고속도로보다 넓은 세상을 줬다"

**start_frame_ref:** Scene 4 end_frame (여자가 골든 리트리버 강아지를 안고 세단으로 돌아감)

### Sora2 Prompt

```
(스타트 프레임: CCTV 앵글, 여자가 골든 리트리버 강아지를 안고 흰색 세단으로 돌아감, 비상등) 에서 시작. 빠르게 전환. 몇 주 후.

여러 CCTV/보안 카메라 영상을 편집한 몽타주. 고정 앵글. 와이드. 따뜻한 톤.

미국 펜실베이니아주 해변 / 공원 산책로. 낮. 맑은 하늘. 햇살.

골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털에 윤기, 약간 웨이브. 큰 갈색 눈. 큰 발. 접힌 귀. 새 파란색 하네스. 건강해진 모습.

20대 후반 여자. 갈색 포니테일. 캐주얼한 복장.

(0-1초) 전 씬에서 빠르게 전환.
(1-5초) 해변 보안 카메라 고정 와이드. 여자와 골든 리트리버 강아지가 해변을 걷는다. 강아지가 파도를 쫓아다닌다.
(5-9초) 공원 CCTV 고정 와이드. 여자가 공원 잔디밭에서 골든 리트리버 강아지와 달린다.
(9-12초) 주차장 카메라 고정 와이드. 여자가 차 뒷문을 열자 골든 리트리버 강아지가 뛰어 올라탄다.
(12-15초) 도어벨 카메라 와이드. 여자와 골든 리트리버 강아지가 현관문으로 들어간다. 강아지 꼬리가 흔들린다.

No background music. 파도 소리, 강아지 발소리, 새소리, 바람, 여자 웃음소리.
```

**end_frame:** 도어벨 카메라 앵글. 여자와 골든 리트리버 강아지가 현관문 안으로 들어가는 뒷모습. 금색 꼬리가 흔들린다.

---

## Scene 6: 우리 집 (Home)

- **Duration:** 15s
- **is_hook:** false
- **Emotion:** 사랑, 행복, 완전함
- **Camera:** 실내 홈캠/보안카메라 고정 앵글
- **Lighting:** 따뜻한 실내 조명

**Caption:**

- EN: "He was thrown away for getting car sick. Now he has a home."
- KR: "차멀미 때문에 버려졌다. 이제 그에게 집이 생겼다."

**start_frame_ref:** Scene 5 end_frame (현관문으로 들어가는 뒷모습)

### Sora2 Prompt

```
(스타트 프레임: 도어벨 카메라, 여자와 골든 리트리버 강아지가 현관문 안으로 들어감) 에서 시작. 빠르게 전환.

실내 홈캠/보안 카메라 영상을 편집한 몽타주. 천장 코너에서 내려다보는 고정 앵글. 와이드. 따뜻한 톤.

미국 펜실베이니아주 여자의 집 거실. 따뜻한 실내 조명. 소파. 카펫. 장난감.

골든 리트리버 강아지 한 마리. 약 13kg, 생후 8-10개월. 중간 길이 금색 털에 윤기, 약간 웨이브. 큰 갈색 눈. 건강한 모습.

회색 줄무늬 고양이. 녹색 눈.

20대 후반 여자. 갈색 포니테일. 편한 실내복.

(0-1초) 전 씬에서 빠르게 전환.
(1-5초) 홈캠 고정 와이드. 거실. 여자가 터그 장난감을 잡고 골든 리트리버 강아지와 터그놀이를 한다.
(5-9초) 같은 앵글. 회색 줄무늬 고양이가 다가와 골든 리트리버 강아지 옆에 눕는다. 강아지가 고양이 얼굴을 핥는다.
(9-12초) 같은 앵글. 여자가 소파에 앉아있고 골든 리트리버 강아지가 무릎 위에 올라와 눕는다. 고양이가 옆에.
(12-15초) 같은 앵글. 여자가 강아지를 안고 있다. 골든 리트리버 강아지가 눈을 감는다. 고양이가 옆에서 잠.

No background music. 강아지 숨소리, 고양이 그르릉, 장난감 소리, 여자 웃음소리.
```

**end_frame:** 홈캠 앵글. 소파 위에서 여자, 골든 리트리버 강아지, 고양이가 함께. 강아지가 눈을 감고 여자에게 기대있음.

---

## 제목 옵션

- **YouTube Shorts:** 💔 Man Dumps Golden Retriever Puppy on Highway... CCTV Caught What Happened Next (True Story)
- **Instagram Reels:** CCTV caught the moment a man abandoned his golden retriever on a highway... then one car stopped 🐾
- **TikTok:** he dumped his golden retriever puppy on a highway because it got car sick... caught on camera 😭

### Hooks

- **Emotional:** 💔 CCTV Caught a Man Dumping His Golden Retriever Puppy on a Busy Highway...
- **Curiosity:** A Golden Retriever Puppy Was Stuck in the Middle of a Highway... Then One Car Stopped
- **Outcome:** Golden Retriever Dumped on a Highway for Getting Car Sick → Watch What Happened Next 😭

### Hashtags

#goldenretriever #puppy #abandoned #rescue #highway #cctv #caughtoncamera #dogrescue #adoptdontshop #animalrescue #goldenretrieverpuppy #fyp #emotional #truestory
