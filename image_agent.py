
import requests
from pathlib import Path
from uuid import uuid4
from io import BytesIO
from PIL import Image, ImageOps

API_URL = (
    "https://stable-diffusion-xl.endpoints.kepler.ai.cloud.ovh.net"
    "/api/text2image"
)

IMAGE_FOLDER = Path("data/generated_images")
IMAGE_FOLDER.mkdir(parents=True, exist_ok=True)



def build_image_prompt(title, content):
    return f"""
Create a premium hand-drawn editorial illustration for a
professional technology blog cover.

ARTICLE TITLE: {title}
ARTICLE CONTEXT: {content[:1000]}

VISUAL IDENTITY:
- Cute, cozy, hand-drawn digital illustration.
- Soft lavender, pastel blue, cream and peach palette.
- Elegant sketch-like outlines and gentle shading.
- Warm lighting and a polished editorial art style.
- Professional, creative and welcoming.
- Consistent visual identity across different articles.

TOPIC-BASED STORYTELLING:
Understand the article topic and illustrate its actual subject.
Include relevant objects, tools, devices and visual metaphors.
For AWS topics, use recognizable cloud, storage, server,
security or networking concepts when relevant.
For AI topics, use meaningful AI and data-related visuals.
For cybersecurity, use shields, locks and security concepts.
Do not use the same generic composition for every topic.

COMPOSITION:
- Wide landscape editorial composition.
- One clear central visual story.
- A cute illustrated student or developer working
  at a laptop when appropriate.
- Balanced background details and decorative elements.
- Keep important objects within the central horizontal area.
- Leave some clean space for a headline overlay.

STRICTLY AVOID:
- Robots as the default subject.
- Plastic 3D mannequins and toy-like objects.
- Generic cloud-and-mountain scenery.
- Fake interface text or unreadable writing.
- Letters, words, numbers, logos and watermarks.
- Excessive pink or childish decorations.

Create beautiful, detailed, topic-relevant artwork.
The image must look like a professional illustrated
technology magazine cover, not a generic AI wallpaper.
"""


def generate_post_image(title, content, aspect_ratio="16:9"):
    prompt = build_image_prompt(title, content)

    payload = {
        "prompt": prompt,
        "negative_prompt": (
            "text, letters, words, watermark, logo, signature, "
            "blurry, low quality, distorted anatomy, extra fingers, "
            "generic robot, plastic mannequin, childish toy, clutter"
        )
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            headers={
                "accept": "application/octet-stream",
                "Content-Type": "application/json"
            },
            timeout=180
        )

        if response.status_code == 429:
            raise RuntimeError(
                "OVHcloud rate limit reached. Please wait before trying again."
            )

        response.raise_for_status()

        image = Image.open(BytesIO(response.content)).convert("RGB")

        # SDXL endpoint returns 1024 x 1024.
        # Crop locally for the requested display ratio.
        if aspect_ratio == "16:9":
            image = ImageOps.fit(
                image,
                (1024, 576),
                method=Image.Resampling.LANCZOS,
                centering=(0.5, 0.45)
            )
        elif aspect_ratio == "1:1":
            image = ImageOps.fit(
                image,
                (1024, 1024),
                method=Image.Resampling.LANCZOS
            )
        else:
            raise ValueError("Supported ratios: 16:9 and 1:1")

        filename = IMAGE_FOLDER / f"buildmate_{uuid4().hex[:10]}.png"
        image.save(filename, quality=95)

        return str(filename)

    except requests.RequestException as error:
        raise RuntimeError(f"Image generation failed: {error}") from error
