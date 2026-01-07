"""Output Agent - Generate output in various formats."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from core.models import Project, Story, Scene, Prompt, TitleSet
from .base import BaseAgent


class OutputAgent(BaseAgent[str]):
    """
    Generates output files in various formats.

    Supported formats:
    - Markdown (.md)
    - JSON (.json)
    - Clipboard text (.txt)
    - PDF (.pdf) - future
    """

    def __init__(self, output_dir: str = "projects"):
        super().__init__(
            name="OutputAgent",
            system_prompt_path=None,
        )
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def _get_default_system_prompt(self) -> str:
        return ""  # This agent doesn't use Claude

    def process(self, input_data: Any) -> str:
        """Not used directly - use specific export methods."""
        return ""

    def export_project(
        self,
        project: Project,
        formats: list[str] | None = None,
    ) -> dict[str, Path]:
        """
        Export project in specified formats.

        Args:
            project: Project to export
            formats: List of formats (markdown, json, clipboard)

        Returns:
            Dict mapping format to file path
        """
        if formats is None:
            formats = ["markdown"]

        # Create project directory
        project_dir = self.output_dir / project.slug
        project_dir.mkdir(exist_ok=True)

        exports_dir = project_dir / "exports"
        exports_dir.mkdir(exist_ok=True)

        results = {}

        if "markdown" in formats:
            md_path = self._export_markdown(project, exports_dir)
            results["markdown"] = md_path

        if "json" in formats:
            json_path = self._export_json(project, exports_dir)
            results["json"] = json_path

        if "clipboard" in formats:
            txt_path = self._export_clipboard(project, exports_dir)
            results["clipboard"] = txt_path

        # Save project metadata
        self._save_project_metadata(project, project_dir)

        return results

    def _export_markdown(self, project: Project, output_dir: Path) -> Path:
        """Export project as Markdown."""
        md_content = self._build_markdown(project)
        output_path = output_dir / "prompts.md"
        output_path.write_text(md_content, encoding="utf-8")
        return output_path

    def _build_markdown(self, project: Project) -> str:
        """Build Markdown content."""
        lines = [
            f"# {project.name}",
            "",
            f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
        ]

        # Story section
        if project.story:
            lines.extend([
                "## 📖 스토리",
                "",
                f"**제목:** {project.story.title}",
                "",
                f"**시놉시스:** {project.story.synopsis}",
                "",
                "### 스토리 아크",
                "",
            ])

            for phase in project.story.arc:
                lines.append(f"- **{phase.phase}**: {phase.description} ({phase.emotion})")

            lines.append("")

        # Titles section
        if project.titles:
            lines.extend([
                "## 🏷️ 제목",
                "",
                f"**메인 제목:** {project.titles.main_title}",
                "",
                "### 플랫폼별 제목",
                "",
                f"- **YouTube Shorts:** {project.titles.platform_variants.youtube_shorts}",
                f"- **Instagram Reels:** {project.titles.platform_variants.instagram_reels}",
                f"- **TikTok:** {project.titles.platform_variants.tiktok}",
                "",
                "### 후킹 변형",
                "",
                f"- **감정형:** {project.titles.hooks.emotional}",
                f"- **호기심형:** {project.titles.hooks.curiosity}",
                f"- **결과형:** {project.titles.hooks.outcome}",
                "",
            ])

        # Prompts section
        if project.prompts:
            lines.extend([
                "## ✨ Sora2 프롬프트",
                "",
            ])

            for prompt in project.prompts:
                scene = next(
                    (s for s in project.scenes if s.id == prompt.scene_id),
                    None
                )
                scene_title = scene.title if scene else f"Scene {prompt.scene_id}"

                lines.extend([
                    "---",
                    "",
                    f"### [Scene {prompt.scene_id}] {scene_title}",
                    "",
                ])

                if prompt.quality_score:
                    lines.append(f"*Quality Score: {prompt.quality_score}/100*")
                    lines.append("")

                lines.extend([
                    "**🇺🇸 English (Sora2용):**",
                    "",
                    "```",
                    prompt.english,
                    "```",
                    "",
                ])

                if prompt.korean:
                    lines.extend([
                        "**🇰🇷 한국어 (참고용):**",
                        "",
                        f"> {prompt.korean}",
                        "",
                    ])

        # Footer
        lines.extend([
            "---",
            "",
            f"*Generated by Animal Shorts Agent System*",
        ])

        return "\n".join(lines)

    def _export_json(self, project: Project, output_dir: Path) -> Path:
        """Export project as JSON."""
        output_path = output_dir / "prompts.json"

        data = {
            "project": {
                "id": project.id,
                "name": project.name,
                "created_at": project.created_at.isoformat(),
            },
            "story": project.story.model_dump() if project.story else None,
            "titles": project.titles.model_dump() if project.titles else None,
            "scenes": [s.model_dump() for s in project.scenes],
            "prompts": [p.model_dump() for p in project.prompts],
        }

        output_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return output_path

    def _export_clipboard(self, project: Project, output_dir: Path) -> Path:
        """Export prompts in clipboard-friendly format."""
        lines = []

        for prompt in project.prompts:
            scene = next(
                (s for s in project.scenes if s.id == prompt.scene_id),
                None
            )
            scene_title = scene.title if scene else f"Scene {prompt.scene_id}"

            lines.extend([
                "═" * 60,
                f"[SCENE {prompt.scene_id}] {scene_title}",
                "═" * 60,
                "",
                prompt.english,
                "",
                "─" * 60,
                f"🇰🇷 {prompt.korean or '(번역 없음)'}",
                "─" * 60,
                "",
            ])

        output_path = output_dir / "prompts_clipboard.txt"
        output_path.write_text("\n".join(lines), encoding="utf-8")
        return output_path

    def _save_project_metadata(self, project: Project, project_dir: Path) -> None:
        """Save project metadata."""
        import yaml

        meta_path = project_dir / "project.yaml"

        metadata = {
            "id": project.id,
            "slug": project.slug,
            "name": project.name,
            "created_at": project.created_at.isoformat(),
            "updated_at": datetime.now().isoformat(),
            "status": project.status.value,
            "style_id": project.style_id,
            "character_id": project.character_id,
            "template_id": project.template_id,
            "summary": {
                "total_scenes": len(project.scenes),
                "total_duration": f"{sum(s.duration for s in project.scenes)}s",
                "prompt_count": len(project.prompts),
            },
        }

        meta_path.write_text(
            yaml.dump(metadata, allow_unicode=True, default_flow_style=False),
            encoding="utf-8",
        )

    def get_clipboard_text(self, prompts: list[Prompt]) -> str:
        """
        Get prompts formatted for clipboard.

        Args:
            prompts: List of prompts

        Returns:
            Formatted text for clipboard
        """
        lines = []

        for prompt in prompts:
            lines.extend([
                "═" * 60,
                f"[SCENE {prompt.scene_id}]",
                "═" * 60,
                "",
                prompt.english,
                "",
            ])

        return "\n".join(lines)

    def print_summary(self, project: Project) -> None:
        """Print project summary to console."""
        from rich.console import Console
        from rich.panel import Panel

        console = Console()

        # Build summary
        exports = list((self.output_dir / project.slug / "exports").glob("*"))
        export_list = "\n".join([f"  - {e.name}" for e in exports])

        console.print(Panel(
            f"""[bold green]✅ 프로젝트 저장 완료![/bold green]

📁 위치: {self.output_dir / project.slug}

📊 요약:
  - 장면 수: {len(project.scenes)}개
  - 프롬프트: {len(project.prompts)}개
  - 총 길이: {sum(s.duration for s in project.scenes)}초

📄 출력 파일:
{export_list}""",
            title="저장 완료",
            border_style="green",
        ))
