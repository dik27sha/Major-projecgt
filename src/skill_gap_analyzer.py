
def analyze_skill_gaps(candidate_skills, required_skills):
    """
    Compare candidate skills with skills required for a target job.

    Args:
        candidate_skills (list): Skills mentioned in the resume.
        required_skills (list): Skills required for the target role.

    Returns:
        dict: Matched skills, missing skills and match percentage.
    """

    if not isinstance(candidate_skills, list):
        raise ValueError("Candidate skills must be a list.")

    if not isinstance(required_skills, list):
        raise ValueError("Required skills must be a list.")

    if not all(isinstance(skill, str) and skill.strip()
               for skill in candidate_skills + required_skills):
        raise ValueError("Every skill must be a non-empty string.")

    # Remove duplicates while preserving original skill names.
    candidate_map = {
        skill.strip().casefold(): skill.strip()
        for skill in candidate_skills
    }

    required_map = {
        skill.strip().casefold(): skill.strip()
        for skill in required_skills
    }

    matched_skills = []
    missing_skills = []

    for normalized, original in required_map.items():
        if normalized in candidate_map:
            matched_skills.append(original)
        else:
            missing_skills.append(original)

    total_required = len(required_map)

    match_percentage = (
        round((len(matched_skills) / total_required) * 100, 2)
        if total_required else 100.0
    )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage,
        "total_required_skills": total_required
    }
