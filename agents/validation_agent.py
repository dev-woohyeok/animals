"""Validation Agent - Validate and score prompts for quality."""

import re
from typing import Any

from core.models import (
    Prompt,
    Scene,
    Character,
    ValidationResult,
    ScoreBreakdown,
    ValidationIssue,
    ConsistencyReport,
)
from .base import BaseAgent


class ValidationAgent(BaseAgent[ValidationResult]):
    """
    Validates Sora2 prompts for quality and consistency.

    Features:
    - Quality scoring (specificity, compatibility, clarity, accuracy)
    - Consistency checking across scenes
    - Issue detection and suggestions
    - Best practice validation
    """

    def __init__(self):
        super().__init__(
            name="ValidationAgent",
            system_prompt_path="validation_system.md",
        )

        # Quality weights
        self.weights = {
            "specificity": 0.3,
            "sora2_compatibility": 0.3,
            "emotional_clarity": 0.2,
            "technical_accuracy": 0.2,
        }

        # Sora2 best practices keywords
        self.positive_keywords = [
            "photorealistic", "4K", "cinematic", "shallow depth of field",
            "bokeh", "natural lighting", "film grain", "handheld",
            "POV", "dolly", "tracking", "close-up", "wide shot",
        ]

        self.negative_keywords = [
            "beautiful", "nice", "good", "amazing", "wonderful",
            "somehow", "kind of", "maybe", "perhaps",
        ]

    def _get_default_system_prompt(self) -> str:
        return """You are a video prompt quality expert specializing in Sora2.

Analyze prompts for:
1. Specificity - concrete, visual details vs vague descriptions
2. Sora2 Compatibility - proper structure, camera directions, lighting
3. Emotional Clarity - clear mood and atmosphere
4. Technical Accuracy - correct terminology, achievable shots

Output JSON:
{
  "score": 0-100,
  "breakdown": {
    "specificity": 0-100,
    "sora2_compatibility": 0-100,
    "emotional_clarity": 0-100,
    "technical_accuracy": 0-100
  },
  "issues": [
    {"severity": "error|warning|info", "message": "...", "suggestion": "..."}
  ],
  "suggestions": ["improvement suggestion 1", "..."]
}"""

    def process(self, input_data: Any) -> ValidationResult:
        """
        Validate a single prompt.

        Args:
            input_data: Prompt object or dict

        Returns:
            ValidationResult with scores and issues
        """
        if isinstance(input_data, dict):
            prompt = Prompt(**input_data)
        else:
            prompt = input_data

        return self.validate_prompt(prompt)

    def validate_prompt(self, prompt: Prompt) -> ValidationResult:
        """
        Validate a single prompt with detailed scoring.

        Args:
            prompt: Prompt to validate

        Returns:
            ValidationResult with breakdown and issues
        """
        text = prompt.english
        issues = []
        suggestions = []

        # Calculate individual scores
        specificity = self._score_specificity(text, issues)
        sora2_compat = self._score_sora2_compatibility(text, issues)
        emotional = self._score_emotional_clarity(text, prompt.structure, issues)
        technical = self._score_technical_accuracy(text, prompt.structure, issues)

        # Calculate weighted total
        total_score = int(
            specificity * self.weights["specificity"] +
            sora2_compat * self.weights["sora2_compatibility"] +
            emotional * self.weights["emotional_clarity"] +
            technical * self.weights["technical_accuracy"]
        )

        # Generate suggestions
        suggestions = self._generate_suggestions(text, issues)

        return ValidationResult(
            score=total_score,
            breakdown=ScoreBreakdown(
                specificity=specificity,
                sora2_compatibility=sora2_compat,
                emotional_clarity=emotional,
                technical_accuracy=technical,
            ),
            issues=issues,
            suggestions=suggestions,
            is_valid=total_score >= 60 and not any(
                i.severity == "error" for i in issues
            ),
        )

    def _score_specificity(
        self,
        text: str,
        issues: list[ValidationIssue],
    ) -> int:
        """Score prompt specificity (0-100)."""
        score = 70  # Base score

        # Check for concrete details
        concrete_patterns = [
            r'\b\d+\b',  # Numbers
            r'\b(small|large|tiny|huge|medium)\b',  # Sizes
            r'\b(red|blue|green|golden|cream|brown|white|black)\b',  # Colors
            r'\b(soft|rough|smooth|fluffy|shiny)\b',  # Textures
        ]

        for pattern in concrete_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                score += 5

        # Check for vague words
        vague_words = ["beautiful", "nice", "good", "somehow", "kind of"]
        for word in vague_words:
            if word.lower() in text.lower():
                score -= 10
                issues.append(ValidationIssue(
                    severity="warning",
                    message=f"Vague word detected: '{word}'",
                    suggestion=f"Replace '{word}' with specific visual description",
                ))

        # Length check
        word_count = len(text.split())
        if word_count < 30:
            score -= 15
            issues.append(ValidationIssue(
                severity="warning",
                message="Prompt may be too short",
                suggestion="Add more visual details for better results",
            ))
        elif word_count > 200:
            score -= 10
            issues.append(ValidationIssue(
                severity="info",
                message="Prompt may be too long",
                suggestion="Consider simplifying for better focus",
            ))

        return max(0, min(100, score))

    def _score_sora2_compatibility(
        self,
        text: str,
        issues: list[ValidationIssue],
    ) -> int:
        """Score Sora2 compatibility (0-100)."""
        score = 60  # Base score

        # Check for positive keywords
        for keyword in self.positive_keywords:
            if keyword.lower() in text.lower():
                score += 3

        # Check for required elements
        required_elements = {
            "character": r"(dog|cat|puppy|kitten|hedgehog|retriever|animal)",
            "setting": r"(room|garden|street|home|outdoor|indoor|living room)",
            "action": r"(walks|runs|sits|lies|carries|moves|looks)",
            "camera": r"(shot|dolly|tracking|handheld|POV|close-up|wide)",
            "lighting": r"(light|lighting|sunlight|lamp|golden|warm|soft)",
        }

        for element, pattern in required_elements.items():
            if not re.search(pattern, text, re.IGNORECASE):
                score -= 8
                issues.append(ValidationIssue(
                    severity="warning",
                    message=f"Missing {element} description",
                    suggestion=f"Add {element} details for better generation",
                ))

        # Check for audio descriptions (not supported)
        audio_patterns = r"\b(sound|music|bark|meow|noise|voice)\b"
        if re.search(audio_patterns, text, re.IGNORECASE):
            score -= 15
            issues.append(ValidationIssue(
                severity="error",
                message="Audio descriptions not supported",
                suggestion="Remove audio-related terms",
            ))

        return max(0, min(100, score))

    def _score_emotional_clarity(
        self,
        text: str,
        structure: Any,
        issues: list[ValidationIssue],
    ) -> int:
        """Score emotional clarity (0-100)."""
        score = 70  # Base score

        # Check for atmosphere keywords
        atmosphere_words = [
            "warm", "cold", "cozy", "tense", "peaceful", "sad",
            "happy", "melancholic", "hopeful", "gentle", "tender",
            "intimate", "dramatic", "magical",
        ]

        found_atmosphere = False
        for word in atmosphere_words:
            if word.lower() in text.lower():
                score += 5
                found_atmosphere = True

        if not found_atmosphere:
            score -= 15
            issues.append(ValidationIssue(
                severity="warning",
                message="No clear emotional atmosphere",
                suggestion="Add mood/atmosphere keywords",
            ))

        # Check structure for atmosphere
        if structure and hasattr(structure, 'atmosphere'):
            if structure.atmosphere:
                score += 10

        return max(0, min(100, score))

    def _score_technical_accuracy(
        self,
        text: str,
        structure: Any,
        issues: list[ValidationIssue],
    ) -> int:
        """Score technical accuracy (0-100)."""
        score = 75  # Base score

        # Check camera terminology
        valid_camera_terms = [
            "dolly", "tracking", "pan", "tilt", "crane", "handheld",
            "static", "push in", "pull out", "wide", "medium", "close-up",
            "extreme close-up", "POV", "overhead",
        ]

        found_camera = False
        for term in valid_camera_terms:
            if term.lower() in text.lower():
                found_camera = True
                score += 3

        if not found_camera:
            score -= 10
            issues.append(ValidationIssue(
                severity="warning",
                message="No camera movement specified",
                suggestion="Add camera direction (e.g., 'slow dolly in')",
            ))

        # Check for quality markers
        quality_markers = ["4K", "photorealistic", "cinematic", "film grain"]
        found_quality = False
        for marker in quality_markers:
            if marker.lower() in text.lower():
                found_quality = True
                score += 5

        if not found_quality:
            issues.append(ValidationIssue(
                severity="info",
                message="Consider adding quality markers",
                suggestion="Add '4K cinematic quality' or similar",
            ))

        return max(0, min(100, score))

    def _generate_suggestions(
        self,
        text: str,
        issues: list[ValidationIssue],
    ) -> list[str]:
        """Generate improvement suggestions based on issues."""
        suggestions = []

        error_count = sum(1 for i in issues if i.severity == "error")
        warning_count = sum(1 for i in issues if i.severity == "warning")

        if error_count > 0:
            suggestions.append("Fix critical errors before proceeding")

        if warning_count > 2:
            suggestions.append("Multiple areas need improvement")

        # Word count suggestion
        word_count = len(text.split())
        if word_count < 50:
            suggestions.append(
                "Add more detail: character features, environment, lighting"
            )
        elif word_count > 150:
            suggestions.append(
                "Focus on key visual elements, remove redundant descriptions"
            )

        # Structure suggestion
        if "." not in text[-50:]:
            suggestions.append("End with quality markers (e.g., '4K cinematic quality')")

        return suggestions

    def validate_prompts(
        self,
        prompts: list[Prompt],
    ) -> list[ValidationResult]:
        """
        Validate multiple prompts.

        Args:
            prompts: List of prompts to validate

        Returns:
            List of ValidationResult objects
        """
        return [self.validate_prompt(p) for p in prompts]

    def check_consistency(
        self,
        prompts: list[Prompt],
        character: Character | None = None,
    ) -> ConsistencyReport:
        """
        Check consistency across prompts.

        Args:
            prompts: List of prompts to check
            character: Optional character for reference

        Returns:
            ConsistencyReport with match scores
        """
        issues = []
        character_match = 1.0
        style_match = 1.0
        background_continuity = 1.0

        if len(prompts) < 2:
            return ConsistencyReport(
                is_consistent=True,
                character_match=1.0,
                style_match=1.0,
                background_continuity=1.0,
                issues=[],
            )

        # Check character consistency
        if character:
            ref_desc = character.sora2_prompt_fragment.lower()
            for i, prompt in enumerate(prompts):
                if ref_desc not in prompt.english.lower():
                    character_match -= 0.15
                    issues.append(
                        f"Scene {prompt.scene_id}: Character description doesn't match reference"
                    )

        # Check style consistency
        first_prompt = prompts[0].english.lower()
        style_indicators = []

        for indicator in ["photorealistic", "cinematic", "home video", "documentary"]:
            if indicator in first_prompt:
                style_indicators.append(indicator)

        for prompt in prompts[1:]:
            for indicator in style_indicators:
                if indicator not in prompt.english.lower():
                    style_match -= 0.1
                    if f"Style mismatch: missing '{indicator}'" not in issues:
                        issues.append(f"Style mismatch: missing '{indicator}' in some scenes")

        # Calculate overall consistency
        is_consistent = (
            character_match >= 0.7 and
            style_match >= 0.7 and
            len(issues) <= 2
        )

        return ConsistencyReport(
            is_consistent=is_consistent,
            character_match=max(0, character_match),
            style_match=max(0, style_match),
            background_continuity=background_continuity,
            issues=issues,
        )

    def get_overall_score(self, results: list[ValidationResult]) -> int:
        """Calculate overall score from multiple validation results."""
        if not results:
            return 0
        return int(sum(r.score for r in results) / len(results))

    def format_report(
        self,
        results: list[ValidationResult],
        consistency: ConsistencyReport | None = None,
    ) -> str:
        """Format validation results as readable report."""
        lines = ["# 프롬프트 검증 리포트", ""]

        # Overall score
        overall = self.get_overall_score(results)
        grade = "A" if overall >= 90 else "B" if overall >= 80 else "C" if overall >= 70 else "D" if overall >= 60 else "F"

        lines.extend([
            f"## 종합 점수: {overall}/100 ({grade})",
            "",
        ])

        # Consistency
        if consistency:
            status = "✅ 일관성 유지" if consistency.is_consistent else "⚠️ 일관성 문제"
            lines.extend([
                f"## 일관성: {status}",
                f"- 캐릭터 일치: {consistency.character_match:.0%}",
                f"- 스타일 일치: {consistency.style_match:.0%}",
                "",
            ])

            if consistency.issues:
                lines.append("### 일관성 이슈")
                for issue in consistency.issues:
                    lines.append(f"- {issue}")
                lines.append("")

        # Individual results
        lines.extend(["## 장면별 점수", ""])

        for result in results:
            lines.extend([
                f"### Scene (점수: {result.score}/100)",
                f"- 구체성: {result.breakdown.specificity}",
                f"- Sora2 호환성: {result.breakdown.sora2_compatibility}",
                f"- 감정 명확성: {result.breakdown.emotional_clarity}",
                f"- 기술 정확성: {result.breakdown.technical_accuracy}",
            ])

            if result.issues:
                lines.append("#### 이슈")
                for issue in result.issues:
                    icon = "❌" if issue.severity == "error" else "⚠️" if issue.severity == "warning" else "ℹ️"
                    lines.append(f"- {icon} {issue.message}")

            lines.append("")

        return "\n".join(lines)
