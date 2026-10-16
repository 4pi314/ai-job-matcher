from matcher import calculate_match, compare_skills, extract_skills


def test_identical_text_returns_full_match():
    text = "Python machine learning SQL Docker"
    assert calculate_match(text, text) == 100.0


def test_empty_resume_returns_zero():
    assert calculate_match("", "Python developer") == 0.0


def test_empty_job_description_returns_zero():
    assert calculate_match("Python developer", "") == 0.0


def test_related_texts_return_partial_match():
    score = calculate_match(
        "Python machine learning SQL",
        "Python SQL developer",
    )
    assert 0.0 < score < 100.0


def test_stop_words_only_return_zero():
    assert calculate_match("the and or", "but if the") == 0.0

def test_extract_skills_is_case_insensitive():
    skills = extract_skills("Python, SQL, Git and Docker")

    assert skills == {"python", "sql", "git", "docker"}


def test_compare_skills_finds_matched_and_missing():
    matched, missing = compare_skills(
        "Python SQL Git",
        "Python SQL Docker Git",
    )

    assert matched == ["git", "python", "sql"]
    assert missing == ["docker"]


def test_compare_skills_with_empty_resume():
    matched, missing = compare_skills(
        "",
        "Python Docker",
    )

    assert matched == []
    assert missing == ["docker", "python"]