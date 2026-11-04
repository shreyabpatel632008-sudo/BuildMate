
def choose_content_format(topic):
    title = topic["title"].lower()

    poll_keywords = [
        "vs", "versus", "should", "which",
        "best", "future of", "challenges"
    ]

    article_keywords = [
        "framework", "architecture", "how to",
        "guide", "evaluation", "deployed",
        "migration", "implementation", "explained"
    ]

    if any(word in title for word in poll_keywords):
        return "Poll"

    if any(word in title for word in article_keywords):
        return "Technical Article"

    return "LinkedIn Post"


def choose_platform(topic):
    category = topic["category"].lower()

    if "aws" in category or "cloud" in category:
        return "AWS Builder Center"

    return "LinkedIn"


def build_content_prompt(topic, content_format, platform):
    prompt = f"""
You are BuildMate, an AI technical content assistant.

Create original content based on this topic:

TOPIC: {topic["title"]}
CATEGORY: {topic["category"]}
SOURCE: {topic["source"]}
SOURCE LINK: {topic["link"]}
SUMMARY: {topic["summary"]}

PLATFORM: {platform}
FORMAT: {content_format}

Rules:
- Keep information accurate to the supplied source.
- Do not invent facts, statistics or personal experiences.
- Write naturally and clearly.
- Avoid unnecessary emojis and hashtags.
- Include a useful takeaway.

For a LinkedIn Post:
Write an engaging opening, explanation,
practical takeaway and closing question.

For a Technical Article:
Write a title, introduction, headings,
detailed explanation and conclusion.

For a Poll:
Write one question and four short options.

Return valid JSON with:
title, format, platform, body, poll_options, source_link.

Return JSON only.
"""
    return prompt.strip()


def prepare_content(topic):
    content_format = choose_content_format(topic)
    platform = choose_platform(topic)

    prompt = build_content_prompt(
        topic,
        content_format,
        platform
    )

    return {
        "topic": topic["title"],
        "format": content_format,
        "platform": platform,
        "prompt": prompt
    }

def build_post_prompt(topic, *args, **kwargs):
    """
    Backward-compatible prompt function
    for the existing Create Post page.
    """

    if isinstance(topic, dict):
        topic_title = topic.get("title", "Technology")
        category = topic.get("category", "Technology")
        summary = topic.get("summary", "")
    else:
        topic_title = str(topic)
        category = "Technology"
        summary = ""

    return f"""
You are BuildMate, an AI content assistant.

Create an original, engaging and useful
LinkedIn post about:

Topic: {topic_title}
Category: {category}
Context: {summary}

Instructions:
- Use natural, human-friendly language.
- Start with an engaging opening.
- Explain the topic clearly.
- Include a practical takeaway.
- End with a meaningful question.
- Do not invent facts or statistics.
- Avoid excessive emojis and hashtags.

Write the complete post.
""".strip()
