candidates = [
    {
        "name": "Alex",
        "years_experience": 3,
        "technical_score": 82,
        "skills": ["python", "sql", "git", "pytorch"],
        "contact": {
            "email": "alex@example.com",
            "city": "Detroit",
        },
    },
    {
        "name": "Emma",
        "years_experience": 6,
        "technical_score": 92,
        "skills": ["python", "sql", "docker", "tensorflow"],
        "contact": {
            "email": "emma@example.com",
            "city": "Chicago",
        },
    },
    {
        "name": "Sam",
        "years_experience": 1,
        "technical_score": 90,
        "skills": ["python", "tensorflow"],
        "contact": {
            "city": "Troy",
        },
    },
    {
        "name": "John",
        "years_experience": 4,
        "technical_score": 65,
        "skills": ["python", "pytorch", "git"],
        "contact": {
            "email": "john@example.com",
            "city": "Ann Arbor",
        },
    },
]

screening_skills = [
    "python",
    "sql",
    "pytorch",
    "tensorflow",
    "docker",
]

required_skill_counts = len(screening_skills)

interview_count = 0
# state/counter placement
# engineering principle：If a value can be reliably derived from another source of truth, don't necessarily store another mutable copy of it.
reject_count = 0 

######################################################
# Requirement 1 — Process every candidate
# 每个 candidate 开头输出类似：
# ==============================
# Candidate: Alex
# City: Detroit
# Email: alex@example.com

# Sam 没有 email，所以要求输出：
# Email: Not provided

for candidate in candidates:
    print("==============================")
    print(f"Candidate: {candidate["name"]}")
    print(f"City: {candidate["contact"]["city"]}")
    print(f"Email: {candidate["contact"].get("email","Not provided")}")

    # experience
    expr = candidate["years_experience"]
    if 0 <= expr < 2:
        print(f"Experience level: Entry")
    elif 2 <= expr < 5:
        print(f"Experience level: Mid")
    elif expr >= 5:
        print(f"Experience level: Senior")

    # skill matching
    count = 0 
    
    for skill in screening_skills:
        if skill in candidate["skills"]:
            print(f"Has {skill}")
            count += 1 
    print(f"Matched Skills: {count}/{required_skill_counts}")

    # interview decision
    if (candidate["years_experience"] >= 2 
        and candidate["technical_score"] >= 75 
        and "python" in candidate["skills"] 
        and ("pytorch" in candidate["skills"] or "tensorflow" in candidate["skills"] )):
        print(f"Decision: ML Interview")
        interview_count +=1
    else:
        print(f"Decision: Reject")
        reject_count += 1 

    # Bonus Skill 
    if "sql" in candidate["skills"]:
        print("Bonus: SQL")
    if "git" in candidate["skills"]:
            print("Bonus: Git")
    if "docker" in candidate["skills"]:
            print("Bonus: Docker")


# Overall Summary
#BUG Python 的普通单引号或双引号字符串（包括 f-string）默认不能直接换行。
# 三引号（f"""...""" 或 f'''...'''）允许字符串直接换行，且会保留你缩进的空格。
# 因为 triple-quoted string 自己已经保留换行，同时你又加了 \n，所以容易产生额外 blank lines。
print(f"""===== Overall Summary ===== 
      Candidates processed: {len(candidates)}
      Candidates invited: {interview_count}
      Candidates rejected: {reject_count}""")

# ALTERNATIVE2  使用隐式字符串拼接（保持左对齐）在小括号 () 内，Python 会自动把相邻的多个字符串字面量拼接成一个。这种方法可以让你在代码中对齐，且不会引入多余的缩进空格：
# 括号中的几个 adjacent strings 会先组合成 一个 string，再传给一次 print()。
# NOTE: 不是每行都调用 print, 是每行一个f-string
print(
    f"===== Overall Summary =====\n"
    f"Candidates processed: {len(candidates)}\n"
    f"Candidates invited: {interview_count}\n"
    f"Candidates rejected: {reject_count}"
)

# 不推荐 - ALTERNATIVE 3 使用反斜杠换行符 \在每行的末尾加上续行符 \，告诉 Python 下一行依然是当前逻辑行
print(f"===== Overall Summary =====\n" \
      f"Candidates processed: {len(candidates)}\n" \
      f"Candidates invited: {interview_count}\n" \
      f"Candidates rejected: {reject_count}")






##########################################################
# Requirement 2 — Experience level
# 
# 每个人只属于一个：
# 0–1 years → Entry
# 2–4 years → Mid
# 5+ years  → Senior
# 
# 输出：
# 
# Experience level: Mid

##########################################################
# Requirement 3 — Skill matching
# 对： screening_skills 逐个检查 candidate 是否拥有。
# 有的话输出： 
# Has python
# Has sql
# Has pytorch
# 
# 同时 count：
# Matched skills: 3/5
# 
# 这里要特别注意：
# matched_skills 应该每个 candidate 都重新从 0 开始。
# 想想这个 variable 应该放在 for loop 外还是里面。
# 这是这次 program 一个很重要的 design point。