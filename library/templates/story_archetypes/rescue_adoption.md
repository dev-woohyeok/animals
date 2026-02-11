# Rescue & Adoption Archetype (구조 → 입양)

> 위기의 동물을 구조하고 가족이 되는 이야기

## Archetype Overview

인간이 위기에 처한 동물을 발견하고, 구조하고, 돌보다가 결국 가족으로 받아들이는 보편적 스토리 구조.

## Core Elements

### 1. 조우 (Encounter)
동물과 인간의 첫 만남

| 유형 | 설명 | 예시 |
|------|------|------|
| **도움 요청** | 동물이 직접 인간에게 도움 요청 | 텐트를 긁는 아기 여우 |
| **발견** | 인간이 위험에 처한 동물 발견 | 길가에 버려진 강아지 |
| **맡겨짐** | 다른 존재가 인간에게 동물을 맡김 | 어미 캥거루가 아기를 건넴 |

### 2. 위기 (Crisis)
동물이 처한 위험 상황

| 유형 | 감정 강도 | 예시 |
|------|----------|------|
| 부모 상실 | 매우 높음 | 어미가 죽음/떠남 |
| 부상/질병 | 높음 | 다친 상태로 발견 |
| 포식자 위협 | 높음 | 늑대/독수리 등에게 쫓김 |
| 환경 위험 | 중간 | 눈보라, 홍수 등 |
| 버림받음 | 중간 | 인간에게 버려짐 |

### 3. 결심 (Decision)
인간이 돌보기로 결심하는 순간

**결심 트리거**:
- 동물의 간절한 눈빛
- 다른 선택지가 없음
- 본능적 보호 욕구
- 과거 경험/상처와 연결

### 4. 양육 (Nurturing)
돌봄과 유대 형성 과정

**필수 장면**:
- 첫 먹이 주기
- 잠자리 마련
- 건강 회복
- 첫 번째 이정표 (눈 뜸, 걸음 등)

### 5. 결속 (Bonding)
가족으로서의 관계 확립

**시각적 표현**:
- 함께 잠들기
- 함께 놀기
- 서로 의지하기
- 일상의 공유

## Story Beats

```yaml
beat_1:
  name: "위기의 발견"
  duration: "10-15%"
  emotion: "충격, 연민"
  action: "인간이 위험에 처한 동물을 발견"

beat_2:
  name: "결심"
  duration: "5-10%"
  emotion: "망설임, 결심"
  action: "돌보기로 마음먹음"

beat_3:
  name: "초기 양육"
  duration: "15-20%"
  emotion: "불안, 희망"
  action: "서툴지만 정성스러운 돌봄"

beat_4:
  name: "성장과 유대"
  duration: "20-30%"
  emotion: "기쁨, 사랑"
  action: "함께 성장하고 가까워짐"

beat_5:
  name: "시련/선택"
  duration: "15-20%"
  emotion: "갈등, 두려움"
  action: "위기 상황 또는 이별 위기"

beat_6:
  name: "새 가족"
  duration: "10-15%"
  emotion: "사랑, 행복"
  action: "완전한 가족으로 결속"
```

## Compatible Emotional Patterns

| 패턴 | 적합도 | 활용법 |
|------|--------|--------|
| **viral_abandonment** | ★★★★★ | 유기 스토리, 분노→감동 5단계 바이럴 |
| **dual_climax** | ★★★★★ | 비극적 발견 + 가족 결심 |
| **gradual_rise** | ★★★★☆ | 비극 시작 → 성장 → 행복 |
| u_curve | ★★☆☆☆ | 유머 요소 적어 덜 적합 |

## Character Archetypes

### 구조자 (The Rescuer)
- 혼자 사는 사람 (외로움 → 연결)
- 과거 상실 경험자 (치유의 기회)
- 자연/동물 애호가
- 우연히 마주친 일반인

### 구조받는 동물 (The Rescued)
- 갓 태어난 아기 (극도로 연약)
- 어린 동물 (부모 잃음)
- 부상당한 동물
- 버려진 동물

## Thematic Messages

이 원형이 전달하는 메시지:

1. **가족은 선택이다** - 피가 아닌 사랑으로 만들어짐
2. **작은 존재의 가치** - 연약한 생명도 구할 가치가 있음
3. **상호 구원** - 구조자도 구조받는다
4. **책임과 사랑** - 돌봄이 사랑으로 변화

## Reference Stories

### 한밤의 숲에서 만난 아기 여우
- 조우: 아기 여우가 텐트를 긁으며 도움 요청
- 위기: 엄마 여우 죽음, 늑대 위협
- 결심: 떠나려다 울며 쫓아오는 여우를 보고 결심
- 결속: "집에 가자"

### 엄마가 남긴 선물 (캥거루)
- 조우: 죽어가는 어미가 아기를 건넴 (맡겨짐)
- 위기: 극도로 연약한 신생아 조이
- 양육: 2시간마다 수유, 인공 주머니
- 결속: 2년 후 자신의 아기와 돌아옴

## Template Usage

```yaml
archetype: rescue_adoption
emotional_pattern: "dual_climax"  # or gradual_rise

setup:
  animal: "{{ANIMAL_TYPE}}"
  age: "{{AGE}}"  # newborn, baby, young
  crisis: "{{CRISIS_TYPE}}"

rescuer:
  type: "{{RESCUER_TYPE}}"
  motivation: "{{MOTIVATION}}"

bonding_scenes:
  - "{{FIRST_CARE}}"
  - "{{MILESTONE}}"
  - "{{TOGETHER_MOMENT}}"

resolution:
  type: "adoption"  # adoption, release_return, stay_together
  final_emotion: "love, hope"
```
