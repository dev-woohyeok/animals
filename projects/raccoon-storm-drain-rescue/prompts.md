# Only Her Face Above Water

> 폭우 속 물이 가득 찬 하수구에서 얼굴만 간신히 내밀고 버티는 라쿤. 지나가던 남자가 발견하고 시간과 싸우며 구조에 나선다.

**총 길이:** 90초 (8개 장면)

---

## 캐릭터 레퍼런스

모든 장면에서 동일하게 사용:

```
라쿤: 중간 크기 성체 라쿤, 회갈색 털, 얼굴에 검은 마스크 무늬, 검은 줄무늬 꼬리, 작고 검은 손 같은 앞발, 크고 둥근 검은 눈
구조자: 30대 백인 남자 (1인칭 시점 - 손/팔만 등장), 회색 후드티 소매
```

---

## 배경 레퍼런스

```yaml
setting_reference:
  country: "United States"
  location: "Washington State, Seattle suburbs"
  outdoor: "suburban neighborhood, asphalt roads, storm drains with metal grates, streetlights"
  weather: "heavy rainstorm at night → sunny morning next day"
  time_span: "rescue night → release next morning"
```

---

## 하수구 레퍼런스

모든 하수구 장면에서 동일하게 사용:

```
도로변 하수구 (storm drain): 도로 가장자리 콘크리트 연석(curb) 바로 옆에 위치한 직사각형 하수구.
가로 60cm, 세로 30cm 크기. 회색 콘크리트 프레임.
위에 검은색 금속 철망 그레이트(metal grate)가 덮여 있음.
그레이트는 긴 직사각형 슬롯이 가로로 7-8줄 나란히 있는 형태.
슬롯 사이 간격은 손가락이 들어갈 정도로 좁음.
그레이트 가장자리에 녹이 약간 슬어있음.
하수구 내부는 깊이 약 1미터, 콘크리트 벽면, 물이 가득 차 있음.
```

---

## Scene 1: 물속의 눈

- **Duration:** 12s
- **Emotion:** 충격, 긴박함
- **Camera:** handheld POV, phone flashlight pointing down, slow push in

**Caption:**

- EN: "A raccoon... trapped in a flooded storm drain"
- KR: "폭우 속 하수구에 갇힌 라쿤..."

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 핸드폰 라이트로 하수구 안을 비추는 장면. 흔들리고 불안정한 아마추어 촬영. 미국 워싱턴주 시애틀 교외. 밤. 폭우가 억수같이 쏟아진다.

도로 가장자리 콘크리트 연석 옆 직사각형 하수구. 가로 60cm 세로 30cm 크기, 회색 콘크리트 프레임, 위에 검은색 금속 철망 그레이트가 덮여 있음. 그레이트는 긴 직사각형 슬롯이 가로로 7-8줄 나란히 있는 형태. 슬롯 사이 간격은 손가락이 들어갈 정도로 좁음. 그레이트 가장자리에 녹이 약간 슬어있음. 빗물이 그레이트 슬롯 사이로 콸콸 쏟아져 들어간다.

핸드폰 라이트가 그레이트 슬롯 사이로 안을 비춘다. 하수구 내부는 깊이 약 1미터, 콘크리트 벽면, 물이 거의 가득 차서 넘칠 것 같다.

중간 크기 성체 라쿤, 회갈색 털이 물에 완전히 젖어 납작하게 몸에 붙음, 얼굴에 검은 마스크 무늬, 검은 줄무늬 꼬리. 코와 눈만 겨우 물 위로 나와있다. 작고 검은 앞발이 그레이트 슬롯을 필사적으로 움켜쥐고 있다. 겁에 질린 크고 둥근 눈으로 라이트를 올려다본다. 고개를 들어 물 위로 코를 유지하려 버틴다.

No background music. 폭우 소리, 하수구로 물 쏟아지는 소리, 라쿤 필사적으로 끼익끼익 우는 소리, 촬영자가 충격받아 숨을 들이쉬는 소리.
```

---

## Scene 2: 발견

- **Duration:** 10s
- **Emotion:** 발견, 충격
- **Camera:** handheld POV, walking then stopping, shaky

**Caption:**

- EN: "Wait... is that...?"
- KR: "잠깐... 저게...?"

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 심하게 흔들리는 아마추어 촬영. 미국 워싱턴주 시애틀 교외 주택가 도로. 밤. 폭우가 억수같이 쏟아진다. 가로등 불빛이 젖은 아스팔트에 반사된다.

카메라가 비를 맞으며 걷다가 갑자기 멈춘다. 하수구 쪽에서 이상한 소리가 들린다. 고개를 돌려 도로변 하수구를 본다. 핸드폰 플래시가 켜진다. 하수구를 비춘다.

도로 가장자리 콘크리트 연석 옆 직사각형 하수구. 검은색 금속 철망 그레이트가 덮여 있음. 빗물이 콸콸 쏟아져 들어간다.

그레이트 슬롯 사이로 보이는 중간 크기 성체 라쿤, 회갈색 털이 젖어 납작함, 검은 마스크 무늬. 코와 눈만 물 위로 나와있다. 겁에 질린 눈으로 카메라를 올려다본다. 끼익끼익 운다.

No background music. 폭우 소리, 촬영자의 놀란 숨소리, 라쿤 끼익끼익 우는 소리, 물 출렁이는 소리.
```

---

## Scene 3: 닿지 않는 손

- **Duration:** 12s
- **Emotion:** 초조함, 좌절
- **Camera:** handheld POV, close-up on reaching hand through grate

**Caption:**

- EN: "I can't reach her..."
- KR: "손이 닿지 않아..."

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 흔들리는 아마추어 촬영. 핸드폰 라이트가 하수구를 비춘다. 미국 워싱턴주 시애틀 교외. 밤. 폭우.

도로 가장자리 콘크리트 연석 옆 직사각형 하수구. 가로 60cm 세로 30cm 크기, 검은색 금속 철망 그레이트가 덮여 있음. 그레이트는 긴 직사각형 슬롯이 가로로 7-8줄 나란히 있는 형태. 슬롯 사이 간격은 손가락이 들어갈 정도로 좁음.

화면 아래쪽에서 회색 후드티 소매를 입은 남자의 손이 나온다. 무릎 꿇고 그레이트 슬롯 사이로 손을 뻗는다. 손가락 끝이 허공을 휘젓는다. 닿지 않는다. 슬롯이 너무 좁아서 팔이 더 들어가지 않는다.

하수구 안. 중간 크기 성체 라쿤, 회갈색 털이 물에 젖어 납작함, 검은 마스크 무늬. 겁에 질린 눈으로 손을 올려다본다. 작은 앞발이 그레이트를 꽉 쥐고 있다. 물이 출렁인다.

No background music. 폭우 소리, 촬영자의 거친 숨소리, 라쿤 끼익끼익 우는 소리, 물 출렁이는 소리.
```

---

## Scene 4: 차오르는 물

- **Duration:** 10s
- **Emotion:** 공포, 절박함
- **Camera:** handheld POV, tight close-up at water level

**Caption:**

- EN: "The water keeps rising..."
- KR: "물이 계속 차오른다..."

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 핸드폰 라이트로 하수구 안을 비추는 장면. 흔들리고 불안정한 아마추어 촬영. 미국 워싱턴주 시애틀 교외. 밤. 폭우가 더 거세진다.

도로 가장자리 콘크리트 연석 옆 직사각형 하수구. 검은색 금속 철망 그레이트가 덮여 있음. 빗물이 그레이트 슬롯 사이로 더 빠르게 쏟아져 들어간다.

핸드폰 라이트가 그레이트 슬롯 사이로 안을 비춘다. 물이 아까보다 더 차올랐다. 중간 크기 성체 라쿤, 회갈색 털이 완전히 젖음, 검은 마스크 무늬. 이제 물이 코 바로 아래까지 차올랐다. 라쿤이 고개를 최대한 뒤로 젖히고 코를 물 위로 내밀며 버틴다. 물이 입에 들어간다. 작은 검은 앞발이 그레이트 슬롯을 움켜쥔 채 힘이 빠져간다. 공포에 질린 눈.

No background music. 물 쏟아지는 소리, 라쿤 끼익끼익 우며 물 먹는 소리, 폭우 소리, 촬영자가 당황해서 소리치는 목소리.
```

---

## Scene 5: 시간과의 싸움

- **Duration:** 10s
- **Emotion:** 긴급함, 결의
- **Camera:** handheld POV, running motion, very shaky

**Caption:**

- EN: "Hold on... just hold on!"
- KR: "버텨... 조금만 버텨!"

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 심하게 흔들리는 아마추어 촬영. 미국 워싱턴주 시애틀 교외 주택가 도로. 밤. 폭우.

카메라가 심하게 흔들리며 길가에 세워둔 차를 향해 전력 질주한다. 화면에 달리는 다리와 젖은 아스팔트가 보인다. 물웅덩이를 밟으며 물이 튄다. 가로등 불빛이 지나간다.

차 트렁크가 열린다. 화면 아래쪽에서 회색 후드티 소매를 입은 남자의 손이 나온다. 트렁크 안에서 빨간색 공구 가방을 꺼낸다. 가방 안에서 빠루를 집는다. 담요도 집는다.

다시 하수구 쪽으로 뛰어간다. 카메라가 심하게 흔들린다.

No background music. 폭우 소리, 발이 물웅덩이 밟는 소리, 거친 숨소리, 트렁크 여는 소리, 공구 부딪히는 소리.
```

---

## Scene 6: 격자를 열다

- **Duration:** 12s
- **Emotion:** 긴장, 희망
- **Camera:** handheld POV, close-up on hands prying grate and pulling raccoon out

**Caption:**

- EN: "Got you!"
- KR: "잡았어!"

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 흔들리는 아마추어 촬영. 핸드폰 라이트가 하수구를 비춘다. 미국 워싱턴주 시애틀 교외. 밤. 폭우.

도로 가장자리 콘크리트 연석 옆 직사각형 하수구. 가로 60cm 세로 30cm 크기, 검은색 금속 철망 그레이트가 덮여 있음. 녹슨 볼트로 고정됨.

화면 아래쪽에서 회색 후드티 소매를 입은 남자의 손이 나온다. 빠루를 그레이트 가장자리에 끼운다. 온 힘을 다해 지렛대처럼 누른다. 그레이트가 삐걱거린다. 녹슨 볼트가 조금씩 들린다. 쾅 소리와 함께 그레이트 한쪽이 들린다. 그레이트를 옆으로 밀어낸다.

맨팔을 하수구 안으로 깊이 집어넣는다. 물속을 더듬는다. 중간 크기 성체 라쿤, 회갈색 털이 완전히 젖음, 검은 마스크 무늬. 손이 라쿤의 몸을 붙잡는다. 물에서 라쿤을 끌어올린다. 라쿤이 물을 뚝뚝 흘리며 올라온다.

No background music. 폭우 소리, 빠루가 금속에 부딪히는 소리, 녹슨 금속 삐걱거리는 소리, 볼트 빠지는 소리, 물 튀기는 소리, 촬영자의 거친 숨소리.
```

---

## Scene 7: 따뜻한 품

- **Duration:** 12s
- **Emotion:** 안도, 따뜻함
- **Camera:** handheld POV, medium shot looking down at raccoon in arms

**Caption:**

- EN: "You're safe now..."
- KR: "이제 괜찮아..."

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 약간 흔들리는 아마추어 촬영. 미국 워싱턴주 시애틀 교외 도로변. 밤. 폭우가 계속 내린다. 가로등 아래.

화면 아래쪽에 회색 후드티 소매를 입은 남자의 팔과 무릎이 보인다. 무릎 꿇고 앉아있다.

중간 크기 성체 라쿤, 회갈색 털이 완전히 젖어 납작하게 몸에 붙음, 검은 마스크 무늬. 물에 흠뻑 젖어 홀쭉하고 지쳐 보인다. 남자의 손이 담요로 라쿤을 감싼다. 라쿤이 담요에 싸여 부들부들 떨고 있다.

남자의 손이 라쿤을 가슴 쪽으로 안아 올린다. 라쿤이 저항하지 않고 안긴다. 천천히 떨림을 멈춘다. 라쿤이 고개를 들어 카메라를 올려다본다. 눈이 점점 편안해진다.

No background music. 빗소리, 라쿤 끼익끼익 우는 소리가 점점 잦아듦, 촬영자가 안도하며 숨을 내쉬는 소리.
```

---

## Scene 8: 새로운 시작

- **Duration:** 12s
- **Emotion:** 희망, 감동, 작별
- **Camera:** handheld POV, outdoor, golden morning light

**Caption:**

- EN: "Go live your life, little one"
- KR: "잘 살아, 꼬마야"

### Sora2 Prompt

```
1인칭 시점 손으로 들고 찍는 핸드폰 영상. 약간 흔들리는 아마추어 촬영. 미국 워싱턴주 시애틀 교외 숲 가장자리. 다음 날 아침. 맑은 하늘, 황금빛 아침 햇살. 이슬이 맺힌 풀밭.

화면 아래쪽에 남자의 손이 보인다. 숲 앞 풀밭에 무릎 꿇고 앉아있다.

중간 크기 성체 라쿤, 회갈색 털이 마르고 복슬복슬해짐, 검은 마스크 무늬, 검은 줄무늬 꼬리. 건강해 보인다. 털이 윤기난다. 남자의 손이 라쿤을 풀밭에 조심스럽게 내려놓는다.

라쿤이 몇 발자국 숲 쪽으로 걸어간다. 멈춘다. 뒤돌아서 카메라를 바라본다. 잠시 눈을 마주친다. 그리고 다시 돌아서서 숲 속으로 뛰어간다. 덤불 사이로 줄무늬 꼬리가 사라진다.

No background music. 새소리, 바람 소리, 라쿤 발소리, 나뭇잎 바스락거리는 소리.
```

---

## 제목 옵션

**메인:** Only Her Face Above Water

**부제목:** A raccoon's desperate fight for survival in a flooded storm drain

| 플랫폼        | 제목                                                                                   |
| ------------- | -------------------------------------------------------------------------------------- |
| **YouTube**   | A raccoon trapped in a flooded drain... only her face above water (True Story)        |
| **TikTok**    | Found a raccoon drowning in a storm drain... wait for the rescue                       |
| **Instagram** | She was drowning in a storm drain. Only seconds left.                                  |

### 후킹 옵션

- **감정형:** You won't watch this without holding your breath...
- **호기심형:** Why was this raccoon holding onto a drain grate for her life?
- **결과형:** I found her drowning... 24 hours later

### Hashtags

```
#raccoonrescue #animalrescue #stormdrain #wildlife #rescue #heartwarming #raccoon #savinglives
```

---

## 제작 노트

### 시각적 일관성
- 모든 장면 1인칭 POV (손/팔만 보임)
- 라쿤: 회갈색 털, 검은 마스크, 줄무늬 꼬리
- 장소: 미국 시애틀 교외
- 날씨: 폭우 (Scene 1-7) → 맑은 아침 (Scene 8)

### 오디오 가이드라인
- 배경음악 없음
- 자연음: 폭우, 물소리, 숨소리, 라쿤 울음소리
- Scene 8: 새소리, 바람, 나뭇잎 소리

### 감정 곡선
```
Scene 1-2: 충격/발견 (90%)
Scene 3-4: 초조/공포 (95-98%)
Scene 5-6: 긴급/희망 (85%)
Scene 7-8: 안도/감동 (90%)
```

---

_Generated by Animal Shorts Agent System_
