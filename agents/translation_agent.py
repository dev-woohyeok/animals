"""Translation Agent - Translate English prompts to Korean."""

from typing import Any

from core.models import Prompt
from .base import BaseAgent


class TranslationAgent(BaseAgent[list[Prompt]]):
    """
    Translates English prompts to Korean for user review.

    The Korean translation is for understanding only;
    the English prompt is used for Sora2.
    """

    def __init__(self):
        super().__init__(
            name="TranslationAgent",
            system_prompt_path="translation_system.md",
        )

    def _get_default_system_prompt(self) -> str:
        return """You are a professional Korean translator specializing in video production terminology.

Your task is to translate English video generation prompts to Korean for user review.

Guidelines:
1. Translate naturally, not word-for-word
2. Keep technical terms understandable:
   - "dolly shot" → "달리 샷" or "전진/후진 촬영"
   - "close-up" → "클로즈업"
   - "golden hour" → "골든아워(해질녘 조명)"
3. Preserve the structure and flow
4. Make it easy for Korean speakers to understand what the video will look like

Output format (JSON):
{
  "translations": [
    {
      "scene_id": 1,
      "korean": "한국어 번역..."
    },
    ...
  ]
}"""

    def process(self, input_data: Any) -> list[Prompt]:
        """
        Translate prompts to Korean.

        Args:
            input_data: List of Prompt objects

        Returns:
            List of Prompt objects with Korean translations
        """
        prompts = input_data if isinstance(input_data, list) else [input_data]

        # Batch translate for efficiency
        user_message = self._build_translation_request(prompts)
        response = self._call_claude(user_message)

        return self._apply_translations(prompts, response)

    def _build_translation_request(self, prompts: list[Prompt]) -> str:
        """Build translation request."""
        prompt_texts = "\n\n".join([
            f"[Scene {p.scene_id}]\n{p.english}"
            for p in prompts
        ])

        return f"""Translate these video prompts to Korean:

{prompt_texts}

Provide natural Korean translations that help the user understand what each video scene will look like."""

    def _apply_translations(
        self,
        prompts: list[Prompt],
        response: str,
    ) -> list[Prompt]:
        """Apply translations to prompts."""
        try:
            data = self._parse_json_response(response)
            translations = {
                t["scene_id"]: t["korean"]
                for t in data.get("translations", [])
            }

            # Apply translations
            for prompt in prompts:
                if prompt.scene_id in translations:
                    prompt.korean = translations[prompt.scene_id]

            return prompts

        except Exception as e:
            self.log(f"Translation parse error: {e}")
            # Try to extract translations from plain text
            return self._extract_translations_fallback(prompts, response)

    def _extract_translations_fallback(
        self,
        prompts: list[Prompt],
        response: str,
    ) -> list[Prompt]:
        """Fallback translation extraction from plain text."""
        # Simple heuristic: look for scene markers
        lines = response.split("\n")
        current_scene = None
        current_translation = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check for scene marker
            if "[Scene" in line or "장면" in line:
                if current_scene and current_translation:
                    # Apply previous translation
                    for prompt in prompts:
                        if prompt.scene_id == current_scene:
                            prompt.korean = " ".join(current_translation)
                            break

                # Extract scene number
                try:
                    import re
                    match = re.search(r"(\d+)", line)
                    if match:
                        current_scene = int(match.group(1))
                        current_translation = []
                except:
                    pass
            elif current_scene:
                current_translation.append(line)

        # Apply last translation
        if current_scene and current_translation:
            for prompt in prompts:
                if prompt.scene_id == current_scene:
                    prompt.korean = " ".join(current_translation)
                    break

        return prompts

    def translate_single(self, text: str) -> str:
        """
        Translate a single text to Korean.

        Args:
            text: English text

        Returns:
            Korean translation
        """
        response = self._call_claude(
            f"Translate this video prompt to Korean:\n\n{text}\n\nProvide only the Korean translation, no explanations."
        )
        return response.strip()
