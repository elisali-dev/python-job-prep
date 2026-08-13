# for loop
# range()
# list(range())
# sum()
# min()
# max()
# squares
# list comprehension

# ================ Notes ======================= 
# for loop - Indentation defines the body of the loop.
languages = ["python", "sql", "java"]

for language in languages:
    print(language) # Indentation defines the body of the loop.

# range(start, stop) stop 不包含在里面
range(1, 5) # return range(1,5)
print(range(1, 5)) # ! return 'range(1,5)', not a [list 1,2,3,4] 
# range(start, stop, step) 
range(2, 11, 2) # return 2, 4, 6, 8, 10
# range() 不是 list 
numbers = range(1, 5)
print(numbers) # range object
print(type(numbers)) # vs
numbers = list(range(1, 5)) # you have to cast it to a list to return [1, 2, 3, 4]
print(numbers) # list

# min() / max() / sum() 都是 function call ->  return a value
scores = [82, 95, 76, 88]

print(min(scores))
print(max(scores))
print(sum(scores))

# 用 loop 新建 list  
# 常见 pattern empty list -> loop -> calculate something -> append 
squares = []

for number in range(1, 6):
    square = number ** 2
    squares.append(square)

print(squares)

# List Comprehension - rewrite a loop  [expression for item in iterable] 
# 上面的代码可以缩写成 
squares = [number ** 2 for number in range(1,6)]
# 

# ================ Exercise 1 ===================== 
print(f"\n{'=' * 20} EXER 1 - Basic Loop {'=' * 20}")
skills = ["python", "sql", "pytorch", "git"]

for skill in skills:
    print(f"I am practicing {skill.title()}")

print("Practice Complete!")

# ================ Exercise 2 ===================== 
print(f"\n{'=' * 20} EXER 2 - Loop + arithmetic {'=' * 20}")
numbers = [2, 4, 6, 8]

for number in numbers:
    print(number ** 2)

square = [item ** 2 for item in numbers]
print (f"List comprehension method output is: {square}")


# ================ Exercise 3 range() ===================== 
print(f"\n{'=' * 20} EXER 3 - range() {'=' * 20}")

print (range(1,6)) # this would print 'range(1,6)' on the screen 

for number in range(1,6):
    print(number)

print(list(range(1,6)))

# ================ Exercise 4 step ===================== 
print(f"\n{'=' * 20} EXER 4 step - {'=' * 20}")

## Note: step can be negative. step > 0 → 往上走 ; step < 0 → 往下走
for num in range(1,6):
    print(num * 2)

print(list(range(2, 12, 2)))

print(list(range(12, 2, -2))) #This is legal, it returns 12, 10, 8, 6, 4. Note: it doesn't contain 2

####### Return None value ########
new_list = list(range(2, 12, 2)).reverse() 
print (new_list) # return None, reverse() is inplace edit

###### BUG FIX #########
new_list = list(range(2, 12, 2))
new_list.reverse()
print (new_list) # return the reversed list value while keeping original list unchanged. 


# ================ Exercise 5 list(range()) ===================== 
print(f"\n{'=' * 20} EXER 5  - {'=' * 20}")
numbers = list(range(1,11))
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# ================ Exercise 6 — Build a list with loop ===================== 
print(f"\n{'=' * 20} EXER 6 - Build a list with loop {'=' * 20}")
squares=[]

for number in range(1,11):
    # squre = number ** 2 BUG 
    # squares.append(square) # wrong var name typing but python didn't catch it, because i declare square before
    squares.append (numbers ** 2) # 可以不需要 intermediate variable 避免出错

print(squares)

# ================ Exercise 7 — List Comprehension ===================== 
print(f"\n{'=' * 20} EXER 7  - List Comprehension  {'=' * 20}")
squares = [number **  2 for number in range(1,11)]

# 忘记print 
print (squares) # 创建 / assign 一个 variable 不会自动显示结果。Script 中要显示，通常要 print()。

# ================ Exercise 8 — MLE flavored ===================== 
print(f"\n{'=' * 20} EXER 8  - Print Loss Value  {'=' * 20}")

losses = [0.82, 0.61, 0.43, 0.31]

for l in losses:    
    print(f"Epoch loss: {l}")

print(f"Best loss: {min(losses)}")


# ================ Exercise 9 Loop doesn't change list values ===================== 
print(f"\n{'=' * 20} EXER 9  - Print Original List after Loop  {'=' * 20}")
numbers = [1, 2, 3]

for number in numbers:
    number = number * 10

print(numbers)

