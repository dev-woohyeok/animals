"""Base agent class for all agents."""

import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, TypeVar, Generic

from anthropic import Anthropic
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseAgent(ABC, Generic[T]):
    """
    Base class for all agents in the system.

    Each agent:
    - Has a specific role and system prompt
    - Processes input and produces typed output
    - Can interact with the Claude API
    """

    def __init__(
        self,
        name: str,
        system_prompt_path: str | None = None,
        model: str = "claude-sonnet-4-20250514",
    ):
        """
        Initialize the agent.

        Args:
            name: Agent name for logging
            system_prompt_path: Path to system prompt file (relative to prompts/)
            model: Claude model to use
        """
        self.name = name
        self.model = model
        self.client = Anthropic()

        # Load system prompt
        self.system_prompt = self._load_system_prompt(system_prompt_path)

    def _load_system_prompt(self, path: str | None) -> str:
        """Load system prompt from file."""
        if path is None:
            return self._get_default_system_prompt()

        # Get project root
        project_root = Path(__file__).parent.parent
        prompt_file = project_root / "prompts" / path

        if prompt_file.exists():
            return prompt_file.read_text(encoding="utf-8")
        else:
            print(f"Warning: System prompt not found at {prompt_file}")
            return self._get_default_system_prompt()

    @abstractmethod
    def _get_default_system_prompt(self) -> str:
        """Return default system prompt if file not found."""
        pass

    @abstractmethod
    def process(self, input_data: Any) -> T:
        """
        Process input and return typed output.

        Args:
            input_data: Input data for processing

        Returns:
            Processed output of type T
        """
        pass

    def _call_claude(
        self,
        user_message: str,
        system_prompt: str | None = None,
        max_tokens: int = 4096,
    ) -> str:
        """
        Call Claude API with the given message.

        Args:
            user_message: User message to send
            system_prompt: Override system prompt (optional)
            max_tokens: Maximum tokens in response

        Returns:
            Claude's response text
        """
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system_prompt or self.system_prompt,
            messages=[
                {"role": "user", "content": user_message}
            ],
        )

        # Extract text from response
        if response.content and len(response.content) > 0:
            return response.content[0].text
        return ""

    def _parse_yaml_response(self, response: str) -> dict:
        """
        Parse YAML from Claude's response.

        Args:
            response: Response text that may contain YAML

        Returns:
            Parsed dictionary
        """
        import yaml

        # Try to extract YAML block
        if "```yaml" in response:
            yaml_start = response.index("```yaml") + 7
            yaml_end = response.index("```", yaml_start)
            yaml_content = response[yaml_start:yaml_end].strip()
        elif "```" in response:
            yaml_start = response.index("```") + 3
            yaml_end = response.index("```", yaml_start)
            yaml_content = response[yaml_start:yaml_end].strip()
        else:
            yaml_content = response.strip()

        return yaml.safe_load(yaml_content)

    def _parse_json_response(self, response: str) -> dict:
        """
        Parse JSON from Claude's response.

        Args:
            response: Response text that may contain JSON

        Returns:
            Parsed dictionary
        """
        import json

        # Try to extract JSON block
        if "```json" in response:
            json_start = response.index("```json") + 7
            json_end = response.index("```", json_start)
            json_content = response[json_start:json_end].strip()
        elif "```" in response:
            json_start = response.index("```") + 3
            json_end = response.index("```", json_start)
            json_content = response[json_start:json_end].strip()
        else:
            json_content = response.strip()

        return json.loads(json_content)

    def log(self, message: str) -> None:
        """Log a message with agent name prefix."""
        print(f"[{self.name}] {message}")
