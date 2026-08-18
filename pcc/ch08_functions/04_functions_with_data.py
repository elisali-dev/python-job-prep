# ============================================================
# Ch08 - Functions with Data
# Knowledge Notes
# ============================================================


# ------------------------------------------------------------
# 1. A whole dictionary can be passed into a function
# ------------------------------------------------------------

# Instead of passing every field separately:
#
# def is_qualified(years_experience, technical_score):
#     return years_experience >= 2 and technical_score >= 75
#
# is_qualified(
#     candidate["years_experience"],
#     candidate["technical_score"]
# )

# We can pass the entire dictionary:
#
# def is_qualified(candidate):
#     return (
#         candidate["years_experience"] >= 2
#         and candidate["technical_score"] >= 75
#     )
#
# is_qualified(candidate)


# ------------------------------------------------------------
# 2. How does the function know what keys are in the dictionary?
# ------------------------------------------------------------

# It DOES NOT know when the function is defined.
#
# Example:
#
# def is_qualified(candidate):
#     return candidate["years_experience"] >= 2
#
# When Python executes the "def" statement, it does NOT check:
#
# - whether candidate is a dictionary
# - whether "years_experience" exists
# - whether its value is an int
#
# Python only performs:
#
# candidate["years_experience"]
#
# when the function is actually CALLED.


# Example:
#
# candidate = {
#     "name": "Alex",
#     "years_experience": 3
# }
#
# is_qualified(candidate)
#
# During the function call:
#
# candidate parameter
#     ↓
# refers to the dictionary passed by the caller
#     ↓
# candidate["years_experience"]
#     ↓
# 3


# If the required key does not exist:
#
# bad_candidate = {"name": "Alex"}
# is_qualified(bad_candidate)
#
# → KeyError: "years_experience"


# This means the function and caller have an informal CONTRACT:
#
# is_qualified(candidate)
#
# expects candidate to contain something like:
#
# {
#     "years_experience": number,
#     "technical_score": number
# }
#
# Python does not enforce this contract when the function is defined.
# Errors may only appear at runtime.
#
# This is related to Python's dynamic typing.


# ------------------------------------------------------------
# 3. Function parameters are just local variable names
# ------------------------------------------------------------

# In:
#
# def is_qualified(candidate):
#
# "candidate" is just a parameter / local variable name.
#
# When we call:
#
# is_qualified(alex)
#
# inside the function:
#
# candidate → refers to whatever object "alex" referred to.


# ------------------------------------------------------------
# 4. Lists can also be passed into functions
# ------------------------------------------------------------

# def show_skills(skills):
#     for skill in skills:
#         print(skill)
#
# skills = ["python", "sql", "pytorch"]
# show_skills(skills)


# ------------------------------------------------------------
# 5. Mutable objects can be changed inside a function
# ------------------------------------------------------------

# Lists and dictionaries are mutable.
#
# def add_skill(skills):
#     skills.append("docker")
#
# skills = ["python", "sql"]
# add_skill(skills)
#
# print(skills)
# → ["python", "sql", "docker"]


# The function parameter and the variable outside can refer
# to the SAME list object:
#
# outside skills ─────┐
#                     ↓
#            ["python", "sql"]
#                     ↑
# function skills ────┘


# If we do NOT want the function to modify the original list:
#
# add_skill(skills.copy())


# ------------------------------------------------------------
# 6. Functions can call other functions
# ------------------------------------------------------------

# def get_experience_level(candidate):
#     years = candidate["years_experience"]
#
#     if years >= 5:
#         return "Senior"
#     elif years >= 2:
#         return "Mid"
#     else:
#         return "Entry"
#
#
# def print_candidate_report(candidate):
#     level = get_experience_level(candidate)
#
#     print(f"Candidate: {candidate['name']}")
#     print(f"Experience level: {level}")


# This is how a larger program begins to get STRUCTURE:
#
# main program
#     ↓
# print_candidate_report()
#     ↓
# get_experience_level()
# is_qualified()
# count_matching_skills()


# ------------------------------------------------------------
# 7. print() vs return
# ------------------------------------------------------------

# print()
# → displays something to a human / terminal
#
# return
# → sends a value from the function back to the caller


# Example:
#
# def add(a, b):
#     return a + b
#
# result = add(2, 3)
#
# The function call:
#
# add(2, 3)
#
# is an expression that evaluates to:
#
# 5


# A function with no explicit return returns None:
#
# def test():
#     print("Hello")
#
# result = test()
# print(result)
#
# → None


# ------------------------------------------------------------
# 8. return immediately exits the entire function
# ------------------------------------------------------------

# def check_score(score):
#     if score < 0:
#         return "Invalid"
#
#     return "Valid"
#
# Once Python reaches return, the function is finished.
# Code after that return is not executed.


# ------------------------------------------------------------
# 9. return vs break vs continue
# ------------------------------------------------------------

# continue
# → stops only the CURRENT loop iteration
# → goes to the next iteration
#
# break
# → exits the nearest loop
# → the function can continue running after the loop
#
# return
# → exits the ENTIRE function
# → may return a value to the caller


# Mental model:
#
# continue → current iteration ends
# break    → current loop ends
# return   → current function ends


# ------------------------------------------------------------
# 10. break does NOT return a value
# ------------------------------------------------------------

# def test():
#     for number in [1, 2, 3]:
#         if number == 2:
#             break
#
#     print("Function still running")
#
# break only exits the loop.
# If the function has no explicit return, it eventually returns None.


# ------------------------------------------------------------
# 11. A bare return is allowed
# ------------------------------------------------------------

# def process_score(score):
#     if score < 0:
#         return
#
#     print("Processing...")
#
# A bare:
#
# return
#
# is equivalent to:
#
# return None
#
# Its main purpose is often to END THE FUNCTION EARLY.


# This is often called an early return / guard clause.


# ------------------------------------------------------------
# 12. return is different from pass
# ------------------------------------------------------------

# pass
# → does nothing
# → execution continues to the next line
#
# return
# → immediately exits the function


# Example:
#
# def test():
#     pass
#     print("Hello")
#
# → prints Hello


# def test():
#     return
#     print("Hello")
#
# → does NOT print Hello


# ------------------------------------------------------------
# 13. Boolean functions
# ------------------------------------------------------------

# Instead of:
#
# def is_qualified(years, score):
#     if years >= 2 and score >= 75:
#         return True
#     else:
#         return False
#
# we can write:
#
# def is_qualified(years, score):
#     return years >= 2 and score >= 75
#
# because:
#
# years >= 2 and score >= 75
#
# already evaluates to True or False.


# Common Boolean-function names:
#
# is_valid(...)
# is_qualified(...)
# has_permission(...)
# needs_update(...)


# ------------------------------------------------------------
# 14. Strings support integer indexing
# ------------------------------------------------------------

# A Python string is an ordered sequence of characters.
#
# text = "python"
#
# text[0]   → "p"
# text[1]   → "y"
# text[-1]  → "n"


# ------------------------------------------------------------
# 15. Strings also support slicing
# ------------------------------------------------------------

# text = "python"
#
# text[0:3]  → "pyt"
# text[:3]   → "pyt"
# text[3:]   → "hon"
# text[-3:]  → "hon"
# text[::-1] → "nohtyp"


# ------------------------------------------------------------
# 16. Strings are immutable
# ------------------------------------------------------------

# This does NOT work:
#
# text = "python"
# text[0] = "P"
#
# → TypeError


# Instead, create a new string:
#
# text = "P" + text[1:]
#
# → "Python"


# ------------------------------------------------------------
# 17. String indexing vs dictionary key access
# ------------------------------------------------------------

# String:
#
# "Alex"[0]
#
# works because strings use INTEGER indexes.


# But:
#
# "Alex"["name"]
#
# does NOT work.


# Dictionary:
#
# candidate["name"]
#
# works because dictionaries use KEYS.


# Quick comparison:
#
# list:
# - ordered
# - integer index
# - slicing
# - mutable
#
# string:
# - ordered
# - integer index
# - slicing
# - immutable
#
# dictionary:
# - access values by key
# - mutable


# ============================================================
# Main takeaway
# ============================================================

# Functions help separate responsibilities.
#
# Instead of one large block of code doing everything:
#
# main program
#
# we can delegate work:
#
# get_experience_level(candidate)
# is_qualified(candidate)
# count_matching_skills(candidate, requirements)
#
#
# Each function should ideally do ONE clear job,
# return a useful result,
# and let other code decide how to use that result.


# ================ Exercise 1  Pass Dictionary ==================== 
print(f"\n{'=' * 20} Exercise 1 Pass dictionary {'=' * 20}")

candidate = {
    "name": "Alex",
    "years_experience": 3,
    "technical_score": 82,
}

def get_candidate_name(candidate):
    return candidate["name"]

name = get_candidate_name(candidate)
print(name)


# ================ Exercise 2 — Dictionary → classification ==================== 
print(f"\n{'=' * 20} Exercise 2 — Dictionary → classification {'=' * 20}")

def get_experience_level(candidate):
    if candidate["years_experience"] >= 5:
        return "Senior"
    elif candidate["years_experience"] >=2:
        return "Mid"
    else:
        return "Entry"



# ================ Exercise 3 — Boolean function using dictionary ==================== 
print(f"\n{'=' * 20} Exercise 3 — Boolean function using dictionary {'=' * 20}")

def is_qualified(candidate):
    return candidate["years_experience"] >= 2 and candidate["technical_score"] >= 75

if is_qualified(candidate):
    print("Pass")
else:
    print("Reject")


# ================ Exercise 4 — Pass list ==================== 
print(f"\n{'=' * 20} Exercise 4 — Pass list {'=' * 20}")

skills = ["python", "sql", "pytorch"]
requirements = ["python", "pytorch", "docker"]

def count_matching_skills(skills, requirements):
    matched_counter = 0
    for skill in requirements:
        if skill in skills:
            matched_counter += 1 
    return matched_counter

result = count_matching_skills(skills, requirements)
print(result)

# ================ Exercise 5 — Mutation experiment ==================== 
print(f"\n{'=' * 20} Exercise 5 — Mutation experiment {'=' * 20}")

def add_skill(skills):
    skills.append("docker")

skills = ["python", "sql"]

add_skill(skills)

print(skills)

# send a copy instead
skills = ["python", "sql"]

add_skill(skills.copy())

print(skills)