# &   intersection   两边都有
# -   difference     A 有、B 没有
# |   union         combined unique values,  两边所有 unique values
# 
# ==== exer 1  Unique skills==========
skills = [
    "python",
    "sql",
    "python",
    "pytorch",
    "sql",
    "docker",
]

unique_skills = set(skills)

print(unique_skills)
print(len(skills))
print(len(unique_skills))

#======= Exercise 2 — Candidate skill matching
candidate_skills = {
    "python",
    "sql",
    "git",
    "pytorch",
}

required_skills = {
    "python",
    "sql",
    "pytorch",
    "docker",
    "aws",
}

matched_skills = candidate_skills & required_skills
missing_skills = required_skills - candidate_skills
# BUG all_unique_skills = set(candidate_skills)
# NOTE all unique skills 应该是合集 union 
all_unique_skills = candidate_skills | required_skills
# 或者可以写成
all_unique_skills = candidate_skills.union(required_skills)

print(f"Matches: {matched_skills}")
print(f"Missing: {missing_skills}")
# BUG 下面这样用 /  会输出一个 quotient 0.6 
# print(f"Matched count: {len(matched_skills)/len(required_skills)}")
match_rate = len(matched_skills) / len(required_skills)
print(
    f"Matched count: "
    f"{len(matched_skills)}/{len(required_skills)}"
    f"({match_rate:.0%})" # percentage 显示办法 
)

#=========== Exercise 3 — Membership ============
seen_candidate_ids = {101, 103, 108}

# set 可以用for loop 历遍,但是不能保证顺序是按照你给的顺序 loop thru
# 如果要保证先103 再检查105的话,可以用 []
checklist_ids = {103, 105}
# 最好不要用id 这个var 因为python 本身有built-in id(object)
for id in checklist_ids:
    if id in seen_candidate_ids:
        print("Candidate already processed")
    else:
        print("New Candidate")
        seen_candidate_ids.add(id)
              

#===========Exercise 4 — Tuple refresh
training_result = (
    "resnet18",
    0.923,
    12,
)

model_name, accuracy, epoch = training_result

# NOTE 如果不加\n 的话这些 f adjacent strings 会直接拼起来：
# NOTE 每个f string 不用逗号隔开,但是想要另起一行的话得加 \n 
print(f"Model:{model_name}\n"
      f"Accuracy: {accuracy}\n"
      f"Epoch: {epoch}"
      )

variable_tuple = ("cuda",)
type(variable_tuple)

# ============================================================
# Python Fundamentals Review - Set + Tuple
# ============================================================


# ============================================================
# PART 1 - SET
# ============================================================


# ------------------------------------------------------------
# 1. A set stores UNIQUE values
# ------------------------------------------------------------

skills = {"python", "sql", "python"}

# Duplicate values are removed.
#
# skills contains only:
# {"python", "sql"}
#
# NOTE:
# Set ordering is not guaranteed.
# Do NOT depend on print order.


# ------------------------------------------------------------
# 2. Set syntax
# ------------------------------------------------------------

skills = {"python", "sql", "pytorch"}

# IMPORTANT:
#
# {}        -> empty DICTIONARY
# set()     -> empty SET

empty_dict = {}
empty_set = set()


# ------------------------------------------------------------
# 3. Set has NO integer indexing
# ------------------------------------------------------------

# This does NOT work:
#
# skills[0]
#
# because a set is not an indexed sequence.


# Compare:
#
# list / tuple / string
# -> ordered sequence
# -> indexing
#
# set
# -> unique collection
# -> no indexing


# ------------------------------------------------------------
# 4. Membership test
# ------------------------------------------------------------

# "python" in skills
#
# -> True / False
#
# Set membership lookup is usually very efficient
# (average O(1)).
#
# This is one reason sets are useful in algorithms / LeetCode.


# ------------------------------------------------------------
# 5. Add values
# ------------------------------------------------------------

skills.add("docker")

# If "docker" already exists, adding it again
# does NOT create a duplicate.


# ------------------------------------------------------------
# 6. Remove values
# ------------------------------------------------------------

# remove()
# -> removes value
# -> raises KeyError if value does not exist

# skills.remove("docker")


# discard()
# -> removes value if present
# -> does NOT raise error if missing

# skills.discard("docker")


# ------------------------------------------------------------
# 7. Intersection
# ------------------------------------------------------------

candidate_skills = {"python", "sql", "pytorch"}
required_skills = {"python", "pytorch", "docker"}

matched = candidate_skills & required_skills

# Result:
# {"python", "pytorch"}
#
# & = intersection
# values existing in BOTH sets


# ------------------------------------------------------------
# 8. Difference
# ------------------------------------------------------------

missing = required_skills - candidate_skills

# Result:
# {"docker"}
#
# A - B
# -> values in A but NOT in B


# ------------------------------------------------------------
# 9. Union
# ------------------------------------------------------------

all_skills = candidate_skills | required_skills

# | = union
# -> all unique values from both sets


# ------------------------------------------------------------
# 10. Symmetric difference
# ------------------------------------------------------------

different = candidate_skills ^ required_skills

# ^ -> values appearing in one set but NOT both


# ------------------------------------------------------------
# 11. Sets are mutable
# ------------------------------------------------------------

skills = {"python", "sql"}

skills.add("docker")
skills.remove("sql")

# The same set object can be modified.


# ------------------------------------------------------------
# 12. Set elements must be hashable
# ------------------------------------------------------------

# These work:
#
# {"python", "sql"}
# {1, 2, 3}
# {(1, 2), (3, 4)}
#
#
# This does NOT:
#
# {[1, 2], [3, 4]}
#
# because lists are mutable/unhashable.


# ------------------------------------------------------------
# 13. Very common use cases
# ------------------------------------------------------------

# Sets are especially useful for:
#
# - removing duplicates
# - fast membership checks
# - finding common items
# - finding missing items
# - comparing two collections


# Example:
#
# list_with_duplicates = [
#     "python",
#     "sql",
#     "python",
# ]
#
# unique_skills = set(list_with_duplicates)


# ============================================================
# PART 2 - TUPLE QUICK REVIEW
# ============================================================


# ------------------------------------------------------------
# 14. Tuple = ordered immutable sequence
# ------------------------------------------------------------

config = ("resnet", 256, 8)

# tuple:
# - ordered
# - indexed
# - sliceable
# - immutable


# ------------------------------------------------------------
# 15. Tuple indexing
# ------------------------------------------------------------

# config[0] -> "resnet"
# config[-1] -> 8


# ------------------------------------------------------------
# 16. Tuple unpacking
# ------------------------------------------------------------

model_name, hidden_size, heads = config

# Equivalent conceptually to:
#
# model_name = config[0]
# hidden_size = config[1]
# heads = config[2]


# ------------------------------------------------------------
# 17. The comma creates a tuple
# ------------------------------------------------------------

one_item_tuple = (5,)

# NOT:
#
# (5)
#
# (5) is just the integer 5 inside parentheses.


# ------------------------------------------------------------
# 18. Tuple is immutable
# ------------------------------------------------------------

# This does NOT work:
#
# config[0] = "cnn"
#
# TypeError


# But the variable can point to a NEW tuple:
#
# config = ("cnn", 128, 4)


# ------------------------------------------------------------
# 19. Tuple appears naturally in Python
# ------------------------------------------------------------

# Function:
#
# def get_sample():
#     return image, label
#
# This really returns:
#
# (image, label)


# And:
#
# image, label = get_sample()
#
# uses tuple unpacking.


# ============================================================
# QUICK COMPARISON
# ============================================================

# list
# -> ordered
# -> indexed
# -> mutable
# -> duplicates allowed
#
# tuple
# -> ordered
# -> indexed
# -> immutable
# -> duplicates allowed
#
# set
# -> no guaranteed order
# -> no indexing
# -> mutable
# -> unique values only
#
# dict
# -> key/value mapping
# -> access by key
# -> mutable
# -> keys unique