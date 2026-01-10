# /animal-shorts - Animal Shorts Prompt Generator

동물 관련 감동 쇼츠 영상 제작을 위한 Sora2 프롬프트 자동 생성 워크플로우

## 사용법

```
/animal-shorts [동물] / [상황] / [감정] / [결말(선택)]
```

### 예시
```
/animal-shorts 골든 리트리버 강아지 / 버려진 후 노인을 만남 / 따뜻함, 감동
/animal-shorts 아기 고슴도치 / 골든리트리버가 입에 물고 옴 / 귀여움, 감동 / 가족이 됨
```

---

## 워크플로우

이 명령을 실행하면 다음 단계를 순차적으로 진행합니다. **각 단계에서 사용자 확인 후 다음 단계로 진행합니다.**

### Step 1: 입력 분석

사용자 입력에서 다음을 추출합니다:
- **동물**: 종류, 나이, 특징 (예: "아기 고슴도치", "골든 리트리버")
- **상황**: 핵심 스토리 전제 (예: "입에 물고 옴", "버려진 후 구조됨")
- **감정**: 목표 감정 톤 (예: "감동", "따뜻함", "희망")
- **결말**: 원하는 결말 (선택사항)

### Step 2: 스토리 생성

`prompts/story_system.md` 규칙에 따라 **5막 구조** 스토리 생성:

1. **도입**: 동물 상황 소개, 공감 구축
2. **전개**: 주요 캐릭터 등장, 연결 시작
3. **위기**: 긴장, 위험, 결정의 순간
4. **해결**: 전환점, 구원 또는 변화
5. **결말**: 감정적 보상, 새로운 시작

**출력 형식**:
```yaml
title: "스토리 제목"
synopsis: "1-2문장 요약"
arc:
  - phase: "도입"
    description: "..."
    emotion: "슬픔, 고독"
  - phase: "전개"
    description: "..."
    emotion: "호기심, 희망"
  # ...
total_duration: 90
```

**[사용자 확인]**: 스토리가 마음에 드시나요? (수정 요청 가능)

### Step 3: 장면 분할

`prompts/scene_system.md` 규칙에 따라 **6개 이상의 15초 장면**으로 분할:

**출력 형식**:
```yaml
scenes:
  - id: 1
    title: "장면 제목"
    title_en: "Scene Title"
    duration: 15
    description: "장면 설명"
    action: "주요 동작"
    emotion: "감정"
    camera:
      movement: "slow dolly in"
      angle: "close-up"
      transition: "fade in"
    lighting: "warm sunset light"
```

**[사용자 확인]**: 장면 구성이 적절한가요? (개별 장면 수정 가능)

### Step 4: Sora2 프롬프트 생성

`prompts/sora2_system.md` 규칙에 따라 각 장면의 **영어 프롬프트** 생성 (한국어 번역 없음):

**핵심 규칙**:
1. **캐릭터 일관성**: 모든 프롬프트에 동일한 캐릭터 설명 사용
2. **프롬프트 구조**:
   - Character Description (캐릭터 설명)
   - Setting/Environment (배경)
   - Action (동작)
   - Camera Movement (카메라)
   - Lighting (조명)
   - Atmosphere (분위기)
   - Technical Specs (품질 마커)

**출력 형식**:
```yaml
character_reference: "A small African pygmy hedgehog with brown and cream quills..."

prompts:
  - scene_id: 1
    prompt: |
      First person POV handheld home video footage. [Character description].
      [Setting]. [Action]. [Camera]. [Lighting]. [Atmosphere]. [Quality markers].
```

**[사용자 확인]**: 프롬프트가 적절한가요? (개별 수정 가능)

### Step 5: 제목 생성

`prompts/title_system.md` 규칙에 따라 플랫폼별 최적화 제목 생성:

**출력 형식**:
```yaml
main_title: "메인 제목"
subtitle: "부제목"
platform_variants:
  youtube_shorts: "YouTube용 제목 (이모지, 100자 이내)"
  instagram_reels: "Instagram용 제목 (세련된 톤)"
  tiktok: "TikTok용 제목 (구어체, 강한 후킹)"
hooks:
  emotional: "감정 자극형 후킹"
  curiosity: "호기심 유발형 후킹"
  outcome: "결과 강조형 후킹"
```

**[사용자 확인]**: 제목이 마음에 드시나요?

### Step 6: 파일 저장

최종 결과물을 `projects/{slug}/prompts.md` 형식으로 저장:

```markdown
# {제목}

> {synopsis}

**총 길이:** {duration}초 ({scene_count}개 장면)

---

## Scene 1: {title}
- **Duration:** 15s
- **Emotion:** {emotion}
- **Camera:** {camera}

### Sora2 Prompt
\`\`\`
{english_prompt}
\`\`\`

---
...

## 제목 옵션
- **YouTube:** {youtube_title}
- **Instagram:** {instagram_title}
- **TikTok:** {tiktok_title}
```

---

## 참조 파일

- `prompts/story_system.md` - 스토리 구조 가이드
- `prompts/scene_system.md` - 장면 분할 가이드
- `prompts/sora2_system.md` - Sora2 프롬프트 규칙
- `prompts/title_system.md` - 제목 생성 전략
- `output/hedgehog_family.md` - 출력 형식 예시

---

## 도구 사용

- **Read**: 시스템 프롬프트 및 설정 파일 로드
- **Write**: 최종 출력 파일 저장
- **TodoWrite**: 워크플로우 진행 상황 추적

---

## 제약사항

**허용**:
- 동물 관련 감동 스토리 생성
- Sora2 최적화 프롬프트 생성
- 일관성 있는 캐릭터 설명 유지

**불허**:
- 폭력적이거나 부적절한 콘텐츠
- 사용자 확인 없이 다음 단계 진행
- 저작권 침해 콘텐츠
