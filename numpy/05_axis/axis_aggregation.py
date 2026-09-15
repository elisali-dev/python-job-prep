# axis=N = 把第 N 个 dimension 聚合掉。
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

print(data)
print("shape:", data.shape)

# =========== 
# 如果不写 axis，NumPy 就把所有元素一起算

print("sum:", data.sum())
print("mean:", data.mean())
print("max:", data.max())
print("min:", data.min())

# axis=N = 把第 N 个 dimension 聚合掉。
print(data.sum())
print(data.sum(axis=0)) # axis=0 会把不同 rows 在同一个 column 上聚合, 可以把 axis=0 暂时理解成： 把 axis 0 这个维度压掉。
print(data.sum(axis=1))

print(data.mean(axis=0))
print(data.mean(axis=1))

print(data.sum(axis=0).shape)
print(data.sum(axis=1).shape)