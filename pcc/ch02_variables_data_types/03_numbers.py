
# operations 
#   # addition +
    # subtraction -
    # multiplication * 
    # division，结果通常是 float  /
    # floor division  //
    # remainder / modulo  %
    # exponent  **



# Exer 1 - Basic Arithmetic
print(f"\n{'='*10} EXERCISE 1 {'='*10}\n") 
# String multiplication can create repeated characters.
# "=" * 10 produces "=========="
# new python does NOT require single quote inside double quote anymore
# You can use Double Quotes INSIDE double quotes now! but still good to keep what I have for readability 
a = 10 
b = 3 
print(type(a))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# use string multiplication to create a clean divider line. output 40 dashes
print("-" * 40) 

# Exercise 2 — Price calculation
print(f"\n{'='*10} EXERCISE 2 {'='*10}\n") 
price = 19.99
quantity = 3
total = price * quantity
print(f"Total price: ${total}")

print("-" * 40) 

# Exercise 3 — Monthly salary
print(f"\n{'='*10} EXERCISE 3 {'='*10}\n") 
annual_salary = 125000
monthly_salary = annual_salary / 12 

print (f"Annual salary: ${annual_salary}")
print(f"Monthly salary: ${monthly_salary}")

print("-" * 40) 

# Exercise 4 — Remainder
print(f"\n{'='*10} EXERCISE 4 {'='*10}\n") 
total_students = 23
group_size = 5

print(f"Full groups: {total_students // group_size}")
print(f"Students left: {total_students % group_size}") # operator around one space for readability

print("-" * 40) 

# Exercise 5 — Even or odd
print(f"\n{'='*10} EXERCISE 5 {'='*10}\n") 
number = 17
print(f"{number % 2}")
# better just write print(number % 2) 
# 这里只有一个 expression，不需要 f-strin : f-string 是为了把 value 插入其他文字，不是每次 print variable 都需要。
number = 20
print(f"{number % 2}")

print("-" * 40) 

# Exercise 6 — Exponent
# 计算 2^10 , note Python 里面的exponent 符号是 ** 不是 ^
print(f"\n{'='*10} EXERCISE 6 {'='*10}\n")  
print(2 ** 10)
# function 后不要空格：print 和 (, 还有 (和 第一个 character 之间不要空格
# binary operator 两边空格：不要写成 2**10 虽然结果也对

# Exercise 7 — Multiple assignment + underscores
print(f"\n{'='*10} EXERCISE 7 {'='*10}\n")  
population = 8_000_000_000
x, y, z = 10, 20, 30 
print(population)
print(x + y + z)

# Closed - Book Drill 
print(f"\n{'='*10} Drill {'='*10}\n")  
#假设一家 MLE consultant：
hourly_rate = 125
hours_per_week = 40
weeks_per_year = 48

weekly_income = hourly_rate * hours_per_week
annual_income = weekly_income * weeks_per_year

#输出：
print(f"Weekly income: ${weekly_income}")
print(f"Annual income: ${annual_income}")
print(f"Average monthly income: ${annual_income / 12:.1f}")
# print(f"Average monthly income: ${annual_income/12}.1f") 这里.1f 被看成普通字符串, 
# 输出是 Average monthly income: $20000.0.1f
# 冒号: 前面不用留空格, money formatting 的话还可以加上逗号 :,.2f thousands comma + 2 decimal places 
#然后再计算： 如果每个月存收入的 20%，一年能存多少钱？
savings = annual_income * 0.2
print (f"you can save {savings} per year")

# Exercise - Float Formating 
print(f"\n{'='*10} Printing Float {'='*10}\n")  
# Floats may have small rounding errors because
# many decimal fractions cannot be represented exactly in binary.
#Python 的 float：是一个数的二进制近似值，不是所有十进制小数的精确值。

print(0.1 + 0.2) # output is 0.30000000000000004
# 比方说十进制里面 1/3 = 0.3333333....没办法用一个有限位十进制表示 1/3
# 同样在二进制(binary)里, 0.1 也是类似无限循环的数字，只不过循环发生在二进制小数里。 


result = 0.1 + 0.2
print(f"{result:.1f}") 

0.1 + 0.2 == 0.3 # return false 

### Data types in Python.
# Python variables do not have declared types.
# A variable is a name bound to an object.
# The object has a type.
# print (type(var)) to check its type
# print (id(var)) to check this object's identity including its memory address 

# Immutable Types: int, float, complex, str, tuple, frozenset, bytes 
# Mutable Types: list, dict, set, bytearray 