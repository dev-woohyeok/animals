# /animal-shorts - Animal Shorts Prompt Generator

동물 관련 감동 쇼츠 영상 제작을 위한 Seedance 2.0 프롬프트 자동 생성 워크플로우

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

## ⚠️ 워크플로우 (완전 자동화)

**스토리 선택만 물어보고, 나머지는 전부 자동 진행. 중간에 절대 멈추지 않는다.**

```
Step 1: 입력 분석 → 스토리 3개 제안 (리스트)
          ↓
    [유일한 사용자 확인] 스토리 선택
          ↓
Step 2: 스토리 생성 → 자동 진행
          ↓
Step 3: 장면 분할 → 자동 진행
          ↓
Step 4: Seedance 2.0 프롬프트 → 자동 진행
          ↓
Step 5: 제목 생성 → 자동 진행
          ↓
Step 6: 파일 저장 + git commit & push → 완료
```

---

### Step 1: 스토리 제안 (유일한 사용자 확인)

사용자 입력에서 동물/상황/감정을 추출한 뒤, **3가지 스토리 방향을 리스트로 제안**:

```
입력: /animal-shorts 강아지 / 벤치에 묶여 버려짐 / 감동

📋 스토리 옵션:

1. 「폭풍우 속 구조」
   벤치에 묶인 채 폭풍우를 맞는 강아지. 우연히 지나가던 여자가 구조.
   차 안에서 깊은 한숨을 쉬며 눈을 감는다.

2. 「기다림 끝에 선택」
   밀쳐지고 버려진 강아지가 벤치를 떠나지 않고 기다린다.
   구조 후 전 주인이 찾아오지만, 강아지는 새 주인을 선택한다.

3. 「벤치의 약속」
   매일 같은 벤치에서 기다리는 강아지. SNS에서 화제.
   전국에서 입양 신청이 쇄도하지만, 매일 밥을 주던 노숙자가 진짜 가족.

→ 번호를 선택하거나, 원하는 방향을 말해주세요.
```

**이 선택 이후 모든 단계는 자동 진행. 중간에 묻지 않는다.**

---

### Step 2: 스토리 생성 (자동)

`prompts/story_system.md` 규칙에 따라 **5막 구조** 스토리 생성.
→ 완료 즉시 Step 3으로 자동 진행.

### Step 3: 장면 분할 (자동)

`prompts/scene_system.md` 규칙에 따라 **6개의 15초 장면**으로 분할 (총 90초):

**핵심 규칙**:
1. **모든 Scene**: 각 15초 장면에 최대 3개 서브샷
2. **⚠️ 서브샷 = 개별 미니 씬**: 자연스럽게 연결되지만 시간이 경과해서 구별 (연속 실시간 ❌)
3. **모든 장면 시간순 전개**: 과거 회상, 시간 되돌림, 플래시백 금지

→ 완료 즉시 Step 4로 자동 진행.

### Step 4: Seedance 2.0 프롬프트 생성 (자동)

`prompts/seedance2_system.md` 규칙에 따라 각 장면의 **영어 프롬프트** 생성:

**핵심 규칙**:
1. **@ 참조 시스템**: `@Image1's [animal] as the subject` 로 캐릭터 일관성
2. **캐릭터 텍스트 설명**: @ 참조 + 텍스트로 상태 변화 표현
3. **멀티샷 시퀀스**: 서브샷을 시간 분할 형태로 (0-5s, 5-10s, 10-15s)
4. **카메라 상세 + 상황 간결**: Seedance 2.0에 자유도
5. **스타일 수식어**: 프롬프트 끝에 amateur, shaky, photorealistic 등

→ 완료 즉시 Step 5로 자동 진행.

### Step 5: 제목 생성 (자동)

`prompts/title_system.md` 규칙에 따라 플랫폼별 최적화 제목 생성.
→ 완료 즉시 Step 6으로 자동 진행.

### Step 6: 파일 저장 + git (자동)

최종 결과물을 `projects/{slug}/prompts.md` 형식으로 저장.
git commit & push 자동 실행.

**출력 형식**:
```markdown
# {제목}

> {synopsis}

**총 길이:** {duration}초 ({scene_count}개 장면)

---

## 캐릭터 레퍼런스
...

## Scene 1: {title}
- **Duration:** 15s
- **is_hook:** true
- **Emotion:** {emotion}
- **Camera:** {camera}

**Caption:**
- (0-15s)
  - EN: "..."
  - KR: "..."

### Seedance 2.0 Prompt
\`\`\`
{prompt}
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
- `prompts/seedance2_system.md` - Seedance 2.0 프롬프트 규칙
- `prompts/title_system.md` - 제목 생성 전략

---

## 제약사항

**허용**:
- 동물 관련 감동 스토리 생성
- Seedance 2.0 최적화 프롬프트 생성
- 일관성 있는 캐릭터 설명 유지

**불허**:
- 폭력적이거나 부적절한 콘텐츠
- 저작권 침해 콘텐츠
- **스토리 선택 이후 중간에 사용자에게 확인 요청 (금지!)**
