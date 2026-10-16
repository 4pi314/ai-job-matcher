import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILLS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",
    "sql",
    "html",
    "css",
    "react",
    "node.js",
    "django",
    "flask",
    "fastapi",
    "git",
    "github",
    "docker",
    "kubernetes",
    "linux",
    "aws",
    "azure",
    "gcp",
    "google cloud",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "nlp",
    "natural language processing",
    "computer vision",
    "rest api",
    "rest apis",
    "mongodb",
    "mysql",
    "postgresql",
}


def calculate_match(resume_text: str, job_description: str) -> float:
    """Return the similarity between a résumé and job description as a percentage."""
    resume_text = resume_text.strip()
    job_description = job_description.strip()

    if not resume_text or not job_description:
        return 0.0

    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(
            [resume_text, job_description]
        ).toarray()  # type: ignore

        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        return round(float(score) * 100, 1)
    except ValueError:
        return 0.0


def extract_skills(text: str) -> set[str]:
    """Extract recognized technical skills from text."""
    normalized_text = text.lower()

    found_skills = {
        skill
        for skill in SKILLS
        if re.search(
            rf"(?<![\w+#.]){re.escape(skill)}(?![\w+#.])",
            normalized_text,
        )
    }

    return found_skills


def compare_skills(
    resume_text: str,
    job_description: str,
) -> tuple[list[str], list[str]]:
    """Return matched skills and skills missing from the résumé."""
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = sorted(resume_skills & job_skills)
    missing_skills = sorted(job_skills - resume_skills)

    return matched_skills, missing_skills

def calculate_skill_coverage(
    resume_text: str,
    job_description: str,
) -> float:
    """Return the percentage of job skills found in the résumé."""
    job_skills = extract_skills(job_description)

    if not job_skills:
        return 0.0

    resume_skills = extract_skills(resume_text)
    matched_skills = resume_skills & job_skills

    coverage = len(matched_skills) / len(job_skills)
    return round(coverage * 100, 1)


def calculate_overall_match(
    resume_text: str,
    job_description: str,
) -> float:
    """Combine text similarity and skill coverage into one score."""
    text_score = calculate_match(resume_text, job_description)
    job_skills = extract_skills(job_description)

    if not job_skills:
        return text_score

    skill_score = calculate_skill_coverage(
        resume_text,
        job_description,
    )

    overall_score = (text_score * 0.4) + (skill_score * 0.6)
    return round(overall_score, 1)