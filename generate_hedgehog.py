"""Generate prompts for Golden Retriever + Hedgehog family story."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Story Configuration
STORY = {
    "title": "솔방울 가족의 탄생",
    "synopsis": "골든 리트리버가 물어온 아기 고슴도치가 성장하여 엄마가 되고, 솔방울 같은 아기들과 함께 특별한 가족을 이루는 감동 이야기",
    "character": {
        "dog": "A gentle golden retriever with soft cream-colored fur, warm brown eyes, and a caring expression",
        "baby_hedgehog": "A tiny African pygmy hedgehog with soft quills, small black bead-like eyes, pink nose, and delicate paws",
        "adult_hedgehog": "A fully grown African pygmy hedgehog with brown and cream quills, bright curious eyes, and a round body",
        "baby_hedgehogs": "Tiny newborn hedgehogs curled up like pinecones, with soft developing quills and closed eyes"
    }
}

SCENES = [
    {
        "id": 1,
        "title": "특별한 발견",
        "title_en": "A Special Discovery",
        "duration": 15,
        "description": "골든 리트리버가 조심스럽게 아기 고슴도치를 입에 물고 집으로 들어온다",
        "emotion": "호기심, 조심스러움, 따뜻함",
        "camera": "handheld POV, owner perspective",
        "lighting": "natural indoor lighting",
        "prompt": """First person POV handheld home video footage. The owner films their golden retriever walking toward them, carefully carrying a tiny African pygmy hedgehog in its mouth. The dog approaches slowly with extreme gentleness, soft lips barely touching the baby hedgehog's delicate quills. The tiny hedgehog is no bigger than a golf ball, eyes closed trustingly. Camera shakes slightly as the owner reacts with surprise. Natural indoor lighting, slight motion blur. Low quality home camera aesthetic, amateur footage feel, authentic and raw. The owner's excited breathing can almost be felt through the shaky footage."""
    },
    {
        "id": 2,
        "title": "첫 만남",
        "title_en": "First Meeting",
        "duration": 12,
        "description": "골든 리트리버가 아기 고슴도치를 부드러운 담요 위에 내려놓는다",
        "emotion": "부드러움, 보호본능, 신뢰",
        "camera": "handheld POV, crouching down",
        "lighting": "warm indoor lamp light",
        "prompt": """First person POV handheld home video. Owner crouches down filming as their golden retriever carefully places the tiny African pygmy hedgehog onto a soft blanket. The camera gets close, slightly shaky and out of focus momentarily as the owner adjusts. The dog's wet nose nudges the baby hedgehog, who uncurls to reveal tiny black bead eyes and pink nose. The golden retriever looks up at the camera, then back at the hedgehog protectively. Warm lamp lighting, grainy home video quality, slight video compression artifacts. Authentic amateur footage aesthetic."""
    },
    {
        "id": 3,
        "title": "함께 자라다",
        "title_en": "Growing Together",
        "duration": 15,
        "description": "시간이 흘러 고슴도치가 성장하고, 골든 리트리버와 함께하는 일상",
        "emotion": "행복, 우정, 일상의 평화",
        "camera": "handheld POV, casual filming",
        "lighting": "bright daylight from window",
        "prompt": """First person POV handheld home video. Owner casually films in their sunny living room. A now fully grown African pygmy hedgehog with brown and cream quills walks confidently next to the golden retriever. The camera follows them to a shared water bowl, the dog waiting patiently as the hedgehog drinks. Camera pans unsteadily, typical home video movement. The golden retriever's tail wags, bumping the camera slightly. Bright window light causes slight overexposure. Low resolution home camera quality, authentic daily life footage, warm and casual atmosphere."""
    },
    {
        "id": 4,
        "title": "새 생명의 기다림",
        "title_en": "Expecting New Life",
        "duration": 12,
        "description": "임신한 고슴도치를 골든 리트리버가 지켜보며 돌본다",
        "emotion": "기대, 보호, 설렘",
        "camera": "handheld POV, quiet observation",
        "lighting": "soft evening indoor light",
        "prompt": """First person POV handheld home video. Owner quietly films a pregnant African pygmy hedgehog with noticeably round belly resting in a cozy nest. Camera moves slowly, trying not to disturb. The golden retriever lies nearby watching protectively, then looks up at the owner holding the camera. Soft evening light from a lamp. The camera zooms in shakily on the hedgehog's belly, then back out. Grainy low-light footage, slight noise in darker areas. Intimate home video moment, authentic and tender."""
    },
    {
        "id": 5,
        "title": "솔방울 아기들",
        "title_en": "Pinecone Babies",
        "duration": 15,
        "description": "갓 태어난 아기 고슴도치들이 솔방울처럼 동글동글하게 모여있다",
        "emotion": "경이로움, 감동, 새 생명의 기적",
        "camera": "handheld POV, excited close-up",
        "lighting": "soft lamp light on nest",
        "prompt": """First person POV handheld home video. Owner excitedly films five tiny newborn hedgehogs curled up together, looking exactly like small pinecones. Camera shakes with excitement, goes in and out of focus trying to capture the tiny details. The soft white developing quills, closed eyes, barely visible pink noses. The mother hedgehog is nearby. The golden retriever's nose enters frame from the side, sniffing curiously. Owner's shadow briefly crosses the frame. Warm lamp light, grainy close-up footage, authentic amazed reaction captured through shaky camera work."""
    },
    {
        "id": 6,
        "title": "성장하는 가족",
        "title_en": "A Growing Family",
        "duration": 15,
        "description": "아기 고슴도치들이 눈을 뜨고 골든 리트리버 주변에서 탐험한다",
        "emotion": "활기, 귀여움, 행복",
        "camera": "handheld POV, following action",
        "lighting": "bright daylight",
        "prompt": """First person POV handheld home video. Owner films from floor level as five baby hedgehogs with open eyes explore around the patient golden retriever. Camera follows the tiny hedgehogs climbing over the dog's paws, sometimes losing focus when they move fast. The golden retriever stays perfectly still, only eyes moving. One baby hedgehog walks toward the camera lens. The mother hedgehog waddles through frame. Bright daylight, cheerful atmosphere. Shaky tracking movement, low quality home footage, genuinely playful and chaotic family moment."""
    },
    {
        "id": 7,
        "title": "우리는 가족",
        "title_en": "We Are Family",
        "duration": 18,
        "description": "골든 리트리버, 엄마 고슴도치, 다섯 아기 고슴도치가 함께 있는 가족 초상화",
        "emotion": "완전한 행복, 사랑, 가족의 완성",
        "camera": "handheld POV, proud owner filming",
        "lighting": "warm sunset through window",
        "prompt": """First person POV handheld home video. Owner proudly films their complete family: the golden retriever lying contentedly with the mother hedgehog nestled against its chest. Five young hedgehogs of varying sizes cuddle between the dog's front paws. Camera slowly pans across the scene, slightly unsteady. The golden retriever looks up at the owner with loving eyes, tail wagging gently. Warm sunset light through window creates golden glow, slightly overexposed. The camera lingers, capturing this perfect moment. Grainy home video quality, emotional amateur footage of an unlikely but beautiful family."""
    }
]

TITLES = {
    "main": "솔방울 가족의 탄생",
    "subtitle": "골든 리트리버가 물어온 작은 기적",
    "youtube": "💕 골든 리트리버가 아기 고슴도치를 물어왔는데... 1년 후 놀라운 일이 (실화)",
    "instagram": "강아지가 데려온 아기 고슴도치의 1년 후 🦔✨ 솔방울 같은 아기들까지",
    "tiktok": "골든리트리버가 입에 뭘 물고왔는데... 결말 보고 심장 녹음 😭🦔",
    "hooks": {
        "emotional": "눈물 없이 못 보는 골든 리트리버와 고슴도치 가족 이야기",
        "curiosity": "강아지가 물어온 고슴도치에게 1년 후 무슨 일이?",
        "outcome": "솔방울 같은 아기들로 완성된 특별한 가족"
    }
}

def main():
    console.print()
    console.print(Panel(
        f"[bold]{STORY['title']}[/bold]\n\n{STORY['synopsis']}",
        title="🦔 프롬프트 생성",
        border_style="green"
    ))

    # Scene table
    table = Table(title="장면 구성", show_header=True, header_style="bold magenta")
    table.add_column("#", width=3)
    table.add_column("제목", width=15)
    table.add_column("시간", width=6)
    table.add_column("감정", width=25)

    for scene in SCENES:
        table.add_row(
            str(scene["id"]),
            scene["title"],
            f"{scene['duration']}s",
            scene["emotion"]
        )

    console.print(table)
    console.print(f"\n[bold]총 영상 길이: {sum(s['duration'] for s in SCENES)}초[/bold]\n")

    # Print each prompt
    console.print("=" * 70)
    console.print("[bold cyan]📋 Sora2 프롬프트 (복사용)[/bold cyan]")
    console.print("=" * 70)

    for scene in SCENES:
        console.print(f"\n[bold yellow]═══ Scene {scene['id']}: {scene['title']} ({scene['title_en']}) ═══[/bold yellow]")
        console.print(f"[dim]Duration: {scene['duration']}s | Camera: {scene['camera']}[/dim]\n")
        console.print(Panel(
            scene["prompt"],
            border_style="green"
        ))

    # Titles
    console.print("\n" + "=" * 70)
    console.print("[bold cyan]🏷️ 제목 옵션[/bold cyan]")
    console.print("=" * 70)

    console.print(Panel(
        f"""[bold]메인 제목:[/bold] {TITLES['main']}
[bold]부제목:[/bold] {TITLES['subtitle']}

[bold cyan]YouTube Shorts:[/bold cyan]
{TITLES['youtube']}

[bold magenta]Instagram Reels:[/bold magenta]
{TITLES['instagram']}

[bold]TikTok:[/bold]
{TITLES['tiktok']}

[bold yellow]후킹 변형:[/bold yellow]
• 감정형: {TITLES['hooks']['emotional']}
• 호기심형: {TITLES['hooks']['curiosity']}
• 결과형: {TITLES['hooks']['outcome']}""",
        title="제목 세트",
        border_style="magenta"
    ))

    # Save to file
    output_file = "/Users/wonny/Documents/woo/animals/output/hedgehog_family.md"
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {STORY['title']}\n\n")
        f.write(f"> {STORY['synopsis']}\n\n")
        f.write(f"**총 길이:** {sum(s['duration'] for s in SCENES)}초 ({len(SCENES)}개 장면)\n\n")
        f.write("---\n\n")

        for scene in SCENES:
            f.write(f"## Scene {scene['id']}: {scene['title']} ({scene['title_en']})\n\n")
            f.write(f"- **Duration:** {scene['duration']}s\n")
            f.write(f"- **Emotion:** {scene['emotion']}\n")
            f.write(f"- **Camera:** {scene['camera']}\n")
            f.write(f"- **Lighting:** {scene['lighting']}\n\n")
            f.write(f"### Sora2 Prompt\n\n")
            f.write(f"```\n{scene['prompt']}\n```\n\n")
            f.write(f"### 장면 설명\n\n{scene['description']}\n\n")
            f.write("---\n\n")

        f.write("## 제목 옵션\n\n")
        f.write(f"**메인:** {TITLES['main']}\n\n")
        f.write(f"**부제목:** {TITLES['subtitle']}\n\n")
        f.write(f"- **YouTube:** {TITLES['youtube']}\n")
        f.write(f"- **Instagram:** {TITLES['instagram']}\n")
        f.write(f"- **TikTok:** {TITLES['tiktok']}\n\n")

    console.print(f"\n[green]✅ 저장 완료: {output_file}[/green]\n")

if __name__ == "__main__":
    main()
