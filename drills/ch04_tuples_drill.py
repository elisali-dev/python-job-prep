model_config = ("transformer", 512, 8)
# model name, hidden size, number of attention heads
# 要求： 用 tuple unpacking 创建三个 variables
# 输出：
# Model: transformer
# Hidden size: 512
# Attention heads: 8
model_name, hidden_size, number_of_attention_heads = model_config
print(f"Model: {model_name}")
print(f"Hidden size: {hidden_size}")
print(f"Attention heads: {number_of_attention_heads}")
# 尝试直接修改 hidden size：
# model_config[1] = 768
# 看 error，然后 comment 掉

# 最后通过重新 assignment 一个新 tuple，把 config 改成： ("transformer", 768, 12)
# 并 print 新 tuple。

model_config =  ("transformer", 768, 12)
print("model_config")