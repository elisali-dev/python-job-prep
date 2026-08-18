# 这个program 暴露的问题

    # data structure 前后不一致
    # function contract 不一致
    # duplicated business logic
    # counter / state 放在哪里
    # boundary condition
    # copy-paste 后 key/name 没同步
    # return indentation 改变 control flow

## NOTE program design/ application coding - 决定哪里应该是 function、这个 function 接收什么、return 什么、谁负责什么。

# Refactor 不是把每三行代码都变成 function。
# 
# 目标是让程序：
# 
# 更容易理解
# 更少重复
# 职责更清楚
# data contract 一致
# 以后更容易修改

############   FUNCTION DEFINITIONS ###############################################
def get_experience_level(candidate):
    years = candidate["years_experience"]

    if years >= 5:
        return "Senior"
    elif years >= 2:
        return "Mid"
    else:
        return "Entry"


def is_qualified(candidate):
    return (
        candidate["years_experience"] >= 2
        and candidate["technical_score"] >= 75
    )

#def count_matching_skills(candidate, screening_skills):
    matched_counter = 0
    for skill in screening_skills:
        if skill in candidate["skills"]:
            matched_counter += 1
    return matched_counter


#BUG -  逻辑重复 - 跟 is qualified 逻辑重复
# def interview_decision (candidate):
#     if (candidate["years_experience"] >= 2 
#              and candidate["technical_score"] >= 75 
#              and "python" in candidate["skills"] 
#              and ("pytorch" in candidate["skills"] or "tensorflow" in candidate["skills"] )):
#              print(f"Decision: ML Interview")
#              # 我没有设这个paramter 
#              interview_count +=1
#     else:
#              print(f"Decision: Reject")
#              # 我没有作为parameter 传进来, 所以会得到 unboundLocalError
#              reject_count += 1 

def add_candidate (candidates):
    c_name = input("Enter the name:")
    c_experience = int(input("Enter years of experience: "))
    c_score = int(input("Enter the technical score:"))
    candidate = {
                 "name": c_name,
                 "years_experience": c_experience,
                 "technical_score": c_score
             }
    candidates.append(candidate)
# NOTE 定义一个函数的时候,一定要用return 吗? 不一定。所有函数都会返回东西,但如果你没有明确定义返回值,函数就只会返回None
# 这里不需要返回值, 只需要 append 所以可以没有 return statement 

def view_candidates(candidates):
     if not candidates:
          print("No candidates found.")
          return
            # 这个 return 的作用是结束 function, 因为这样后面就不用整个套在 else: 里面. candidates 是空的 → 已经没什么可做了 → 立刻结束 function。
     # no need to have else, normal processing here
     for candidate in candidates:
        print("===== Candidate Report =====")
        print(f"Candidate: {candidate["name"]}")
        # BUG 你 add candidate 里并没有下面这些 key. Function contact 
        # BUG data model inconsistency
       # print(f"City: {candidate["contact"]["city"]}")
        #print(f"Email: {candidate["contact"].get("email","Not provided")}")
        print(f"Experience level: {get_experience_level(candidate)}")
        print(f"Technical score: {candidate['technical_score']}")

        if is_qualified(candidate):
            print("Decision: Pass")
        else:
            print("Decision: Reject")
        # print(f"Matched skills: {count_matching_skills(candidate, screening_skills)}/{len(screening_skills)}")
        # interview_decision (candidate)

        # Bonus Skill 
        # if "sql" in candidate["skills"]:
        #     print("Bonus: SQL")
        # if "git" in candidate["skills"]:
        #         print("Bonus: Git")
        # if "docker" in candidate["skills"]:
        #         print("Bonus: Docker")





################## DATA #############3
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

######### VAR ###########
# interview_count = 0




###################  MAIN LOOP ##################
prompt = (
"1. Add candidate\n"
"2. View candidates\n"
"3. Quit\n"
"Please enter your choice:" 
)

while True:
    choice = input(prompt)

    if choice == "1":
        add_candidate(candidates)

    elif choice == "2":
        view_candidates(candidates)

    elif choice == "3":
        break

    else:
        print("Invalid option")

# Overall Summary
# print(
#     f"===== Overall Summary =====\n"
#     f"Candidates processed: {len(candidates)}\n"
#     f"Candidates invited: {interview_count}\n"
#     #f"Candidates rejected: {reject_count}"
# )