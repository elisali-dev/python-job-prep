import numpy as np


scores = np.array([70, 80, 90])
result = scores + 5
print(result)

# 2D Broadcasting
# broadcasting 最核心的规则：从右往左比较 dimensions。 
# 两个 dimension 可以兼容，如果：
# 1. 它们相等
#  或者
# 2. 其中一个是 1
#==========================
# broadcasting 不是新的矩阵加法规则；它是 NumPy 先把较小的 array 按规则扩展到兼容 shape，然后做 element-wise operation。
# NumPy array 运算 ≠ 全部都是传统矩阵运算。有些是线性代数，有些是 element-wise numerical computing。
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

bonus = np.array([1, 2, 3])

print("\n\ndata shape:", data.shape) # shape(2,3)
print("bonus shape:", bonus.shape)

print(data + bonus)

#============= 
row_bonus = np.array([1, 2, 3]) # shape(3,)
column_bonus = np.array([
    [1],
    [2],
]) # shape(2,1)

print(data + row_bonus) # [[11,22,33],[41,52,63]]
print(data + column_bonus) # [[11,21,31],[42,52,62]]

# 最经典的 broadcasting 例子： (2, 1) + (1, 3)
a = np.array([
    [10],
    [20],
])

b = np.array([
    [1, 2, 3],
])

print("a shape:", a.shape) # (2,1) -> row 1 - 10,10,10 row 2 - 20, 20, 20 
print("b shape:", b.shape) # (1,3) -> row 1 - 1, 2, 3  row 2 -  1, 2, 3 

print(a + b) # [[11,12,13][21,22,23] ] 