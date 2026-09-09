import pytest

from candidate_processor.validation import (
    validate_candidate,
)


def test_valid_candidate():
    candidate = {
        "name": "Alice",
        "years_experience": 3,
        "technical_score": 85,
        "skills": ["Python", "SQL", "Docker"],
    }

   # assert validate_candidate(candidate) is True
    validate_candidate(candidate) # 只要没有exception 这个测试就算是通过


def test_negative_experience():
    candidate = {
        "name": "Alice",
        "years_experience": -1,
        "technical_score": 85,
        "skills": ["Python"],
    }

    with pytest.raises(
        ValueError,
        match="Years of experience cannot be negative",
    ):
        validate_candidate(candidate)


def test_invalid_technical_score():
    candidate = {
        "name": "Alice",
        "years_experience": 3,
        "technical_score": 120,
        "skills": ["Python"],
    }

    with pytest.raises(
        ValueError,
        match="Technical score must be between 0 and 100",
    ):
        validate_candidate(candidate)


def test_missing_field():
    candidate = {
        "name": "Alice",
        "years_experience": 3,
        "technical_score": 85,
    }

    with pytest.raises(ValueError):
        validate_candidate(candidate)