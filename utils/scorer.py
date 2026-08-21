def calculate_score(text, skills):

    text = text.lower()

    # -----------------------------
    # 1. Technical Skills - 30%
    # -----------------------------

    all_skills = [
        "python",
        "java",
        "c",
        "c++",
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

    if len(all_skills) > 0:

        skill_percentage = len(skills) / len(all_skills)

        skill_score = skill_percentage * 30

    else:

        skill_score = 0


    # -----------------------------
    # 2. Education - 15%
    # -----------------------------

    education_keywords = [
        "education",
        "b.tech",
        "btech",
        "bachelor",
        "degree",
        "engineering",
        "university",
        "college"
    ]

    education_score = 15 if any(
        keyword in text
        for keyword in education_keywords
    ) else 0


    # -----------------------------
    # 3. Experience - 15%
    # -----------------------------

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "worked",
        "developer",
        "engineer"
    ]

    experience_score = 15 if any(
        keyword in text
        for keyword in experience_keywords
    ) else 0


    # -----------------------------
    # 4. Projects - 15%
    # -----------------------------

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "implemented"
    ]

    project_score = 15 if any(
        keyword in text
        for keyword in project_keywords
    ) else 0


    # -----------------------------
    # 5. Certifications - 10%
    # -----------------------------

    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certified"
    ]

    certification_score = 10 if any(
        keyword in text
        for keyword in certification_keywords
    ) else 0


    # -----------------------------
    # 6. Keywords - 10%
    # -----------------------------

    keyword_list = [
        "communication",
        "teamwork",
        "leadership",
        "problem solving",
        "problem-solving",
        "analytical",
        "programming"
    ]

    keyword_count = sum(
        1 for keyword in keyword_list
        if keyword in text
    )

    keyword_score = min(
        (keyword_count / len(keyword_list)) * 10,
        10
    )


    # -----------------------------
    # 7. Resume Structure - 5%
    # -----------------------------

    sections = [
        "education",
        "skills",
        "experience",
        "projects",
        "certifications"
    ]

    section_count = sum(
        1 for section in sections
        if section in text
    )

    structure_score = (
        section_count / len(sections)
    ) * 5


    # -----------------------------
    # FINAL SCORE
    # -----------------------------

    total_score = (
        skill_score
        + education_score
        + experience_score
        + project_score
        + certification_score
        + keyword_score
        + structure_score
    )


    return round(total_score, 2)