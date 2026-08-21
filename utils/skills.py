def extract_skills(text):

    text = text.lower()

    # Skills we want to detect
    skills_list = [
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

    detected_skills = []

    # Detect skills
    for skill in skills_list:

        if skill in text:

            # Avoid duplicates
            if skill not in detected_skills:
                detected_skills.append(skill)

    # HTML5 → HTML
    if "html5" in text and "html" not in detected_skills:
        detected_skills.append("html")

    # CSS3 → CSS
    if "css3" in text and "css" not in detected_skills:
        detected_skills.append("css")

    return detected_skills