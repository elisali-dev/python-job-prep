# NOTE 常见truthiness 
bool([])     # False
bool("")     # False
bool(0)      # False

bool([1])    # True
bool("abc")  # True
bool(5)      # True
# NOTE 
# candidates =[]
# if not candidates: # True 如果 candidates 是 empty这个就是 True。 这个以后非常常见


# ================ Exercise 3  ==================== 
print(f"\n{'=' * 20} Exercise 3 {'=' * 20}")

candidates = []
while True:
    candidate_name = input("Candidate name: ")
    if candidate_name == "quit":
        break
    score = int(input("Score: "))
    candidate = {
        "name": candidate_name,
        "score": score
    }
    candidates.append(candidate)

print(candidates)


# ================ Exercise 5 ==================== 
print(f"\n{'=' * 20} Exercise 5 {'=' * 20}")

prompt = (
"1. Add candidate\n"
"2. View candidates\n"
"3. Quit\n"
"Please enter your choice:" 
)
#BUG - 拼写错误
# candiadtes =  []

candidates = []

while True:
    choice = input(prompt)
    if choice == "1":
        c_name = input("Enter the name:")
        c_socre = int(input("Enter the technical score:"))

        candidate = {
            "name": c_name,
            "score": c_socre
        }
        candidates.append(candidate)
    elif choice == '2':
        if not candidates:
            print("No candidates found.")
        else:
            counter = 1
            for i in candidates:
                print(f"====#{counter} candidate====\n"
                      f"    name: {i["name"]}\n"
                      f"    score: {i["score"]}"
                      )
                counter +=1 
    elif choice == '3':
        break

    else:
        print("Invalid options") 

# ================ Exercise 6 ==================== 
print(f"\n{'=' * 20} Exercise 6 {'=' * 20}")


prompt = (
"1. Add candidate\n"
"2. View candidates\n"
"3. Quit\n"
"Please enter your choice:" 
)

#BUG 拼写错误
# candiadtes =  []

candidates = []

while True:
    choice = input(prompt)
    if choice == "1":
        c_name = input("Enter the name:")
        c_experience = int(input("Enter years of experience: "))
        # BUG - 拼写错误 - syntax 没问题，但 naming quality 有问题。
        # c_socre = int(input("Enter the technical score:"))
        # 因为你定义和使用都拼成同一个错误，所以 Python 不会报错. 但还是应该改
        c_score = int(input("Enter the technical score:"))
    
        candidate = {
            "name": c_name,
            "experience": c_experience,
            "score": c_score
        }
        candidates.append(candidate)


    elif choice == '2':
        if not candidates:
            print("No candidates found.")
        else:
            counter = 1
            # NOTE: 虽然 i 没有问题, 但因为 i 通常容易让人以为是 integer index。而这里是指代的一个完整的 dictionary 所以把i 改成 candidate readability 更高. 
            for i in candidates:
                print(f"====#{counter} candidate====\n"
                      f"    name: {i["name"]}\n"
                      f"    experience: {i["experience"]}\n"
                      f"    score: {i["score"]}"
                      )
                if i["experience"] >= 2 and i["score"] >= 75:
                    print("Pass")
                else: 
                    print("Reject")
                counter +=1 
    else:
        break