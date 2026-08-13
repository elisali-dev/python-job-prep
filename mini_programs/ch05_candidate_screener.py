# data 
# candidate_name = "Alex"
# years_of_experience = 3
# technical_score = 82 
# skills = ["python", "sql", "git", "pytorch"]

# test data Sam 
candidate_name = "Sam"
years_of_experience = 1
technical_score = 90 
skills = ["python", "tensorflow"]

# Emma
# 6 years
# score 92
# skills = python, sql, docker, tensorflow
# 
# John
# 4 years
# score 65
# skills = python, pytorch, git

# Output Candidate Summary
print("===== Candidate Screening Report =====\n\n")
print(f"Candidate: {candidate_name}")
print(f"Experience: {years_of_experience}")
print(f"Technical score: {technical_score}")


print("\n\n")

# Validate the data 
if years_of_experience < 0:
    print("Invalid experience value")
if technical_score >100 or technical_score < 0:
    print("Invalid technical score")

# Experience level 
if 0 <= years_of_experience < 2:
    print("Entry")
elif 2 <= years_of_experience < 5:
    print("Mid")
else: # 这里 -3 就会被判断成 senior 因为前面 detect invalid 这里没有 handle 
    print("Senior")

# Skill Report 
print("\n\n")
skill_requirements = ["python", "sql", "pytorch", "tensorflow", "docker"]
matched_skills = 0

for skill in skills:
    if skill in skill_requirements:
        print(f"Has {skill}")
        matched_skills = matched_skills + 1
        # ‼️ python 里面没有 ++ 运算符
        # 可以用 += 赋值运算符 x += 1 可以 
        # ++x 不会报错, 因为 python 会把它看成正号 

## 我的写法：遍历 candidate 会什么 → 看是不是我们关心的
## 但 requirement 的本质是: 对公司关心的每项 skill，检查 candidate 有没有。
## 更符合requirement的设计是: 遍历我们关心什么 → 看 candidate 会不会, 也避免 candidate skills 里如果不小心出现 duplicate

# matched_skills = 0
# for skill in skill_requirements:
#     if skill in skills:
#         print(f"Has {skill}")
#         matched_skills += 1


# Count matched skills
print("\n\n")
# print(f"Matched skills: {matched_skills}/5")
#应该避免 hard code 5 
print(f"Matched skills: {matched_skills}/{len(skill_requirements)}")

# Final Decision 
print("\n\n")
if (
    years_of_experience >= 2
    and technical_score >= 75
    and "python" in skills
    and ("pytorch" in skills or "tensorflow" in skills) 
):
    print("Final decision: ML Interview")
else:
    print("Final decision: Reject")

# Bonus Message 
print("\n\n")
if "sql" in skills:
    print("Bonus: SQL experience")
if "git" in skills:
    print("Bonus: Git experience")
#if "Docker" in skills: #BUG D in capital 
if "docker" in skills:
    print("Bonus: Docker experience")

