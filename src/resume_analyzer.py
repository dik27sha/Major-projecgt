
import json
from src.helper import ask_openai
from src.prompts import RESUME_ANALYSIS_PROMPT


REQUIRED_FIELDS = [
    "summary",
    "skills",
    "education",
    "experience",
    "skill_gaps",
    "roadmap",
    "job_keywords"
]


def analyze_resume(resume_text):
    """
    Analyze resume and generate personalized career recommendations.

    Args:
        resume_text (str): Extracted text from the candidate's resume.

    Returns:
        dict: Structured resume analysis.
    """

    if not isinstance(resume_text, str) or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    prompt = RESUME_ANALYSIS_PROMPT.replace(
        "{resume_text}", resume_text
    )

    # Day 4: Handle AI API failures
    try:
        response = ask_openai(prompt, max_tokens=2000)
    except Exception as error:
        raise RuntimeError(
            "Unable to connect to AI service."
        ) from error

    try:
        analysis = json.loads(response)
    except (json.JSONDecodeError, TypeError) as error:
        raise ValueError(
            "AI returned an invalid JSON response."
        ) from error

    if not isinstance(analysis, dict):
        raise ValueError("AI response must be a JSON object.")

    for field in REQUIRED_FIELDS:
        if field not in analysis:
            raise ValueError(
                f"Missing field in AI response: {field}"
            )

    if not isinstance(analysis["summary"], str):
        raise ValueError("Summary must be a string.")

    list_fields = [
        "skills",
        "education",
        "experience",
        "skill_gaps",
        "roadmap",
        "job_keywords"
    ]

    for field in list_fields:
        if not isinstance(analysis[field], list):
            raise ValueError(
                f"{field} must be a list."
            )

        if not all(isinstance(item, str) for item in analysis[field]):
            raise ValueError(
                f"Every item in {field} must be a string."
            )

    return analysis
