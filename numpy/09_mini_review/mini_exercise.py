# Pipeline 模拟：生成数据 → 计算 prediction → 加 bias → 加一点随机噪声 → 筛选高分样本 → 汇总结果

import numpy as np 

rng = np.random.default_rng(42) # 每次运行都能得到同样的随机结果，方便 debug 和复现实验

X = np.array([
    [90, 85],
    [75, 80],
    [88, 92],
    [65, 70],
    [82, 78],
])

print("X shape:", X.shape)

weights = np.array([
    [0.6],
    [0.4],
])

bias = 5

predictions = X @ weights + bias

print("\nPredictions:")
print(predictions)
print("shape:", predictions.shape)

noise = rng.normal(
    loc=0,
    scale=1,
    size=(5,1), # size 必须跟prediction一致  如果是(5,1) 和(5,) 相加, broadcasting 会让每个 prediction 和每个 noise 分别加一遍, 得到一个 (5,5) matrix 
)
# 如果用 size = 5 生成 noise = rng.normal(0,1,5), 就可以 reshape noise = noise.reshape(5, 1)
# noise = noise[:, np.newaxis] 升维 
print("\nNoise:")
print(noise)

noisy_predictions = predictions + noise 

print("\n Noisy predictions:")
print(noisy_predictions)

high_score_mask = noisy_predictions[:,0] >= 85 
print("\nHigh score mask:")
print(high_score_mask)

selected_candidates = X[high_score_mask]

print("\nSelected candidates:")
print(selected_candidates)
print("shape:",selected_candidates.shape)

mean_prediction = noisy_predictions.mean()
max_prediction = noisy_predictions.max()
min_prediction = noisy_predictions.min()

print("\nSummary:")
print("Mean:", mean_prediction)
print("Max:", max_prediction)
print("Min:", min_prediction)