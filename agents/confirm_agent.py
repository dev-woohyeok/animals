"""Confirm Agent - Handle user confirmation at each step."""

from typing import Any, Callable

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.markdown import Markdown

from core.models import Story, Scene, Prompt, TitleSet
from .base import BaseAgent


class ConfirmAgent(BaseAgent[bool]):
    """
    Handles user confirmation and feedback at each workflow step.

    Features:
    - Display formatted content for review
    - Collect user approval or feedback
    - Route modifications back to appropriate agents
    """

    def __init__(self):
        super().__init__(
            name="ConfirmAgent",
            system_prompt_path=None,
        )
        self.console = Console()

    def _get_default_system_prompt(self) -> str:
        return ""  # This agent doesn't use Claude

    def process(self, input_data: Any) -> bool:
        """Not used directly - use specific confirm methods."""
        return True

    def confirm_story(self, story: Story) -> tuple[bool, str | None]:
        """
        Display story for user confirmation.

        Args:
            story: Story to confirm

        Returns:
            Tuple of (approved, feedback if not approved)
        """
        self.console.print()
        self.console.print(Panel(
            f"[bold]{story.title}[/bold]\n\n{story.synopsis}",
            title="📖 생성된 스토리",
            border_style="blue",
        ))

        # Display story arc
        table = Table(title="스토리 아크", show_header=True)
        table.add_column("단계", style="cyan")
        table.add_column("설명", style="white")
        table.add_column("감정", style="yellow")

        for phase in story.arc:
            table.add_row(
                phase.phase,
                phase.description,
                phase.emotion,
            )

        self.console.print(table)
        self.console.print()

        # Get confirmation
        choice = Prompt.ask(
            "이 스토리가 괜찮으신가요?",
            choices=["y", "n", "e"],
            default="y",
        )

        if choice == "y":
            return True, None
        elif choice == "e":
            feedback = Prompt.ask("수정 사항을 입력하세요")
            return False, feedback
        else:
            return False, "재생성 요청"

    def confirm_scenes(self, scenes: list[Scene]) -> tuple[bool, str | None, int | None]:
        """
        Display scenes for user confirmation.

        Args:
            scenes: List of scenes to confirm

        Returns:
            Tuple of (approved, feedback, scene_id to modify)
        """
        self.console.print()
        self.console.print(Panel(
            f"총 {len(scenes)}개 장면, {sum(s.duration for s in scenes)}초",
            title="🎬 장면 분할",
            border_style="green",
        ))

        # Display scenes table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=3)
        table.add_column("제목", width=15)
        table.add_column("시간", width=5)
        table.add_column("감정", width=12)
        table.add_column("카메라", width=15)

        for scene in scenes:
            table.add_row(
                str(scene.id),
                scene.title,
                f"{scene.duration}s",
                scene.emotion,
                f"{scene.camera.movement}",
            )

        self.console.print(table)
        self.console.print()

        # Get confirmation
        choice = Prompt.ask(
            "장면 분할이 괜찮으신가요?",
            choices=["y", "n", "e"],
            default="y",
        )

        if choice == "y":
            return True, None, None
        elif choice == "e":
            scene_id = int(Prompt.ask("수정할 장면 번호"))
            feedback = Prompt.ask("수정 사항을 입력하세요")
            return False, feedback, scene_id
        else:
            return False, "전체 재생성 요청", None

    def confirm_prompts(self, prompts: list[Prompt]) -> tuple[bool, str | None, int | None]:
        """
        Display prompts for user confirmation.

        Args:
            prompts: List of prompts to confirm

        Returns:
            Tuple of (approved, feedback, prompt scene_id to modify)
        """
        self.console.print()

        for prompt in prompts:
            panel_content = f"""[bold cyan]🇺🇸 English:[/bold cyan]
{prompt.english}

[bold yellow]🇰🇷 한국어:[/bold yellow]
{prompt.korean or '(번역 대기 중)'}"""

            score_text = ""
            if prompt.quality_score:
                score_text = f" | 품질: {prompt.quality_score}/100"

            self.console.print(Panel(
                panel_content,
                title=f"[Scene {prompt.scene_id}]{score_text}",
                border_style="cyan",
            ))

        self.console.print()

        # Get confirmation
        choice = Prompt.ask(
            "프롬프트가 괜찮으신가요?",
            choices=["y", "n", "e"],
            default="y",
        )

        if choice == "y":
            return True, None, None
        elif choice == "e":
            scene_id = int(Prompt.ask("수정할 장면 번호"))
            feedback = Prompt.ask("수정 사항을 입력하세요")
            return False, feedback, scene_id
        else:
            return False, "전체 재생성 요청", None

    def confirm_titles(self, titles: TitleSet) -> tuple[bool, str | None]:
        """
        Display titles for user confirmation.

        Args:
            titles: TitleSet to confirm

        Returns:
            Tuple of (approved, feedback)
        """
        self.console.print()
        self.console.print(Panel(
            f"[bold]{titles.main_title}[/bold]",
            title="🏷️ 생성된 제목",
            border_style="magenta",
        ))

        # Platform variants
        table = Table(title="플랫폼별 제목", show_header=True)
        table.add_column("플랫폼", style="cyan", width=15)
        table.add_column("제목", style="white")

        table.add_row("YouTube Shorts", titles.platform_variants.youtube_shorts)
        table.add_row("Instagram Reels", titles.platform_variants.instagram_reels)
        table.add_row("TikTok", titles.platform_variants.tiktok)

        self.console.print(table)

        # Hooks
        self.console.print()
        self.console.print("[bold]후킹 변형:[/bold]")
        self.console.print(f"  감정형: {titles.hooks.emotional}")
        self.console.print(f"  호기심형: {titles.hooks.curiosity}")
        self.console.print(f"  결과형: {titles.hooks.outcome}")
        self.console.print()

        # Get confirmation
        choice = Prompt.ask(
            "제목이 괜찮으신가요?",
            choices=["y", "n", "e"],
            default="y",
        )

        if choice == "y":
            return True, None
        elif choice == "e":
            feedback = Prompt.ask("수정 사항을 입력하세요")
            return False, feedback
        else:
            return False, "재생성 요청"

    def confirm_final(
        self,
        story: Story,
        scenes: list[Scene],
        prompts: list[Prompt],
        titles: TitleSet,
    ) -> bool:
        """
        Final confirmation before output.

        Args:
            story: Final story
            scenes: Final scenes
            prompts: Final prompts
            titles: Final titles

        Returns:
            Whether to proceed with output
        """
        self.console.print()
        self.console.print(Panel(
            f"""[bold]{story.title}[/bold]

📖 스토리: {story.synopsis}
🎬 장면 수: {len(scenes)}개 ({sum(s.duration for s in scenes)}초)
✨ 프롬프트: {len(prompts)}개
🏷️ 제목: {titles.main_title}
#️⃣ 해시태그: {len(titles.hashtags)}개""",
            title="✅ 최종 확인",
            border_style="green",
        ))

        return Confirm.ask("이대로 출력하시겠습니까?", default=True)

    def get_user_input(self, prompt_text: str, default: str = "") -> str:
        """Get text input from user."""
        return Prompt.ask(prompt_text, default=default)

    def get_choice(
        self,
        prompt_text: str,
        choices: list[str],
        default: str | None = None,
    ) -> str:
        """Get choice from user."""
        return Prompt.ask(prompt_text, choices=choices, default=default)

    def display_message(self, message: str, style: str = "info") -> None:
        """Display a message to the user."""
        styles = {
            "info": "blue",
            "success": "green",
            "warning": "yellow",
            "error": "red",
        }
        self.console.print(f"[{styles.get(style, 'white')}]{message}[/]")

    def display_progress(self, message: str) -> None:
        """Display progress message."""
        self.console.print(f"[dim]⏳ {message}...[/dim]")
