#======= input(prompt) ========
# input 永远返回string 
# 需要数字时convert age = int(input("Enter your age: "))
# score = float(input("Enter score: "))
# python 不同类别不能比较 比方说 string"85" 和 int 85, 但是数字兼容：Python 的设计哲学中，只要是数字家族的成员（如 int、float、bool、complex），它们之间就可以直接进行算术运算和比较大小
# prompt 可以放variable 或者直接打一个string 


# ================ Exercise 1 — Basic Input ===================== 
print(f"\n{'=' * 20} Exercise 1 — Basic Input {'=' * 20}")

name = input("Enter your name: ")
print(f"Hello, {name}!")


# ================ Exercise 2 — Inspect the Type ===================== 
print(f"\n{'=' * 20} Exercise 2 — Inspect the Type {'=' * 20}")

age = input("Enter your age: ")
print(age)
print(type(age)) # intput()always return string

# ================ Exercise 3 — Convert to int ===================== 
print(f"\n{'=' * 20} Exercise 3 — Convert to int {'=' * 20}")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# ================ Exercise 4 — Numeric Calculation ===================== 
print(f"\n{'=' * 20} Exercise 4 — Numeric Calculation {'=' * 20}")

# cast to float is more proper than int
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter your hours worked: "))

#NOTE: Money formatting
print(f"Weekly pay: ${hourly_rate * hours_worked:.2f}")
# print(f"Weekly pay: ${hourly_rate * hours_worked}")


# ================ Exercise 5 — Even / odd interactive version ===================== 
print(f"\n{'=' * 20} Exercise 5 — Even / odd interactive version {'=' * 20}")

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# ================ Exercise 6 — Candidate input ===================== 
print(f"\n{'=' * 20} Exercise 6 — Candidate input {'=' * 20}")

candidate_name = input("Enter your name: ")
years_of_experience = int(input("Enter your years of experience: "))
technical_score = int(input("Enter your technical score: "))

print(
    f"Candidate: {candidate_name}\n"
    f"Experience: {years_of_experience} years\n"
    f"Technical score: {technical_score}\n"
    )

if 0<= years_of_experience < 2:
    print("Entry")
elif 2 <= years_of_experience < 5:
    print("Mid")
else: 
    print("Senior")



# ================ Experiment ===================== 
print(f"\n{'=' * 20} Experiment {'=' * 20}")

# "20"+"1"
age = input("Enter age: ")
print(age + "1")

# 20 + 1 
age = int(input("Enter age: "))
print(age + 1)

# ================ Closed-book drill ===================== 
print(f"\n{'=' * 20} Drill {'=' * 20}")

candidate_name = input("Enter your name: ")
years_of_experience = int(input("Enter your years of experience: "))
technical_score = int(input("Enter your technical score: "))

if years_of_experience >= 2 and technical_score >= 75:
    print(f"{candidate_name} passes initial screen")
else:
    print(f"{candidate_name} does not pass initial screen")

