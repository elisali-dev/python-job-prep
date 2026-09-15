import numpy as np

scores = np.array([70, 80, 90, 100])

# 每一个运算都是 element wise operation, 普通 python list 只能通过 for loop 实现
print(scores + 5)
print(scores * 2) # 如果是普通 python list ,结果是 list 重复两次 [70, 80, 90, 100, 70, 80, 90, 100]
print(scores / 10)
print(scores ** 2)

# 两个array 之间也可以逐元素计算 
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a * b) # element wise multiplication 而 a @ b 才是 matrix multiplication


##### A * B VS A @ B 
A = np.array([
    [1, 2],
    [3, 4],
])

B = np.array([
    [10, 20],
    [30, 40],
])

print("A + B:")
print(A + B)

print("\nA * B:")
print(A * B)

print("\nA @ B:")
print(A @ B)  # 例如一个 Linear Layer 本质上经常可以抽象成：output = X @ W + b