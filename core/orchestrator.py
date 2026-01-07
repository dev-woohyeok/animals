"""Orchestrator - Main workflow controller for Animal Shorts Agent System."""

from enum import Enum
from typing import Any, Callable

from rich.console import Console
from rich.panel import Panel

from .models import (
    InputData,
    Story,
    Scene,
    Prompt,
    TitleSet,
    Project,
    ProjectStatus,
    SessionState,
)
from .state_manager import StateManager
from agents import (
    InputAgent,
    StoryAgent,
    SceneAgent,
    PromptAgent,
    TranslationAgent,
    TitleAgent,
    ConfirmAgent,
    OutputAgent,
)
from utils import get_logger, get_timestamp, slugify


class WorkflowStep(str, Enum):
    """Workflow steps."""
    INPUT = "input"
    STORY = "story"
    SCENE = "scene"
    PROMPT = "prompt"
    TRANSLATION = "translation"
    TITLE = "title"
    CONFIRM = "confirm"
    OUTPUT = "output"
    COMPLETE = "complete"


class Orchestrator:
    """
    Main workflow orchestrator that coordinates all agents.

    Manages the flow:
    Input -> Story -> Scene -> Prompt -> Translation -> Title -> Confirm -> Output
    """

    def __init__(self, config: dict[str, Any] | None = None):
        """
        Initialize orchestrator with optional configuration.

        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.console = Console()
        self.logger = get_logger("Orchestrator")

        # Initialize state manager
        self.state_manager = StateManager()

        # Initialize agents
        self._init_agents()

        # Workflow callbacks
        self._step_callbacks: dict[WorkflowStep, list[Callable]] = {
            step: [] for step in WorkflowStep
        }

    def _init_agents(self) -> None:
        """Initialize all agents."""
        self.input_agent = InputAgent()
        self.story_agent = StoryAgent()
        self.scene_agent = SceneAgent()
        self.prompt_agent = PromptAgent()
        self.translation_agent = TranslationAgent()
        self.title_agent = TitleAgent()
        self.confirm_agent = ConfirmAgent()
        self.output_agent = OutputAgent()

    def register_callback(
        self,
        step: WorkflowStep,
        callback: Callable[[Any], None],
    ) -> None:
        """
        Register a callback for a workflow step.

        Args:
            step: Workflow step to attach callback to
            callback: Callback function
        """
        self._step_callbacks[step].append(callback)

    def _run_callbacks(self, step: WorkflowStep, data: Any) -> None:
        """Run all callbacks for a step."""
        for callback in self._step_callbacks[step]:
            try:
                callback(data)
            except Exception as e:
                self.logger.warning(f"Callback error at {step}: {e}")

    def create_project(self, name: str) -> Project:
        """
        Create a new project.

        Args:
            name: Project name

        Returns:
            New Project instance
        """
        project = Project(
            id=f"proj_{get_timestamp()}",
            slug=slugify(name),
            name=name,
            status=ProjectStatus.DRAFT,
        )
        self.state_manager.set_project(project)
        return project

    def run_workflow(
        self,
        input_data: InputData | dict[str, Any],
        interactive: bool = True,
    ) -> Project:
        """
        Run the complete workflow.

        Args:
            input_data: User input data
            interactive: Whether to run in interactive mode with confirmations

        Returns:
            Completed Project
        """
        # Ensure InputData
        if isinstance(input_data, dict):
            input_data = InputData(**input_data)

        # Create project
        project = self.create_project(
            f"{input_data.animal}_{input_data.situation[:20]}"
        )
        project.input_data = input_data

        self.logger.info(f"Starting workflow for project: {project.name}")
        self.console.print(Panel(
            f"[bold]프로젝트 시작[/bold]\n{project.name}",
            border_style="green"
        ))

        try:
            # Step 1: Process Input
            self._run_step_input(project, input_data)

            # Step 2: Generate Story
            story = self._run_step_story(project, interactive)
            if story is None:
                return project

            # Step 3: Generate Scenes
            scenes = self._run_step_scenes(project, story, interactive)
            if scenes is None:
                return project

            # Step 4: Generate Prompts
            prompts = self._run_step_prompts(project, scenes, interactive)
            if prompts is None:
                return project

            # Step 5: Translate Prompts
            prompts = self._run_step_translation(project, prompts)

            # Step 6: Generate Titles
            titles = self._run_step_titles(project, story, prompts, interactive)
            if titles is None:
                return project

            # Step 7: Final Confirmation
            if interactive:
                confirmed = self._run_step_final_confirm(
                    project, story, scenes, prompts, titles
                )
                if not confirmed:
                    self.logger.info("User cancelled at final confirmation")
                    return project

            # Step 8: Output
            self._run_step_output(project)

            # Mark complete
            project.status = ProjectStatus.COMPLETED
            self.state_manager.save_project(project)

            self.console.print(Panel(
                "[bold green]워크플로우 완료![/bold green]",
                border_style="green"
            ))

        except KeyboardInterrupt:
            self.logger.info("Workflow interrupted by user")
            self.console.print("\n[yellow]작업이 중단되었습니다.[/yellow]")

        except Exception as e:
            self.logger.error(f"Workflow error: {e}")
            self.console.print(f"\n[red]오류 발생: {e}[/red]")
            raise

        return project

    def _run_step_input(
        self,
        project: Project,
        input_data: InputData,
    ) -> InputData:
        """Process input step."""
        self.state_manager.set_step(WorkflowStep.INPUT)
        self.confirm_agent.display_progress("입력 데이터 처리 중")

        processed = self.input_agent.process(input_data)
        project.input_data = processed

        self._run_callbacks(WorkflowStep.INPUT, processed)
        return processed

    def _run_step_story(
        self,
        project: Project,
        interactive: bool,
    ) -> Story | None:
        """Generate story step."""
        self.state_manager.set_step(WorkflowStep.STORY)
        self.confirm_agent.display_progress("스토리 생성 중")

        max_attempts = 3
        for attempt in range(max_attempts):
            story = self.story_agent.process(project.input_data)
            project.story = story

            if not interactive:
                return story

            approved, feedback = self.confirm_agent.confirm_story(story)

            if approved:
                self._run_callbacks(WorkflowStep.STORY, story)
                return story

            if feedback == "재생성 요청":
                self.confirm_agent.display_message(
                    f"스토리 재생성 중... ({attempt + 2}/{max_attempts})",
                    "info"
                )
                continue

            # User provided feedback, regenerate with it
            story = self.story_agent.regenerate_with_feedback(story, feedback)
            project.story = story

        return story

    def _run_step_scenes(
        self,
        project: Project,
        story: Story,
        interactive: bool,
    ) -> list[Scene] | None:
        """Generate scenes step."""
        self.state_manager.set_step(WorkflowStep.SCENE)
        self.confirm_agent.display_progress("장면 분할 중")

        max_attempts = 3
        for attempt in range(max_attempts):
            scenes = self.scene_agent.process(story)
            project.scenes = scenes

            if not interactive:
                return scenes

            approved, feedback, scene_id = self.confirm_agent.confirm_scenes(scenes)

            if approved:
                self._run_callbacks(WorkflowStep.SCENE, scenes)
                return scenes

            if feedback == "전체 재생성 요청":
                self.confirm_agent.display_message(
                    f"장면 재생성 중... ({attempt + 2}/{max_attempts})",
                    "info"
                )
                continue

            if scene_id is not None and feedback:
                # Regenerate specific scene
                scenes = self.scene_agent.regenerate_scene(scenes, scene_id, feedback)
                project.scenes = scenes

        return scenes

    def _run_step_prompts(
        self,
        project: Project,
        scenes: list[Scene],
        interactive: bool,
    ) -> list[Prompt] | None:
        """Generate prompts step."""
        self.state_manager.set_step(WorkflowStep.PROMPT)
        self.confirm_agent.display_progress("Sora2 프롬프트 생성 중")

        # Get character from project if available
        character = project.character

        max_attempts = 3
        for attempt in range(max_attempts):
            prompts = self.prompt_agent.process(scenes, character=character)
            project.prompts = prompts

            if not interactive:
                return prompts

            approved, feedback, scene_id = self.confirm_agent.confirm_prompts(prompts)

            if approved:
                self._run_callbacks(WorkflowStep.PROMPT, prompts)
                return prompts

            if feedback == "전체 재생성 요청":
                self.confirm_agent.display_message(
                    f"프롬프트 재생성 중... ({attempt + 2}/{max_attempts})",
                    "info"
                )
                continue

            if scene_id is not None and feedback:
                # Regenerate specific prompt
                scene = next((s for s in scenes if s.id == scene_id), None)
                if scene:
                    prompts = self.prompt_agent.regenerate_prompt(
                        prompts, scene, feedback, character
                    )
                    project.prompts = prompts

        return prompts

    def _run_step_translation(
        self,
        project: Project,
        prompts: list[Prompt],
    ) -> list[Prompt]:
        """Translate prompts step."""
        self.state_manager.set_step(WorkflowStep.TRANSLATION)
        self.confirm_agent.display_progress("한국어 번역 중")

        translated = self.translation_agent.process(prompts)
        project.prompts = translated

        self._run_callbacks(WorkflowStep.TRANSLATION, translated)
        return translated

    def _run_step_titles(
        self,
        project: Project,
        story: Story,
        prompts: list[Prompt],
        interactive: bool,
    ) -> TitleSet | None:
        """Generate titles step."""
        self.state_manager.set_step(WorkflowStep.TITLE)
        self.confirm_agent.display_progress("제목 생성 중")

        max_attempts = 3
        for attempt in range(max_attempts):
            titles = self.title_agent.process(story, prompts=prompts)
            project.titles = titles

            if not interactive:
                return titles

            approved, feedback = self.confirm_agent.confirm_titles(titles)

            if approved:
                self._run_callbacks(WorkflowStep.TITLE, titles)
                return titles

            if feedback == "재생성 요청":
                self.confirm_agent.display_message(
                    f"제목 재생성 중... ({attempt + 2}/{max_attempts})",
                    "info"
                )
                continue

            # Regenerate with feedback
            # For now, just regenerate all
            continue

        return titles

    def _run_step_final_confirm(
        self,
        project: Project,
        story: Story,
        scenes: list[Scene],
        prompts: list[Prompt],
        titles: TitleSet,
    ) -> bool:
        """Final confirmation step."""
        self.state_manager.set_step(WorkflowStep.CONFIRM)
        return self.confirm_agent.confirm_final(story, scenes, prompts, titles)

    def _run_step_output(self, project: Project) -> str:
        """Output generation step."""
        self.state_manager.set_step(WorkflowStep.OUTPUT)
        self.confirm_agent.display_progress("결과물 생성 중")

        output_path = self.output_agent.process(project)

        self._run_callbacks(WorkflowStep.OUTPUT, output_path)
        self.state_manager.set_step(WorkflowStep.COMPLETE)

        return output_path

    def run_single_step(
        self,
        step: WorkflowStep,
        project: Project,
        **kwargs,
    ) -> Any:
        """
        Run a single workflow step.

        Args:
            step: Step to run
            project: Project to process
            **kwargs: Additional arguments for the step

        Returns:
            Step result
        """
        step_methods = {
            WorkflowStep.INPUT: lambda: self._run_step_input(
                project, kwargs.get("input_data")
            ),
            WorkflowStep.STORY: lambda: self._run_step_story(
                project, kwargs.get("interactive", True)
            ),
            WorkflowStep.SCENE: lambda: self._run_step_scenes(
                project, project.story, kwargs.get("interactive", True)
            ),
            WorkflowStep.PROMPT: lambda: self._run_step_prompts(
                project, project.scenes, kwargs.get("interactive", True)
            ),
            WorkflowStep.TRANSLATION: lambda: self._run_step_translation(
                project, project.prompts
            ),
            WorkflowStep.TITLE: lambda: self._run_step_titles(
                project, project.story, project.prompts,
                kwargs.get("interactive", True)
            ),
            WorkflowStep.OUTPUT: lambda: self._run_step_output(project),
        }

        if step not in step_methods:
            raise ValueError(f"Unknown step: {step}")

        return step_methods[step]()
