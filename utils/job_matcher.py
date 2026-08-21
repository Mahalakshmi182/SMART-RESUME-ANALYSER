def match_job_description(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    skills = [
        "python",
        "java",
        "c++",
        "c",
        "html",
        "css",
        "javascript",
        "sql",
        "flask",
        "django",
        "react",
        "machine learning",
        "data science",
        "git",
        "github",
        "vs code",
        "matlab",
        "power bi",
        "vlsi"
    ]

    matched_skills = []
    missing_skills = []

    for skill in skills:

        if skill in job_description:

            if skill in resume_text:
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)

    total_required = len(matched_skills) + len(missing_skills)

    if total_required > 0:

        match_percentage = (
            len(matched_skills) / total_required
        ) * 100

    else:

        match_percentage = 0

    return (
        round(match_percentage, 2),
        matched_skills,
        missing_skills
    )