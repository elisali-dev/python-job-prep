# 它只负责：candidate data 合不合法. separation of concerns

def validate_candidate(candidate):

    # 用花括号 {} 包裹了一组字符串，且没有 key: value 的键值对结构。这在 Python 中表示一个集合（Set），而不是字典
    required_fields = {
        "name",
        "years_experience",
        "technical_score",
        "skills",
    }

    #Python 的集合（Set）差集运算，而不是字典的直接相
    missing_fields = required_fields - candidate.keys()
    # candidate.keys() 返回一个类似集合的视图（Set-like View）在 Python 3 中，字典的 .keys() 方法返回一个 dict_keys 对象。这个对象具有集合的特性，支持交集、并集和差集等位运算。
    # 减号（-）代表求差集（Difference）集合支持用减号 - 来计算差集。A - B 的意思是：找出存在于 A 中、但不存在于 B 中的所有元素。

    if missing_fields:
        raise ValueError(f"Missing fields: {missing_fields}")

    if not candidate["name"].strip():
        raise ValueError("Candidate name cannot be empty.")

    if candidate["years_experience"] < 0:
        raise ValueError("Years of experience cannot be negative.")

    if not 0 <= candidate["technical_score"] <= 100:
        raise ValueError("Technical score must be between 0 and 100.")

    if not isinstance(candidate["skills"], list):
        raise ValueError("Skills must be a list.")

    return True