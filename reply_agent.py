
from gemini_agent import client, MODEL_NAME


def generate_reply(comment, platform, tone="Professional"):

    if not comment.strip():
        raise ValueError("Please enter the original comment.")

    prompt = f"""
You are BuildMate, a professional social media reply assistant.

PLATFORM: {platform}

ORIGINAL COMMENT:
{comment}

REPLY TONE:
{tone}

Instructions:
- Reply directly to the person's comment.
- Sound natural, polite and human.
- Keep the reply concise and meaningful.
- Be professional without sounding robotic.
- Avoid unnecessary emojis and hashtags.
- Do not repeat the original comment.
- Do not invent personal experiences or facts.
- If the comment asks a question, answer it thoughtfully.
- If someone appreciates the work, acknowledge them warmly.

Return only the suggested reply.
"""

    interaction = client.interactions.create(
        model=MODEL_NAME,
        input=prompt
    )

    if not interaction.output_text:
        raise ValueError("Gemini returned an empty reply.")

    return interaction.output_text.strip()
