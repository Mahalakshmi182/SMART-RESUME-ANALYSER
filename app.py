from flask import Flask, render_template, request
import os

from utils.parser import extract_text
from utils.skills import extract_skills
from utils.scorer import calculate_score
from utils.job_matcher import match_job_description


app = Flask(__name__)


# --------------------------------
# HOME PAGE
# --------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# --------------------------------
# RESUME ANALYSIS
# --------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")

    if not resume:

        return "Please upload a resume."

    # Extract text from PDF
    text = extract_text(resume)

    # Detect skills
    skills = extract_skills(text)


    # --------------------------------
    # Skills used for missing skills
    # --------------------------------

    all_skills = [
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


    # Find missing skills
    missing_skills = []

    for skill in all_skills:

        if skill not in skills:

            missing_skills.append(skill)


    # Calculate ATS score
    score = calculate_score(text, skills)


    # Send everything to result.html
    return render_template(
        "result.html",
        score=score,
        skills=skills,
        missing_skills=missing_skills,
        resume_text=text
    )


# --------------------------------
# JOB MATCH PAGE
# --------------------------------

@app.route("/job-match", methods=["GET"])
def job_match():

    resume_text = request.args.get("resume_text", "")

    return render_template(
        "job_match.html",
        resume_text=resume_text
    )


# --------------------------------
# PERFORM JOB MATCHING
# --------------------------------

@app.route("/job-match", methods=["POST"])
def perform_job_match():

    resume_text = request.form.get(
        "resume_text",
        ""
    )

    job_description = request.form.get(
        "job_description",
        ""
    )


    # Compare resume with job description

    match_percentage, matched_skills, missing_skills = match_job_description(
        resume_text,
        job_description
    )


    # Show result

    return render_template(
        "job_result.html",
        match_percentage=match_percentage,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )


# --------------------------------
# RUN FLASK
# --------------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )