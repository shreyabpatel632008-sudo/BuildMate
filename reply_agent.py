

from gemini_agent import client, MODEL_NAME
import time


def generate_reply(comment, platform, tone="Professional"):

    if not comment.strip():
        raise ValueError("Please enter the original comment.")

    prompt = f"""
You are BuildMate, a natural and professional social media reply assistant.

Platform: {platform}
Tone: {tone}

Original comment:
{comment}

Write one concise, meaningful reply.
Sound human, warm, and natural.
Answer questions thoughtfully.
Acknowledge appreciation warmly.
Do not invent facts or personal experiences.
Avoid unnecessary emojis and hashtags.

Return only the reply.
"""

    start_time = time.time()

    interaction = client.interactions.create(
    model=MODEL_NAME,
    input=prompt,
    generation_config={"max_output_tokens": 80},
    timeout=8
)

    elapsed = time.time() - start_time
    print(f"Reply generation time: {elapsed:.2f} seconds", flush=True)

    if not interaction.output_text:
        raise ValueError("Gemini returned an empty reply.")

    return interaction.output_text.strip()
