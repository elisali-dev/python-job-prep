import numpy as np

# Step1 - build feature matrix 
# columns:
# 0 = years_experience
# 1 = technical_score
# 2 = interview_score 

X = np.array([
    [5, 90, 85],
    [2, 75, 80],
    [7, 88, 92],
    [1, 65, 70],
    [4, 82, 78],
])

print(X)
print("Shape of X: ", X.shape) # (5,3)
print("Dimensions: ", X.ndim) #2
print("Dtype: ", X.dtype) # int64

## 4. Get all technical scores NOTE 
print("\nTechnical scores:\n",X[:,1:2]) # return 2D array 
print("\nTechnical scores:\n",X[:,1]) # return 1D NumPy array

# Get the first 3 candidates 
print("The First Three candidates:\n", X[0:3,:]) # first three 写法一 X[0:3, :],写法二 X[:3, :], 写法三 X[:3]

# # 6. Get technical_score + interview_score
#    for ALL candidates
scores_only = X[:,1:3]
print(scores_only)

# Step 2 - Boolean Masking Review

#创建条件 technical >= 80
technical_mask = X[:,1] >= 80  # You only create mask at this step 

# interview >= 80
interview_mask = X[:,2] >= 80

# both conditions
qualified_mask = technical_mask & interview_mask

# 进行筛选 filter X
qualified_candidates = X[qualified_mask] # NOTE use square brackets [] to filter 

print("Technical mask:", technical_mask)
print("Interview mask:", interview_mask)
print("Qualified mask:", qualified_mask)

print("\nQualified candidates:")
print(qualified_candidates)

print("Shape:", qualified_candidates.shape)


# Step 3: Axis + Aggregation - axis=N = 把第 N 个 dimension 聚合掉。
# scores_only = X[:, 1:3]

# 算 每个 candidate 的平均分。
print("\n average score of every candidate:")
print(scores_only.mean(axis=1))

# 算 technical 和 interview 两列各自的平均分：
print("\n average technical score and average interview score across all candidates:")
print(scores_only.mean(axis=0))

# Step 4 — Matrix Multiplication + Broadcasting
features = scores_only
print(features.shape) # (5, 2)

weights = np.array([
    [0.6],
    [0.4],
])
print(weights.shape)

print("features shape:", features.shape)
print("weights shape:", weights.shape)

weighted_scores = features @ weights

print("weighted scores:")
print(weighted_scores)
print("shape:", weighted_scores.shape)

final_scores = weighted_scores + 5

print("final scores:")
print(final_scores)


# compare 1D weights 
weights_1d = np.array([0.6, 0.4])

print("weights_1d shape:", weights_1d.shape)

weighted_scores_1d = features @ weights_1d
# @ 不遵循 broadcasting 机制, 它尊守的是 线性代数核心规则（内侧维度消去） + 自动降维
"""
NumPy 官方对 np.matmul 处理一维数组的定义非常明确：如果第二个参数是一维数组，它会通过在其形状前隐式添加 1 来临时提升为矩阵（即 (2,) 变成 (2, 1)）。
矩阵乘法执行后，得到 (5, 1)。关键的一步： 运算结束后，NumPy 会自动自动移除（Squeeze） 那个临时添加的维度。
"""
print("weighted_scores_1d: ")
print(weighted_scores_1d)


# (5,)   ≠   (5,1) 数字数量相同，但结构不同。
# 在 ML 里，两种都可能出现，所以以后看到：prediction.shape
# 一定要认真看它到底是(batch,) 还是：(batch, 1)

#Step 5 - Reshape + transpose + shape thinking 
reshaped = features.reshape(1, 10)
print("\nReshaped:")
print(reshaped)
print("shape:", reshaped.shape) # note ndim still = 2 
print("ndim:",reshaped.ndim)

column_form = features.reshape(10,1)
print(column_form)
print(column_form.shape)


features_T = features.T

print("original shape:", features.shape)
print("transposed shape:", features_T.shape)
print(features_T)

print(features.shape) # (5,2)
print(features.T.shape) #(2,5)
print(features.reshape(-1).shape) # (10,)
print(features.reshape(5, -1).shape) #(5,2)  
print(features.reshape(-1, 5).shape) #(2,5)

flat = features.flatten() # flatten everything into 1D

print(flat)
print(flat.shape)