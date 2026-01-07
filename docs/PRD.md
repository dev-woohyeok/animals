# Product Requirements Document (PRD)
# Animal Shorts Agent System v2.0

> **문서 버전**: 1.0
> **작성일**: 2025-01-07
> **상태**: Draft → Review 대기

---

## 1. 개요

### 1.1 프로젝트 목표
동물 관련 감동 쇼츠(Shorts) 영상 제작을 위한 AI 에이전트 시스템 구축.
사용자가 동물 키워드와 간략한 줄거리를 제공하면, Sora2에 최적화된 일관성 있는 영상 프롬프트를 자동 생성한다.

### 1.2 핵심 가치
- **효율성**: 반복적인 프롬프트 작성 작업 자동화
- **일관성**: 캐릭터/배경/스타일의 연속성 보장
- **품질**: Sora2 모범사례 기반 최적화된 프롬프트
- **재사용성**: 캐릭터/템플릿 라이브러리를 통한 자산 축적

### 1.3 대상 사용자
- 동물 관련 쇼츠/릴스 콘텐츠 크리에이터
- Sora2를 활용한 AI 영상 제작자
- 감동/치유 콘텐츠 기획자

---

## 2. 기능 요구사항

### 2.1 핵심 에이전트 (Core Agents)

#### 2.1.1 Input Agent (입력 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 사용자 입력 파싱, 검증, 구조화 |
| **입력** | 자연어 (동물 + 상황 + 감정 + 결말) |
| **출력** | 구조화된 InputData 객체 |
| **우선순위** | P0 (필수) |

```python
# 입력 예시
"골든 리트리버 강아지 / 버려진 후 노인을 만나 서로 위로가 됨 / 따뜻하고 감동적"

# 출력 구조
InputData:
  animal: "골든 리트리버 강아지"
  situation: "버려진 후 노인을 만남"
  emotion: ["따뜻함", "위로", "감동"]
  ending: "서로의 빈자리를 채움"
  template_id: Optional[str]
  character_id: Optional[str]
```

#### 2.1.2 Story Agent (스토리 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 줄거리 확장, 감정선 설계, 스토리 아크 구성 |
| **입력** | InputData + 선택된 템플릿 |
| **출력** | Story 객체 (전체 서사 구조) |
| **우선순위** | P0 (필수) |

```python
Story:
  title: str
  synopsis: str  # 1-2문장 요약
  arc:
    - phase: "도입"
      description: str
      emotion: str
      beats: List[str]
    - phase: "전개"
      ...
  character_development: str
  emotional_journey: List[EmotionPoint]
```

#### 2.1.3 Scene Agent (장면 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 스토리를 개별 장면(15초 단위)으로 분할 |
| **입력** | Story 객체 |
| **출력** | List[Scene] (6개 이상) |
| **우선순위** | P0 (필수) |

```python
Scene:
  id: int
  title: str
  duration: 15  # 초
  description: str
  action: str
  emotion: str
  camera:
    movement: str  # "dolly in", "tracking", "static"
    angle: str     # "wide", "medium", "close-up"
    transition: str  # 이전 장면과의 연결
  lighting: str
  key_elements: List[str]
```

#### 2.1.4 Prompt Agent (프롬프트 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | Scene을 Sora2 최적화 프롬프트로 변환 |
| **입력** | Scene + Character + Style 설정 |
| **출력** | Prompt 객체 |
| **우선순위** | P0 (필수) |

```python
Prompt:
  scene_id: int
  english: str  # Sora2용 영어 프롬프트
  structure:
    character_desc: str   # 캐릭터 외형 (일관성 유지용)
    action: str           # 행동/동작
    camera: str           # 카메라 워크
    lighting: str         # 조명 설정
    atmosphere: str       # 분위기/감정
  tokens_estimate: int    # 예상 토큰 수
  quality_score: int      # 검증 점수 (0-100)
```

#### 2.1.5 Translation Agent (번역 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 영어 프롬프트를 한국어로 번역 (이해용) |
| **입력** | Prompt.english |
| **출력** | Prompt with korean field |
| **우선순위** | P0 (필수) |

#### 2.1.6 Title Agent (제목 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 쇼츠 영상 제목 생성 (플랫폼별 최적화) |
| **입력** | Story + List[Prompt] + 플랫폼 설정 |
| **출력** | TitleSet 객체 |
| **우선순위** | P0 (필수) |

```python
TitleSet:
  main_title: str           # 메인 제목 (감정 후킹)
  subtitle: Optional[str]   # 부제목
  hashtags: List[str]       # 관련 해시태그
  platform_variants:
    youtube_shorts: str     # YouTube Shorts용 (최대 100자)
    instagram_reels: str    # Instagram Reels용
    tiktok: str             # TikTok용 (후킹 강조)
  hooks:
    emotional: str          # 감정 자극형 ("눈물 없이 못 보는...")
    curiosity: str          # 호기심 유발형 ("이 강아지에게 무슨 일이...")
    outcome: str            # 결과 강조형 ("버려진 강아지의 기적 같은 결말")

# 제목 생성 전략
TitleStrategy:
  - hook_first: "감정/호기심 후킹으로 시작"
  - animal_mention: "동물 종류 포함"
  - emotion_keyword: "감동/눈물/치유 등 감정 키워드"
  - length_optimize: "플랫폼별 최적 길이"
  - hashtag_trends: "트렌딩 해시태그 포함"
```

**제목 생성 예시**:
```
입력 스토리: 버려진 골든 리트리버가 외로운 노인을 만나 서로의 가족이 됨

출력:
  main_title: "버려진 강아지가 할아버지를 만났을 때 일어난 일"

  platform_variants:
    youtube_shorts: "💔 버려진 강아지의 눈물나는 재회 (실화)"
    instagram_reels: "이 강아지가 할아버지를 만나고 일어난 기적 🐕✨"
    tiktok: "버려진 강아지한테 일어난 일... 결말 보고 눌물남 😭"

  hooks:
    emotional: "눈물 없이 못 보는 강아지 이야기"
    curiosity: "이 강아지에게 무슨 일이 있었을까?"
    outcome: "버려진 강아지에게 찾아온 기적 같은 결말"

  hashtags:
    - "#감동"
    - "#강아지"
    - "#반려동물"
    - "#치유"
    - "#눈물주의"
    - "#실화"
    - "#골든리트리버"
```

### 2.2 검증 에이전트 (Validation Agent)

| 항목 | 설명 |
|------|------|
| **역할** | 프롬프트 품질 검증 및 개선 제안 |
| **우선순위** | P1 (높음) |

```python
ValidationResult:
  score: int  # 0-100
  breakdown:
    specificity: int      # 구체성 (30점)
    sora2_compat: int     # Sora2 호환성 (30점)
    emotional_clarity: int # 감정 명확성 (20점)
    technical: int        # 기술 정확성 (20점)
  issues: List[Issue]
  suggestions: List[Suggestion]

ConsistencyReport:
  is_consistent: bool
  character_match: float  # 0-1
  style_match: float
  background_continuity: float
  issues: List[str]
```

### 2.3 유틸리티 에이전트 (Utility Agents)

#### 2.3.1 Version Agent (버전 관리 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | A/B 테스트 변형 생성, 버전 관리 |
| **우선순위** | P1 (높음) |

```python
# 기능
- create_variation(prompt, variation_type) → Variation
- list_versions(project_id) → List[Version]
- compare_versions(v1, v2) → ComparisonResult
- rollback(project_id, version) → Project
```

#### 2.3.2 Regen Agent (재생성 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 특정 장면/요소 부분 재생성 |
| **우선순위** | P1 (높음) |

```python
# 기능
- regen_scene(scene_id, feedback) → Scene
- regen_prompt(prompt_id, aspect) → Prompt  # aspect: 조명, 카메라 등
- regen_story_section(section, feedback) → Story
```

#### 2.3.3 Compare Agent (비교 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 버전/변형 간 비교 뷰 생성 |
| **우선순위** | P2 (중간) |

```python
ComparisonView:
  items: List[ComparisonItem]
  differences: List[Difference]
  recommendation: Optional[str]
```

#### 2.3.4 Confirm Agent (확인 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 각 단계별 사용자 확인 및 수정 반영 |
| **우선순위** | P0 (필수) |

```python
# 확인 포인트
1. 스토리 생성 후 확인
2. 장면 분할 후 확인
3. 각 프롬프트 생성 후 확인
4. 최종 출력 전 전체 확인

# 수정 플로우
User Feedback → Parse → Route to Agent → Regenerate → Re-confirm
```

#### 2.3.5 Output Agent (출력 에이전트)
| 항목 | 설명 |
|------|------|
| **역할** | 다양한 형식으로 결과물 내보내기 |
| **우선순위** | P0 (필수) |

```python
# 지원 형식
- Markdown (.md): 읽기 쉬운 형식
- JSON (.json): 구조화된 데이터
- Clipboard (.txt): Sora2 바로 붙여넣기용
- PDF (.pdf): 인쇄/공유용

# 출력 구조
exports/
├── prompts.md           # 전체 프롬프트 (영한 병기)
├── prompts.json         # 구조화된 데이터
├── prompts_clipboard.txt # 복사용 (영어만)
└── prompts.pdf          # 스토리보드 형식
```

---

## 3. 라이브러리 시스템

### 3.1 캐릭터 라이브러리

```yaml
# library/characters/{character_id}.yaml
id: string           # unique identifier
name: string         # 한글 이름 (옵션)
species: string      # 종 (영문)
visual_description:
  fur: string
  eyes: string
  size: string
  distinctive_features: List[string]
sora2_prompt_fragment: string  # Sora2용 설명
personality_traits: List[string]
created_at: datetime
used_in_projects: List[string]
```

**기능**:
- 캐릭터 생성/수정/삭제
- 프로젝트에서 캐릭터 선택
- 캐릭터 자동 저장 (프로젝트 완료 시)
- 캐릭터 검색 (종, 특징 등)

### 3.2 스토리 템플릿 라이브러리

```yaml
# library/templates/{template_id}.yaml
id: string
name: string
genre: string
description: string
structure:
  - phase: string
    beats: List[string]
    emotion: string
    suggested_duration: string
visual_suggestions: List[string]
example_animals: List[string]
```

**제공 템플릿**:
1. 구조 & 재회 - 버려진 동물의 새 가족 찾기
2. 성장 스토리 - 동물의 도전과 성장
3. 우정 이야기 - 다른 종 간의 우정
4. 가족의 의미 - 가족과의 재회/이별
5. 작은 영웅 - 동물의 용감한 행동
6. 사계절 - 계절과 함께하는 동물 이야기

### 3.3 모범사례 DB

```yaml
# library/best_practices/sora2_tips.yaml
general_rules:
  - rule: string
    good: string
    bad: string

consistency_patterns:
  character_reference:
    template: string
    examples: List[string]

emotional_keywords:
  sadness: List[string]
  hope: List[string]
  joy: List[string]
```

---

## 4. 설정 시스템

### 4.1 스타일 프리셋

| 프리셋 ID | 이름 | 설명 |
|-----------|------|------|
| cinematic_realistic | 시네마틱 실사 | 영화급 4K 실사 |
| anime_style | 애니메이션 | 일본 애니메이션 스타일 |
| pixar_3d | 픽사 3D | 픽사풍 3D 애니메이션 |
| watercolor_soft | 수채화 | 부드러운 수채화 스타일 |
| documentary | 다큐멘터리 | 자연 다큐 스타일 |

```yaml
# config/styles/{style_id}.yaml
id: string
name: string
description: string
base_prompt:
  style: string
  rendering: string
  aspect_ratio: string
camera_defaults:
  movement: string
  focus: string
lighting_defaults:
  primary: string
  mood: string
color_grading:
  warm: string
  cold: string
  neutral: string
```

### 4.2 검증 규칙

```yaml
# config/validation_rules.yaml
prompt_validation:
  min_length: 50
  max_length: 500
  required_elements:
    - subject_description
    - action
    - camera_movement
    - lighting
  quality_scoring:
    specificity: { weight: 0.3 }
    sora2_compatibility: { weight: 0.3 }
    emotional_clarity: { weight: 0.2 }
    technical_accuracy: { weight: 0.2 }
```

---

## 5. 프로젝트 구조

### 5.1 프로젝트 저장 구조

```
projects/{project-slug}/
├── project.yaml          # 메타데이터
├── versions/
│   ├── v1/
│   │   ├── story.md
│   │   ├── scenes.yaml
│   │   └── prompts/
│   │       ├── scene_01.yaml
│   │       ├── scene_01_alt_a.yaml
│   │       └── ...
│   └── v2/
│       └── ...
├── history.yaml          # 수정 이력
└── exports/
    ├── prompts.md
    ├── prompts.json
    ├── prompts_clipboard.txt
    └── prompts.pdf
```

### 5.2 프로젝트 메타데이터

```yaml
# project.yaml
id: string
slug: string
name: string
created_at: datetime
updated_at: datetime
character_id: string
template_id: Optional[string]
style_id: string
current_version: int
status: "draft" | "in_progress" | "completed"
summary:
  total_scenes: int
  total_duration: string
  average_quality_score: float
```

---

## 6. 워크플로우

### 6.1 기본 워크플로우

```
┌─────────────────────────────────────────────────────────────────┐
│                       MAIN WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [시작] → 메뉴 선택                                              │
│            │                                                     │
│            ├─→ [1] 새 프로젝트                                   │
│            │      │                                              │
│            │      ├─→ 템플릿 선택 (선택)                         │
│            │      ├─→ 캐릭터 선택/생성                           │
│            │      ├─→ 입력 (동물+상황+감정+결말)                  │
│            │      ├─→ 스토리 생성 ←──┐                           │
│            │      │      ↓          │ 수정                       │
│            │      │   [확인] ───────┘                            │
│            │      │      ↓ 승인                                  │
│            │      ├─→ 장면 분할 ←──┐                             │
│            │      │      ↓         │ 수정                        │
│            │      │   [확인] ──────┘                             │
│            │      │      ↓ 승인                                  │
│            │      ├─→ 스타일 선택                                │
│            │      ├─→ 프롬프트 생성 ←──┐                         │
│            │      │      ↓            │ 수정                     │
│            │      │   [검증] ─────────┘                          │
│            │      │      ↓                                       │
│            │      ├─→ 변형 생성 (선택)                           │
│            │      ├─→ 한국어 번역                                │
│            │      ├─→ 최종 확인 ←──┐                             │
│            │      │      ↓         │ 수정                        │
│            │      │   [확인] ──────┘                             │
│            │      │      ↓ 승인                                  │
│            │      └─→ 내보내기 → [완료]                          │
│            │                                                     │
│            ├─→ [2] 기존 프로젝트                                 │
│            │      ├─→ 프로젝트 목록                              │
│            │      ├─→ 버전 선택                                  │
│            │      └─→ 수정/내보내기                              │
│            │                                                     │
│            ├─→ [3] 라이브러리                                    │
│            │      ├─→ 캐릭터 관리                                │
│            │      └─→ 템플릿 보기                                │
│            │                                                     │
│            └─→ [4] 설정                                          │
│                   ├─→ 스타일 프리셋                              │
│                   └─→ 검증 규칙                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 부분 재생성 워크플로우

```
[프로젝트 열기]
    ↓
[장면 선택] → Scene 3
    ↓
[재생성 옵션]
    ├─→ 전체 재생성
    ├─→ 프롬프트만 재생성
    └─→ 특정 요소 재생성
           ├─→ 카메라
           ├─→ 조명
           └─→ 감정/분위기
    ↓
[피드백 입력] → "더 드라마틱하게"
    ↓
[재생성] → [검증] → [비교 뷰] → [선택]
```

### 6.3 버전 비교 워크플로우

```
[프로젝트 열기] → [비교 뷰어]
    ↓
[버전/변형 선택]
    ├─→ v1 vs v2
    └─→ Scene 1 기본 vs 드라마틱 변형
    ↓
[나란히 비교]
    ↓
[차이점 하이라이트]
    ↓
[선택/병합]
```

---

## 7. 기술 스택

### 7.1 핵심 기술

| 구분 | 기술 | 용도 |
|------|------|------|
| 언어 | Python 3.11+ | 메인 언어 |
| AI | Claude API (Anthropic) | 에이전트 로직 |
| CLI | Rich / Textual | 터미널 UI |
| 데이터 | YAML / JSON | 설정 및 저장 |
| PDF | ReportLab / WeasyPrint | PDF 생성 |

### 7.2 의존성

```
# requirements.txt
anthropic>=0.18.0      # Claude API
pyyaml>=6.0            # YAML 처리
rich>=13.0             # 터미널 UI
textual>=0.50.0        # TUI 프레임워크 (선택)
pydantic>=2.0          # 데이터 검증
reportlab>=4.0         # PDF 생성
jinja2>=3.1            # 템플릿 렌더링
```

---

## 8. 우선순위 및 마일스톤

### 8.1 우선순위 정의

| 우선순위 | 설명 |
|----------|------|
| P0 | 필수 - MVP에 포함 |
| P1 | 높음 - 첫 릴리스에 포함 |
| P2 | 중간 - 후속 릴리스 |
| P3 | 낮음 - 향후 고려 |

### 8.2 마일스톤

#### Phase 1: MVP (P0 기능)
- [ ] 프로젝트 구조 설정
- [ ] Input Agent
- [ ] Story Agent
- [ ] Scene Agent
- [ ] Prompt Agent
- [ ] Translation Agent
- [ ] Confirm Agent
- [ ] Output Agent (Markdown)
- [ ] 기본 CLI 인터페이스

#### Phase 2: 품질 강화 (P1 기능)
- [ ] Validation Agent
- [ ] Version Agent
- [ ] Regen Agent
- [ ] 캐릭터 라이브러리
- [ ] 스토리 템플릿
- [ ] 스타일 프리셋
- [ ] 모범사례 DB
- [ ] 프로젝트 저장/불러오기

#### Phase 3: 고급 기능 (P2 기능)
- [ ] Compare Agent
- [ ] A/B 테스트 변형
- [ ] PDF 내보내기
- [ ] 수정 히스토리
- [ ] 롤백 기능
- [ ] 고급 TUI (Textual)

---

## 9. 성공 지표

### 9.1 정량적 지표

| 지표 | 목표 |
|------|------|
| 프롬프트 생성 시간 | < 2분 (6장면 기준) |
| 평균 품질 점수 | > 85/100 |
| 일관성 점수 | > 90% |
| 사용자 수정 횟수 | < 3회/프로젝트 |

### 9.2 정성적 지표

- Sora2에서 생성된 영상의 캐릭터 일관성
- 스토리 감정선의 자연스러움
- 사용자 만족도

---

## 10. 리스크 및 완화 방안

| 리스크 | 영향 | 완화 방안 |
|--------|------|-----------|
| Sora2 프롬프트 형식 변경 | 높음 | 모듈화된 프롬프트 템플릿, 업데이트 용이한 구조 |
| 캐릭터 일관성 한계 | 중간 | 상세한 캐릭터 설명, 여러 변형 제공 |
| Claude API 비용 | 중간 | 캐싱, 프롬프트 최적화 |
| 복잡한 UX | 낮음 | 단계별 가이드, 기본값 제공 |

---

## 부록 A: 샘플 프롬프트 출력

```markdown
═══════════════════════════════════════════════════════════════
[SCENE 1] 버려진 강아지 / The Abandoned Puppy
Duration: 15s | Emotion: 슬픔, 고독
═══════════════════════════════════════════════════════════════

🇺🇸 ENGLISH (Sora2용):
A golden retriever puppy with fluffy cream-colored fur, large
expressive brown eyes, slightly floppy ears, and a white patch
on chest. The puppy sits alone in a wet cardboard box on a
rainy urban street corner at dusk. Rain drops fall around the
box, creating ripples in small puddles. Slow dolly shot moving
closer to the puppy's face, revealing hopeful yet sad eyes
looking up at passing pedestrians who ignore it. Cold blue-grey
lighting with occasional warm streetlight highlights.
Melancholic, lonely atmosphere with subtle rain sounds.

───────────────────────────────────────────────────────────────
🇰🇷 한국어 (참고용):
크림색 복슬복슬한 털, 크고 표현력 있는 갈색 눈, 살짝 늘어진 귀,
가슴의 흰 반점을 가진 골든 리트리버 강아지. 비 오는 저녁, 도시
골목 모퉁이에서 젖은 골판지 상자 안에 홀로 앉아있다. 빗방울이
상자 주변에 떨어지며 작은 웅덩이에 파문을 만든다. 카메라가 천천히
다가가며 지나가는 행인들을 바라보는 희망적이면서도 슬픈 눈을
클로즈업한다. 차가운 청회색 조명과 간헐적인 따뜻한 가로등 빛.
우울하고 외로운 분위기.
───────────────────────────────────────────────────────────────
Quality Score: 92/100 | Tokens: ~180
═══════════════════════════════════════════════════════════════
```

---

## 부록 B: 시스템 프롬프트 예시

### Story Agent System Prompt

```markdown
You are a professional screenwriter specializing in emotional
animal stories for short-form video content.

Given an animal and situation, create a compelling 90-second
story arc with:

1. STRUCTURE
- 도입 (15-30s): Establish the animal's situation
- 전개 (30-45s): Build emotional connection
- 위기 (15s): Moment of tension or decision
- 해결 (15-30s): Resolution and transformation
- 결말 (15s): Emotional payoff

2. EMOTIONAL JOURNEY
- Start with empathy-building
- Build through hope and setbacks
- End with emotional catharsis

3. VISUAL STORYTELLING
- Think in 15-second scenes
- Each scene should have clear visual action
- Consider weather, lighting, and setting changes

Output in structured YAML format.
```

---

**문서 끝**
