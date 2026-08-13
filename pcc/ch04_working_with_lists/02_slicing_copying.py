### =================  1. Slicing: items[start:stop] ===========
#和 range() 一样：start included, stop excluded
skills = ["python", "sql", "git", "pytorch", "docker"]  
# print(skills[1:4]) -> ["sql", "git", "pytorch"]
#常见写法：
skills[:3]     # first 3
skills[2:]     # index 2 → end
skills[-2:]    # last 2
skills[:]      # entire list

### =================  2. Slice creates a new list ==============
skills = ["python", "sql", "git"]
new_skills = skills[:]

# 这里： 
# skills       → one list
# new_skills   → another list

# 所以下面的结果通常不同

print(id(skills))
print(id(new_skills))


### =================  3. Assignment is NOT copy ==============
a = [1, 2, 3]
b = a
# # 这不是 copy。 而是： 
# a ──┐
#     ├──► [1, 2, 3]
# b ──┘
# 所以：
b.append(4)
print(a) 
# a 也会变。

### =================  4. Copy ==============
##两种 shallow copy：
b = a[:]
# 或者：
b = a.copy()
# 它们都是 shallow copy , 对于普通一层 list，现在可以认为效果一样。它们都会在内存中创建一个全新的列表对象。因此，a 和 b 的 id 是完全不同的。
# 深层思考: 虽然 a 和 b 本身的 id 不同（它们是两个不同的外壳盒子），但是它们内部所包含的元素的 id 是相同的。
# 检查列表里第一个元素（数字 1）的 id
print(id(a[0]))  # 输出类似: 140411325043120
print(id(b[0]))  # 输出类似: 140411325043120 (完全相同！)

## shallow copy in Trouble  
# 原始数据：包含一个字符串和一个列表
student_a = ["Alex", ["Math", "Science"]] 
student_b = student_a.copy()
# 1. 修改外壳元素（没问题）
student_b[0] = "Bob"  # because str immutable, changing it to Bob create a new string,  this = means reassign
# 2. 修改嵌套的子列表（出问题了！）
student_b[1].append("Art") # this is in-place mutable
print(student_a)  # 输出: ['Alex', ['Math', 'Science', 'Art']] 💥 跟着变了！
print(student_b)  # 输出: ['Bob', ['Math', 'Science', 'Art']]

student_b[1] = ["History", "Music"] # 注意：这里用的是等号赋值，而不是 .append() student_a 不会跟着变

## DEEP COPY ##
import copy
student_a = ["Alex", ["Math", "Science"]]
student_b = copy.deepcopy(student_a)

# 修改 student_b 内部嵌套的列表
student_b[1].append("Art")
print(student_a)  # 输出: ['Alex', ['Math', 'Science']]      ✅ 完好无损！
print(student_b)  # 输出: ['Alex', ['Math', 'Science', 'Art']] ✅ 独立修改！




# ================ Exercise 1 ===================== 
print(f"\n{'=' * 20} EXER 1 - Basic Slicing {'=' * 20}")

models = [
    "linear regression",
    "random forest",
    "cnn",
    "transformer",
    "xgboost"
]

print(f"First two: {models[:2]}")
print(f"Middle two: {models[1:3]}") 
# 如果是“一个任意长度 list，动态找中间元素”，以后才需要算：middle = len(models) // 2
print(f"Last two: {models[-2:]}")

# ================ Exercise 2 ===================== 
print(f"\n{'=' * 20} EXER 2 - Loop over Slice {'=' * 20}")
languages = ["python", "java", "sql", "javascript", "c++"]

for i in languages[:3]:
    print(i.title()) # 只有一个 expression 时没必要用 f-string
    # print(f"{i.title()}") 
    # BUG print(f"i.title()"") # fstring 里 忘记加 {} var evaluation 符号 # "i.title()"→ literal text

# ================ Exercise 3 ===================== 
print(f"\n{'=' * 20} EXER 3 — alias vs copy {'=' * 20}")

original = ["python", "sql", "git"]

alias = original
copied = original[:]

alias.append("docker") # original changed
copied.append("pytorch") # original doesn't changed

print(original)
print(alias)
print(copied)

print(id(original))
print(id(alias)) # same
print(id(copied)) # different 

# ================ Exercise 4 ===================== 
print(f"\n{'=' * 20} EXER 4 — .copy() {'=' * 20}")

training_data = [100, 200, 300]
validation_data = training_data.copy()

validation_data.append(400) # training_data not chagned

print(id(validation_data))
print(id(training_data))

print(f"Training: {training_data}")
print(f"Validation: {validation_data}")
