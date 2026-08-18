
# ================ Closed Book Drill ==================== 
print(f"\n{'=' * 20} Drill {'=' * 20}")


# NOTE """ ... """ 会保留你写进去的换行和空格
prompt = """
        ===== Candidate Tracker =====
        1. Add candidate
        2. View candidates
        3. Quit"""
# 这里前面的 8 个 spaces 是 string 内容的一部分，所以 terminal 也会显示
# 注意 opening """ 后面立刻换行，所以 string 最前面还有一个 newline。
# 如果这个 prompt 放在 function 里，就会出现一个很常见的问题：为了 Python indentation 你给它缩进了 4 spaces，但那 4 spaces 也进入 string。

# NOTE ("...""....")

# ("..."
#  "...")
# → 代码可以随意漂亮地缩进
# → indentation 不属于 string
# 
# # """..."""
# → 格式本身就是内容
# → newline / indentation 会保留


prompt = (
    "===== Candidate Tracker =====\n"
    "1. Add candidate\n"
    "2. View candidates\n"
    "3. Quit\n"
    "Choose an option: "
)

candidates = []

while True:
    # NOTE: you don't have to conver it to int. String can do comparision as well. 
    # BUG two layers, forgot one, program won't run from beginning    
    # option = input(prompt)
    # if option == "1":


    option = int(input(prompt))
    if option == 1:
        # NOTE incrementally build dictionary。
        # 更好的办法是先问 input 然后统一建立 candidate 
        # ? 我必须得先 declare 这个 candidate var 去创建一个空的 dict 吧
        # candidate = {}
        # # dict[key] = value 加或者 modify 
        # c_name = input("Enter Candidate name: ")
        # candidate["name"] = c_name
# 
        # c_experience = int(input("Enter Candidate's years of experience: "))
        # candidate["experience"] = c_experience
# 
        # c_score = int(input("Enter Candidate's technical score: "))
        # candidate["score"] = c_score

        # NOTE 当你一开始就知道完整 structure 时通常更清楚
        c_name = input("Enter candidate name: ")
        c_experience = int(input("Enter candidate's years of experience: "))
        c_score = int(input("Enter candidate's technical score: "))

        candidate = {
            "name": c_name,
            "experience": c_experience,
            "score": c_score,
        }

        candidates.append(candidate)

    elif option == 2:
        # NOTE empty list[] 是 falsy 所以下面的写法更 Pythonic  
        # if not candidates:
        # NOTE pyhton buil-in list 没有 empty()或者 isEmpty()
        # empty collection 在 Boolean context 中被认为是 False
        # 非空则通常是 True
        if len(candidates) == 0:
            print("No candidates found")
        else:
            for candidate in candidates:
                print (candidate)
                if candidate["experience"] >= 2 and candidate["score"] >= 75:
                    print("Pass")
                else:
                    print("Reject")
    elif option == 3:
        break

    else:
        print("Invalid input. Choose again")


