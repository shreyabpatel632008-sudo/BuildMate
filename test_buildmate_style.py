
from image_agent import generate_post_image

image_path = generate_post_image(
    title="My First AWS Project: Building a Static Website with S3",
    content=(
        "A beginner-friendly guide to creating an S3 bucket, "
        "uploading website files and hosting a static website."
    ),
    aspect_ratio="16:9"
)

print("BuildMate image generated!")
print("Saved at:", image_path)
