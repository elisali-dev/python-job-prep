# Comparison expressions return True or False.

# =   assignment
# ==  equality comparison

# >= means "at least"
# <= means "at most"

# and: all conditions must be True
# or: at least one condition must be True

# in / not in: membership tests

# String comparison is case-sensitive.

#### =============== 1. Comparison operators ======================
age = 18

print(age == 18)
print(age != 18)
print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)

#### ================ 2. String comparison ==========================
language = "python"
# Python string comparison 默认 case-sensitive。
print(language == "python")   # True
print(language == "Python")   # False
print(language.lower()  == "python")   # True

#### ================ 3. and, or =======================================
# Python 有 & operator, 但 & 主要是做 bitwise operation 的. 
                ## Bitwise AND (Integers): It compares each bit of two numbers and returns 1 if both bits are 1, otherwise 0. 
                    # 5  in binary is 0101
                    # 3  in binary is 0011
                    # 5 & 3 binary is 0001 (which is 1)
                    # print(5 & 3)  # Output: 1
                ## Set Intersection: When used on Python sets, & finds the common elements between them.
                    # set_a = {1, 2, 3}
                    # set_b = {3, 4, 5}
                    # print(set_a & set_b)  # Output: {3}
                ## Pandas / NumPy Filtering: If you ever use data analysis libraries like Pandas, you must use & instead of and to combine conditions for filtering data frames. 
                    # df[(df['age'] > 20) & (df['city'] == 'New York')]

# and: the Logical Operator used for Boolean logic (True/False). Both needs to be true 
# or : at least one is true
## When you chain multiple and and or operators together in one expression, Python does not simply read them from left to right. Instead, it evaluates all the and operations first, and then evaluates the or operations.

#### ================== 4. in, not in ======================
# in 检查一个 value 是否在 collection 里面：

skills = ["python", "sql", "git"]

print("python" in skills)
print("java" in skills)

# ================ Exercise 1 — basic comparisons ===================== 
print(f"\n{'=' * 20} Exercise 1 — basic comparisons {'=' * 20}")

age = 20

print(age == 20) # True
print(age != 20) # False
print(age > 18) # True
print(age < 18) # False
print(age >= 20) # True
print(age <= 19) # False 

## ‼️ In Python, a Boolean value (True or False) is completely different from a text string value ("True" or "False").
# (a > 20) == "True" returns False because True is a bool data type and "True" is a str (string) data type, Python looks at them and says, "A boolean value cannot equal a piece of text." Therefore, the comparison results in False. 
a = 25
if str(a > 20) == "True": # ⚠️ cast boolean True to str 
    print("This works, but it is unnecessary!")

## ‼️ True is equal to 1, False is equal to 0 
## Booleans do equal integers in Python. This is because Python's bool class is actually a subclass of int.

# ================ Exercise 2 — "=" vs "=="" ===================== 
print(f"\n{'=' * 20} Exercise 2 - vs =={'=' * 20}")

score = 90
print(score == 90) # True
print(score == 80) # False 

# ================ Exercise 2 — "=" vs "=="" ===================== 
print(f"\n{'=' * 20} Exercise 2 - vs =={'=' * 20}")

# ================ Exercise 3 — String Comparison ===================== 
language = "Python"
# python string comparison is case sensitive 
print(language == "python") # False 
print(language.lower() == "python") # True 

# ================ Exercise 4 — and ===================== 
years_python = 2
years_ml = 1

# Python experience 至少 1 年，且 ML experience 至少 1 年
print(years_python >= 1 and years_ml >= 1)

years_ml = 0
print(years_python >= 1 and years_ml == 1)

# ================ Exercise 5 — or ===================== 
knows_pytorch = True
knows_tensorflow = False

# 判断是否至少会一个 deep learning framework
print (knows_pytorch or knows_tensorflow)

# ================ Exercise 6 — in ===================== 
skills = ["python", "sql", "git", "pytorch"]
# 分别检查：python, "java", "pytorch" 是否在 skills 里。
print ("python" in skills)
print ("java" in skills)
print ("pytorch" in skills)

# ================ Exercise 7 — not in ===================== 
skills = ["python", "sql", "git", "pytorch"]

print("docker" not in skills)
print("git" not in skills)

# ================= Drills ========================
candidate_skills = ["python", "sql", "pytorch"]
years_experience = 3

# 请只写 Boolean expressions，判断：
print(years_experience >= 2) # 是否至少 2 年经验
print("python" in candidate_skills) #是否会 Python
print("python" in candidate_skills and "sql" in candidate_skills) # 是否同时会 Python 和 SQL
print("python" in candidate_skills or "java" in candidate_skills) # 是否会 Python 或 Java
print("docker" not in candidate_skills) # 是否不会 Docker
print(years_experience >= 2 and "python" in candidate_skills and "pytorch" in candidate_skills)# 是否满足：至少 2 年经验, 并且会 Python, 并且会 PyTorch
