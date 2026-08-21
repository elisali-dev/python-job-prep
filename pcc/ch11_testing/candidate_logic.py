# production code / code under test

def get_experience_level(years):
    if years >= 5:
        return "Senior"
    elif years >= 2:
        return "Mid"
    else:
        return "Entry"


def is_qualified(years, score):
    return years >= 2 and score >= 75


def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError(
            "Score must be between 0 and 100."
        )