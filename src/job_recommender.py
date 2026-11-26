

from src.job_api import fetch_all_jobs


def filter_jobs(jobs, user_skills):


    matched_jobs = []

    user_skills = [
        skill.lower() for skill in user_skills
    ]

    for job in jobs:

        required_skills = job.get("skills", [])

        matched_skills = [
            skill for skill in required_skills
            if skill.lower() in user_skills
        ]

        if matched_skills and required_skills:

            job = job.copy()

            match_score = (
                len(matched_skills) /
                len(required_skills)
            ) * 100

            job["matched_skills"] = matched_skills
            job["match_score"] = round(match_score, 2)

            matched_jobs.append(job)

    return matched_jobs


def remove_duplicate_jobs(jobs):


    unique_jobs = {}

    for job in jobs:

        key = (
            job.get("title", "").strip().lower(),
            job.get("company", "").strip().lower()
        )

        if key not in unique_jobs:
            unique_jobs[key] = job

    return list(unique_jobs.values())


def sort_jobs_by_relevance(jobs):


    return sorted(
        jobs,
        key=lambda job: job.get("match_score", 0),
        reverse=True
    )


def recommend_jobs(user_skills):


    try:
        all_jobs = fetch_all_jobs()

        filtered_jobs = filter_jobs(
            all_jobs,
            user_skills
        )

        unique_jobs = remove_duplicate_jobs(
            filtered_jobs
        )

        recommended_jobs = sort_jobs_by_relevance(
            unique_jobs
        )

        return recommended_jobs

    except Exception as error:
        print(f"Job recommendation error: {error}")
        return []
