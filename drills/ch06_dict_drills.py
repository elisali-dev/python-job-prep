
training_run = {
    "model": "transformer",
    "epochs": 20,
    "device": "cuda",
    "accuracy": 0.91,
}

print(training_run.get("model","Not recorded"))
print(training_run.get("loss","Not recorded"))

for key, value in training_run.items():
    # BUG key, value 不一定是 string 所以下面的不对 
    # print(key + " : " +value)
    print(f"{key} -> {value}")
    
# BUG if 后边不需要括号
# BUG 逻辑上把两个要求写成了一个
# if ("accuracy" in training_run):
#    print(training_run["accuracy"] == 0.91)
# BUG 题目想练的是 membership, 是看 key 和 value 是不是分别在这个 dict 里面
print("accuracy" in training_run)
print(0.91 in training_run.values())

# ============ Lesson Learned ========== # 
# 1. expression 不等于 output
#    → 想看到结果要 print()
# 
# 2. dictionary value 可以是不同 type
#    → 不要假设 value 都是 str
# 
# 3. in dict            → check keys
#    in dict.values()   → check values

