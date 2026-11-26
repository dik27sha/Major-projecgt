SAMPLE_JOBS = [
    {
        "title": "Python Developer",
        "company": "Tech Solutions",
        "location": "Noida",
        "skills": ["Python", "SQL", "Django"],
        "source": "LinkedIn",
        "apply_link": "https://www.linkedin.com/jobs/"
    },
    {
        "title": "Java Developer",
        "company": "Infosys",
        "location": "Bangalore",
        "skills": ["Java", "Spring Boot", "SQL"],
        "source": "Naukri",
        "apply_link": "https://www.naukri.com/"
    },
    {
        "title": "Data Analyst",
        "company": "Data Tech",
        "location": "Delhi",
        "skills": ["Python", "SQL", "Excel"],
        "source": "LinkedIn",
        "apply_link": "https://www.linkedin.com/jobs/"
    },
    {
        "title": "Web Developer",
        "company": "Web Solutions",
        "location": "Noida",
        "skills": ["HTML", "CSS", "JavaScript"],
        "source": "Naukri",
        "apply_link": "https://www.naukri.com/"
    },
    {
        "title": "Machine Learning Engineer",
        "company": "AI Innovations",
        "location": "Gurgaon",
        "skills": ["Python", "Machine Learning", "SQL"],
        "source": "LinkedIn",
        "apply_link": "https://www.linkedin.com/jobs/"
    }
]


def fetch_linkedin_jobs():
    """Fetch sample jobs representing LinkedIn listings."""
    try:
        return [
            job.copy()
            for job in SAMPLE_JOBS
            if job["source"] == "LinkedIn"
        ]
    except Exception as error:
        print(f"LinkedIn job fetching error: {error}")
        return []


def fetch_naukri_jobs():
    """Fetch sample jobs representing Naukri listings."""
    try:
        return [
            job.copy()
            for job in SAMPLE_JOBS
            if job["source"] == "Naukri"
        ]
    except Exception as error:
        print(f"Naukri job fetching error: {error}")
        return []


def fetch_all_jobs():
    """Combine job listings from both sources."""
    try:
        linkedin_jobs = fetch_linkedin_jobs()
        naukri_jobs = fetch_naukri_jobs()

        all_jobs = linkedin_jobs + naukri_jobs

        return all_jobs

    except Exception as error:
        print(f"Job fetching error: {error}")
        return []
