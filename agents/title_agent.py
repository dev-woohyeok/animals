"""Title Agent - Generate video titles for different platforms."""

from typing import Any

from core.models import Story, Prompt, TitleSet, PlatformTitles, TitleHooks
from .base import BaseAgent


class TitleAgent(BaseAgent[TitleSet]):
    """
    Generates optimized video titles for different platforms.

    Creates:
    - Main title with emotional hook
    - Platform-specific variants (YouTube Shorts, Instagram Reels, TikTok)
    - Multiple hook styles (emotional, curiosity, outcome)
    - Relevant hashtags
    """

    def __init__(self):
        super().__init__(
            name="TitleAgent",
            system_prompt_path="title_system.md",
        )

    def _get_default_system_prompt(self) -> str:
        return """You are a viral content specialist for animal-related short videos.

Your task is to create engaging titles that maximize views and emotional engagement.

TITLE STRATEGIES:
1. Emotional Hook: "눈물 없이 못 보는...", "가슴이 먹먹해지는..."
2. Curiosity Hook: "이 강아지에게 무슨 일이...", "믿기 힘든 일이..."
3. Outcome Hook: "기적 같은 결말", "반전 있는 이야기"

PLATFORM GUIDELINES:
- YouTube Shorts: 최대 100자, 감정 이모지 사용, "(실화)" 등 신뢰도 표시
- Instagram Reels: 세련된 톤, 적절한 이모지
- TikTok: 구어체, 강한 후킹, "...결말 보고 눈물남" 스타일

Output in JSON format:
{
  "main_title": "메인 제목",
  "subtitle": "부제목 (선택)",
  "platform_variants": {
    "youtube_shorts": "YouTube용 제목",
    "instagram_reels": "Instagram용 제목",
    "tiktok": "TikTok용 제목"
  },
  "hooks": {
    "emotional": "감정 자극형 제목",
    "curiosity": "호기심 유발형 제목",
    "outcome": "결과 강조형 제목"
  }
}"""

    def process(
        self,
        input_data: Any,
        prompts: list[Prompt] | None = None,
    ) -> TitleSet:
        """
        Generate title set from story and prompts.

        Args:
            input_data: Story object
            prompts: List of prompts (optional, for context)

        Returns:
            TitleSet object
        """
        if isinstance(input_data, dict):
            story = Story(**input_data)
        else:
            story = input_data

        # Build prompt
        user_message = self._build_title_prompt(story, prompts)

        # Call Claude
        response = self._call_claude(user_message)

        # Parse response
        return self._parse_title_response(response, story)

    def _build_title_prompt(
        self,
        story: Story,
        prompts: list[Prompt] | None,
    ) -> str:
        """Build prompt for title generation."""
        # Extract key emotions from story
        emotions = []
        for phase in story.arc:
            if phase.emotion:
                emotions.extend(phase.emotion.split(","))
        emotions = list(set([e.strip() for e in emotions]))

        # Build context
        context = f"""Story Information:
Title: {story.title}
Synopsis: {story.synopsis}
Key Emotions: {', '.join(emotions)}
Duration: {story.total_duration} seconds

Story Arc:
"""
        for phase in story.arc:
            context += f"- {phase.phase}: {phase.description}\n"

        if prompts:
            context += "\nKey Scenes:\n"
            for p in prompts[:3]:  # First 3 scenes
                context += f"- Scene {p.scene_id}: {p.structure.action}\n"

        return f"""{context}

Generate engaging titles optimized for Korean short-form video platforms.
Focus on emotional hooks that will make viewers want to watch."""

    def _parse_title_response(self, response: str, story: Story) -> TitleSet:
        """Parse response into TitleSet."""
        try:
            data = self._parse_json_response(response)

            platform_data = data.get("platform_variants", {})
            hooks_data = data.get("hooks", {})

            return TitleSet(
                main_title=data.get("main_title", story.title),
                subtitle=data.get("subtitle"),
                platform_variants=PlatformTitles(
                    youtube_shorts=platform_data.get(
                        "youtube_shorts",
                        f"💔 {story.title} (감동 실화)"
                    )[:100],
                    instagram_reels=platform_data.get(
                        "instagram_reels",
                        f"{story.title} ✨"
                    ),
                    tiktok=platform_data.get(
                        "tiktok",
                        f"{story.title}... 결말 보고 울었음"
                    ),
                ),
                hooks=TitleHooks(
                    emotional=hooks_data.get(
                        "emotional",
                        f"눈물 없이 못 보는 {story.title}"
                    ),
                    curiosity=hooks_data.get(
                        "curiosity",
                        f"이 동물에게 무슨 일이 있었을까?"
                    ),
                    outcome=hooks_data.get(
                        "outcome",
                        f"기적 같은 결말을 맞이한 {story.title}"
                    ),
                ),
            )

        except Exception as e:
            self.log(f"Parse error: {e}, creating defaults")
            return self._create_default_titles(story)

    def _create_default_titles(self, story: Story) -> TitleSet:
        """Create default title set."""
        return TitleSet(
            main_title=story.title,
            platform_variants=PlatformTitles(
                youtube_shorts=f"💔 {story.title} (감동 실화)"[:100],
                instagram_reels=f"{story.title} ✨",
                tiktok=f"{story.title}... 결말에 눈물남 😭",
            ),
            hooks=TitleHooks(
                emotional=f"눈물 없이 못 보는 {story.title}",
                curiosity=f"이 동물에게 무슨 일이 있었을까?",
                outcome=f"기적 같은 결말의 {story.title}",
            ),
        )

    def regenerate_for_platform(
        self,
        title_set: TitleSet,
        platform: str,
        feedback: str,
    ) -> TitleSet:
        """
        Regenerate title for a specific platform.

        Args:
            title_set: Current title set
            platform: Platform to regenerate (youtube_shorts, instagram_reels, tiktok)
            feedback: User feedback

        Returns:
            Updated TitleSet
        """
        current_title = getattr(title_set.platform_variants, platform, "")

        prompt = f"""Current {platform} title:
{current_title}

Feedback: {feedback}

Generate a better title for {platform}. Output only the new title, no explanation."""

        response = self._call_claude(prompt)
        new_title = response.strip().strip('"').strip("'")

        # Update the specific platform
        platform_dict = title_set.platform_variants.model_dump()
        platform_dict[platform] = new_title

        title_set.platform_variants = PlatformTitles(**platform_dict)
        return title_set
