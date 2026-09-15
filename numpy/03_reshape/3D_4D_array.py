import numpy as np

# think 3d array as a group of matrix . Imagine its shape (3,n,m) as 3 groups * n rows * m columns 
data_3d = np.array([
    [
        [1,2,3],
        [4,5,6],
    ],
    [
        [7,8,9],
        [10,11,12],
    ]
])
print(data_3d)

print("shape:",data_3d.shape)
print("ndim:", data_3d.ndim)

# 3d array indexing
print("\nfirst group:", data_3d[0]) # group 0 - [[1 2 3] [4 5 6]]
print("shape:",data_3d[0].shape) # (2,3)

print("\nOne Row:",data_3d[0,1]) # group 0, row 1[4 5 6]
print("shape:",data_3d[0,1].shape) # shape: (3,)

print("\nOne Value:", data_3d[0,1,2]) # group 0, row 1, column 2 -> 6 
print("Shape:", data_3d[0,1,2].shape) # Shape: ()
# 每指定一个 index，通常就少一个 dimension。




# 4D array
data_4d = np.array([
    [ # sample0
        [ # channel 0
            [1, 2, 3],
            [4, 5, 6],
        ],
        [ # channel 1
            [7, 8, 9],
            [10, 11, 12],
        ],
    ],
     [
            [
                [13, 14, 15],
                [16, 17, 18],
            ],
            [
                [19, 20, 21],
                [22, 23, 24],
            ],
        ],

])

print(data_4d.shape) # (2,2,2,3) 
#按这个方式读: 2 samples
#每个 sample 有 2 channels
#每个 channel 有 2 rows
#每个 row 有 3 values
print(data_4d.ndim)

# 4D array indexing 
print(data_4d[0]) # 取第 0 个 sample
print(data_4d[0].shape) # (2,2,3)

print(data_4d[0,1]) #取 sample 0, channel 1 
print(data_4d[0,1].shape) (2,3)

print(data_4d[0, 1, 0]) # sample0, channel 1, row 0 
print(data_4d[0, 1, 0].shape) (3,)

print(data_4d[0, 1, 0, 2]) # sample 0, channel 1, row 0, column 2

# 看 4D tensor，不需要想“4D 空间”。你只需要想：一层套一层的数据组织。


# understand 3D array as a group of 2D arrays
# perspective 1 - array of matrix 

# data.shape
# (2, 2, 3)
# 意思是：
# 2 个 matrix
# 每个 matrix 有 2 rows
# 每个 row 有 3 columns

# perspective 2 - 3D shape in ML - Tensor shape thinking
# x.shape
# (32, 10, 128)
# 32 个东西 -比方说32 个学生
# 每个东西里面有 10 个东西 - 每个学生做 10 次考试
# 每个里面又有 128 个数 - 每个考试里有 128 个分数




# ============================================= 
# 4D Array - like a group of 3D arrays 