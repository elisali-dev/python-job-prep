# for = 已知要遍历什么
# while = 只要某个 condition 还成立，就一直重复
# 最重要的是：while loop 里面通常必须有东西最终改变 condition。
# NOTE:
# while True
# while var != "Sentinel value": ... # sentinel value 也就是一个特殊 value，代表：stop looping
# NOTE:
# break：→ 整个 loop 结束. immediately exit the nearest loop
# continue: → 只跳过 current iteration. 跳过这一轮剩余 code，直接进入下一轮 loop。

# ================ Exercise 1 — COUNT ===================== 
print(f"\n{'=' * 20} Exercise 1 — Count {'=' * 20}")

count = 1 

while count <= 5:
    print(count)
    count += 1

# ================ Exercise 2 — COUNT DOWN===================== 
print(f"\n{'=' * 20} Exercise 2 — Count down {'=' * 20}")

count = 5 

while count >= 1:
    print(count)
    count -= 1

print("Done!")


# ================ Exercise 3 —Infinite loop experiment ==================== 
print(f"\n{'=' * 20} Exercise 3 — Infinite loop experiment {'=' * 20}")

count = 1

while count <= 3:
    print(count)
    # Infinite loop happened if there is not status update
    count += 1 

# ================ Exercise 4 — User-controlled loop ==================== 
print(f"\n{'=' * 20} Exercise 4 — Break {'=' * 20}")
# message = ''
# NOTE python 3.8 以后出了 "":=" 运算符 可以不先 declare message var 了

# while (message := input("Enter a message (or 'quit'): ")) != 'quit':
# while message != 'quit':
#     message = input("Enter a message (or 'quit')")
#     print(f"You entered: {message}")

while True:
    message = input("Enter a message (or 'quit')")
    if message == "quit":
        break 
    print(f"You entered: {message}")


# ================ Exercise 5 — Continue ==================== 
print(f"\n{'=' * 20} Exercise 5 — Continue {'=' * 20}")

while True:
    number = int(input("Please enter an integer: "))
    if number < 0:
        print("Negative number ignored")
        continue
    elif number == 0:
        break
    else:
        print(f"Accepted: {number}")

#NOTE 处理特殊情况后尽早退出，让正常路径少一层 indentation。 更简单/更推荐写法如下

while True:
    number = int(input("Please enter an integer: "))

    if number < 0:
        print("Negative number ignored")
        continue

    if number == 0:
        break

    print(f"Accepted: {number}")


# ================ Exercise 6 — Simple menu ==================== 
print(f"\n{'=' * 20} Exercise 6 — Simple menu {'=' * 20}")

while True:
    print(
        f"1. Say hello\n"
        f"2. Show status\n"
        f"3. Quit\n\n"
    )
    number = int(input("Choose an option"))

    if number == 1:
        print("Hello!")
    elif number == 2:
            print("Program is running")
    elif number == 3:
            break
    else:
         print("Invalid option")


# ================ Closed Book Drill ==================== 
print(f"\n{'=' * 20} Drill {'=' * 20}")

while True:
     candidate_name = input("Candidate name (or 'quit')")
     if candidate_name == 'quit':
          break
     # NOTE break 后面其实不用 else     
     # NOTE 其实更推荐不写 code 可以少一层 indention 更清晰 
     else: # ?? 感觉这个 else 不写也行
          year = int(input("Years of experience: "))
          score = int(input("Technical score: "))
          if year >= 2 and score >= 75:
               # BUG print("f{candidate_name}")     # 普通 string ❌
               # f"{candidate_name}"     # f-string ✅
               #print("f{candidate_name} passes initial screen.")
               print(f"{candidate_name} passes initial screen.")
          else:
                #print("f{candidate_name} does not pass initial screen.")
                print(f"{candidate_name} does not pass initial screen.")
                
          

    








