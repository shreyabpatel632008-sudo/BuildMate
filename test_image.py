
from image_agent import generate_post_image

image_path = generate_post_image(
    title="Building Trust in AI Agents",
    content="Evaluating AI agents for accuracy, reliability, security and performance using Amazon Bedrock.",
    aspect_ratio="16:9"
)

print("Image generated successfully!")
print("Saved at:", image_path)
