import numpy as np

data = np.array(
  [10, 20, 30, 40, 50, 60]
) # np.array() 函数的第一个参数必须是完整的数据对象（比如一个嵌套列表）所以总是([列表,或者嵌套列表]) 方括号不能省

print("Original:")
print(data)
print("Shape:", data.shape)

#======================================================
#Reshape
reshaped= data.reshape(2,3)

print("\nreshaped:", reshaped)
print("shape:", reshaped.shape)

print(data.reshape(3, 2))
print(data.reshape(2, -1))
print(data.reshape(-1, 2))
# reshape(-1) 把所有  element 压缩到一维
# reshape(batch_size, -1) = 保留每个 sample，压平每个 sample 内部的 feature dimensions。第一维别碰，剩下的全部合并. 

#==========================================
#flatten()
matrix = np.array([
        [10,20,30],
        [40, 50, 60],
    ])

print(matrix.shape)

flattened = matrix.flatten()

print(flattened)
print(flattened.shape)
print(flattened.ndim)

print(matrix.reshape(-1))

# NOTE TIPS 
# 手动打 [[[]]] 去对齐维度和 Shape 非常痛苦且容易出错。在实际写代码时，极少会通过纯手动打括号来创建高维数组。
# 1. 先用一维列表（只需一层括号），再用 .reshape(行数, 列数)
arr = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)

# 2. 或者用 np.arange 自动生成序列，直接变形（全程不需要手动打一堆括号）
arr_auto = np.arange(1, 7).reshape(2, 3)

#=================================================
# Transpose .T
print("\nTranspose Example")

# transpose 的核心不是“把数据改了”，而是 交换 axis 的顺序。

# for 1D array, 
x = np.array([1,2,3])
print("Original x:",x)
print(x.shape) #(3,)
print(x.T.shape) #(3,) Transpose does not affect 1D array shape 

# NOTE 如果 1D array 想要 row 变成 column vector 要先变成 2D 
x_col = x.reshape(3,1)
print("Reshape to Column Vector:")
print(x_col)
print(x_col.shape)

# for 2D array, row <-> column 
matrix = np.array([
        [1,2,3],
        [4,5,6],
])
print("\nOriginal:")
print(matrix)
print("Shape:",matrix.shape)

print("\nTransposed")
transposed = matrix.T 
print(transposed)
print("Shape:", transposed.shape)

# 3D Array Transpose 
data = np.arange(1,25).reshape(2,3,4)
# data = np.zeros(2,3,4)
print("\n\n3D array Transpose")
print("Original:")
print(data)
# data.shape (2,3,4) ->oringal axis order (0,1,2) axis 0 = 2; axis 1 = 3, axis 2 = 4 

new_data = data.transpose(1, 0, 2) # 新的 axis 顺序改成原来的 axis 1, axis 0, axis 2

# Reshape 改 shape，但基本按照原来的元素顺序重新分组
# transpose：明确重新排列 axis。