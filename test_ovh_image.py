
import requests
from pathlib import Path

API_URL = "https://stable-diffusion-xl.endpoints.kepler.ai.cloud.ovh.net/api/text2image"

prompt = """
A cute but professional technical editorial illustration about AI agents,
pastel lavender, soft pink, purple and white palette,
elegant 3D elements, subtle glass effects, soft lighting,
clean composition, premium technology magazine aesthetic,
no text, no watermark.
"""

payload = {
    "prompt": prompt,
    "negative_prompt": "blurry, low quality, distorted, watermark, text",
    "width": 1024,
    "height": 576
}

try:
    response = requests.post(
        API_URL,
        json=payload,
        timeout=180
    )

    print("Status:", response.status_code)
    print("Content type:", response.headers.get("content-type"))

    response.raise_for_status()

    if "image" in response.headers.get("content-type", ""):
        output = Path("data/generated_images")
        output.mkdir(parents=True, exist_ok=True)

        image_path = output / "ovh_test.png"
        image_path.write_bytes(response.content)

        print("Image generated successfully!")
        print("Saved at:", image_path)

    else:
        print("Unexpected response:")
        print(response.text[:2000])

except requests.RequestException as error:
    print("Request failed:", error)
    if getattr(error, "response", None) is not None:
        print(error.response.text[:2000])
