
import feedparser
import re
import html
from datetime import datetime, timezone
from urllib.parse import quote_plus


# Technical topics BuildMate should monitor
TOPIC_CATEGORIES = {
    "AWS & Cloud": [
        "AWS", "Amazon Web Services", "cloud computing",
        "Amazon Bedrock", "serverless", "cloud security"
    ],
    "Artificial Intelligence": [
        "artificial intelligence", "AI agents", "generative AI",
        "large language models", "machine learning"
    ],
    "Cybersecurity": [
        "cybersecurity", "data breach", "phishing",
        "ransomware", "security vulnerability"
    ],
    "Programming & Developer Tools": [
        "Python", "programming", "GitHub",
        "developer tools", "software development"
    ]
}


def clean_text(text):
    """Remove HTML tags and extra spaces."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return " ".join(text.split())


def get_category(title):
    """Identify the technical category of a headline."""
    title_lower = title.lower()

    for category, keywords in TOPIC_CATEGORIES.items():
        if any(word.lower() in title_lower for word in keywords):
            return category

    return "Technology"


def calculate_score(title, published):
    """Rank topics using relevance and freshness."""
    title_lower = title.lower()
    score = 0

    for keywords in TOPIC_CATEGORIES.values():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                score += 3

    if published:
        try:
            age_days = (
                datetime.now(timezone.utc) - published
            ).days

            if age_days <= 1:
                score += 5
            elif age_days <= 3:
                score += 3
            elif age_days <= 7:
                score += 1

        except (TypeError, ValueError):
            pass

    return score


def get_feeds():
    """Build RSS feed URLs for technical news searches."""

    searches = [
        "AWS cloud computing",
        "AI agents generative AI",
        "cybersecurity technology",
        "Python developer tools"
    ]

    feeds = [
        "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
    ]

    for search in searches:
        url = (
            "https://news.google.com/rss/search?q="
            + quote_plus(search)
            + "&hl=en-IN&gl=IN&ceid=IN:en"
        )
        feeds.append(url)

    return feeds


def discover_trends(limit=10):
    """Discover and rank current technical topics."""

    all_topics = {}
    feeds = get_feeds()

    feedparser.USER_AGENT = "BuildMate/1.0"

    for feed_url in feeds:

        try:
            feed = feedparser.parse(feed_url)

            if feed.bozo and not feed.entries:
                continue

            for entry in feed.entries:

                title = clean_text(entry.get("title", ""))

                if not title:
                    continue

                link = entry.get("link", "")

                published = None
                if entry.get("published_parsed"):
                    published = datetime(
                        *entry.published_parsed[:6],
                        tzinfo=timezone.utc
                    )

                score = calculate_score(title, published)

                # Ignore unrelated headlines
                if score < 3:
                    continue

                unique_key = title.lower()

                topic = {
                    "title": title,
                    "link": link,
                    "source": entry.get("source", {}).get(
                        "title", "Technical News"
                    ),
                    "category": get_category(title),
                    "summary": clean_text(
                        entry.get("summary", "")
                    ),
                    "published": (
                        published.strftime("%Y-%m-%d %H:%M UTC")
                        if published else "Date unavailable"
                    ),
                    "score": score
                }

                if (
                    unique_key not in all_topics
                    or score > all_topics[unique_key]["score"]
                ):
                    all_topics[unique_key] = topic

        except Exception as error:
            print("Feed error:", error)

    ranked_topics = sorted(
        all_topics.values(),
        key=lambda item: item["score"],
        reverse=True
    )

    return ranked_topics[:limit]
