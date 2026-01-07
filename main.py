#!/usr/bin/env python3
"""
Animal Shorts Agent System - Main Entry Point

동물 관련 감동 쇼츠 영상 제작을 위한 AI 에이전트 시스템
"""

import sys
import uuid
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from core.models import (
    Project,
    ProjectStatus,
    InputData,
    Character,
    VisualDescription,
)
from agents.input_agent import InputAgent
from agents.story_agent import StoryAgent
from agents.scene_agent import SceneAgent
from agents.prompt_agent import PromptAgent
from agents.translation_agent import TranslationAgent
from agents.title_agent import TitleAgent
from agents.confirm_agent import ConfirmAgent
from agents.output_agent import OutputAgent


class AnimalShortsSystem:
    """Main orchestrator for the Animal Shorts Agent System."""

    def __init__(self):
        self.console = Console()

        # Initialize agents
        self.input_agent = InputAgent()
        self.story_agent = StoryAgent()
        self.scene_agent = SceneAgent(target_scenes=6)
        self.prompt_agent = PromptAgent()
        self.translation_agent = TranslationAgent()
        self.title_agent = TitleAgent()
        self.confirm_agent = ConfirmAgent()
        self.output_agent = OutputAgent()

        # Current project
        self.project: Project | None = None

    def run(self):
        """Run the main application loop."""
        self._show_welcome()

        while True:
            choice = self._show_main_menu()

            if choice == "1":
                self._new_project()
            elif choice == "2":
                self._load_project()
            elif choice == "3":
                self._manage_library()
            elif choice == "q":
                self._exit()
                break

    def _show_welcome(self):
        """Show welcome message."""
        self.console.print()
        self.console.print(Panel(
            """[bold cyan]🐾 Animal Shorts Agent System v2.0[/bold cyan]

동물 관련 감동 쇼츠 영상 제작을 위한 AI 에이전트 시스템
Sora2 최적화 프롬프트를 자동으로 생성합니다.""",
            border_style="cyan",
        ))

    def _show_main_menu(self) -> str:
        """Show main menu and get choice."""
        self.console.print()
        self.console.print("[bold]메인 메뉴[/bold]")
        self.console.print("  [1] 새 프로젝트 시작")
        self.console.print("  [2] 기존 프로젝트 열기")
        self.console.print("  [3] 라이브러리 관리")
        self.console.print("  [q] 종료")
        self.console.print()

        return Prompt.ask("선택", choices=["1", "2", "3", "q"], default="1")

    def _new_project(self):
        """Start a new project workflow."""
        self.console.print()
        self.console.print(Panel("🆕 새 프로젝트", border_style="green"))

        # Step 1: Get user input
        self.console.print()
        self.console.print("[bold]Step 1: 입력[/bold]")
        self.console.print("동물 키워드와 줄거리를 입력하세요.")
        self.console.print("[dim]형식: 동물 / 상황 / 감정 / 결말(선택)[/dim]")
        self.console.print("[dim]예: 골든 리트리버 강아지 / 버려진 후 노인을 만남 / 따뜻함, 감동[/dim]")
        self.console.print()

        raw_input = Prompt.ask("입력")

        # Parse input
        self.confirm_agent.display_progress("입력 분석 중")
        input_data = self.input_agent.process(raw_input)

        # Create project
        project_id = str(uuid.uuid4())[:8]
        slug = self._create_slug(input_data.animal)

        self.project = Project(
            id=project_id,
            slug=slug,
            name=f"{input_data.animal}의 이야기",
            input_data=input_data,
            status=ProjectStatus.IN_PROGRESS,
        )

        # Create character if not selected
        if not self.project.character:
            self.project.character = self._create_character_from_input(input_data)

        # Step 2: Generate Story
        self.console.print()
        self.console.print("[bold]Step 2: 스토리 생성[/bold]")
        self.confirm_agent.display_progress("스토리 생성 중")

        story = self.story_agent.process(input_data)
        self.project.story = story

        # Confirm story
        approved, feedback = self.confirm_agent.confirm_story(story)
        while not approved:
            if feedback:
                self.confirm_agent.display_progress("스토리 수정 중")
                story = self.story_agent.regenerate_phase(story, "전체", feedback)
                self.project.story = story
            approved, feedback = self.confirm_agent.confirm_story(story)

        # Step 3: Scene Division
        self.console.print()
        self.console.print("[bold]Step 3: 장면 분할[/bold]")
        self.confirm_agent.display_progress("장면 분할 중")

        scenes = self.scene_agent.process(story)
        self.project.scenes = scenes

        # Confirm scenes
        approved, feedback, scene_id = self.confirm_agent.confirm_scenes(scenes)
        while not approved:
            if scene_id and feedback:
                self.confirm_agent.display_progress(f"장면 {scene_id} 수정 중")
                scenes = self.scene_agent.regenerate_scene(scenes, scene_id, feedback)
            elif feedback:
                self.confirm_agent.display_progress("장면 재생성 중")
                scenes = self.scene_agent.process(story)
            self.project.scenes = scenes
            approved, feedback, scene_id = self.confirm_agent.confirm_scenes(scenes)

        # Step 4: Generate Prompts
        self.console.print()
        self.console.print("[bold]Step 4: 프롬프트 생성[/bold]")

        # Select style
        style_choice = Prompt.ask(
            "스타일 선택",
            choices=["1", "2"],
            default="1",
        )
        style_id = "cinematic_realistic" if style_choice == "1" else "anime_style"
        self.project.style_id = style_id
        self.prompt_agent.style_id = style_id

        self.confirm_agent.display_progress("Sora2 프롬프트 생성 중")
        prompts = self.prompt_agent.process(scenes, self.project.character)
        self.project.prompts = prompts

        # Step 5: Translate
        self.console.print()
        self.console.print("[bold]Step 5: 한국어 번역[/bold]")
        self.confirm_agent.display_progress("번역 중")

        prompts = self.translation_agent.process(prompts)
        self.project.prompts = prompts

        # Confirm prompts
        approved, feedback, scene_id = self.confirm_agent.confirm_prompts(prompts)
        while not approved:
            if scene_id and feedback:
                prompt_to_fix = next((p for p in prompts if p.scene_id == scene_id), None)
                if prompt_to_fix:
                    self.confirm_agent.display_progress(f"프롬프트 {scene_id} 수정 중")
                    char_desc = self.project.character.sora2_prompt_fragment if self.project.character else ""
                    new_prompt = self.prompt_agent.regenerate_prompt(
                        prompt_to_fix, feedback, char_desc
                    )
                    prompts = [new_prompt if p.scene_id == scene_id else p for p in prompts]
                    # Re-translate
                    prompts = self.translation_agent.process(prompts)
            self.project.prompts = prompts
            approved, feedback, scene_id = self.confirm_agent.confirm_prompts(prompts)

        # Step 6: Generate Titles
        self.console.print()
        self.console.print("[bold]Step 6: 제목 생성[/bold]")
        self.confirm_agent.display_progress("제목 생성 중")

        titles = self.title_agent.process(story, prompts)
        self.project.titles = titles

        # Confirm titles
        approved, feedback = self.confirm_agent.confirm_titles(titles)
        while not approved:
            if feedback:
                self.confirm_agent.display_progress("제목 수정 중")
                titles = self.title_agent.process(story, prompts)
            self.project.titles = titles
            approved, feedback = self.confirm_agent.confirm_titles(titles)

        # Step 7: Final Confirmation & Output
        self.console.print()
        self.console.print("[bold]Step 7: 최종 확인 및 출력[/bold]")

        if self.confirm_agent.confirm_final(story, scenes, prompts, titles):
            # Select output formats
            self.console.print()
            self.console.print("출력 형식 선택:")
            self.console.print("  [1] Markdown만")
            self.console.print("  [2] Markdown + JSON")
            self.console.print("  [3] 전체 (Markdown + JSON + Clipboard)")

            format_choice = Prompt.ask("선택", choices=["1", "2", "3"], default="1")

            formats = ["markdown"]
            if format_choice in ["2", "3"]:
                formats.append("json")
            if format_choice == "3":
                formats.append("clipboard")

            # Export
            self.project.status = ProjectStatus.COMPLETED
            results = self.output_agent.export_project(self.project, formats)

            # Show summary
            self.output_agent.print_summary(self.project)

            # Show clipboard prompt
            self.console.print()
            if Prompt.ask("프롬프트를 클립보드에 복사하시겠습니까?", choices=["y", "n"], default="n") == "y":
                clipboard_text = self.output_agent.get_clipboard_text(prompts)
                try:
                    import pyperclip
                    pyperclip.copy(clipboard_text)
                    self.confirm_agent.display_message("클립보드에 복사되었습니다!", "success")
                except ImportError:
                    self.confirm_agent.display_message(
                        "pyperclip이 설치되지 않았습니다. 파일에서 복사하세요.",
                        "warning"
                    )

    def _load_project(self):
        """Load an existing project."""
        self.console.print()
        self.console.print(Panel("📂 기존 프로젝트", border_style="blue"))

        projects_dir = Path("projects")
        if not projects_dir.exists():
            self.confirm_agent.display_message("저장된 프로젝트가 없습니다.", "warning")
            return

        # List projects
        projects = list(projects_dir.iterdir())
        if not projects:
            self.confirm_agent.display_message("저장된 프로젝트가 없습니다.", "warning")
            return

        self.console.print()
        for i, proj in enumerate(projects, 1):
            self.console.print(f"  [{i}] {proj.name}")

        self.console.print()
        self.confirm_agent.display_message("프로젝트 로드 기능은 추후 구현 예정입니다.", "info")

    def _manage_library(self):
        """Manage character/template library."""
        self.console.print()
        self.console.print(Panel("📚 라이브러리 관리", border_style="yellow"))
        self.confirm_agent.display_message("라이브러리 관리 기능은 추후 구현 예정입니다.", "info")

    def _create_slug(self, text: str) -> str:
        """Create URL-friendly slug from text."""
        import re
        # Simple slug creation
        slug = text.lower().replace(" ", "-")
        slug = re.sub(r"[^a-z0-9가-힣-]", "", slug)
        slug = f"{slug}-{datetime.now().strftime('%Y%m%d%H%M')}"
        return slug[:50]

    def _create_character_from_input(self, input_data: InputData) -> Character:
        """Create a basic character from input data."""
        char_id = str(uuid.uuid4())[:8]

        # Basic character description
        sora2_fragment = f"A {input_data.animal}"

        return Character(
            id=char_id,
            species=input_data.animal,
            visual_description=VisualDescription(
                fur="",
                eyes="",
                size="",
                distinctive_features=[],
            ),
            sora2_prompt_fragment=sora2_fragment,
        )

    def _exit(self):
        """Exit the application."""
        self.console.print()
        self.console.print("[dim]감사합니다. 안녕히 가세요! 🐾[/dim]")


def main():
    """Main entry point."""
    try:
        app = AnimalShortsSystem()
        app.run()
    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다.")
        sys.exit(0)
    except Exception as e:
        console = Console()
        console.print(f"[red]Error: {e}[/red]")
        raise


if __name__ == "__main__":
    main()
