######  ============== Knowledge Notes ===================### 
### 1. Tuple 是什么
    #Tuple 和 list 很像，但用 () 比如 dimensions = (200, 50) 而 list 是：dimensions = [200, 50]
    # 核心区别：list is mutable , tuple is immutable
                #也就是 tuple 创建以后，里面的 element 不能直接改。

### 2. Access 和 list 一样
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[-1])

for dimension in dimensions:
    print(dimension)

### 3. Tuple 不能修改 element
dimensions = (200, 50)
# dimensions[0] = 250 # TypeError 因为 tuple immutable。
# TypeError: 'tuple' object does not support item assignment

### 4. 但是 variable 可以重新指向一个新 tuple 这完全合法：
dimensions = (200, 50)
dimensions = (250, 100)
# 不是修改旧 tuple。
# 而是： dimensions → old tuple 
#  然后重新 assignment  dimensions → new tuple


### 5. Tuple unpacking
point = (10, 20)
x, y = point

x == 10
y == 20

### unpacking in Python 
x, y, z = 1, 2, 3
# Unpacking is a Python feature that allows you to split an iterable (like a list, tuple, string, or dictionary) into multiple separate variables in a single line of code.
# You can unpack any iterable object in Python.
    # Lists: x, y = [10, 20]
    # Tuples: x, y = (10, 20)
    # Strings: x, y, z = "ABC" (Assigns 'A' to x, 'B' to y, 'C' to z)
    # Sets: x, y = {10, 20} (Be careful: sets are unordered, so assignment order is unpredictable)
    # Dictionaries: x, y = {"a": 1, "b": 2} (Unpacks the keys 'a' and 'b')

### 6. 一个 element 的 tuple
value = (5) # 这不是 tuple，是 int。

# 真正 one-element tuple：
value = (5,)  # 关键是 comma。

# ================ Exercise 1 — basic tuple ===================== 
print(f"\n{'=' * 20} Exercise 1 — basic tuple {'=' * 20}")

dimensions = (1920, 1080)
print(f"Width: {dimensions[0]}\nHeight: {dimensions[1]}")

# ================ Exercise 2 - Immutability ===================== 
print(f"\n{'=' * 20} Exercise 2 {'=' * 20}")
dimensions = (1920, 1080)
# dimensions[0] = 2560 # TypeError 因为 tuple immutable。


# ================ Exercise 3 - reassign tuple ===================== 
print(f"\n{'=' * 20} Exercise 3 {'=' * 20}")

model_input_shape = (224, 224)
print (model_input_shape)
print (id(model_input_shape))

model_input_shape = (256, 256) # reassign is ok
print (model_input_shape) 
print (id(model_input_shape)) # id changed although the same variable name

# ================ Exercise 4 - unpacking ===================== 
print(f"\n{'=' * 20} Exercise 4 {'=' * 20}")
image_size = (128, 256)
height, width = image_size
print(f"Height: {height}")
print(f"Width: {width}")

# ================ Exercise 5 - one-element tuple ===================== 
print(f"\n{'=' * 20} Exercise 5 {'=' * 20}")

a = (5)
b = (5,) # Tuple 的关键其实是 comma，不是 parentheses。

print(type(a))
print(type(b))