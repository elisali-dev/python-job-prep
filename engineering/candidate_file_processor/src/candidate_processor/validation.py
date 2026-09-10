# 它只负责：candidate data 合不合法. separation of concerns

def validate_candidate(candidate:dict[str,str|int|float|list[str]]) -> None:

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

    # NOTE 没有意义 删除是更好更干净的设计
    # valid   → 正常执行完毕 → None -> main block 继续运行
    # invalid → raise ValueError -> 被 main catch
    # return True


"""
Engineering 05A — Type Hints Basics

1. Parameter hint

def greet(name: str):

2. Return hint

def greet(name: str) -> str:

3. No return value

def validate_score(score: int) -> None:

4. Type hints describe expected types.
They do not enforce types at runtime.

type hint != runtime validation

5. Most valuable place for hints:
function parameters + return values

6. Think of function signatures as contracts:

float -> str
int -> None
candidate -> evaluation

7. File paths can use pathlib.Path

from pathlib import Path

def load_file(file_path: Path):
    ...


"""