import numpy as np

##### ============= vector @ vector ============
# 两个 1D vectors 的 dot product

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("a * b:", a * b)
print("a @ b:", a @ b) # NumPy专门定义：两个 1D vectors 用 @ → inner/dot product。
print("np.dot(a, b):", np.dot(a, b))
result = a @ b 
print("a @ b result shape:", result.shape) # scalar value 140 , NOTE no shape 



# NumPy 的 1D array (3,) 既不是数学上的 1×3 row vector，也不是 3×1 column vector。
# b 的 shape 不是 (1, 3)，而是：(3,) 它只有一个 axis，NumPy 没有给它“横”或者“竖”的方向。 数学上的 dot product 其实和 NumPy 是一致的。
# 数学上的 dot product 本身并不要求你先把 vector 想成 row/column；但如果用矩阵乘法来表示，就需要 transpose。

## 转置后用矩阵乘法 #### 
# BUG b_col = b.T 一维矩阵 transpose 之后还是它自己
# print("\n\n b transpose:")
# print(b.T) 
# print(b_col.shape) # (3,)
# print( "a * b.T:", a @ b_col) 140 

print("Reshape b to column matrix")
b_col = b.reshape(3,1)
print(b_col)
print("b_col shape:", b_col.shape)
print("a @ b_col", a @ b_col)
print((a @ b_col).shape) # return [140], NOTE shape (1,)

print("Reshape a to row matrix")
a_row = a.reshape(1,3)
print(a_row)
print("a_row shape: ",a_row.shape)
print("a_row @ b_col:")
print(a_row @ b_col)
print((a_row @ b_col).shape) # return [[140]] (1, 1) NOTE 结果是 一个 2D (1,1) matrix



# (3,)      1D vector，没有 row/column orientation
# 
# (1,3)     2D row matrix
# 
# (3,1)     2D column matrix


### ============ Matrix @ Vector ================
# matrix 的每一行分别跟 vector 做 dot product 
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

x = np.array([10, 20, 30])

print(A @ x)
print((A @ x).shape) # (2,)

### ============ Vector @ Matrix ==============
# matrix 的每一列分别跟 vector 做 dot product 

x = np.array([1, 2])

B = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print(x @ B)
print((x @ B).shape) # (3,)