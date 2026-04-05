# /animal-shorts-analyze - 쇼츠 영상 분석 → 스토리 생성

YouTube Shorts 링크를 분석하여 레퍼런스 기반 스토리를 생성합니다.

## 사용법

```
/animal-shorts-analyze [YouTube Shorts URL]
```

### 예시
```
/animal-shorts-analyze https://www.youtube.com/shorts/FN8oHXBWxV8
/animal-shorts-analyze https://youtube.com/shorts/abc123
```

---

## 워크플로우

### Step 1: 영상 다운로드

`yt-dlp`로 YouTube Shorts 영상을 임시 폴더에 다운로드:

```bash
# 임시 디렉토리 생성
mkdir -p temp_analysis/{video_id}

# 영상 다운로드 (최대 720p)
yt-dlp -f "best[height<=720]" -o "temp_analysis/{video_id}/video.mp4" "{URL}"

# 영상 메타데이터 추출 (제목, 설명, 채널)
yt-dlp --print title --print description --print channel "{URL}"
```

### Step 2: 프레임 캡처

`ffmpeg`로 주요 장면 스크린샷 추출:

```bash
# 2초 간격으로 프레임 캡처 (쇼츠 60초 기준 약 30장)
ffmpeg -i "temp_analysis/{video_id}/video.mp4" -vf "fps=1/2" "temp_analysis/{video_id}/frame_%03d.jpg"

# 영상 길이 확인
ffmpeg -i "temp_analysis/{video_id}/video.mp4" 2>&1 | grep Duration
```

### Step 3: 프레임 분석 (이미지 분석)

캡처된 프레임을 Read 도구로 읽어 다음을 분석:

```yaml
analysis:
  # 1. 기본 정보
  animal:
    species: "동물 종류"
    age: "성체/아기"
    appearance: "외모 특징 (색상, 크기, 상태)"
    condition: "건강 상태 (부상, 질병, 정상)"

  # 2. 스토리 추출
  narrative:
    situation: "무슨 상황인가"
    key_moments:
      - frame: "frame_001.jpg"
        timestamp: "0:00"
        description: "장면 설명"
      - frame: "frame_015.jpg"
        timestamp: "0:30"
        description: "장면 설명"
    emotional_arc: "감정 흐름 (슬픔→희망→감동 등)"
    hook: "시청자를 끌어당기는 포인트"

  # 3. 영상 스타일 분석
  style:
    camera_perspective: "1인칭 POV / 3인칭 / 홈비디오 / CCTV 등"
    camera_movement: "핸드헬드 / 고정 / 추적 등"
    lighting: "자연광 / 실내 / 야간 등"
    editing_style: "컷 편집 / 연속 / 슬로우모션 등"
    color_tone: "따뜻한 / 차가운 / 자연스러운 등"
    text_overlay: "자막 스타일 (있으면)"

  # 4. 바이럴 요소
  viral_elements:
    hook_type: "감정 / 충격 / 귀여움 / 미스터리"
    pacing: "빠름 / 보통 / 느림"
    music_style: "감성 피아노 / 업비트 / 없음"
    engagement_triggers:
      - "어떤 요소가 시청자 반응을 유발하는가"
```

### Step 4: 스토리 3개 제안

분석 결과를 기반으로 **3가지 스토리 옵션 제안**:

```
📊 영상 분석 결과

🎬 원본: {영상 제목}
🐾 동물: {종류} ({상태})
📖 원본 스토리: {요약}
🎥 스타일: {카메라/편집 스타일}

---

📋 스토리 옵션:

1. 「{제목 1}」 — 원본 충실 재현
   {원본 스토리를 우리 스타일로 재해석}
   감정선: {감정 흐름}

2. 「{제목 2}」 — 변주/확장
   {원본의 핵심 감정은 유지하되 다른 전개}
   감정선: {감정 흐름}

3. 「{제목 3}」 — 창작 영감
   {원본에서 영감만 받은 오리지널 스토리}
   감정선: {감정 흐름}

→ 번호를 선택하거나, 원하는 방향을 말해주세요.
```

**스토리 제안 규칙:**
- 옵션 1: 원본 영상의 스토리를 최대한 충실하게 재현 (우리 프롬프트 스타일로)
- 옵션 2: 핵심 감정/동물은 유지하되 전개를 변주
- 옵션 3: 동물만 같고 완전히 다른 오리지널 스토리

---

## ⚠️ 스토리 선택 후 자동 진행 (영구 고정)

**사용자가 스토리를 선택하면, 이후 모든 단계는 자동 진행. 중간에 절대 묻지 않는다.**

1. 스토리 선택 완료
2. → 즉시 스토리 생성 (`/animal-shorts-story` 규칙 적용)
3. → 즉시 장면 분할 (`/animal-shorts-scene` 규칙 적용)
4. → 즉시 Sora2 프롬프트 (`/animal-shorts-prompt` 규칙 적용)
5. → 즉시 제목 생성 (`/animal-shorts-title` 규칙 적용)
6. → 즉시 파일 저장 + git (`/animal-shorts-export` 규칙 적용)

**중간에 사용자에게 확인을 구하거나 멈추는 것은 금지.**

---

## 참조 파일 (스토리 생성 시 적용)

- `prompts/story_system.md` - 스토리 구조 가이드
- `prompts/scene_system.md` - 장면 분할 가이드
- `prompts/sora2_system.md` - Sora2 프롬프트 규칙
- `prompts/title_system.md` - 제목 생성 전략

---

## 분석 팁

### 프레임 선택 우선순위
1. **첫 프레임** — 오프닝 훅 분석
2. **감정 전환점** — 슬픔→희망 등 변화 순간
3. **클라이맥스** — 가장 감동적인 순간
4. **엔딩** — 마무리 분위기

### 스타일 매핑
원본 영상 스타일을 우리 프롬프트 스타일에 매핑:

| 원본 스타일 | 우리 프롬프트 |
|-----------|------------|
| CCTV | → 주변인이 핸드폰으로 몰래 촬영 |
| 드론 | → 멀리서 핸드폰 줌인 촬영 |
| 전문 촬영 | → 아마추어 핸드헬드 POV |
| 슬로우모션 | → 실시간 아마추어 촬영 |
| 자막 스토리텔링 | → 시각적 스토리텔링 (자막은 캡션용) |

---

## 임시 파일 정리

분석 완료 후 임시 파일은 유지 (사용자가 참고할 수 있도록):
```
temp_analysis/{video_id}/
├── video.mp4        # 원본 영상
├── frame_001.jpg    # 캡처 프레임들
├── frame_002.jpg
└── ...
```

사용자가 원하면 수동 삭제: `rm -rf temp_analysis/{video_id}/`

---

## 제약사항

**허용**:
- 공개된 YouTube Shorts 영상 다운로드 및 분석
- 영상 스타일/구조 참고
- 레퍼런스 기반 오리지널 스토리 생성

**불허**:
- 저작권 있는 콘텐츠 그대로 복사
- 비공개/삭제된 영상 접근 시도
- 개인정보 수집
