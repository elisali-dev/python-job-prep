# 动态类型语言。在这些语言里，你不需要（也不能直接）在定义函数时指定返回值类型。
# Java 中，定义函数（Java 中通常叫“方法”，Method）时，必须明确指定返回值类型（Return Type）。这是因为 Java 是一种静态类型语言，编译器在编译时就必须清楚地知道每个函数会返回什么类型的数据。比方说 java 里就得写
#  public int add(int a, int b) {
#    return a + b;
# }

##### ============ 1. print() 和 return 完全不是一回事 ==========###########

# 所以 function 没有 explicit return 时，Python 默认： return None
# print→ show something to human
# return → send a value back to the code that called the function

#### no return , but print #######
def add(a, b):
    print(a + b)

# call . output is None 
result = add(2, 3)
print(result)

#### return and print ### 
def add(a, b):
    return a + b

result = add(2, 3)
print(result)


##### ============ 2. Returned value 可以继续参与程序  ==========###########
# 因为 function call 本身是一个 expression, evaluate 后变成一个 value。
def calculate_salary(hourly_rate, hours):
    return hourly_rate * hours

weekly_pay = calculate_salary(40, 35)

print(f"Weekly pay: ${weekly_pay:.2f}")

annual_pay = calculate_salary(40, 35) * 52

##### ============ 3. return 会立即结束 function  ==========###########
# return 不仅返回 value，也会 exit the current function。
def check_score(score):
    if score < 0:
        return "Invalid"

    return "Valid"

##### ============ 4. Multiple branches 可以 return 不同结果  ==========###########
def get_level(years):
    if years >= 5:
        return "Senior"
    elif years >= 2:
        return "Mid"
    else:
        return "Entry"

level = get_level(3)
print(level)

# 注意这里 function 不负责 print "Mid"。
# 它只负责：根据 years calculate / determine level。
# 至于怎么 display，是 caller 的事情。
# 这是更好的 separation of responsibility。


##### ============ 5. Boolean function 很常见  ==========###########
# 之前这样写 
def evaluate_candidate(name, years, score):
    if years >= 2 and score >= 75:
        print(f"{name}: Pass")
    else:
        print(f"{name}: Reject")

# 现在可以变成：
def is_qualified(years, score):
    return years >= 2 and score >= 75

# NOTE
# 注意甚至不用：
# if ...
#     return True
# else:
#     return False
# 
# 因为：years >= 2 and score >= 75
# 本身就已经 evaluate 成 True / False。

#然后外面：
qualified = is_qualified(3, 82)
if qualified:
    print("Pass")
else:
    print("Reject")

# 这种 function 命名也很常见：
# is_valid()
# is_qualified()
# has_permission()
# needs_update()
# 通常 return Boolean。

# ================ Exercise 1 ==================== 
print(f"\n{'=' * 20} Exercise 1 print vs return{'=' * 20}")

def multiply(a, b):
    print(a * b)

result = multiply(4, 5)
print(result)

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)


# ================ Exercise 2 ==================== 
print(f"\n{'=' * 20} Exercise 2 — Return calculated value {'=' * 20}")

def calculate_weekly_pay(hourly_rate, hours_worked):
    return hours_worked * hourly_rate

weekly_pay = calculate_weekly_pay(4, 40)

# NOTE 当输出是 money 的时候, 建议用格式 :.2f
print(f"Weekly pay: ${weekly_pay:.2f}")

# ================ Exercise 3 ==================== 
print(f"\n{'=' * 20} Exercise 3 — Return classification {'=' * 20}")

def get_experience_level(years_experience):
    if years_experience >= 5:
        return "Senior"

    # BOUNDARY BUG 
    # elif 2<= years_experience < 4: 
    elif 2<= years_experience < 5: 
        return "Mid"
    else:
        return "Entry" 

# NOTE 更简洁写法 - 利用 if elif 的逻辑顺序联调, 使需要写的条件少一半,
# def get_experience_level(years_experience):
#     if years_experience >= 5:
#         return "Senior"
#     elif years_experience >= 2:
#         return "Mid"
#     else:
#         return "Entry"



level = get_experience_level(3)
print(f"Experience level: {level}")


# ================ Exercise 4 ==================== 
print(f"\n{'=' * 20} Exercise 4 Boolean Return {'=' * 20}")

def is_candidate_qualified(years_experience, technical_score):
    return years_experience >= 2 and technical_score >= 75

result = is_candidate_qualified(3, 82)
print(result)

# 注意：is_candidate_qualified(...) 可以直接放进 if condition。
if is_candidate_qualified(3, 82):
    print("Pass")
else:
    print("Reject")


# ================ Drill 1==================== 
print(f"\n{'=' * 20} Drill 1 {'=' * 20}")

# NOTE 没必要重新define 或者copy - 因为function本来就是define once , call many times 
def get_experience_level(years_experience):
    if years_experience >= 5:
        return "Senior"
    elif 2<= years_experience < 4: 
        return "Mid"
    else:
        return "Entry" 

level = get_experience_level(3)
print(f"Experience level: {level}")

# NOTE Function 在同一个 .py 文件里没必要重复定义。前面 define 一次，下面直接 reuse：
def is_candidate_qualified(years_experience, technical_score):
    return years_experience >= 2 and technical_score >= 75


candidate = {
    "name":"Alex",
    "years_experience": 3,
    "technical_score": 82
}

result = is_candidate_qualified(candidate["years_experience"], candidate["technical_score"])

# 注意：is_candidate_qualified(...) 可以直接放进 if condition。
if result:
    print("Pass")
else:
    print("Reject")







################
# print → human output
# return → program output
# 
# function without explicit return → None
# 
# return value can be:
# int
# str
# bool
# list
# dict
# ...几乎任何 Python object
# 
# return → immediately exits current function


# break 必须用在loop里 

# return：
# 立刻结束 function
# → returns None

# pass： 
# 什么也不做
# → 然后继续执行下一行

# 例如： 
# def test():
#     pass
#     print("Hello")
# 会输出：Hello