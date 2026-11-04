
from gemini_agent import generate_content

sample_topic = {
    "title": "Why evaluating AI agents matters",
    "category": "Artificial Intelligence",
    "source": "BuildMate test",
    "link": "https://example.com",
    "summary": (
        "AI agents should be evaluated for reliability, "
        "accuracy and safe behavior."
    )
}

try:
    result = generate_content(
        sample_topic,
        "LinkedIn Post",
        "LinkedIn"
    )

    print("\nGEMINI CONNECTION SUCCESSFUL!")
    print("\nTITLE:")
    print(result["title"])
    print("\nGENERATED CONTENT:")
    print(result["body"])

except Exception as error:
    print("\nGEMINI TEST FAILED:")
    print(error)
