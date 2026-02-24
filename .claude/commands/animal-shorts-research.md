# /animal-shorts-research - 스토리 리서치 에이전트

인터넷에서 감동적인 동물 구조/rescue 스토리를 검색하고 90초 쇼츠에 적합한 시나리오를 추천합니다.

## 사용법

```
/animal-shorts-research [동물 종류] [--viral] [--recent]
```

### 예시
```
/animal-shorts-research 올빼미
/animal-shorts-research 고양이 --viral
/animal-shorts-research 강아지 --recent
```

---

## 워크플로우

### Step 1: 웹 검색

다음 소스에서 감동적인 동물 스토리 검색:

```yaml
search_queries:
  viral_stories:
    - "{animal} rescue story viral"
    - "{animal} saved heartwarming"
    - "{animal} rescue tiktok viral"
    - "{animal} found injured saved"

  news_stories:
    - "{animal} rescue news 2024 2025"
    - "wildlife rescue {animal} story"
    - "animal rescue organization {animal}"

  reddit_stories:
    - "site:reddit.com {animal} rescue story"
    - "site:reddit.com found injured {animal}"
```

### Step 2: 스토리 분석

검색된 스토리에서 다음 요소 추출:

```yaml
analysis_criteria:
  emotional_hooks:
    - 발견 상황 (어떻게 발견했는가?)
    - 위기 요소 (어떤 위험이 있었나?)
    - 반전 포인트 (예상치 못한 전개?)
    - 감동 요소 (왜 사람들이 감동했나?)

  viral_factors:
    - 조회수/공유수 (인기도)
    - 댓글 반응 (감정적 반응)
    - 플랫폼 (TikTok, YouTube, Instagram)

  story_structure:
    - 시작 상황
    - 구조 과정
    - 결말/현재 상태
```

### Step 3: 쇼츠 시나리오 변환

검색된 스토리를 90초 쇼츠 구조로 변환:

```yaml
conversion_template:
  scene_1: "0-15초: Hook (가장 충격적 장면)"
  scene_2: "15-30초: 배경/맥락"
  scene_3: "30-45초: 전개/위기"
  scene_4: "45-60초: 해결/전환"
  scene_5: "60-75초: 회복/유대"
  scene_6: "75-90초: 결말/여운"
```

---

## 출력 형식

```yaml
research_results:
  query: "{검색한 동물}"
  sources_searched: 5
  stories_found: 3

stories:
  - id: 1
    title: "스토리 제목"
    source: "URL 또는 플랫폼"
    summary: "1-2문장 요약"

    viral_metrics:
      views: "예상 조회수"
      engagement: "높음/중간/낮음"
      platforms: ["TikTok", "YouTube"]

    emotional_elements:
      hook: "무엇이 시선을 끌었나"
      crisis: "어떤 위기 상황"
      resolution: "어떻게 해결"
      payoff: "감동 포인트"

    shorts_potential:
      score: 8/10
      strengths: ["강한 오프닝 후킹", "명확한 감정선"]
      challenges: ["장면 수 조절 필요"]

    suggested_adaptation:
      hook_a: "..."
      climax_c: "..."
      ending_e: "..."

  - id: 2
    ...

recommendation:
  best_story: 1
  reason: "가장 강한 감정적 후킹과 명확한 구조"
  next_step: "/animal-shorts 명령으로 스토리 생성 가능"
```

---

## 검색 키워드 전략

### 감동 스토리 키워드
```
영어:
- "heartwarming {animal} rescue"
- "found injured {animal} saved life"
- "{animal} rescue story went viral"
- "wildlife rescue {animal} recovery"

한국어:
- "{동물} 구조 감동"
- "{동물} 구출 스토리"
- "다친 {동물} 살리다"
```

### 바이럴 스토리 키워드
```
- "viral {animal} rescue tiktok"
- "{animal} rescue millions views"
- "most viewed {animal} rescue"
```

### 뉴스 스토리 키워드
```
- "{animal} rescue news"
- "wildlife rescue {animal} 2024 2025"
- "{animal} rehabilitation center story"
```

---

## 분석 기준

### 쇼츠 적합성 점수 (1-10)

| 요소 | 가중치 | 기준 |
|------|--------|------|
| 시각적 임팩트 | 25% | 영상으로 표현 가능한가? |
| 감정적 후킹 | 25% | 첫 5초에 시선 잡는가? |
| 스토리 구조 | 20% | 90초에 담을 수 있는가? |
| 반전/서프라이즈 | 15% | 예상치 못한 전개가 있는가? |
| 해피엔딩 | 15% | 감동적 마무리가 있는가? |

### 바이럴 가능성 지표

```yaml
high_viral_potential:
  - 동물의 표정이 명확함 (큰 눈, 감정 전달)
  - 위기→구조 과정이 극적
  - 전후 비교가 선명 (before/after)
  - 사람과 동물의 교감 순간

medium_viral_potential:
  - 스토리는 좋으나 시각적 요소 부족
  - 구조 과정이 길어서 편집 필요

low_viral_potential:
  - 스토리가 복잡하거나 설명 필요
  - 시각적으로 표현하기 어려움
```

---

## 도구 사용

- **WebSearch**: 인터넷 검색 (바이럴 스토리, 뉴스)
- **WebFetch**: 특정 URL 내용 분석
- **TodoWrite**: 검색 진행 상황 추적

---

## 사용 예시

### 기본 검색
```
/animal-shorts-research 올빼미
```
→ 올빼미 관련 감동 스토리 3-5개 검색 및 분석

### 바이럴 중심 검색
```
/animal-shorts-research 고양이 --viral
```
→ 가장 많이 공유된 고양이 구조 스토리 우선 검색

### 최신 스토리 검색
```
/animal-shorts-research 강아지 --recent
```
→ 최근 1년 내 강아지 구조 뉴스/스토리 검색

---

## 제약사항

**허용**:
- 공개된 뉴스/바이럴 스토리 검색 및 분석
- 스토리 구조 추출 및 변환 제안
- 쇼츠 적합성 평가

**불허**:
- 저작권 있는 콘텐츠 전체 복사
- 개인정보 수집
- 허위 정보 생성

---

## 다음 단계

리서치 완료 후:
```
/animal-shorts [추천 스토리 기반 입력]
```
→ 선택한 스토리를 90초 쇼츠 프롬프트로 변환
