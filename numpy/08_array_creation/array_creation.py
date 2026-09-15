# 快速创建特定 shape / 特定数值分布的 array 
import numpy as np 

#  zeros/ ones/ full 
zeros = np.zeros((2,3)) # dtype float64
zeros_int = np.zeros((2,3), dtype=int)
ones = np.ones((2,3))
sevens = np.full((2,3), 7)


print("zeros:")
print(zeros)
print("\nzeros_int:")
print(zeros_int)
print("\nones:")
print(ones)

print("\nfull:")
print(sevens)


# np.arange(start, stop, step) # start included, stop excluded, 主要指定几个 step
numebrs = np.arange(0, 10)
print("\narange:")
print(numebrs)


# linspace() # start, stop included, 主要指定一共要几个点
numbers = np.linspace(0,1,5)
print("\nnumbers:")
print(numbers)

# random number generator
rng = np.random.default_rng()

print("\nrandom floats:")
print(rng.random(5)) # 会生成 5 个 [0, 1) 之间的随机小数。

print("\nrandome integers:")
print(rng.integers(0,10,size=5)) # 从 0 到 9随机生成 5 个整数, 注意 stop 10 不包含，和 range() 类似。

random_matrix = rng.random((2,3))

print("\nrandom matrix:")
print(random_matrix)
print(random_matrix.shape)

# random distribution 

# 从均值 0、标准差 1 的正态分布采样 5 个数。
# 本质上是“按某种规定好的分布方式进行随机抽样（Sampling）”。
normal_values = rng.normal(
    loc = 0, 
    scale = 1, 
    size=5,
)
print(normal_values)


# Seed for random number generator
rng_seed = np.random.default_rng(42) # 42 是 seed。它的作用不是“取消随机”，而是： 给随机数生成器一个固定起点，所以每次都能重现同一串伪随机结果。
print("\nSeeding random number generator")
print(rng_seed.random(5))


"""
在正态分布中有一个著名的 68-95-99.7 法则（经验法则）：约 68% 的随机数会落在 [均值 - 1个标准差, 均值 + 1个标准差] 之间。在代码中（scale=0.1），这意味着大约 68% 的权重会在 -0.1 到 0.1 之间。约 95% 的随机数会落在 [均值 - 2个标准差, 均值 + 2个标准差] 之间（即 -0.2 到 0.2）。

“分布”本身是一个数学数学模型（概率密度函数），它规定了每一个区域出数字的概率高低。rng.normal() 做的不是创造这个模型，而是在这个已有的数学规则下，吐出符合该规则的随机数字。因为计算机不能真的无中生有，它必须通过算法。所以用“正态分布采样”或“从正态分布中抽取随机样本”在计算机科学中是更准确的严谨表述。

NumPy 的 default_rng() 功能非常强大，几乎涵盖了统计学和机器学习中所有常用的分布。
它们被归类为连续分布和离散分布两大类：
#连续分布（抽样结果是连续的小数）
均匀分布 rng.uniform(low, high, size)：在指定的区间内，每一个小数被抽到的概率完全一样（比如模拟均匀的噪声）。
指数分布 rng.exponential(scale, size)：常用于模拟事件发生的时间间隔（如排队等待时间、放射性衰变）。
贝塔分布 / 伽马分布 rng.beta(), rng.gamma()：常用于贝叶斯统计中作为先验概率分布。
#离散分布（抽样结果是整数/计数）
二项分布 rng.binomial(n, p, size)：模拟做 \(n\) 次独立的“硬币实验”，每次成功的概率是 \(p\)，最后成功的次数。
泊松分布 rng.poisson(lam, size)：模拟在一段固定时间内，某随机事件发生的次数（如某网页一分钟内的访问量）。
整数均匀分布 rng.integers(low, high, size)：在指定整数区间内随机抽样（如掷骰子）。

"""

