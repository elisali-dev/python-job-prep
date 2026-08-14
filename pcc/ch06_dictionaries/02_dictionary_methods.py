# ==============================================================================
#  STRUCTURAL & CONCEPTUAL DIFFERENCES
# ==============================================================================
# Feature        | list (List)                       | dict (Dictionary)
# ---------------|-----------------------------------|----------------------------------
# Structure      | Ordered sequence of values        | Mapping of Key-Value pairs
# Syntax         | square_brackets = [v1, v2, v3]     | curly_braces = {k1: v1, k2: v2}
# Access Method  | Numerical index: list[0]          | Unique hashable key: dict["key"]
# Duplicates     | Allows duplicate values            | Values can duplicate; KEYS MUST BE UNIQUE
# Look-up Speed  | O(n) - Slow for large datasets    | O(1) average - Extremely fast (Hash Table)
# Use Case       | Ordered elements, simple sequences | Labeled data, fast lookups, profiles





#============ 1. .get(key,"Not Provided") ============
    # 安全读取 key, 给 key 值, 找 value 值, 如果没有, 返回 default 值 , here is "Not Provided"

#============ 2.Loop dictionary 默认拿 key  ============  
employee = {
    "name": "Emma",
    "role": "ML Engineer",
    "location": "Detroit",
}
for key in employee:
# 等价于 for key in employee.keys():
    print(key)

# OUTPUT is 
    # name
    # role
    # location

#============ 3. values() 拿 values ============ 

scores = {
    "Alex": 90,
    "Emma": 95,
    "Sam": 82,
}

for score in scores.values():
    print(score)

print(scores.values()) # dict_values([90, 95, 82])
## scores.values() 返回的不是一个真正的 list（列表），而是一个 dict_values 视图对象（View Object）
## 这个视图对象是与原字典动态绑定的。如果字典里的数据变了，视图对象里的数据也会自动同步改变，而不需要重新获取。节省内存：它不会在内存中创建一份新的列表拷贝，因此比直接返回列表更省内存。
## 虽然它不是列表，但它是一个可迭代对象（Iterable）。Python 的 for 循环只需要对象是可迭代的就能正常工作，所以你完全可以像遍历列表一样去遍历它。
## 可以用 list() 例如 scores_list = list(scores.values()) 强制对它进行类别转换成 list type 
## 同理，字典的 scores.keys() 返回的是 dict_keys，scores.items() 返回的是 dict_items，它们都是类似的视图对象。


#============ 4. items() key, values一起拿 ============ 
for key, value in employee.items():
    print(key, value)

## ?? .items() 返回的是 dict_items  然后能再["keys"] 这样去 index 吗?
## No, you cannot index dict_items using ["keys"] or integers.
    # If you try to run scores.items()["keys"], Python will raise a TypeError: 'dict_items' object is not subscriptable.
    # Why this fails:  dict_items is a view object: It behaves like a set, not a dictionary or a list.
    # It lacks an index structure: It does not map string keys (like "keys") to values, nor does it support integer positioning (like [0]).
    # How to get keys and values from .items() : The standard and most efficient way to access the keys and values from .items() is through loop unpacking
    # If you really need direct indexing. Convert to a list for positional index ([0])
        #   items_list = list(scores.items())
        #   print(items_list[0])  # Output: ('Alex', 90)

#============ 5. in 对 dictionary 默认检查 key ============ 
candidate = {
    "name": "Alex",
    "score": 90,
}
"name" in candidate      # True
"Alex" in candidate      # False

# 如果想查 values：
"Alex" in candidate.values() # True

# ================ Exercise 1 get()  ===================== 
print(f"\n{'=' * 20} Exercise 1 — get() {'=' * 20}")

candidate = {
    "name": "Alex",
    "score": 90,
}
print(candidate["name"])
print(candidate.get("name"))
print(candidate.get("email"))
print(candidate.get("email", "Not provided"))

# ================ Exercise 2 — loop over keys  ===================== 
print(f"\n{'=' * 20} Exercise 2 — loop over keys {'=' * 20}")
model_config = {
    "model": "transformer",
    "epochs": 20,
    "batch_size": 32,
    "device": "cuda",
}

for key in model_config:
    print(key)

for key in model_config.keys():
    print(key)

# ================ Exercise 3 — .items()  ===================== 
print(f"\n{'=' * 20} Exercise 3 — .items() {'=' * 20}")

for key, value in model_config.items():
    print (f"{key}: {value}") # ? 这样写是不是有点啰嗦


# ================ Exercise 4 — .values()  ===================== 
print(f"\n{'=' * 20} Exercise 4 — .values() {'=' * 20}")
scores = {
    "Alex": 88,
    "Emma": 95,
    "Sam": 79,
    "John": 91,
}
score_list = list(scores.values())
# → max/min/sum/for 都可以直接使用 不 convert 成 list 也可以
print(score_list)
print(max(score_list))
print(min(score_list))
print(sum(score_list))

# ================ Exercise 5 — membership  ===================== 
print(f"\n{'=' * 20} Exercise 5 - membership {'=' * 20}")

candidate = {
    "name": "Alex",
    "role": "ML Engineer",
    "location": "Detroit",
}
# BUG 不需要fstring 
print(f"{"name" in candidate}") 
# "name" in candidate 本身已经产生 Boolean：True
# 直接：
print("name" in candidate)
# print(expression) 完全可以直接 print expression 的 result。
# f-string 是你想加 text 时使用：
# print(f"Is name a key? {'name' in candidate}")

print(f"{"salary" in candidate}")
print(f"{"Alex" in candidate}")
print(f"{"Alex" in candidate.values()}")
print(f"{"Chicago" in candidate.values()}")



# ================ Exercise 6 — missing fields  ===================== 
print(f"\n{'=' * 20} Exercise 6 — missing fields {'=' * 20}")

candidate = {
    "name": "Emma",
    "skills": ["python", "sql"],
}
# Dictionary keys 是 case-sensitive，而且必须 exact match。
print(f"Name: {candidate["name"]}")
print(f"Location: {candidate.get("Location", "Unknown")}") # better change to "location"
print(f"Years experience: {candidate.get("Years experience", "Not provided")}")

# ================ Exercise 7 — if + dictionary ===================== 
print(f"\n{'=' * 20} Exercise 7 — dictionary + if {'=' * 20}")

candidate = {
    "name": "Alex",
    "score": 85,
    "skills": ["python", "sql", "pytorch"],
}
if "score" in candidate:
    print("Score available")
# BUG elif "email" not in candidate: # 不应该用elif 因为是分别检查两个条件
if "email" not in candidate:
    print ("Email missing")

    