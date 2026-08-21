# names = ["alice", "bob", "charlie"]
# 
# key Summary
# 
# names[0]       # first item
# names[-1]      # last item
# 
# names[0] = "anna"      # modify
# 
# names.append("david")  # add to end
# names.insert(1, "ben") # insert at index
# 
# del names[0]           # delete by position
# names.pop()            # remove + return last item
# names.pop(1)           # remove + return item at index
# names.remove("bob")    # remove by value, the first occurence of the value.
# 
# 最重要的区别先记：
# 
# del       → 删除，不需要这个 value
# pop()     → 删除，并且把删除的 value 返回给你
# remove()  → 根据 value 删除
# 
# 还有一个非常重要的 concept：
# 
# list is mutable, 和 str 不一样 names.append("david") 会直接修改原来的 names list。


# Exercise 1 — Access list items
print(f"\n{'=' * 20} EXER 1 {'=' * 20}")

languages = ["python", "java", "sql", "javascript"]

#NOTE Python 列表最后一个值后面可以有逗号，也可以没有。这被称为尾随逗号（trailing comma）。Python 语法允许这样做，并且解释器会自动忽略它。

print(languages[0])
print(languages[-1]) # last item using negative index 
print(languages[2].upper())

# Exercise 2 — Modify
print(f"\n{'=' * 20} EXER 2 {'=' * 20}")
skills = ["python", "excel", "java"]

skills[1] = "pytorch"
print(skills)


# Exercise 3 — append / insert
print(f"\n{'=' * 20} EXER 3 {'=' * 20}")

tools = ["python", "git"]
tools.insert(1, "vscode") # comma 后面留一个空格
tools.append("github") # 真正“加到末尾”应该用 append()
# tools.insert(-1,"github") 得到：["python", "github", "git"]
# 因为 -1 指的是最后一个元素 "git" 的位置，而 insert() 是：在该 index 前面插入。

#Exercise 4 — del / pop / remove
print(f"\n{'=' * 20} EXER 4 {'=' * 20}")

skills = ["python", "java", "excel", "sql", "pytorch"]

del skills[1] ##  del is a keyword in the statement, NOT built-in function!  because it doesn not have () around skills[1], not like print(), len()

# list.remove() method only removes the first matching element from a list. It modifies the list in place and does not return a new list. 
# To remove all occurences of a value, you can choose a loop or list comprehension
skills.remove("excel") ## dot method access 不留空格 obj.method(); binary operators 两边有空格 a + b


removed_skill = skills.pop() 
print (f"Current skills: {skills}\nRemoved skill: {removed_skill}")

# Exercise 5 — 理解 pop()
print(f"\n{'=' * 20} EXER 5 {'=' * 20}") 

tasks = ["clean data", "train model", "deploy model"]
completed_task = tasks.pop(0)
print (f"Completed: {completed_task}\nRemaining: {tasks}")

# Exercise 6 — Mutability
print(f"\n{'=' * 20} EXER 6 {'=' * 20}") 
numbers = [1, 2, 3] 
#Python 不要求 list elements 是同一个 type。但是实际 programming / data work 中，我们通常希望一个 list 里的数据有比较一致的含义
# 这和以后 NumPy / PyTorch 很不一样。比如 tensor 通常要求里面元素有统一的 dtype。

print(id(numbers))

numbers.append(4)

print(numbers)
print(id(numbers)) # 两次 id 通常相同，因为： append() 是 in-place mutation： 同一个 list object 内部内容发生变化

# Exercise 7 - Shallow copy and Reference Assignment 
list_a = [1, 2, 3]
# aliasing, reference assignment - two ids are still the same
list_b = list_a 

# shallow/ simple copy - list_b and list_a has different id, list_b is a brand new copy, further operations do not affect list_a
# list_b = list_a.copy()

list_b.append(4)

print(list_a)
print(list_b)

print(id(list_a))
print(id(list_b))