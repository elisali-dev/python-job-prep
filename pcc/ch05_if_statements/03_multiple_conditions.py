### ============= if/elif vs multiple independent if =============
# 这一部分最重要的不是 syntax，而是判断：这些条件是“互斥选择一个”，还是“每个条件都应该独立检查”？
    # if / elif / else → choose ONE branch
    # multiple if → every True condition can run


# ================ Exercise 1 —  ===================== 
print(f"\n{'=' * 20} Exercise 1 — {'=' * 20}")

score = 95

if score >= 70:
    print("Pass")

if score >= 80:
    print("Good")

if score >= 90:
    print("Excellent")
#########################
score = 95

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Pass")


# ================ Exercise 2 ===================== 
print(f"\n{'=' * 20} Exercise 2 {'=' * 20}")

skills = ["python", "sql", "pytorch", "git"]

if "python" in skills:
    print("Python skill found")
if "sql" in skills:
    print("SQL skill found")
if "pytorch" in skills:
    print("PyTorch skill found")

# Exercise 3 — 为什么 elif 在这里是错的
# # This is wrong for this requirement because candidate 明明三个都会，但程序只 report 第一个。
if "python" in skills:
    print("Python skill found")
elif "sql" in skills:
    print("SQL skill found")
elif "pytorch" in skills:
    print("PyTorch skill found")

# ================ Exercise 4 一个 classification + 多个 independent checks ===================== 
print(f"\n{'=' * 20} Exercise 4 {'=' * 20}")

candidate_score = 88
skills = ["python", "sql", "pytorch"]

# 根据 candidate_score 输出一个 classification：
# >= 90 → Strong
# >= 75 → Qualified
# else  → Not qualified

if candidate_score >= 90:
    print("Strong")
elif candidate_score >= 75:
    print ("Qualified")
else:
    print("Not qualified")

if "python" in skills:
    print("Python skill found")
if "sql" in skills:
    print("SQL skill found")
if "pytorch" in skills:
    print("PyTorch skill found")


# ================ Exercise 5 — Required skill vs bonus skills ===================== 
print(f"\n{'=' * 20} Exercise 5 {'=' * 20}")
skills = ["python", "sql", "git"]

if "python" not in skills:
    print ("Reject")
else:
    if "sql" in skills:
        print("Bonus: SQL")
    if "git" in skills:
        print("Bonus Git")
    if "pytorch" in skills:
        print("Bonus PyTorch")

# ================ Exercise 6 — and vs multiple if ===================== 
print(f"\n{'=' * 20} Exercise 6 {'=' * 20}")

has_python = True
has_sql = True
# 是否同时满足两个条件？
if has_python and has_sql:
    print("Candidate has both Python and SQL")

# 分别告诉我每个条件是否满足。
if has_python:
    print("Candidate has Python")
if has_sql:
    print("Candidate has SQL")


# ================ Closed book drill ===================== 
print(f"\n{'=' * 20} Drill {'=' * 20}")

candidate_name = "Alex"
years_experience = 3
skills = ["python", "sql", "git", "pytorch"]

# Experience level 
if years_experience >= 5:
    print ("Senior")
elif 2 <= years_experience < 5:
    print("Mid")
elif 0 <= years_experience < 2:
    print("Entry")
else:
    print ("Wrong Input")

# Skill report
skills_requirement = ["python", "sql", "pytorch", "docker"]
matrix = [0,0,0,0]
# this first way is good try, but wrong 
# BUG 
# BUG 这里 i 不是 index. 第一次 loop i = "python" , matrix[i] 会变成 matrix["python"] = 1 
# TypeError: list indices must be integers or slices, not str
# ‼️ list index 必须是 integer 
for i in skills: # i 代表 skills 里的每一个 element, 所以用 skill 更好 
    if i in skills_requirement:
        print(f"Has {i}")
        matrix[i] = 1

# another way to report skills 
if "python" in skills:
    print ("Has Python") # ‼️ code block 相对于它所属的 if 再缩进一级，通常 4 spaces。
if "sql" in skills:
        print("Has SQL")
if "pytorch" in skills:
        print("Has PyTorch")
# BUG: "Docker" used.  string comparison case-sensitive："Docker" != "docker"
if "docker" in skills:
        print("Has Docker")

# Final Eligibility 
# ‼️ if header 多行写法
# if years_experience >=2 and "python" in skills and ("pytorch" in skills or "tensorflow" in skills):
if (years_experience >=2 
    and "python" in skills 
    and ("pytorch" in skills or "tensorflow" in skills)
): # ‼️closing ) 后面马上就是 :
    # print("Alex qualifies for ML interview")
    print(f"{candidate_name} qualifies for ML interview") # 有 variable 就避免 hardcoding 
else:
    print("Alex does not qualify for ML interview") # if code block，缩进 4 spaces。

####### implicit line continuation ###
# Python 在尚未闭合的 (), [], {} 里面允许自然换行 
# if (
#     condition       ← continuation indentation
# ):
#     print(...)      ← if block indentation
# 

######## ‼️ DO NOT Mix use Tab and Space ######### 
# 在 Python 3 中，绝对不能在同一个 .py 文件里混合使用真正的 Tab（制表符）和真正的空格。如果混用了，Python 解释器会直接报 IndentationError（缩进错误）并拒绝运行。只要确保你的编辑器设置了“将 Tab 转换为空格（Tab to Spaces）”，你就可以放心地用 Tab 键来缩进。

######## 关于 copy paste code 的 rule of thumb #########3
# 正在学习的核心 syntax / logic：自己打。 比如 if/elif, loop, list comprehension, f-string。
# 纯 boilerplate / 装饰：可以 copy。 比如你每次那个 print(f"\n{'=' * 20}...")，完全没必要重复手打。
# 已经非常熟练的代码：可以 copy/edit。
# 如果你 copy 了一段自己其实还写不出来的核心逻辑，那就失去了练习价值。
# 
# 真正工作也没人靠“全部手敲”证明能力。最终目标是：你知道该写什么、能 debug、能改、能从 blank file 开始组织程序。

