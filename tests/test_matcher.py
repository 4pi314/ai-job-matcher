from matcher import calculate_match


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