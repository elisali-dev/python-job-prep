import numpy as np

scores = np.array([85, 90, 78, 92, 88])

print(scores)

# indexing
print(scores[0]) # 85
print(scores[2]) #78
print(scores[-1]) # 88

# slicing [start: stop) 
print(scores[1:4]) # [90 78 92] NumPy 打印 array 时通常没有逗号, while Python might 
print(scores[:3]) # 85, 90, 78
print(scores[2:]) # 78, 92, 88

# NOTE ML important 
# 2D Indexing
# 2D array Slicing

data = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ]
)
print("\n2D array:", data)

print(data[0, 0])
print(data[1,2])
# Numpy 2D array index is written as      ----  data[row, column]
# Python nested list indexing is written as --  data[1][2]

# Slicing - but return 1 D array 
print("first row:", data[0,:]) # means row = 0, all column, 1st sample 
# NOTE shape(3,) 1D
# OUTPUT [10 40 70]
print("first column:", data[:,0]) # first feature of all rows 
# 取所有 samples 的 feature 0，结果是 1D

#2D Slicing , return 2D array
print(data[:,0:1])
# NOTE shape(3,1) 2D , 取所有 samples，并且保留 feature dimension，结果还是 2D
# OUTPUT
# [[10]
#  [40]
#  [70]]

print(data[:, [0]])
# NOTE shape(3,1), 因为 [0] 是一个 list，NumPy 会保留这一维。
# [[10]
# [40]
# [70]]

print(data[0:2, 1:3]) # [[20 30] [50 60]]


# ML Example 

candidate_data = np.array(
    [
        [5, 90, 85],
        [2, 75, 80],
        [7, 88, 92],
        [1, 65, 70]
    ]
)

# column 0 = years_experience
# column 1 = technical_score
# column 2 = interview_score

#           exp   tech   interview
# row 0      5     90       85
# row 1      2     75       80
# row 2      7     88       92
# row 3      1     65       70

print("\n\n technical_score:", candidate_data[:,1])

# 这个 boolean mask 是作用在 rows 上。这就是现实数据处理中非常典型的模式：data[data[:, 1] >= 80
print("Qualified Candidate:\n" ,candidate_data[candidate_data[:,1]>=80])


strong_candidates = candidate_data[
     (candidate_data[:,1]>=80) & 
     (candidate_data[:,2] >= 90)
     ]
print("Strong Candidate:\n", strong_candidates)
print(strong_candidates.shape) # shape(1,3) 因为筛选出来的是“1 个 row 的 2D dataset”