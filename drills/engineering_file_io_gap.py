import pathlib 

# Exercise 1: read file as a whole
print("=========Exercise 1: read file as a whole===========")
with open("model_notes.txt", "r") as file:
    contents = file.read()
    print(contents)
# 离开 with block 自动 close, 所以不需要 写 file.close()


# Exercise 2: read line by line 
print("=========Exercise 2: read line by line=======")
with open("model_notes.txt", "r") as file:
    for line in file: # 本身就会自动逐行迭代
        # BUG line = file.readline().strip() 又强行跳行去读第二行
        clear_line = line.strip()
        print(clear_line)

# Exercise 3: Write to a file 
print("=======Exercise 3: Write to a file =========")
summary = (f"Total models: 3\n"
           f"Best model: model_c\n") 
        # NOTE f 可以去掉,因为这里没有变量, 直接两个 string 在括号里就行
with open("model_summary.txt", "w", encoding="UTF-8") as file: 
    file.write(summary)

# Exercise 4：观察 "w" 的行为
print("=======Exercise 4: Write to a file =========")
summary_1 = (f"Total models: 3\n"
           f"Best model: model_a\n")
with open("model_summary.txt", "w", encoding="UTF-8") as file: 
    file.write(summary_1)


# Exercise 5：观察 "a"
print("======== Exercise 5: append to a file ======")
with open("model_summary.txt", "a") as file:
    file.write("Reviewed: yes\n")

# NOTE print("hello") → 默认帮你加 \n
# file.write("hello") → 原样写，不自动换行