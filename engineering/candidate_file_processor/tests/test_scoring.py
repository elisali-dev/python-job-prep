import pytest

from candidate_processor.scoring import (
    evaluate_candidate,
    get_experience_level,
    get_matched_skills,
)


@pytest.mark.parametrize(
    "years_experience, expected_level",
    [
        (0, "Entry"),
        (1, "Entry"),
        (2, "Mid"),
        (4, "Mid"),
        (5, "Senior"),
        (10, "Senior"),
    ],
)
def test_get_experience_level(
    years_experience,
    expected_level,
):
    assert (
        get_experience_level(years_experience)
        == expected_level
    )


def test_get_matched_skills():
    skills = [
        "Python",
        "SQL",
        "Excel",
        "Docker",
    ]

    result = get_matched_skills(skills)

    assert result == [
        "docker",
        "python",
        "sql",
    ]


def test_recommend_candidate():
    candidate = {
        "name": "Alice",
        "years_experience": 5,
        "technical_score": 85,
        "skills": [
            "Python",
            "SQL",
            "Docker",
        ],
    }

    result = evaluate_candidate(candidate)

    assert result["experience_level"] == "Senior"
    assert result["decision"] == "Recommend"


def test_do_not_recommend_low_score():
    candidate = {
        "name": "Bob",
        "years_experience": 5,
        "technical_score": 60,
        "skills": [
            "Python",
            "SQL",
            "Docker",
        ],
    }

    result = evaluate_candidate(candidate)

    assert result["decision"] == "Do Not Recommend"