
import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        API_KEY = None

client = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(
        timeout=10000,
        retry_options=types.HttpRetryOptions(
            attempts=1
        )
    )
)

MODEL_NAME = "gemini-3.5-flash-lite"


def generate_content(topic, content_format, platform):

    prompt = f"""
You are BuildMate, a technical content creator.

TOPIC: {topic["title"]}
CATEGORY: {topic["category"]}
SOURCE: {topic["source"]}
SOURCE LINK: {topic["link"]}
SUMMARY: {topic["summary"]}

PLATFORM: {platform}
FORMAT: {content_format}

Rules:
- Write naturally and clearly.
- Be useful to students and developers.
- Do not invent statistics or facts.
- Do not invent personal experiences.
- Do not copy the source article.
- Include practical takeaways.
- Avoid unnecessary emojis and hashtags.

For LinkedIn Post:
Write an engaging opening, explanation,
practical takeaway and closing question.

For Technical Article:
Write a title, introduction, headings,
detailed explanation and conclusion.

For Poll:
Write one question and exactly four short options.

Return valid JSON only:
{{
    "title": "Content title",
    "format": "{content_format}",
    "platform": "{platform}",
    "body": "Complete content in Markdown",
    "poll_options": [],
    "source_link": "{topic["link"]}"
}}
"""

    print("Connecting to Gemini...", flush=True)

    try:
      interaction = client.interactions.create(
        model=MODEL_NAME,
        input=prompt,
        timeout=30
      )
      print("Gemini response received!", flush=True)

    except Exception as error:
        print("Gemini request failed:", error, flush=True)
        raise

    if not interaction.output_text:
        raise ValueError("Gemini returned an empty response.")

    raw_text = interaction.output_text.strip()

    # Remove Markdown code fences if Gemini adds them
    if raw_text.startswith("```"):
        raw_text = raw_text.replace("```json", "", 1)
        raw_text = raw_text.replace("```", "").strip()

    # Extract the JSON object
    start = raw_text.find("{")
    end = raw_text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(
            "Gemini did not return valid JSON. Response: "
            + raw_text[:1000]
        )

    json_text = raw_text[start:end + 1]

    try:
        result = json.loads(json_text)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Could not parse Gemini JSON: {error}\n"
            f"Gemini response: {raw_text[:1000]}"
        )

    required_fields = [
        "title",
        "format",
        "platform",
        "body",
        "poll_options",
        "source_link"
    ]

    for field in required_fields:
        if field not in result:
            raise ValueError(
                f"Gemini response is missing: {field}"
            )

    return result
