# /animal-shorts-evaluate - 프롬프트 평가 에이전트

Sora2 프롬프트의 품질, 정책 준수, 일관성을 자동 평가

## 사용법

```
/animal-shorts-evaluate [프로젝트 경로]
```

예시:
```
/animal-shorts-evaluate projects/midnight-forest-baby-fox/prompts.md
```

---

## 평가 항목

### 1. Content Policy 검증 (CRITICAL)

**금지 표현 자동 탐지:**

| 카테고리 | 금지 단어 | 심각도 |
|----------|----------|--------|
| 죽음 | dead, death, die, corpse, lifeless | 🔴 HIGH |
| 폭력 | kill, attack, devour, maul, bite, tear | 🔴 HIGH |
| 상해 | blood, bleeding, wound, injury, gore | 🔴 HIGH |
| 공포 | horrifying, terrifying, gruesome | 🟡 MEDIUM |
| 학대 | abuse, cruelty, torture | 🔴 HIGH |

**허용 대체 표현:**

| 의도 | 허용 표현 |
|------|----------|
| 죽음 암시 | motionless, still, not responding, lying still, collapsed |
| 포식 암시 | crouched over, feeding posture, muzzle wet, backs away |
| 긴장감 | tense, dramatic, intense, devastating, shocking |

### 2. 캐릭터 일관성 검사

```
[ ] 모든 씬에서 동일한 캐릭터 설명 사용
[ ] Character Reference와 본문 설명 일치
[ ] 나이/크기/색상 정보 일관성
```

### 3. 기술 품질 검사

```
[ ] 각 씬에 카메라 스타일 명시
[ ] 조명 조건 포함
[ ] 분위기 키워드 포함
[ ] "No background music" 문구 포함
[ ] 200단어 미만
```

### 4. 스토리 일관성 검사

```
[ ] 장면 간 시간 흐름 자연스러움
[ ] 감정 아크 논리적 진행
[ ] 장면 전환 부드러움
```

---

## 출력 형식

```yaml
evaluation_result:
  project: "프로젝트명"
  timestamp: "YYYY-MM-DD HH:MM"

  overall_score: "A/B/C/D/F"

  policy_check:
    status: "PASS/FAIL"
    violations:
      - scene: 4
        word: "blood"
        severity: "HIGH"
        suggestion: "삭제하거나 'muzzle wet and dark'로 대체"

  character_consistency:
    status: "PASS/FAIL"
    issues: []

  technical_quality:
    status: "PASS/FAIL"
    missing_elements:
      - scene: 3
        missing: "lighting condition"

  story_coherence:
    status: "PASS/FAIL"
    notes: []

  scene_scores:
    - scene: 1
      score: 95
      notes: "잘 작성됨"
    - scene: 2
      score: 90
      notes: "캐릭터 설명 정확"
    ...

  recommendations:
    - "씬 4의 'blood' 표현을 'muzzle glistening dark'로 수정 권장"
    - "씬 6에 조명 조건 추가 필요"
```

---

## 평가 기준

### 점수 체계

| 등급 | 점수 | 기준 |
|------|------|------|
| A | 90-100 | 모든 검사 통과, 수정 불필요 |
| B | 80-89 | 경미한 이슈, 선택적 수정 |
| C | 70-79 | 일부 수정 필요 |
| D | 60-69 | 상당한 수정 필요 |
| F | 0-59 | 심각한 정책 위반, 반드시 수정 |

### 자동 FAIL 조건

1. 🔴 HIGH 심각도 금지 단어 1개 이상
2. 캐릭터 설명 불일치 2개 이상
3. "No background music" 누락

---

## 평가 실행 후 액션

### PASS인 경우
```
✅ 평가 완료 - 모든 검사 통과
프롬프트가 Sora2 생성에 적합합니다.
```

### FAIL인 경우
```
❌ 평가 실패 - 수정 필요

발견된 문제:
1. [씬 번호]: [문제 설명]
   → 권장 수정: [수정 방안]

수정 후 다시 /animal-shorts-evaluate 실행 필요
```

---

## 자동 평가 트리거

프롬프트 파일 수정 시 자동으로 평가 실행:

```
[프롬프트 수정 완료]
    ↓
[자동 평가 실행]
    ↓
[결과 출력]
    ↓
[PASS] → Git commit & push
[FAIL] → 수정 권장사항 제시
```
