import json
from src.helper import ask_openai
from src.prompts import RESUME_ANALYSIS_PROMPT


def analyze_resume(resume_text):
    """
    Analyze resume and generate personalized career recommendations.

    Args:
        resume_text (str): Extracted text from the candidate's resume.

    Returns:
        dict: Resume analysis containing summary, skills, education,
              experience, skill gaps, roadmap and job keywords.
    """

    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    prompt = RESUME_ANALYSIS_PROMPT.replace(
        "{resume_text}", resume_text
    )

    response = ask_openai(prompt, max_tokens=2000)

    try:
        analysis = json.loads(response)
    except json.JSONDecodeError as error:
        raise ValueError(
            "AI returned an invalid JSON response."
        ) from error

    required_fields = [
        "summary",
        "skills",
        "education",
        "experience",
        "skill_gaps",
        "roadmap",
        "job_keywords"
    ]

    for field in required_fields:
        if field not in analysis:
            raise ValueError(
                f"Missing field in AI response: {field}"
            )

    return analysis