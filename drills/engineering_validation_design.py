# ====== PIPELINE ============
# RAW EXTERNAL DATA
    # "3", "85", "python|sql"
#        ↓
# PARSE / NORMALIZE
    # 3, 85, ["python", "sql"]
#        ↓
# VALIDATE
    #   是否合法？
    #   required fields?
    #   range?
    #   empty?
#        ↓
# EVALUATE
    # 合法数据应该得到什么结果？

# Parsing / normalization → 把外部数据变成标准 python representation
    # Parsing error→ 无法构造正确 Python representation
# Validation → 检查  python representation 是否符合 contract 
    # Validation error→ Python representation 存在，但违反 contract
# Scoring → 使用已经合法的数据, 在合法 input 上执行 business logic 
    # Business Result → 输入合法，只是结果可能 Recommend / Do Not Recommend

# False 是正常的否定结果；exception 表示 function 无法按自己的 contract 正常完成。

#========== Exer 1 =====================
model_config = {
    "model_name": "classifier_v1",
    "learning_rate": 0.001,
    "epochs": 10,
}

## BUG Version #### 
def validate_model_config(config):
    if (config["model_name"] 
        and config["learning_rate"] >0
        and config["epochs"] > 0 
        # DESIGN BUG 先访问 key,再检查 key 存不存在 不合理 如果某个 key 不存在就会直接 raise KeyError 
        # DEISNG BUG 这样写hard coded 了 key 值检查, 也隐藏限制 config 只能有这三个 key , 而且一个都不能多. 
        # 通常 validation 想表达的是：required fields 必须存在，但允许其他 fields。
        # and {"model_name", "learning_rate","epochs"} == config.keys() 
        ):
        return True
    # DESIGN BUG 要求是只有上述情况全为真 return true, 但是应该分别处理每种不同的 ValueError exception 
    raise ValueError("Input isn't valid")

###‼️ Better Shape
#这里比一个巨大：if A and B and C and D: 更适合 validation。
#因为每一种 failure 都可以告诉调用者：到底哪里错了。
#这正是我们前面讨论 raise ValueError 比单纯 False 更有价值的原因。

def validate_model_config(config):
    required_fields = {
        "model_name",
        "learning_rate",
        "epochs",
    }

    missing_fields = required_fields - config.keys()

    if missing_fields:
        raise ValueError(f"Missing fields: {missing_fields}")
    if not config["model_name"].strip():
        raise ValueError("Model name cannot be empty.")
    if config["laerning_rate"] <= 0:
        raise ValueError("Learning rate must be greater than 0")
    if config["epochs"] <= 0:
        raise ValueError("Epochs must be greater than 0")

    return True





# ========= Exer 2 Responsibility Boundary =============== 
# A.CSV 里 years_experience = "hello"  -> File parsing / normalization 因为这是 loader 的任务 , years_experience = int( row["years_experience"])
# 
# B.Python candidate 里 years_experience = -2  -> validationo 
# 
# C. candidate 缺少 technical_score -> # NOTE 
                    # 最佳答案：Validation ✅ 因为 required-field check 本来就是：required_fields - candidate.keys() validation responsibility。
                    #不过这里有一个很好的现实问题：你当前的 CSV loader 如果 header 本身没有：technical_score. 它可能在： row["technical_score"] 这里先发生 KeyError。 也就是说：我们的理# 想 architecture 说它属于 validation，但当前 implementation 可能会在 parsing layer 过早 crash。
# 
# D.candidate technical_score = 92， 最后决定 Recommend - > scoring 
# 
# E.CSV skills 是： "python|sql|docker" 把它转成： ["python", "sql", "docker"] -> file parsing / normalization 





#========== LEARNING NOTE ================= 
# {"model_name", "learning_rate","epochs"} == config.keys() 
        # NOTE check if two sets are equal in python , use the comparsion operator ==
        # NOTE 
        # # dict.keys() returns a dict_keys view.
                        # - iterable
                        # - set-like: supports &, |, -, comparisons
                        # - dynamically reflects changes made to the original dictionary, 如果 config 自己被修改了 key 这里会反应,但是不能通过 keys()的 return 结果再来修改
                        # - but the dict_keys view itself cannot be directly modified 
                                    # 例如  keys = config.keys()
                                    # keys.add("batch_size")       # ❌
                                    # keys.remove("epochs")        # ❌

#========= NOTE SET A - SET B ============
# setA - setB 代表计算两个集合的差集（Difference）. 
# 它会返回一个新的集合，里面包含所有存在于 setA 中、但不存在于 setB 中的元素。也就是说，从 setA 里剔除了所有属于 setB 的元素。
# 使用 - 运算符与调用 setA 的 .difference() 方法效果完全相同. result = setA.difference(setB)  # 等价于 setA - setB

#==== NOTE 判断一个集合是否为另一个集合的子集 ===========
# 想检查 setA 是不是 setB 的子集，请使用 issubset() 或 <=  运算符：
# setA = {1, 2}
# setB = {1, 2, 3}
# # 检查子集
# print(setA.issubset(setB))  # 输出: True
# print(setA <= setB)         # 输出: True（等价写法）


# ====== LEARNING NOTE ========= 
# 在 Python 中，int() 是一个内置函数，主要用于将其他数据类型转换为整数（Integer），或者进行进制转换。
# 1. 不传参数（默认值）如果不给 int() 传递任何参数，它会默认返回 0。
        # int(int())  # 输出: 0
# 2. 基础类型转换（常用）浮点数转整数：直接截断小数部分（只保留整数，不进行四舍五入）。
        # print(int(3.14))   # 输出: 3
        # print(int(-2.9))   # 输出: -2
# 3. 纯数字字符串转整数：
        # print(int("42"))   # 输出: 42
# 4. 布尔值转整数：
        # print(int(True))   # 输出: 1
        # print(int(False))  # 输出: 0
# 5. 进制转换（带两个参数）当你传入一个字符串和第二个参数 base（进制）时，int(x, base) 可以将该进制的字符串转换为十进制整数：
        ## 二进制转十进制
         #print(int("1010", 2))   # 输出: 10

        ## 八进制转十进制
         #print(int("12", 8))     # 输出: 10

        ## 十六进制转十进制
         #print(int("a", 16))     # 输出: 10
# 6. NOTE 常见报错 Value Error
        # int("3.14")  # 报错！字符串里带小数点无法直接转 int
        # int("abc")   # 报错！无法识别的数字字符串

# ========== LEARNING NOTE ===============
# 要安全地将带小数点的字符串转换为整数，最常用的有以下三种方法：
    # 1. 先转浮点数，再转整数（最常用）# 直接丢弃小数点后面的所有数字（向下取整）。如 "3.99" 转换后也是 3。
            # s = "3.14"
            # result = int(float(s))
            # print(result)  # 输出: 3
    # 2. 四舍五入转换: 如果你希望转换时满足“四舍五入”的数学逻辑，应该在中间加入 round() 函数：
            #s1 = "3.14"
            #s2 = "3.67"
            #print(int(round(float(s1))))  # 输出: 3  (3.14 四舍五入为 3)
            #print(int(round(float(s2))))  # 输出: 4  (3.67 四舍五入为 4)
    # 3. 使用 try-except 捕获异常

#TODO 
# 从混合文本中提取数字并转换（如 "价格：3.14元"）
# 处理带千分位逗号的数字字符串（如 "1,234.56"）