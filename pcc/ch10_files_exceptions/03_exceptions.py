# Common exceptions:
#
# ValueError        -> bad value/content → value 内容不合适 → int("hello")
# TypeError         -> wrong type/unsupported operation → type 不对 / operation 不支持 → "3" + 5
# KeyError          -> missing dict key → dict key 不存在 → candidate["email"]
# IndexError        -> invalid sequence index → list/string index 越界 → nums[100]
# FileNotFoundError -> file path does not exist → path 找不到文件 → Path("missing.txt").read_text()
# ZeroDivisionError -> divide by zero  → 除以 0 → 10 / 0


#==== Exercise 1 — ValueError =========
#? how to enclose this in a while loop? so if keep getting valueerror, then go back to the try block?? 

try:
    score_input = int(input("Enter technical score: "))
except ValueError:
    print ("Invalid score. Please enter a number.")
else:
     if not 0 <= score_input <= 100:
        #print(f"Score: {score_input}")
        print("A number but Not a valid score number")
     #else: 逻辑反了 , 而且可以省去这个 else 
     #    print("A number but Not a valid score number")
     print(f"Score: {score_input}")

# Exception handling ≠ Business validation

# ====== Exercise 2 — FileNotFoundError ===========
from pathlib import Path

path = Path(__file__).parent / "does_not_exist.txt"

try:
    contents = path.read_text()
except FileNotFoundError:
    print("file not found")
else:
    print(contents)

# ====== Exercise 3 — KeyError vs .get() =========
candidate = {
    "name": "Alex",
    "technical_score": 82,
}
try:
    candidate["email"]
except KeyError:
    print("Key not found")
else:
    # []→ "这个 key 应该存在，缺了是问题"
    # .get() → "这个 key 可以不存在，给我 default 就行"
    print(candidate.get("email", "Not provided"))


# ========= Exercise 4 — Parsing a candidate record ===========
records = [
    "Alex,3,82",
    "Emma,6,hello",
    "Sam,1,90",
]

for record in records:
    name, experience, score = record.split(",")
    try:
        years_experience = int(experience)
        technical_score = int(score)
    except ValueError:
        print(f"Invalid numeric data: {record}")
    else:
        print(record)
        # 按照题目，成功时更值得输出真正 parse 出来的 data：
        print(
        f"{name}: "
        f"experience={years_experience}, "
        f"score={technical_score}"
    )

# ============================================================
# raise
# ============================================================


# ------------------------------------------------------------
# 1. raise means: create / trigger an exception
# ------------------------------------------------------------

# Python sometimes raises exceptions automatically:
#
# int("hello")
# → Python raises ValueError
#
#
# But our own code can also decide that a situation is invalid:
#
# raise ValueError("Score must be between 0 and 100.")


# ------------------------------------------------------------
# 2. Validation with if vs raising an exception
# ------------------------------------------------------------

# Simple validation:
#
# if not 0 <= score <= 100:
#     print("Invalid score")
#
#
# Raising:
#
# if not 0 <= score <= 100:
#     raise ValueError("Score must be between 0 and 100.")
#
#
# Difference:
#
# print()
# → displays a message
# → normal execution may continue
#
# raise
# → creates an exception
# → normal execution stops at that point
# → exception must be handled somewhere or program crashes


# ------------------------------------------------------------
# 3. Common pattern: function validates its own inputs
# ------------------------------------------------------------

# def update_score(score):
#     if not 0 <= score <= 100:
#         raise ValueError("Score must be between 0 and 100.")
#
#     return score
#
#
# The function establishes a contract:
#
# valid score:
# → return normally
#
# invalid score:
# → raise ValueError


# ------------------------------------------------------------
# 4. Caller can catch the exception
# ------------------------------------------------------------

# try:
#     score = update_score(150)
#
# except ValueError as error:
#     print(error)
#
#
# Flow:
#
# caller
#   ↓
# update_score(150)
#   ↓
# detects invalid data
#   ↓
# raise ValueError(...)
#   ↓
# jumps back up to caller
#   ↓
# matching except handles it


# ------------------------------------------------------------
# 5. raise is different from return
# ------------------------------------------------------------

# return:
# → normal function completion
# → sends a value back to caller
#
# raise:
# → abnormal function completion
# → sends an exception up the call stack


# Example:
#
# def process_score(score):
#     if score < 0:
#         raise ValueError("Score cannot be negative.")
#
#     return score * 2


# ------------------------------------------------------------
# 6. Code after raise does not execute
# ------------------------------------------------------------

# def test():
#     print("Before")
#     raise ValueError("Something went wrong")
#     print("After")
#
#
# "After" will never run.


# ------------------------------------------------------------
# 7. Choosing the exception type
# ------------------------------------------------------------

# Use an exception type that describes the problem.
#
# ValueError
# → correct kind/type of value,
#   but unacceptable content/value
#
# Example:
# score = 150
#
# It is an int,
# but 150 violates the allowed range.


# TypeError
# → caller passed something of an inappropriate type
#
# KeyError
# → missing required dictionary key
#
# FileNotFoundError
# → expected file/path is missing


# For now, ValueError is the main one you should practice raising yourself.


# ------------------------------------------------------------
# 8. Why raise instead of print inside the function?
# ------------------------------------------------------------

# Suppose:
#
# def update_score(score):
#     if not 0 <= score <= 100:
#         print("Invalid score")
#         return
#
#
# The function decides HOW the error is displayed.
#
#
# With raise:
#
# def update_score(score):
#     if not 0 <= score <= 100:
#         raise ValueError("Invalid score")
#
#
# The caller decides what to do:
#
# CLI:
# → print message
#
# API:
# → return HTTP error
#
# batch job:
# → log error
#
# test:
# → verify that ValueError was raised


# ------------------------------------------------------------
# 9. Important design idea
# ------------------------------------------------------------

# Lower-level function:
# → detect problem
# → raise exception
#
# Higher-level caller:
# → decide how to handle it
#
#
# This separation is common in real software.


# ------------------------------------------------------------
# 10. Mental model
# ------------------------------------------------------------

# return value
#
# function
#    ↓
# return result
#    ↓
# caller continues normally


# exception
#
# function
#    ↓
# raise Error
#    ↓
# normal execution stops
#    ↓
# search for matching except
#    ↓
# handled OR program terminates