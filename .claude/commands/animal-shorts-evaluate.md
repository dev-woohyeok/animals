# /animal-shorts-evaluate - 프롬프트 평가 에이전트

Seedance 2.0 프롬프트의 품질, 정책 준수, 일관성을 자동 평가

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
| 죽음 | dead, death, die, corpse, lifeless | HIGH |
| 폭력 | kill, attack, devour, maul, bite, tear | HIGH |
| 상해 | blood, bleeding, wound, injury, gore | HIGH |
| 공포 | horrifying, terrifying, gruesome | MEDIUM |
| 학대 | abuse, cruelty, torture | HIGH |
| 실사 인간 얼굴 | realistic human face reference | HIGH |

**허용 대체 표현:**

| 의도 | 허용 표현 |
|------|----------|
| 죽음 암시 | motionless, still, not responding, lying still, collapsed |
| 포식 암시 | crouched over, feeding posture, muzzle wet, backs away |
| 긴장감 | tense, dramatic, intense, shocking |

### 2. @ 참조 시스템 검사

```
[ ] 모든 프롬프트에 @Image1 참조 포함
[ ] @ 참조에 역할이 명시되어 있음 (e.g., "as the subject")
[ ] 실사 인간 얼굴 이미지 참조 없음
```

### 3. 캐릭터 일관성 검사

```
[ ] 모든 씬에서 동일한 기본 캐릭터 설명 유지
[ ] 씬마다 상태 변화 반영 (동일 상태 2씬 이상 반복 없음)
[ ] 나이/크기/색상 정보 일관성
```

### 4. 기술 품질 검사

```
[ ] 각 씬에 촬영 스타일 명시 (amateur, handheld 등)
[ ] 조명 조건 포함
[ ] 분위기/스타일 수식어 포함
[ ] 오디오 지시 포함
[ ] 프롬프트가 영어로 작성됨
[ ] 200단어 미만
```

### 5. 스토리 일관성 검사

```
[ ] // Story: 에 Overall + Previous + This scene 모두 포함
[ ] 장면 간 시간 흐름 자연스러움 (시간순)
[ ] 감정 아크 논리적 진행
[ ] 플래시백/시간 역행 없음
```

### 6. Seedance 2.0 특화 검사

```
[ ] 서브샷 시간 분할 형태 사용 (0-5s, 5-10s, 10-15s)
[ ] 서브샷 간 "— natural transition —" 포함
[ ] Scene 1은 단일 연속 장면 (서브샷 금지)
[ ] 스타일 수식어가 프롬프트 끝에 포함
[ ] 서브샷별 자막(EN/KR) 포함
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
        suggestion: "Remove or replace with 'muzzle glistening dark'"

  reference_check:
    status: "PASS/FAIL"
    issues: []

  character_consistency:
    status: "PASS/FAIL"
    issues: []

  technical_quality:
    status: "PASS/FAIL"
    missing_elements:
      - scene: 3
        missing: "style modifiers"

  story_coherence:
    status: "PASS/FAIL"
    notes: []

  seedance2_compliance:
    status: "PASS/FAIL"
    issues: []

  scene_scores:
    - scene: 1
      score: 95
      notes: "Well structured"
    - scene: 2
      score: 90
      notes: "Character description accurate"
    ...

  recommendations:
    - "Scene 4: Replace 'blood' with 'muzzle glistening dark'"
    - "Scene 6: Add style modifiers at end of prompt"
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

1. HIGH 심각도 금지 단어 1개 이상
2. 캐릭터 설명 불일치 2개 이상
3. 오디오 지시 누락
4. @ 참조 누락
5. 프롬프트가 한국어로 작성됨

---

## 평가 실행 후 액션

### PASS인 경우
```
✅ 평가 완료 - 모든 검사 통과
프롬프트가 Seedance 2.0 생성에 적합합니다.
```

### FAIL인 경우
```
❌ 평가 실패 - 수정 필요

발견된 문제:
1. [씬 번호]: [문제 설명]
   → 권장 수정: [수정 방안]

수정 후 다시 /animal-shorts-evaluate 실행 필요
```
