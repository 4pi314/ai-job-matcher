from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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