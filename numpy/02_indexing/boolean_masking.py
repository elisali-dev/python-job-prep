import numpy as np

scores = np.array([85, 90, 78, 92, 65, 88])

mask = scores >= 80 

print("scores:", scores)

print("mask:", mask)

# NumPy 会保留 True 对应的位置的值
print("filtered:", scores[mask])


# NOTE array[condition] NumPy 非常典型的写法。
print(scores[scores >= 80])


# Python 标量逻辑	            NumPy array
# a and b                 	    a & b
# a or b	                    a | b
# not a	                        ~a

# 普通python list 不能写 scores>=80 , 会报错
# 普通 python list 要写 [x for x in scores if x >=80]

"""
核心操作对比表
运算符     🐍 Python 原生 (以 list 为例)           🧱 NumPy (np.ndarray)                            🔥 PyTorch (torch.Tensor)
x + y        列表拼接[1,2] + [3,4]                  按元素相加 (Element-wise)[1,2] + [3,4]              按元素相加 (Element-wise)与 NumPy 行为完全一致 
                得到 [1,2,3,4]                      得到 [4,6]            

x * y        列表重复[1,2] * 2                       按元素相乘 (Element-wise)对应位置数字相乘             按元素相乘 (Element-wise)与 NumPy 行为完全一致
            得到 [1,2,1,2] (若 y 也是列表会报错)        (Hadamard product)

x @ W       ❌ 不支持直接报错 TypeError              矩阵乘法 (Matrix Multiplication)                    矩阵乘法 (Matrix Multiplication)标准的线性代数点积（神经网络最核心操作）
                                                    标准的线性代数点积（Dot Product）                       相当于 torch.matmul(x,W)
                                                    相当于np.dot(x,W)或者 x.dot(W)


x > 0       ❌ 不支持不能直接拿列表和数字比大小           条件广播 (Broadcasting)返回一个由 True/False 组成的布尔矩阵            (报错)条件广播 (Broadcasting)返回一个由 True/False (或 0/1) 组成的布尔张量
                                                     例如 ReLU  scores[scores < 0] = 0  把所有负数变成 0

"""