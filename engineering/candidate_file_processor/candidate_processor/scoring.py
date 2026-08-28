#这个 module 负责：合法 candidate 应该得到什么 evaluation？
# 注意这里有一个很重要的 design：evaluate_candidate() 没有 print。它只是： input -> logic -> return result 这会让它非常容易测试。
# 以后写 ML pipeline 也是一样：prediction = model.predict(data) 最好不要 prediction function 自己到处 print / save / ask user input。

REQUIRED_SKILLS = {
    "python",
    "sql",
    "pytorch",
    "tensorflow",
    "docker",
}


def get_experience_level(years_experience:float) -> str:
    if years_experience < 2:
        return "Entry"

    if years_experience < 5:
        return "Mid"

    return "Senior"


def get_matched_skills(skills:list[str]) -> set[str]:
    normalized_skills = {
        skill.strip().lower()
        for skill in skills
    }

    matched_skills = REQUIRED_SKILLS & normalized_skills

    return sorted(matched_skills)


def evaluate_candidate(candidate:dict[str,str|int|float|list[str]]) -> dict[str,str|set[str]]:
    experience_level = get_experience_level(
        candidate["years_experience"]
    )
    # NOTE set type 
    matched_skills = get_matched_skills(
        candidate["skills"]
    )

    if (
        candidate["technical_score"] >= 70
        and len(matched_skills) >= 3
    ):
        decision = "Recommend"
    else:
        decision = "Do Not Recommend"

    return {
        "experience_level": experience_level,
        "matched_skills": matched_skills,
        "decision": decision,
    }