import numpy as np

# 1 D array 
scores = np.array([85, 90, 78, 92])

print(scores)
print(type(scores)) # <class 'numpy.ndarray'>

print("shape:", scores.shape) # shape: (4,)
print("ndim:", scores.ndim) # ndim: 1
print("dtype:", scores.dtype) # dtype: int64 
# NOTE Numpy requires same data type of all the elements in the list, whereas no need for Python list
# purpose:  vectorization- faster computing, better memory management

# 2 D array 
scores_2D = np.array([[85, 90, 78, 92]])
print("\n", scores_2D)
print("ndim:",scores_2D.ndim)
print("shape:",scores_2D.shape) 
# 2d array shape = (row, column), index starts from 0,  ndim 表示需要 2 个坐标确定一个值, 
# in ML, shape = (samples, features)
print("dtype:",scores_2D.dtype)


student_scores = np.array([[85, 90, 78],
                           [92, 88, 95],
                           [70, 75, 80],
                           ])

print("\n2D array:", student_scores)
print("shape:", student_scores.shape)
print("ndim:", student_scores.ndim)
print("dtype:",student_scores.dtype)