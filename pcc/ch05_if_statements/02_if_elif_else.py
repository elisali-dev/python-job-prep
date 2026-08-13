### ===================== 1. if ====================
    # 重要的是：Python 的 if 条件通常不需要加括号。
    # if condition:        ✅ Python style
    # if (condition):      ✅ works, but usually unnecessary
            # ========================================================
                # if 加括号的情况, 加了 ()，注意原因不一样：
                # 不是因为 if 要括号，而是因为 expression 太长，我想把它分成多行。
            #    if (
            #        years_experience >= 2
            #        and "python" in skills
            #        and "pytorch" in skills
            #    ):
            #        print("Qualified")


    # Python 支持 chained comparison：
        # if years_experience >= 0 and years_experience < 2: 可以写成
        # if 0 <= years_experience < 2:
 
### ===================== 2. if else  ====================
### ===================== 3.if / elif / else ================
    # Python 从上往下检查，遇到第一个 True 就停。所以顺序很重要。
    # 所以一般要从：most restrictive / highest threshold -> less restrictive

# if / elif / else -> choose ONE branch
# multiple independent if -> every True condition can run


# ================ Exercise 1 — simple if ===================== 
print(f"\n{'=' * 20} Exercise 1 — simple if {'=' * 20}")
temperature = 85 
# if termperature >= 70:
if temperature >= 80:
    print("It is hot")

# ================ Exercise 1 — if / else ===================== 
print(f"\n{'=' * 20} Exercise 2 — if / else {'=' * 20}")
number = 17
if number % 2 == 0:
    print (f"{number} is even.")
else:
    print (f"{number} is odd.")

# ================ Exercise 3 — if / elif/ else ===================== 
print(f"\n{'=' * 20} Exercise 3 — if / elif/ else {'=' * 20}")

score = 87

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Pass")
else:
    print("Needs Improvement")

# ================  Exercise 4 — MLE candidate level ===================== 
print(f"\n{'=' * 20}  Exercise 4 — MLE candidate level {'=' * 20}")

years_experience = 4

if 0 <= years_experience < 2:
   print("Entry level")
elif 2 <= years_experience < 5:
   print("Mid level")
else:
   print("Senior level")

# ================  Drill ===================== 
print(f"\n{'=' * 20}  Exercise Drill {'=' * 20}")

candidate_score = 82
has_python = True

# if (has_python != True):
if not has_python:
    # not 是一个 Boolean operator / logical operator，更准确说是 unary operator，因为它只作用在一个 expression 上
    print(f"Reject: Python required")
else:
    if (candidate_score >= 82):
        print(f"Strong interview")
    elif (candidate_score >= 75):
        print(f"Interview")
    elif (candidate_score >= 60):
        print(f"Phone screen")
    else:
        print("Reject")

