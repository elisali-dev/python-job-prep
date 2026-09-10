import os


VALID_APP_ENVS = {
    "development",
    "testing",
    "production",
}

def get_passing_score(
        cli_value: int|None = None,
) -> int:

    if cli_value is not None:
        score = cli_value
    else:
        raw_value = os.getenv("PASSING_SCORE", "80")

        try:
            score = int(raw_value)
        except ValueError:
            raise ValueError(
                "PASSING_SCORE must be an integer."
            )

    if score < 0 or score > 100:
        raise ValueError(
            "PASSING_SCORE must be between 0 and 100."
        )

    return score



def get_app_env() -> str:
    app_env = os.getenv(
        "APP_ENV",
        "development",
    )

    if app_env not in VALID_APP_ENVS:
        raise ValueError(
            "APP_ENV must be one of: "
            "development, testing, production."
        )

    return app_env