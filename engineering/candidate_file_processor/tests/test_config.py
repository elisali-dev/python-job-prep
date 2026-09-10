import pytest
from candidate_processor.config import get_passing_score 

def test_cli_passing_score_overrides_environment(monkeypatch):
    monkeypatch.setenv("PASSING_SCORE", "85")

    result = get_passing_score(
        cli_value=90
    )

    assert result == 90 

def test_environment_passing_score_used_when_no_cli(monkeypatch):
    monkeypatch.setenv("PASSING_SCORE", "85")
    result = get_passing_score(
        cli_value=None
    )
    assert result == 85

def test_default_passing_score_used_when_no_cli_or_environment(
    monkeypatch,
):
    monkeypatch.delenv(
        "PASSING_SCORE",
        raising=False,
    )

    result = get_passing_score(
        cli_value=None
    )

    assert result == 80

def test_invalid_environment_passing_score_raises_error(
    monkeypatch,
):
    monkeypatch.setenv(
        "PASSING_SCORE",
        "banana",
    )

    with pytest.raises(
        ValueError,
        match="PASSING_SCORE must be an integer",
    ):
        get_passing_score(
            cli_value=None
        )

def test_out_of_range_passing_score_raises_error(
    monkeypatch,
):
    monkeypatch.setenv(
        "PASSING_SCORE",
        "150",
    )

    with pytest.raises(
        ValueError,
        match="PASSING_SCORE must be between 0 and 100",
    ):
        get_passing_score(
            cli_value=None
        )

        