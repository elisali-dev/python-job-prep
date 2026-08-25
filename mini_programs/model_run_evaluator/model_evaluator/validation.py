# model_run = {
#     "model_name": "image_classifier_v1",
#     "accuracy": 0.87,
#     "latency_ms": 75,
#     "memory_mb": 1200,
# }
# 
# 你的程序要做三件事：
# 
# 检查这些数据是否合法
# 判断模型 performance level
# 判断是否推荐 deployment

#规则：
# model_name 不能是空字符串
# 
# accuracy:
#     必须 >= 0
#     必须 <= 1
# 
# latency_ms:
#     必须 > 0
# 
# memory_mb:
#     必须 > 0

def validate_model_run(model_run):
    if (model_run["model_name"] # 只会拒绝："" 但："   "会被认为是真。
        # 小改进: model_run["model_name"].strip()
        and 0 <= model_run["accuracy"] <= 1 
        and model_run["latency_ms"] > 0 
        and model_run["memory_mb"] > 0 
        ):
            return True 
    return False
    
