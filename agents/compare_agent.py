"""Compare Agent - Side-by-side comparison and merging."""

from typing import Any
from dataclasses import dataclass
from enum import Enum

from core.models import Prompt, Scene, Story
from .base import BaseAgent


class DiffType(Enum):
    """Types of differences."""
    ADDED = "added"
    REMOVED = "removed"
    CHANGED = "changed"
    UNCHANGED = "unchanged"


@dataclass
class DiffResult:
    """Result of a diff operation."""
    diff_type: DiffType
    field: str
    value_a: Any
    value_b: Any

    def to_dict(self) -> dict:
        return {
            "type": self.diff_type.value,
            "field": self.field,
            "value_a": self.value_a,
            "value_b": self.value_b,
        }


class CompareAgent(BaseAgent[dict]):
    """
    Handles side-by-side comparison of prompts, scenes, and stories.

    Features:
    - Compare two versions of prompts
    - Highlight differences
    - Generate diff reports
    - Merge functionality
    """

    def __init__(self):
        super().__init__(
            name="CompareAgent",
            system_prompt_path="compare_system.md",
        )

    def _get_default_system_prompt(self) -> str:
        return """You are an expert at analyzing and comparing video prompts.

Given two versions of content, identify:
1. Structural differences
2. Semantic differences
3. Quality differences
4. Recommendation for which version to use

Output format:
{
  "summary": "Brief comparison summary",
  "differences": [...],
  "recommendation": "A or B",
  "merge_suggestion": "Merged content if applicable"
}"""

    def process(self, input_data: Any) -> dict:
        """
        Process comparison request.

        Args:
            input_data: Dict with 'a' and 'b' items to compare

        Returns:
            Comparison result dict
        """
        if not isinstance(input_data, dict):
            raise ValueError("Input must be dict with 'a' and 'b' keys")

        item_a = input_data.get("a")
        item_b = input_data.get("b")

        if isinstance(item_a, Prompt) and isinstance(item_b, Prompt):
            return self.compare_prompts(item_a, item_b)
        elif isinstance(item_a, Scene) and isinstance(item_b, Scene):
            return self.compare_scenes(item_a, item_b)
        elif isinstance(item_a, Story) and isinstance(item_b, Story):
            return self.compare_stories(item_a, item_b)
        elif isinstance(item_a, str) and isinstance(item_b, str):
            return self.compare_text(item_a, item_b)

        return {"error": "Unsupported comparison types"}

    # ============================================================
    # Prompt Comparison
    # ============================================================

    def compare_prompts(self, prompt_a: Prompt, prompt_b: Prompt) -> dict:
        """
        Compare two prompts in detail.

        Args:
            prompt_a: First prompt
            prompt_b: Second prompt

        Returns:
            Detailed comparison dict
        """
        diffs = []

        # Compare main text
        if prompt_a.english != prompt_b.english:
            text_diff = self._compare_text_detailed(
                prompt_a.english, prompt_b.english
            )
            diffs.append(DiffResult(
                diff_type=DiffType.CHANGED,
                field="english",
                value_a=prompt_a.english,
                value_b=prompt_b.english,
            ))

        # Compare structure fields
        struct_a = prompt_a.structure
        struct_b = prompt_b.structure

        structure_fields = [
            "character_desc", "setting", "action",
            "camera", "lighting", "atmosphere"
        ]

        for field in structure_fields:
            val_a = getattr(struct_a, field, None)
            val_b = getattr(struct_b, field, None)

            if val_a != val_b:
                diffs.append(DiffResult(
                    diff_type=DiffType.CHANGED,
                    field=f"structure.{field}",
                    value_a=val_a,
                    value_b=val_b,
                ))

        # Calculate similarity
        similarity = self._calculate_text_similarity(
            prompt_a.english, prompt_b.english
        )

        return {
            "type": "prompt_comparison",
            "scene_id": prompt_a.scene_id,
            "differences": [d.to_dict() for d in diffs],
            "diff_count": len(diffs),
            "similarity": similarity,
            "summary": self._generate_prompt_summary(diffs, similarity),
        }

    def _compare_text_detailed(self, text_a: str, text_b: str) -> dict:
        """Compare two texts and return detailed diff."""
        words_a = text_a.split()
        words_b = text_b.split()

        # Simple word-level comparison
        set_a = set(words_a)
        set_b = set(words_b)

        added = set_b - set_a
        removed = set_a - set_b
        common = set_a & set_b

        return {
            "added_words": list(added)[:20],
            "removed_words": list(removed)[:20],
            "common_count": len(common),
            "word_count_a": len(words_a),
            "word_count_b": len(words_b),
        }

    def _calculate_text_similarity(self, text_a: str, text_b: str) -> float:
        """Calculate similarity between two texts."""
        if not text_a and not text_b:
            return 1.0
        if not text_a or not text_b:
            return 0.0

        words_a = set(text_a.lower().split())
        words_b = set(text_b.lower().split())

        intersection = len(words_a & words_b)
        union = len(words_a | words_b)

        return intersection / union if union > 0 else 0.0

    def _generate_prompt_summary(
        self,
        diffs: list[DiffResult],
        similarity: float,
    ) -> str:
        """Generate human-readable summary."""
        if not diffs:
            return "두 프롬프트가 동일합니다."

        changed_fields = [d.field for d in diffs]

        if similarity > 0.8:
            level = "약간"
        elif similarity > 0.5:
            level = "상당히"
        else:
            level = "크게"

        return f"두 프롬프트가 {level} 다릅니다. 변경된 필드: {', '.join(changed_fields)}"

    # ============================================================
    # Scene Comparison
    # ============================================================

    def compare_scenes(self, scene_a: Scene, scene_b: Scene) -> dict:
        """Compare two scenes."""
        diffs = []

        # Compare basic fields
        basic_fields = ["title", "description", "action", "emotion", "lighting", "duration"]

        for field in basic_fields:
            val_a = getattr(scene_a, field, None)
            val_b = getattr(scene_b, field, None)

            if val_a != val_b:
                diffs.append(DiffResult(
                    diff_type=DiffType.CHANGED,
                    field=field,
                    value_a=val_a,
                    value_b=val_b,
                ))

        # Compare camera settings
        if scene_a.camera.movement != scene_b.camera.movement:
            diffs.append(DiffResult(
                diff_type=DiffType.CHANGED,
                field="camera.movement",
                value_a=scene_a.camera.movement,
                value_b=scene_b.camera.movement,
            ))

        if scene_a.camera.angle != scene_b.camera.angle:
            diffs.append(DiffResult(
                diff_type=DiffType.CHANGED,
                field="camera.angle",
                value_a=scene_a.camera.angle,
                value_b=scene_b.camera.angle,
            ))

        return {
            "type": "scene_comparison",
            "scene_number": scene_a.scene_number,
            "differences": [d.to_dict() for d in diffs],
            "diff_count": len(diffs),
            "summary": f"씬 비교: {len(diffs)}개 차이점 발견",
        }

    # ============================================================
    # Story Comparison
    # ============================================================

    def compare_stories(self, story_a: Story, story_b: Story) -> dict:
        """Compare two stories."""
        diffs = []

        # Compare basic info
        if story_a.title != story_b.title:
            diffs.append(DiffResult(
                diff_type=DiffType.CHANGED,
                field="title",
                value_a=story_a.title,
                value_b=story_b.title,
            ))

        if story_a.synopsis != story_b.synopsis:
            diffs.append(DiffResult(
                diff_type=DiffType.CHANGED,
                field="synopsis",
                value_a=story_a.synopsis,
                value_b=story_b.synopsis,
            ))

        # Compare arc phases
        arc_diffs = self._compare_arcs(story_a.arc, story_b.arc)
        diffs.extend(arc_diffs)

        return {
            "type": "story_comparison",
            "differences": [d.to_dict() for d in diffs],
            "diff_count": len(diffs),
            "arc_diff_count": len(arc_diffs),
            "summary": f"스토리 비교: {len(diffs)}개 차이점 ({len(arc_diffs)}개 arc 변경)",
        }

    def _compare_arcs(self, arc_a: list, arc_b: list) -> list[DiffResult]:
        """Compare story arcs."""
        diffs = []

        max_len = max(len(arc_a), len(arc_b))

        for i in range(max_len):
            if i >= len(arc_a):
                diffs.append(DiffResult(
                    diff_type=DiffType.ADDED,
                    field=f"arc[{i}]",
                    value_a=None,
                    value_b=arc_b[i].phase if i < len(arc_b) else None,
                ))
            elif i >= len(arc_b):
                diffs.append(DiffResult(
                    diff_type=DiffType.REMOVED,
                    field=f"arc[{i}]",
                    value_a=arc_a[i].phase,
                    value_b=None,
                ))
            elif arc_a[i].description != arc_b[i].description:
                diffs.append(DiffResult(
                    diff_type=DiffType.CHANGED,
                    field=f"arc[{i}].description",
                    value_a=arc_a[i].description[:50] + "...",
                    value_b=arc_b[i].description[:50] + "...",
                ))

        return diffs

    # ============================================================
    # Text Comparison
    # ============================================================

    def compare_text(self, text_a: str, text_b: str) -> dict:
        """Compare two text strings."""
        detailed = self._compare_text_detailed(text_a, text_b)
        similarity = self._calculate_text_similarity(text_a, text_b)

        return {
            "type": "text_comparison",
            "similarity": similarity,
            "details": detailed,
            "summary": f"텍스트 유사도: {similarity:.0%}",
        }

    # ============================================================
    # Formatting
    # ============================================================

    def format_side_by_side(
        self,
        item_a: Any,
        item_b: Any,
        label_a: str = "Version A",
        label_b: str = "Version B",
        width: int = 50,
    ) -> str:
        """
        Format two items side by side for display.

        Args:
            item_a: First item
            item_b: Second item
            label_a: Label for first item
            label_b: Label for second item
            width: Width of each column

        Returns:
            Formatted string
        """
        lines = []

        # Header
        header = f"{'─' * width}┬{'─' * width}"
        lines.append(header)
        lines.append(f"{label_a:^{width}}│{label_b:^{width}}")
        lines.append(header)

        # Get text content
        if isinstance(item_a, Prompt):
            text_a = item_a.english
            text_b = item_b.english if isinstance(item_b, Prompt) else str(item_b)
        else:
            text_a = str(item_a)
            text_b = str(item_b)

        # Split into lines and pad
        lines_a = self._wrap_text(text_a, width - 2)
        lines_b = self._wrap_text(text_b, width - 2)

        max_lines = max(len(lines_a), len(lines_b))

        for i in range(max_lines):
            line_a = lines_a[i] if i < len(lines_a) else ""
            line_b = lines_b[i] if i < len(lines_b) else ""
            lines.append(f" {line_a:<{width-1}}│ {line_b:<{width-1}}")

        # Footer
        lines.append(f"{'─' * width}┴{'─' * width}")

        return "\n".join(lines)

    def _wrap_text(self, text: str, width: int) -> list[str]:
        """Wrap text to specified width."""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(" ".join(current_line))

        return lines or [""]

    def format_diff_report(self, comparison: dict) -> str:
        """
        Format comparison result as a readable report.

        Args:
            comparison: Comparison result dict

        Returns:
            Formatted report string
        """
        lines = [
            "# 비교 리포트",
            "",
            f"**타입:** {comparison.get('type', 'unknown')}",
            f"**요약:** {comparison.get('summary', '')}",
            "",
        ]

        if "similarity" in comparison:
            lines.append(f"**유사도:** {comparison['similarity']:.0%}")
            lines.append("")

        diffs = comparison.get("differences", [])
        if diffs:
            lines.append("## 차이점")
            lines.append("")

            for diff in diffs:
                diff_type = diff.get("type", "changed")
                field = diff.get("field", "")

                if diff_type == "added":
                    lines.append(f"+ **{field}**: {diff.get('value_b', '')}")
                elif diff_type == "removed":
                    lines.append(f"- **{field}**: {diff.get('value_a', '')}")
                else:
                    lines.append(f"~ **{field}**:")
                    lines.append(f"  - A: {diff.get('value_a', '')}")
                    lines.append(f"  - B: {diff.get('value_b', '')}")

            lines.append("")
        else:
            lines.append("*차이점 없음*")

        return "\n".join(lines)

    # ============================================================
    # Merge Functionality
    # ============================================================

    def merge_prompts(
        self,
        prompt_a: Prompt,
        prompt_b: Prompt,
        prefer: str = "a",
        merge_fields: list[str] | None = None,
    ) -> Prompt:
        """
        Merge two prompts.

        Args:
            prompt_a: First prompt
            prompt_b: Second prompt
            prefer: Which to prefer for conflicts ("a" or "b")
            merge_fields: Specific fields to take from the non-preferred

        Returns:
            Merged Prompt
        """
        from copy import deepcopy
        from core.models import PromptStructure

        # Start with preferred prompt
        base = prompt_a if prefer == "a" else prompt_b
        other = prompt_b if prefer == "a" else prompt_a

        merged = deepcopy(base)

        # Apply specific field overrides
        if merge_fields:
            other_struct = other.structure
            merged_struct = merged.structure

            for field in merge_fields:
                if hasattr(other_struct, field):
                    setattr(merged_struct, field, getattr(other_struct, field))

            merged.structure = merged_struct

        return merged

    def suggest_merge(
        self,
        prompt_a: Prompt,
        prompt_b: Prompt,
    ) -> dict:
        """
        Suggest a merge strategy for two prompts.

        Returns:
            Dict with merge suggestion and reasoning
        """
        comparison = self.compare_prompts(prompt_a, prompt_b)

        # Analyze which has better attributes
        scores = {"a": 0, "b": 0}

        # Score based on length (moderate length preferred)
        len_a = len(prompt_a.english.split())
        len_b = len(prompt_b.english.split())

        # Prefer prompts between 30-80 words
        if 30 <= len_a <= 80:
            scores["a"] += 1
        if 30 <= len_b <= 80:
            scores["b"] += 1

        # Score based on structure completeness
        struct_a = prompt_a.structure
        struct_b = prompt_b.structure

        for field in ["character_desc", "setting", "action", "camera", "lighting"]:
            val_a = getattr(struct_a, field, "") or ""
            val_b = getattr(struct_b, field, "") or ""

            if len(val_a) > len(val_b):
                scores["a"] += 1
            elif len(val_b) > len(val_a):
                scores["b"] += 1

        preferred = "a" if scores["a"] >= scores["b"] else "b"

        return {
            "preferred": preferred,
            "scores": scores,
            "reasoning": f"Version {preferred.upper()} 선호 (A: {scores['a']}점, B: {scores['b']}점)",
            "suggestion": f"기본: Version {preferred.upper()}, 필요시 다른 버전의 특정 필드 병합 가능",
        }
