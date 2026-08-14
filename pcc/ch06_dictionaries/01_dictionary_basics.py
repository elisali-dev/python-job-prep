#### =========== Dictionary ===============
# ==============================================================================
#  QUICK-REFERENCE SYNTAX SUMMARY
# ==============================================================================
# Operation       | List Syntax               | Dictionary Syntax
# ----------------|---------------------------|---------------------------------
# Creation        | my_list = []              | my_dict = {}
# Add / Update    | my_list.append(val)       | my_dict[key] = val
# Value Lookup    | my_list[index_int]        | my_dict[key_object]
# Check Existence | if val in my_list:        | if key in my_dict: (Checks keys!)
# Deletion        | del my_list[index_int]    | del my_dict[key]


# ========= 1. core grammar =================
# dict = {"key1": val, } key - value pairs 
    # 核心语法规则
        # 键值对（Key-Value Pair）：一个 key，一个 :，一个 value。
        # 逗号分隔：多个键值对之间用逗号 , 隔开。
        # 大括号包裹：整个字典用大括号 {} 包裹。
        # PEP 8 规定：冒号前面不留空格，冒号后面必须留一个空格。

# dictionary[key] 取值
# dictionary is mutable 

#  key 不限于 string，只要是不可变类型（immutable）的数据都可以做 key（例如数字、元组等）。
    # 常见可以作为 key 的类型字符串 (str)：最常用的 key 类型（例如 {"name": "Alice"}）。
    # 数字 (int, float, bool)：整数、浮点数甚至布尔值都可以（例如 {1: "one", 3.14: "pi", True: "yes"}）。
    # 元组 (tuple)：如果元组内的所有元素都是不可变类型，它就能做 key（例如 {(1, 2): "coordinates"}）
    # Key 必须唯一
            #比如：
                    # candidate = {
                    #     "name": "Alex",
                    #     "score": 82,
                    #     "score": 95,
                    # }
                    # 
                    # 不会保存两个 "score"。
                    # 后面的会覆盖前面的，所以最终：
                    # candidate["score"]   # 95

# value（值）可以是任何类型（any object），没有任何限制。
    # Value 的核心特点没有任何限制：可以是数字、字符串、列表、元组、字典、集合，甚至是函数、类、模块或自定义的对象。
    # 可以是可变的：key 必须不可变，但 value 可以是随时修改的可变类型（如 list、dict）。
    # 可以重复：不同的 key 可以指向完全相同的 value。

# ========= 2. Add/modify dict[key] = value ============
# dict[key] = value
# 可能是：
        # key 不存在 → add
        # key 已存在 → modify
# dict[key] 要求 key 存在，否则 KeyError 
    # candidate = {
    #     "name": "Alex",
    # }
    # # BUG key 不存在会发生什么 
    # print(candidate["salary"])

# ========= 3. Deletion del dict[key] ===========
# del candidate["score"]

    # 和之前 list： del skills[0] 是同一个 del keyword。
    # 区别只是：
        #list → index
        # dict → key




# ================ Exercise 1 — Create and access  ===================== 
print(f"\n{'=' * 20} Exercise 1 — Create and access {'=' * 20}")

employee = {
    "name" : "Emma",
    "role" : "ML Engineer",
    "years_experience" : 4
}

# print(employee)
# Output is enclosed with {} -> {'name': 'Emma', 'role': 'ML Engineer', 'years_experience': 4}

# for key, val in employee: # BUG ValueError: too many values to unpack (expected 2)
### ??? how to for loop thru dictionary 

print(f"Name: {employee["name"]}")
print(f"Role: {employee["role"]}")
print(f"Experience: {employee["years_experience"]} years")


# ================ Exercise 2 — Add  ===================== 
print(f"\n{'=' * 20} Exercise 2 — Add {'=' * 20}")

employee = {
    "name": "Emma",
    "role": "ML Engineer",
}

employee["location"] = "Detroit"
employee["salary"] = 120000 # key 是一个 str 时,一定要加引号哦

print(employee)

#如果不加引号，写成 employee[salary] = 120000，Python 会认为 salary 是一个变量名。如果不加引号且没有定义变量：Python 会直接报错 NameError: name 'salary' is not defined。如果不加引号但定义了变量：Python 会使用该变量的值作为 key。
# salary = "monthly_pay"
# employee[salary] = 120000
# 结果字典会变成：{"monthly_pay": 120000}，而不是 {"salary": 120000}


# ================ Exercise 3 — Modify  ===================== 
print(f"\n{'=' * 20} Exercise 3 — Modify {'=' * 20}")

model = {
    "name": "resnet18",
    "accuracy": 0.82,
}

model["accuracy"] = 0.87

print(f"Model: {model["name"]}")
print(f"Accuracy: {model["accuracy"]}")



# ================ Exercise 4 — Delete  ===================== 
print(f"\n{'=' * 20} Exercise 4 — Delete {'=' * 20}")

candidate = {
    "name": "Alex",
    "age": 28,
    "temporary_note": "remove me",
}

del candidate["temporary_note"]
print (candidate)

# ================ Exercise 5 — Mixed data types  ===================== 
print(f"\n{'=' * 20} Exercise 5 — Mixed data types {'=' * 20}")

ml_candidate = {
    "name": "Brian",
    "years_experience": 5,
    "technical_score": 85,
    "available": True,
    "skills": ["python","sql","pytorch"] # mac本上 Option + 向右键（按单词向右跳跃），光标会智能地停在每个 key 的引号末尾、冒号前面。
}

print(ml_candidate["name"])
print(ml_candidate["technical_score"])
print(ml_candidate["skills"][0]) # 拿出来以后本身又是一个 list, 所以...[0]

# ================ Exercise 6 — Observe add vs modify  ===================== 
print(f"\n{'=' * 20} Exercise 6 — Observe add vs modify {'=' * 20}")

config = {
    "batch_size": 32,
    "learning_rate": 0.001,
}

config["batch_size"] = 64
config["epochs"] = 20
print(config)

# ================ Exercise 7 — Intentionally trigger KeyError  ===================== 
print(f"\n{'=' * 20} Exercise 7 — Intentionally trigger KeyError {'=' * 20}")

candidate = {
    "name": "Alex",
    "score": 90,
}

# print(candidate["email"])

# ================ Closed book drill  ===================== 
print(f"\n{'=' * 20} Closed book drill {'=' * 20}")

training_run = {
    "model_name": "transformer",
    "epochs": 10,
    "learning_rate": 0.001,
    "device": "cpu",
    #"completed" = False BUG Key Value 中间用 : 而不是 = 
    "completed": False
}

print(training_run["model_name"])
training_run["epochs"] = 20
training_run["device"] = "cuda"
training_run["accuracy"] = 0.91
del training_run["completed"] 

print(training_run)


