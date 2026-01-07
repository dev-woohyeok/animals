#!/usr/bin/env python3
"""Test script for Animal Shorts Agent System (Mock Mode)."""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.models import (
    InputData, Story, StoryPhase, EmotionPoint,
    Scene, CameraSettings, Prompt, PromptStructure,
    TitleSet, PlatformTitles, TitleHooks,
    Character, VisualDescription,
)

console = Console()


def test_input_agent():
    """Test Input Agent."""
    console.print("\n[bold cyan]═══ Testing Input Agent ═══[/bold cyan]")

    from agents.input_agent import InputAgent

    agent = InputAgent()

    # Test simple format
    test_input = "골든 리트리버 강아지 / 버려진 후 외로운 노인을 만나 서로의 가족이 됨 / 따뜻함, 감동, 치유"

    console.print(f"[dim]입력: {test_input}[/dim]")

    result = agent.process(test_input)

    console.print(Panel(
        f"""동물: {result.animal}
상황: {result.situation}
감정: {', '.join(result.emotions)}
결말: {result.ending or '(없음)'}""",
        title="✓ Input Agent 결과",
        border_style="green",
    ))

    return result


def create_mock_story(input_data: InputData) -> Story:
    """Create mock story for testing."""
    return Story(
        title=f"{input_data.animal}의 새로운 시작",
        synopsis="비 오는 골목에서 버려진 강아지가 외로운 노인을 만나 서로의 빈자리를 채우며 가족이 되는 감동 실화",
        arc=[
            StoryPhase(
                phase="도입",
                description="비 오는 저녁, 젖은 골판지 상자 안에서 떨고 있는 골든 리트리버 강아지. 지나가는 사람들은 눈길도 주지 않는다.",
                beats=["강아지의 외로운 모습", "차가운 빗속", "무관심한 행인들"],
                emotion="슬픔, 고독, 불안",
            ),
            StoryPhase(
                phase="전개",
                description="우산을 쓴 노인이 천천히 다가온다. 최근 아내를 잃고 혼자 살게 된 그는 강아지의 눈빛에서 자신의 외로움을 본다.",
                beats=["노인의 등장", "눈빛 교환", "감정적 연결"],
                emotion="호기심, 공감, 희망의 시작",
            ),
            StoryPhase(
                phase="망설임",
                description="노인은 강아지를 데려갈까 망설인다. 혼자 살기도 힘든데... 하지만 강아지의 촉촉한 눈이 그를 붙잡는다.",
                beats=["내적 갈등", "강아지의 기다림", "결정의 순간"],
                emotion="긴장, 갈등, 기대",
            ),
            StoryPhase(
                phase="해결",
                description="노인이 결심하고 강아지를 품에 안는다. 강아지가 처음으로 꼬리를 흔든다. 비가 그치기 시작한다.",
                beats=["구원의 순간", "첫 포옹", "날씨 변화"],
                emotion="안도, 따뜻함, 기쁨",
            ),
            StoryPhase(
                phase="결말",
                description="따뜻한 집에서 함께하는 노인과 강아지. 서로의 빈자리를 채우며 새로운 가족이 된 둘의 평화로운 일상.",
                beats=["새로운 시작", "행복한 일상", "완전한 가족"],
                emotion="행복, 감동, 치유",
            ),
        ],
        emotional_journey=[
            EmotionPoint(position=0.0, emotion="슬픔", intensity=80),
            EmotionPoint(position=0.2, emotion="고독", intensity=70),
            EmotionPoint(position=0.4, emotion="희망", intensity=40),
            EmotionPoint(position=0.6, emotion="긴장", intensity=60),
            EmotionPoint(position=0.8, emotion="안도", intensity=75),
            EmotionPoint(position=1.0, emotion="행복", intensity=95),
        ],
        total_duration=105,
    )


def create_mock_scenes(story: Story) -> list[Scene]:
    """Create mock scenes for testing."""
    return [
        Scene(
            id=1,
            title="버려진 강아지",
            title_en="The Abandoned Puppy",
            duration=15,
            description="비 오는 저녁, 도시 골목 구석 젖은 골판지 상자 안에 웅크린 골든 리트리버 강아지",
            action="강아지가 희망을 담은 눈으로 지나가는 행인들을 올려다보지만, 모두 지나친다",
            emotion="슬픔, 고독, 미약한 희망",
            camera=CameraSettings(
                movement="slow dolly in",
                angle="wide to close-up",
                transition="fade in",
            ),
            lighting="cold blue-grey, overcast, rain",
            key_elements=["wet cardboard box", "rainy street", "puppy's hopeful eyes", "indifferent pedestrians"],
        ),
        Scene(
            id=2,
            title="노인의 등장",
            title_en="The Old Man Appears",
            duration=15,
            description="검은 우산을 쓴 노인이 천천히 걸어오다 강아지를 발견하고 멈춘다",
            action="노인이 강아지와 눈이 마주치고, 잠시 멈춰 선다. 빗소리 속 고요한 순간",
            emotion="호기심, 연민, 감정적 연결",
            camera=CameraSettings(
                movement="tracking shot",
                angle="medium",
                transition="cut",
            ),
            lighting="cold with warm streetlight accent",
            key_elements=["black umbrella", "eye contact", "pause in rain", "lonely figure"],
        ),
        Scene(
            id=3,
            title="첫 교감",
            title_en="First Connection",
            duration=15,
            description="노인이 천천히 쪼그려 앉아 강아지에게 손을 내민다",
            action="강아지가 조심스럽게 손 냄새를 맡고, 노인의 손가락을 핥는다",
            emotion="조심스러운 희망, 신뢰의 시작",
            camera=CameraSettings(
                movement="slow push in",
                angle="close-up on hands",
                transition="dissolve",
            ),
            lighting="transitioning to warmer tones",
            key_elements=["reaching hand", "sniffing", "gentle lick", "trembling paw"],
        ),
        Scene(
            id=4,
            title="망설임",
            title_en="Hesitation",
            duration=15,
            description="노인이 일어서려다 강아지의 눈을 다시 바라본다. 내적 갈등의 순간",
            action="노인의 얼굴에 갈등이 스치고, 강아지는 꼬리를 조심스럽게 흔들기 시작한다",
            emotion="갈등, 긴장, 기대",
            camera=CameraSettings(
                movement="static with subtle shake",
                angle="alternating close-ups",
                transition="cut",
            ),
            lighting="dramatic shadows, emotional",
            key_elements=["conflicted expression", "wagging tail", "rain drops", "decision moment"],
        ),
        Scene(
            id=5,
            title="구원",
            title_en="Rescue",
            duration=15,
            description="노인이 결심하고 강아지를 품에 안아 올린다",
            action="강아지가 노인의 품에 안기며 처음으로 활기차게 꼬리를 흔든다. 비가 그치기 시작",
            emotion="안도, 따뜻함, 기쁨의 폭발",
            camera=CameraSettings(
                movement="crane up",
                angle="medium to wide",
                transition="dissolve",
            ),
            lighting="warm golden light breaking through",
            key_elements=["embrace", "excited tail wag", "rain stopping", "sunlight"],
        ),
        Scene(
            id=6,
            title="새로운 시작",
            title_en="New Beginning",
            duration=15,
            description="따뜻한 집 안, 벽난로 앞에서 함께 있는 노인과 강아지",
            action="노인이 소파에서 책을 읽고, 강아지가 발치에 누워 평화롭게 잠들어 있다",
            emotion="평화, 행복, 완전한 치유",
            camera=CameraSettings(
                movement="slow dolly out",
                angle="wide establishing",
                transition="fade",
            ),
            lighting="warm golden interior, fireplace glow",
            key_elements=["cozy living room", "fireplace", "sleeping puppy", "content smile"],
        ),
        Scene(
            id=7,
            title="서로의 눈",
            title_en="Eyes of Family",
            duration=15,
            description="노인과 강아지가 서로를 바라보며 미소 짓는 엔딩",
            action="강아지가 노인의 얼굴을 핥고, 노인이 웃으며 강아지를 쓰다듬는다",
            emotion="사랑, 감동, 가족의 완성",
            camera=CameraSettings(
                movement="slow push in",
                angle="close-up, eye level",
                transition="fade to black",
            ),
            lighting="soft warm backlighting",
            key_elements=["loving gaze", "gentle touch", "happy ending", "family portrait"],
        ),
    ]


def create_mock_prompts(scenes: list[Scene], character: Character) -> list[Prompt]:
    """Create mock prompts for testing."""
    char_desc = character.sora2_prompt_fragment
    prompts = []

    for scene in scenes:
        english = f"""{char_desc}. {scene.description}. {scene.action}. {scene.camera.movement} shot transitioning to {scene.camera.angle}. {scene.lighting}. {scene.emotion} atmosphere. Photorealistic 4K cinematic quality with subtle film grain."""

        prompts.append(Prompt(
            scene_id=scene.id,
            english=english,
            korean=None,  # Will be filled by translation
            structure=PromptStructure(
                character_desc=char_desc,
                setting=scene.description,
                action=scene.action,
                camera=f"{scene.camera.movement}, {scene.camera.angle}",
                lighting=scene.lighting,
                atmosphere=scene.emotion,
            ),
            quality_score=85 + (scene.id % 10),
        ))

    return prompts


def create_mock_translations(prompts: list[Prompt]) -> list[Prompt]:
    """Add mock Korean translations."""
    translations = [
        "크림색 복슬복슬한 털, 크고 표현력 있는 갈색 눈, 살짝 늘어진 귀, 분홍 코, 가슴에 흰 반점을 가진 골든 리트리버 강아지가 비 오는 저녁 도시 골목 구석 젖은 골판지 상자 안에 웅크려 있다. 희망을 담은 눈으로 지나가는 행인들을 올려다보지만 모두 지나친다. 와이드에서 클로즈업으로 천천히 다가가는 달리 샷. 차갑고 푸른 회색 조명, 흐린 하늘, 비. 슬프고 고독하지만 미약한 희망이 담긴 분위기.",
        "골든 리트리버 강아지가 검은 우산을 쓴 노인과 눈이 마주친다. 노인이 천천히 걸어오다 멈춰 서서 강아지를 바라본다. 빗소리 속 고요한 순간. 트래킹 샷으로 노인을 따라가다 미디엄 앵글로 전환. 차가운 조명에 따뜻한 가로등 빛이 강조된다.",
        "노인이 천천히 쪼그려 앉아 강아지에게 손을 내민다. 강아지가 조심스럽게 손 냄새를 맡고 노인의 손가락을 핥는다. 손에 집중하는 클로즈업으로 천천히 다가가는 샷. 조명이 점점 따뜻해진다. 조심스러운 희망과 신뢰의 시작.",
        "노인이 일어서려다 강아지의 눈을 다시 바라본다. 얼굴에 갈등이 스치고, 강아지는 꼬리를 조심스럽게 흔들기 시작한다. 정적인 샷에 미세한 떨림, 얼굴 클로즈업 교차. 극적인 그림자와 감정적인 조명.",
        "노인이 결심하고 강아지를 품에 안아 올린다. 강아지가 처음으로 활기차게 꼬리를 흔든다. 비가 그치기 시작하고 햇살이 비친다. 크레인 업 샷으로 미디엄에서 와이드로 전환. 따뜻한 황금빛이 비쳐든다.",
        "따뜻한 집 안, 벽난로 앞에서 함께 있는 노인과 강아지. 노인이 소파에서 책을 읽고, 강아지가 발치에 평화롭게 잠들어 있다. 천천히 뒤로 빠지는 달리 아웃 와이드 샷. 따뜻한 황금빛 실내 조명, 벽난로 불빛.",
        "노인과 강아지가 서로를 바라보며 미소 짓는다. 강아지가 노인의 얼굴을 핥고, 노인이 웃으며 쓰다듬는다. 눈높이 클로즈업으로 천천히 다가가는 샷. 부드러운 따뜻한 역광. 사랑, 감동, 가족의 완성.",
    ]

    for i, prompt in enumerate(prompts):
        if i < len(translations):
            prompt.korean = translations[i]

    return prompts


def create_mock_titles(story: Story) -> TitleSet:
    """Create mock titles for testing."""
    return TitleSet(
        main_title="버려진 강아지가 할아버지를 만났을 때",
        subtitle="서로의 빈자리를 채운 기적 같은 인연",
        platform_variants=PlatformTitles(
            youtube_shorts="💔 버려진 강아지가 외로운 할아버지를 만나고 일어난 일 (실화)",
            instagram_reels="비 오는 날 운명처럼 만난 강아지와 할아버지의 이야기 🐕💕",
            tiktok="버려진 강아지한테 일어난 일... 결말 보고 진짜 울었음 😭😭",
        ),
        hooks=TitleHooks(
            emotional="눈물 없이 못 보는 강아지와 할아버지 이야기",
            curiosity="이 버려진 강아지에게 무슨 일이 있었을까?",
            outcome="버려진 강아지에게 찾아온 기적 같은 결말",
        ),
    )


def main():
    """Run all tests with mock data."""
    console.print(Panel(
        "[bold]🐾 Animal Shorts Agent System - 테스트 실행[/bold]\n[dim](Mock Mode - API 키 없이 테스트)[/dim]",
        border_style="cyan",
    ))

    try:
        # Test 1: Input Agent (실제 동작)
        input_data = test_input_agent()

        # Test 2: Story (Mock)
        console.print("\n[bold cyan]═══ Testing Story Agent (Mock) ═══[/bold cyan]")
        story = create_mock_story(input_data)

        console.print(Panel(
            f"""[bold]{story.title}[/bold]

{story.synopsis}""",
            title="✓ Story Agent 결과",
            border_style="green",
        ))

        table = Table(title="스토리 아크", show_header=True)
        table.add_column("단계", style="cyan")
        table.add_column("설명")
        table.add_column("감정", style="yellow")

        for phase in story.arc:
            table.add_row(phase.phase, phase.description[:40] + "...", phase.emotion)
        console.print(table)

        # Test 3: Scenes (Mock)
        console.print("\n[bold cyan]═══ Testing Scene Agent (Mock) ═══[/bold cyan]")
        scenes = create_mock_scenes(story)

        table = Table(title=f"✓ Scene Agent 결과 ({len(scenes)}개 장면)", show_header=True)
        table.add_column("#", style="dim", width=3)
        table.add_column("제목", width=12)
        table.add_column("감정", width=20)
        table.add_column("카메라", width=15)

        for scene in scenes:
            table.add_row(
                str(scene.id),
                scene.title,
                scene.emotion[:20],
                scene.camera.movement,
            )
        console.print(table)

        # Test 4: Character
        character = Character(
            id="test-char",
            name="희망이",
            species="Golden Retriever Puppy",
            visual_description=VisualDescription(
                fur="fluffy cream-colored fur with golden undertones",
                eyes="large expressive brown eyes",
                size="small puppy, approximately 3 months old",
                distinctive_features=["slightly floppy ears", "pink nose", "white patch on chest"],
            ),
            sora2_prompt_fragment="A golden retriever puppy with fluffy cream-colored fur, large expressive brown eyes, slightly floppy ears, pink nose, and a white patch on chest",
        )

        # Test 5: Prompts (Mock)
        console.print("\n[bold cyan]═══ Testing Prompt Agent (Mock) ═══[/bold cyan]")
        prompts = create_mock_prompts(scenes, character)

        console.print(Panel(
            f"""[bold]Scene {prompts[0].scene_id}: {scenes[0].title}[/bold]
[dim]Quality Score: {prompts[0].quality_score}/100[/dim]

{prompts[0].english[:350]}...""",
            title=f"✓ Prompt Agent 결과 ({len(prompts)}개 프롬프트)",
            border_style="green",
        ))

        # Test 6: Translation (Mock)
        console.print("\n[bold cyan]═══ Testing Translation Agent (Mock) ═══[/bold cyan]")
        prompts = create_mock_translations(prompts)

        console.print(Panel(
            f"""[bold]🇺🇸 English:[/bold]
{prompts[0].english[:200]}...

[bold]🇰🇷 한국어:[/bold]
{prompts[0].korean[:150]}...""",
            title="✓ Translation Agent 결과",
            border_style="green",
        ))

        # Test 7: Titles (Mock)
        console.print("\n[bold cyan]═══ Testing Title Agent (Mock) ═══[/bold cyan]")
        titles = create_mock_titles(story)

        console.print(Panel(
            f"""[bold]메인 제목:[/bold] {titles.main_title}
[bold]부제목:[/bold] {titles.subtitle}

[bold]플랫폼별 제목:[/bold]
• YouTube: {titles.platform_variants.youtube_shorts}
• Instagram: {titles.platform_variants.instagram_reels}
• TikTok: {titles.platform_variants.tiktok}

[bold]후킹 변형:[/bold]
• 감정형: {titles.hooks.emotional}
• 호기심형: {titles.hooks.curiosity}
• 결과형: {titles.hooks.outcome}""",
            title="✓ Title Agent 결과",
            border_style="green",
        ))

        # Final Summary
        console.print("\n")
        console.print(Panel(
            f"""[bold green]✅ 모든 테스트 완료![/bold green]

📊 결과 요약:
• 스토리: {story.title}
• 장면 수: {len(scenes)}개
• 프롬프트: {len(prompts)}개
• 총 영상 길이: {sum(s.duration for s in scenes)}초
• 메인 제목: {titles.main_title}

💡 실제 API 연동 실행 방법:
   export ANTHROPIC_API_KEY="your-api-key"
   python main.py""",
            title="테스트 완료",
            border_style="green",
        ))

        # Show sample output format
        console.print("\n[bold cyan]═══ 샘플 출력 (클립보드용) ═══[/bold cyan]")
        console.print()

        for i, prompt in enumerate(prompts[:2]):
            console.print(f"{'═' * 60}")
            console.print(f"[bold][SCENE {prompt.scene_id}] {scenes[i].title}[/bold]")
            console.print(f"{'═' * 60}")
            console.print()
            console.print(prompt.english)
            console.print()
            console.print(f"{'─' * 60}")
            console.print(f"[dim]🇰🇷 {prompt.korean[:100]}...[/dim]")
            console.print(f"{'─' * 60}")
            console.print()

        console.print("[dim]... (총 7개 장면)[/dim]")

    except Exception as e:
        console.print(f"\n[red]❌ 에러 발생: {e}[/red]")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
