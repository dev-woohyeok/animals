"""Exporter - Export projects to various formats."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from core.models import Project, Story, Scene, Prompt, TitleSet
from utils import get_logger, ensure_dir


class Exporter:
    """
    Exports projects to various formats.

    Supported formats:
    - JSON: Full project data
    - Markdown: Formatted documentation
    - Clipboard: Optimized for pasting
    - Storyboard: Scene-by-scene breakdown
    """

    def __init__(self, export_dir: str | Path | None = None):
        """
        Initialize exporter.

        Args:
            export_dir: Directory for exports
        """
        self.logger = get_logger("Exporter")

        if export_dir is None:
            export_dir = Path(__file__).parent.parent / "exports"

        self.export_dir = Path(export_dir)
        ensure_dir(self.export_dir)

    # ============================================================
    # JSON Export
    # ============================================================

    def export_json(
        self,
        project: Project,
        include_metadata: bool = True,
    ) -> Path:
        """
        Export project to JSON.

        Args:
            project: Project to export
            include_metadata: Include export metadata

        Returns:
            Path to exported file
        """
        data = project.model_dump(mode="json")

        if include_metadata:
            data["_export"] = {
                "format": "json",
                "version": "1.0",
                "exported_at": datetime.now().isoformat(),
                "generator": "Animal Shorts Agent System",
            }

        file_path = self.export_dir / f"{project.slug}_export.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        self.logger.info(f"Exported JSON: {file_path}")

        return file_path

    def export_prompts_json(
        self,
        prompts: list[Prompt],
        project_slug: str,
    ) -> Path:
        """
        Export only prompts to JSON.

        Args:
            prompts: List of prompts
            project_slug: Project identifier

        Returns:
            Path to exported file
        """
        data = {
            "project_slug": project_slug,
            "exported_at": datetime.now().isoformat(),
            "prompt_count": len(prompts),
            "prompts": [p.model_dump(mode="json") for p in prompts],
        }

        file_path = self.export_dir / f"{project_slug}_prompts.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return file_path

    def export_scenes_json(
        self,
        scenes: list[Scene],
        project_slug: str,
    ) -> Path:
        """Export only scenes to JSON."""
        data = {
            "project_slug": project_slug,
            "exported_at": datetime.now().isoformat(),
            "scene_count": len(scenes),
            "total_duration": sum(s.duration for s in scenes),
            "scenes": [s.model_dump(mode="json") for s in scenes],
        }

        file_path = self.export_dir / f"{project_slug}_scenes.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return file_path

    # ============================================================
    # Markdown Export
    # ============================================================

    def export_markdown(
        self,
        project: Project,
        include_korean: bool = True,
    ) -> Path:
        """
        Export project to Markdown.

        Args:
            project: Project to export
            include_korean: Include Korean translations

        Returns:
            Path to exported file
        """
        lines = self._build_markdown(project, include_korean)
        content = "\n".join(lines)

        file_path = self.export_dir / f"{project.slug}_export.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        self.logger.info(f"Exported Markdown: {file_path}")

        return file_path

    def _build_markdown(
        self,
        project: Project,
        include_korean: bool,
    ) -> list[str]:
        """Build markdown content."""
        lines = [
            f"# {project.story.title if project.story else project.slug}",
            "",
            f"> 생성일: {project.created_at.strftime('%Y-%m-%d %H:%M')}",
            "",
        ]

        # Story section
        if project.story:
            lines.extend([
                "## 스토리",
                "",
                f"**시놉시스:** {project.story.synopsis}",
                "",
                "### 스토리 아크",
                "",
            ])

            for phase in project.story.arc:
                lines.append(f"- **{phase.phase}**: {phase.description}")

            lines.append("")

        # Scenes section
        if project.scenes:
            lines.extend([
                "## 장면 구성",
                "",
                f"총 {len(project.scenes)}개 장면, {sum(s.duration for s in project.scenes)}초",
                "",
            ])

            for scene in project.scenes:
                lines.extend([
                    f"### 장면 {scene.scene_number}: {scene.title}",
                    "",
                    f"- **설명:** {scene.description}",
                    f"- **액션:** {scene.action}",
                    f"- **감정:** {scene.emotion}",
                    f"- **카메라:** {scene.camera.movement}, {scene.camera.angle}",
                    f"- **조명:** {scene.lighting}",
                    f"- **길이:** {scene.duration}초",
                    "",
                ])

        # Prompts section
        if project.prompts:
            lines.extend([
                "## Sora2 프롬프트",
                "",
            ])

            for prompt in project.prompts:
                lines.extend([
                    f"### Scene {prompt.scene_id}",
                    "",
                    "**English:**",
                    "```",
                    prompt.english,
                    "```",
                    "",
                ])

                if include_korean and prompt.korean:
                    lines.extend([
                        "**한국어:**",
                        "```",
                        prompt.korean,
                        "```",
                        "",
                    ])

        # Titles section
        if project.titles:
            lines.extend([
                "## 쇼츠 제목",
                "",
                f"- **YouTube:** {project.titles.youtube}",
                f"- **Instagram:** {project.titles.instagram}",
                f"- **TikTok:** {project.titles.tiktok}",
                "",
            ])

        return lines

    # ============================================================
    # Storyboard Export
    # ============================================================

    def export_storyboard(
        self,
        project: Project,
    ) -> Path:
        """
        Export as storyboard format.

        Args:
            project: Project to export

        Returns:
            Path to exported file
        """
        lines = self._build_storyboard(project)
        content = "\n".join(lines)

        file_path = self.export_dir / f"{project.slug}_storyboard.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path

    def _build_storyboard(self, project: Project) -> list[str]:
        """Build storyboard content."""
        lines = [
            f"# 스토리보드: {project.story.title if project.story else project.slug}",
            "",
            "---",
            "",
        ]

        if not project.scenes or not project.prompts:
            lines.append("*씬 또는 프롬프트 없음*")
            return lines

        # Build prompt lookup
        prompt_lookup = {p.scene_id: p for p in project.prompts}

        for scene in project.scenes:
            prompt = prompt_lookup.get(scene.scene_number)

            lines.extend([
                f"## [{scene.scene_number}] {scene.title}",
                "",
                "| 항목 | 내용 |",
                "|------|------|",
                f"| 길이 | {scene.duration}초 |",
                f"| 감정 | {scene.emotion} |",
                f"| 카메라 | {scene.camera.movement} / {scene.camera.angle} |",
                f"| 조명 | {scene.lighting} |",
                "",
                "### 설명",
                f"> {scene.description}",
                "",
                "### 액션",
                f"> {scene.action}",
                "",
            ])

            if prompt:
                lines.extend([
                    "### Sora2 프롬프트",
                    "```",
                    prompt.english,
                    "```",
                    "",
                ])

            lines.extend([
                "---",
                "",
            ])

        return lines

    # ============================================================
    # Clipboard Format
    # ============================================================

    def get_clipboard_text(
        self,
        project: Project,
        format_type: str = "prompts",
    ) -> str:
        """
        Get text optimized for clipboard.

        Args:
            project: Project to format
            format_type: "prompts", "titles", "all"

        Returns:
            Formatted text for clipboard
        """
        if format_type == "prompts":
            return self._format_prompts_clipboard(project.prompts)
        elif format_type == "titles":
            return self._format_titles_clipboard(project.titles)
        else:
            return self._format_all_clipboard(project)

    def _format_prompts_clipboard(self, prompts: list[Prompt]) -> str:
        """Format prompts for clipboard."""
        lines = []

        for prompt in prompts:
            lines.append(f"[Scene {prompt.scene_id}]")
            lines.append(prompt.english)
            lines.append("")

        return "\n".join(lines)

    def _format_titles_clipboard(self, titles: TitleSet | None) -> str:
        """Format titles for clipboard."""
        if not titles:
            return ""

        return f"""YouTube: {titles.youtube}
Instagram: {titles.instagram}
TikTok: {titles.tiktok}"""

    def _format_all_clipboard(self, project: Project) -> str:
        """Format all content for clipboard."""
        lines = []

        if project.story:
            lines.extend([
                f"제목: {project.story.title}",
                f"시놉시스: {project.story.synopsis}",
                "",
            ])

        if project.prompts:
            lines.append("=== Sora2 Prompts ===")
            lines.append("")
            lines.append(self._format_prompts_clipboard(project.prompts))

        if project.titles:
            lines.append("=== Titles ===")
            lines.append(self._format_titles_clipboard(project.titles))

        return "\n".join(lines)

    # ============================================================
    # Sora2-Ready Export
    # ============================================================

    def export_sora2_ready(
        self,
        prompts: list[Prompt],
        project_slug: str,
    ) -> Path:
        """
        Export prompts in Sora2-ready format.

        Each prompt in a separate section, ready to copy-paste.

        Args:
            prompts: List of prompts
            project_slug: Project identifier

        Returns:
            Path to exported file
        """
        lines = [
            "# Sora2 Prompts - Ready to Use",
            "",
            f"Project: {project_slug}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"Total Scenes: {len(prompts)}",
            "",
            "---",
            "",
        ]

        for prompt in prompts:
            lines.extend([
                f"## Scene {prompt.scene_id}",
                "",
                "```",
                prompt.english,
                "```",
                "",
                "---",
                "",
            ])

        file_path = self.export_dir / f"{project_slug}_sora2_ready.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return file_path

    # ============================================================
    # PDF Export (Simple HTML-based)
    # ============================================================

    def export_pdf_html(
        self,
        project: Project,
    ) -> Path:
        """
        Export as HTML file that can be printed to PDF.

        Args:
            project: Project to export

        Returns:
            Path to HTML file
        """
        html = self._build_pdf_html(project)

        file_path = self.export_dir / f"{project.slug}_storyboard.html"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

        self.logger.info(f"Exported HTML (print to PDF): {file_path}")

        return file_path

    def _build_pdf_html(self, project: Project) -> str:
        """Build HTML for PDF printing."""
        title = project.story.title if project.story else project.slug

        scenes_html = ""
        prompt_lookup = {p.scene_id: p for p in project.prompts} if project.prompts else {}

        for scene in project.scenes or []:
            prompt = prompt_lookup.get(scene.scene_number)
            prompt_text = prompt.english if prompt else "No prompt"

            scenes_html += f"""
            <div class="scene">
                <div class="scene-header">
                    <span class="scene-number">Scene {scene.scene_number}</span>
                    <span class="scene-title">{scene.title}</span>
                    <span class="scene-duration">{scene.duration}s</span>
                </div>
                <div class="scene-body">
                    <div class="scene-meta">
                        <p><strong>Emotion:</strong> {scene.emotion}</p>
                        <p><strong>Camera:</strong> {scene.camera.movement}, {scene.camera.angle}</p>
                        <p><strong>Lighting:</strong> {scene.lighting}</p>
                    </div>
                    <div class="scene-description">
                        <p><strong>Description:</strong> {scene.description}</p>
                        <p><strong>Action:</strong> {scene.action}</p>
                    </div>
                    <div class="scene-prompt">
                        <strong>Sora2 Prompt:</strong>
                        <pre>{prompt_text}</pre>
                    </div>
                </div>
            </div>
            """

        return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{title} - Storyboard</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 12px;
            line-height: 1.5;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }}
        h1 {{
            font-size: 24px;
            margin-bottom: 10px;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }}
        .meta {{
            color: #666;
            margin-bottom: 20px;
        }}
        .scene {{
            border: 1px solid #ddd;
            margin-bottom: 20px;
            page-break-inside: avoid;
        }}
        .scene-header {{
            background: #f5f5f5;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #ddd;
        }}
        .scene-number {{
            font-weight: bold;
            color: #333;
        }}
        .scene-title {{
            flex: 1;
            margin-left: 15px;
        }}
        .scene-duration {{
            background: #333;
            color: white;
            padding: 2px 8px;
            border-radius: 3px;
            font-size: 11px;
        }}
        .scene-body {{
            padding: 15px;
        }}
        .scene-meta {{
            display: flex;
            gap: 20px;
            margin-bottom: 10px;
            font-size: 11px;
            color: #666;
        }}
        .scene-meta p {{
            margin: 0;
        }}
        .scene-description {{
            margin-bottom: 10px;
        }}
        .scene-description p {{
            margin-bottom: 5px;
        }}
        .scene-prompt {{
            background: #f9f9f9;
            padding: 10px;
            border-radius: 4px;
        }}
        .scene-prompt pre {{
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: monospace;
            font-size: 11px;
            margin-top: 5px;
        }}
        @media print {{
            body {{
                padding: 0;
            }}
            .scene {{
                break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="meta">
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        <p>Scenes: {len(project.scenes or [])} | Total Duration: {sum(s.duration for s in project.scenes or [])}s</p>
    </div>
    {scenes_html}
</body>
</html>"""
