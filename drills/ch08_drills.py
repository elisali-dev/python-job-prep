# ================ Drill ==================== 
print(f"\n{'=' * 20} Drill {'=' * 20}")

candidate = {
    "name": "Alex",
    "years_experience": 3,
    "technical_score": 82,
    "skills": ["python", "sql", "git", "pytorch"],
}

def get_experience_level(candidate):
    if candidate["years_experience"] >= 5:
        return "Senior"
    elif candidate["years_experience"] >=2:
        return "Mid"
    else:
        return "Entry"


def is_qualified(candidate):
    # 括号的作用仍然是：允许 expression 自然跨多行 + 提高 readability。
    return (
        candidate["years_experience"] >= 2 
        and candidate["technical_score"] >= 75 
        and "python" in candidate["skills"] 
        and (
            "pytorch" in candidate["skills"] 
            or "tensorflow" in candidate["skills"]
            )
        )


screening_skills = [
    "python",
    "sql",
    "pytorch",
    "tensorflow",
    "docker",
]

def count_matching_skills(candidate, screening_skills):
    matched_counter = 0
    for skill in candidate["skills"]:
        if skill in screening_skills:
            matched_counter += 1 
    return matched_counter

# NOTE 更推荐
# for skill in screening_skills:
    if skill in candidate["skills"]:
        matched_counter += 1
# 因为 function 的问题是：公司要求的每个 screening skill，candidate match 了几个？
# 而且如果 candidate 数据错误出现： ["python", "python", "sql"]
# 你现在的方法可能把 Python count 两次。

print("===== Candidate Report =====")
print(f"Candidate: {candidate["name"]}")
print(f"Experience level: {get_experience_level(candidate)}")
print(f"Matched skills: {count_matching_skills(candidate, screening_skills)}/{len(screening_skills)}")
if is_qualified(candidate):
    print("Decision: Pass")
else:
    print("Decision: Reject")

# 学 def 并不重要；学会把大问题拆成有职责的 functions 才重要。