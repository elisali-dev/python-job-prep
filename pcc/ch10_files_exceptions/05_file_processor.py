from pathlib import Path
import json


# 读取candidates.json
# 处理以后创建 candidate_report.json
# 把每个 candidate record 加上 "decision": "Pass"/ "Reject"


def load_candidates(path):
    """
    Read JSON file and return Python candidate data.
    """
    # BUG return json.load(path)
    # path 是一个路径对象（Path object）或字符串路径，它只是一个“地址”，而不是一个打开的文件对象。json.load(f) 的输入参数必须是一个文件对象（File-like object）。如果直接把路径传给它，json.load() 会因为它没有 read() 方法而直接抛出 AttributeError。
    # 在调用 json.load() 之前，我们必须先用 with open() 把这个路径真正打开，变成文件数据流。
    with open(path, "r", encoding = "utf-8") as file:
        return json.load(file)
    # NOTE 第二种写法 with path.open("r", encoding="utf-8") as file:
                        # return json.load(file)
    # NOTE 第三种写法 return json.loads(path.read_text(encoding="utf-8"))


def validate_candidate(candidate):
    """
    Validate required fields and values.
    """
    # 1. 这一步直接访问三个必需的 key。如果其中任何一个不存在，Python 会在此处自动、自然地抛出 KeyError！
    # 完全不需要写 try-except，也不需要手动检查是否存在。
    exp = candidate["years_experience"]
    score = candidate["technical_score"]
    _ = candidate["name"]  # 只是为了触发可能存在的 KeyError
    # 下划线 _ 是一个约定俗成的特殊变量名，用来表示“这是一个临时变量，我只是不得不把它写出来，但我后面完全不会用到它的值”
    
    # 2. 检查业务规则 (Business rules)
    # 如果不满足条件，直接抛出 ValueError
    if not (exp >= 0 and 0 <= score <= 100):
        raise ValueError("Business rule invalid: years_experience must be >= 0 and technical_score must be between 0 and 100")



    # for candidate in load_candidates():
    #     try:
    #         "name", "years_experience", "technical_score" in candidate
    #     except KeyError:
    #         print("Key Error!")
    #     else:
    #         if not (candidate["years_experience"] >= 0 and 0 <= candidate["technical_score"] <= 100):
    #             raise ValueError
    # NOTE v1 is a total failure 
    # 混淆了函数的职责（最严重）- for candidate in load_candidates():。这变成了在函数内部去加载并循环所有候选人。这破坏了函数原本的接口设计
    # 题目的函数是 validate_candidate(candidate)，参数是一个单单个体的字典

    # "name", "years_experience", "technical_score" in candidate。在 Python 中，这并不会检查三个键是否都在字典里。这其实是一个元组（Tuple），等同于 ("name", "years_experience", ( "technical_score" in candidate ))。它绝对不会触发 KeyError。

    # 题目明确写了：Required key 如果不存在，可以让 candidate["..."] 自然产生 KeyError，并且这里不要 print。- 而我的代码里用了 try except 完全违反了要求

    # NOTE - 用一行代码快速判断多个 key 是否都在 dict 里面
    #写法 1：使用 all() 配合列表推导式（最推荐、最 Pythonic）
        # # 判断这三个 key 是否【全部】在 candidate 中
            #all_keys_exist = all(k in candidate for k in ["name", "years_experience", "technical_score"])
                # all() 函数要求括号里的所有条件都为 True 才会返回 True。只要有一个 key 不存在，它就会立刻返回 False（具备短路求值特性，非常高效）。
    # 写法 2：使用集合（Set）的子集判断
        ## 判断集合是否是 dict 的子集
            # all_keys_exist = {"name", "years_experience", "technical_score"}.issubset(candidate)



def get_experience_level(candidate):
    if candidate["years_experience"] >= 5:
        return "Senior"
    elif 2<= candidate["years_experience"] <5:
        return "Mid"
    elif 0<= candidate["years_experience"] <2:
        return "Entry"
    return "Invalid Input"

# 简化版本写法
# 一个地方已经负责 validation，后面的 function 可以基于这个 contract 工作。
def get_experience_level(candidate):
    years = candidate["years_experience"]

    if years >= 5:
        return "Senior"
    elif years >= 2:
        return "Mid"
    else:
        return "Entry"


def is_qualified(candidate):
    return candidate["years_experience"] >=2 and candidate["technical_score"] >= 75 

def build_report(candidates):
    report = []

    for candidate in candidates:
        validate_candidate(candidate)
        name = candidate["name"]
        experience_level = get_experience_level(candidate)
        score = candidate["technical_score"]
        report_record = {
            "name": name,
            "experience_level": experience_level,
            "technical_score": score
        } 
        if is_qualified(candidate):
            report_record["decision"] = "Pass"
        else:
            report_record["decision"] = "Reject"
        report.append(report_record)

    return report 

    
def save_report(report, path):
    with path.open("w",encoding="utf-8") as file:
        json.dump(report, file,indent=4)



input_path = Path(__file__).parent/"candidates.json"
output_path = Path(__file__).parent/"candidate_report.json"

try:
    candidates = load_candidates(input_path)
    report = build_report(candidates)
    save_report(report, output_path)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Decoding error")
except KeyError as error:
     print(f"Missing required field: {error}")
except ValueError as error:
    print(f"Invalid candidate data: {error}")
else:
    print(f"Processed {len(candidates)} candidates.\n"
          f"Report saved to candidate_report.json")

        