
def generate_learning_roadmap(missing_skills):
    """
    Generate a structured learning roadmap for missing skills.

    Args:
        missing_skills (list): Skills the candidate needs to learn.

    Returns:
        list: Learning stages with duration, tasks and projects.
    """

    if not isinstance(missing_skills, list):
        raise ValueError("Missing skills must be a list.")

    if not all(isinstance(skill, str) and skill.strip()
               for skill in missing_skills):
        raise ValueError("Every skill must be a non-empty string.")

    # Remove duplicate skills while preserving order.
    skills = list(dict.fromkeys(
        skill.strip() for skill in missing_skills
    ))

    roadmap = []

    for index, skill in enumerate(skills, start=1):
        roadmap.append({
            "week": index,
            "skill": skill,
            "duration": "1 week",
            "learning_tasks": [
                f"Understand the fundamentals of {skill}.",
                f"Practice important concepts of {skill}.",
                f"Build a small application using {skill}."
            ],
            "practical_project": f"Create a mini project using {skill}.",
            "milestone": f"Complete a practical task using {skill}."
        })

    return roadmap
