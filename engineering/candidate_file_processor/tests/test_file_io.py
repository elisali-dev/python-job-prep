import pytest
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR/"test_candidates.csv"

def test_load_candidates():
    candidates = []
    with open(
        CSV_FILE,
        "r",
        encoding="UTF-8"
    )as file:
        reader = csv.DictReader(file)
        for row in reader:
            candidate = {
                "name": row["name"],
                "years_experience": row["years_experience"],
                "technical_score": int(row["technical_score"]),
                # BUG "skills":list(row["skills"], "|") 
                # # list() 的功能是把一个可迭代对象（如元组、集合、字符串）整体转换成列表。例如 list("abc") 会变成 ['a', 'b', 'c']。它不接受第二个parameter, 无法指定按某个字符切分。
                "skills": row["skills"].split("|") # 用 string 自带的 split()方法把一个包含分隔符的字符串切分成列表
            }
            candidates.append(candidate)

    assert len(candidates) == 2 
    assert candidates[0]["name"] == "Test Alice"
    assert candidates[0]["years_experience"] == "3"
    assert candidates[0]["technical_score"] == 85
    assert candidates[0]["skills"] == ["python", "sql"]

    # NOTE 在同一个测试函数（def test_...）中，pytest 执行断言是从上到下的。
    # 只要其中一个 assert 失败（报错），Python 就会立刻抛出 AssertionError 并中断当前测试函数，后面的代码和 assert 都不会再运行了。
            
