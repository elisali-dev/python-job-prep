#========= JSON ============
# JSON 不规定必须是 {} 还是 []。它们是不同的数据类型，可以嵌套混用。
# 技术上，一个 JSON 顶层甚至可以只是： "hello" 或： 123, 但现实 API/config/data files 最常见的是 {} 或 []。
# 
# {} 遵循 dict（字典）格式：里面必须是 键: 值（key: value）形式，并且 key 必须是双引号的字符串。
# [] 遵循 list（列表）格式：里面就是一串单纯的值，没有 key。
# 怎么套无所谓：你可以在 value 的位置塞入任何合法的 JSON 类型（包括另一个 {} 或 []），无限套娃。
 
#########Python vs JSON 不同点 ###########
# Python        JSON
# 
# True          true
# False         false
# None          null
# 
########### 3 个极小的“坑”需要注意 ############
# Key 必须用双引号 ""Python 里写 {'name': '张三'} 是合法的。但在 JSON 里，必须写成 {"name": "张三"}（单引号会报错）。
# 最后一个元素后面不能有逗号Python 列表中 [1, 2, 3, ] 尾部加逗号是允许的。JSON 中 [1, 2, 3, ] 或 {"a": 1, "b": 2, } 属于非法语法。
# 值（Value）的类型是有限的只能是：字符串（双引号）、数字、true/false（小写）、null（对应 Python 的 None）、{}、[]。不能放 Python 的 tuple（元组）、set（集合）或时间对象。


# Python 怎么读取 JSON? 
import json

#NOTE Path("data.json") 不是 relative to .py file，而是 relative to： Path.cwd()
# 这个取决于你terminal 正停留在哪个文件夹下面运行. 
# 所以如果你今天在：python-job-prep/运行，明天又在：
# python-job-prep/pcc/ch11_testing/运行，同一条 relative path 可能代表完全不同的位置。
# 从 repo root 跑可以形成统一习惯：

#### dumps(): converts a jason string to a python object ######

text = '{"name": "Alex", "score": 82}'

candidate = json.loads(text) # This converts a jason string to a python object 

print(candidate) # {'name': 'Alex', 'score': 82}
print(type(candidate)) # <class 'dict'>

text = json.dumps(candidate)


##### loads() : load json string to python object 


# ============================================================
# Ch10 - 04 JSON Data
# Knowledge Notes
# ============================================================

import json


# ------------------------------------------------------------
# 1. JSON = a text format for structured data
# ------------------------------------------------------------

# JSON object:
#
# {
#     "name": "Alex",
#     "score": 82
# }
#
# corresponds to Python dict.


# JSON array:
#
# [
#     {"name": "Alex"},
#     {"name": "Emma"}
# ]
#
# corresponds to Python list.


# JSON can mix / nest:
#
# {
#     "name": "Alex",
#     "skills": ["python", "sql"],
#     "contact": {
#         "city": "Detroit"
#     }
# }


# ------------------------------------------------------------
# 2. JSON types vs Python types
# ------------------------------------------------------------

# JSON                Python
#
# object {}       ->  dict
# array []        ->  list
# string          ->  str
# number          ->  int / float
# true / false    ->  True / False
# null            ->  None


# ------------------------------------------------------------
# 3. json.loads()
# ------------------------------------------------------------

# loads = load string
#
# JSON STRING
#     ↓
# json.loads()
#     ↓
# Python object


# Example:
#
# json_text = '{"name": "Alex", "score": 82}'
#
# candidate = json.loads(json_text)
#
# candidate is now a Python dict.


# ------------------------------------------------------------
# 4. json.dumps()
# ------------------------------------------------------------

# dumps = dump string
#
# Python object
#     ↓
# json.dumps()
#     ↓
# JSON STRING


# Example:
#
# candidate = {
#     "name": "Alex",
#     "score": 82,
# }
#
# json_text = json.dumps(candidate)


# ------------------------------------------------------------
# 5. dumps() returns str
# ------------------------------------------------------------

# json.dumps(...)
# does NOT automatically create a file.
#
# It only returns a string.


# ------------------------------------------------------------
# 6. indent makes JSON human-readable
# ------------------------------------------------------------

# json.dumps(data, indent=4)
#
# produces pretty-formatted JSON.


# ------------------------------------------------------------
# 7. json.load() vs json.loads()
# ------------------------------------------------------------

# json.loads(...)
# → takes a STRING
#
# json.load(...)
# → takes an OPEN FILE OBJECT


# Example:
#
# with open("data.json", "r") as file:
#     data = json.load(file)


# ------------------------------------------------------------
# 8. json.dump() vs json.dumps()
# ------------------------------------------------------------

# json.dumps(...)
# → returns JSON STRING
#
# json.dump(...)
# → writes JSON directly to an OPEN FILE OBJECT


# Example:
#
# with open("output.json", "w") as file:
#     json.dump(data, file, indent=4)


# ------------------------------------------------------------
# 9. Easy memory trick
# ------------------------------------------------------------

# "s" means STRING
#
# loads  -> JSON string → Python
# dumps  -> Python → JSON string
#
# no "s":
#
# load   -> file object → Python
# dump   -> Python → file object


# ------------------------------------------------------------
# 10. JSON syntax is not exactly Python syntax
# ------------------------------------------------------------

# Python:
#
# {
#     "active": True,
#     "email": None,
# }
#
#
# JSON:
#
# {
#     "active": true,
#     "email": null
# }


# ------------------------------------------------------------
# 11. Invalid JSON raises JSONDecodeError
# ------------------------------------------------------------

# bad_json = '{"name": "Alex",}'
#
# json.loads(bad_json)
#
# → json.JSONDecodeError


# ------------------------------------------------------------
# Main takeaway
# ------------------------------------------------------------

# JSON is TEXT.
#
# json.loads / json.load
# → JSON → Python
#
# json.dumps / json.dump
# → Python → JSON



#======== Exercise 1 — loads() ==============
print("Exercise 1 — loads()")
json_text = """
{
    "name": "Alex",
    "years_experience": 3,
    "technical_score": 82,
    "active": true,
    "email": null
}
"""

candidate = json.loads(json_text)  

print(candidate)
print(type(candidate))
print(type(candidate["active"])) # true changed to True in python
print(candidate["email"]) # null in json changed to None in python 

#========= Exercise 2 — JSON array =============
print(" Exer 2 - JSON array")

json_text = """
[
    {"name": "Alex", "score": 82},
    {"name": "Emma", "score": 92}
]
"""

candidates = json.loads(json_text)

print(type(candidates))
print(type(candidates[0]))
print(candidates[1]["name"])

# ========= Exercise 3 — dumps() =====
print("========= Exercise 3 — dumps() =====")
candidate = {
    "name": "Sam",
    "years_experience": 1,
    "technical_score": 90,
    "active": True,
    "email": None,
}

json_text = json.dumps(candidate, indent=4)

print(json_text)
print(type(json_text))



# ========== Exercise 4 — load() / dump() ============
print("========== Exercise 4 — load() / dump() ============")

from pathlib import Path

path = Path(__file__).parent / "candidates.json"

with path.open("r", encoding="utf-8") as file:
    candidates = json.load(file)

print(type(candidates))
print(candidates[0]["name"])    

# 常用方法对比
# 方法            |输入参数                                   |返回的 Python 类型
# json.load()     文件对象（File-like object）                dict 或 list 等原生对象
# json.loads()    包含 JSON 数据的字符串（String）              dict 或 list 等原生对象
# f.read()        无（作用于文件对象）                            str（大字符串）

#json.load() 不会把 JSON 文件读成一个大字符串（String），而是直接把它转换成 Python 的原生数据结构（比如字典 dict 或列表 list）。核心区别不是大字符串：如果你想把文件读成字符串，应该用 f.read()。是 Python 对象：json.load() 接受一个已经打开的文件对象，解析里面的 JSON 格式，然后变成可以直接用键（Key）或索引（Index）访问的 Python 字典或列表。工作流程读取文件：它一行行或一块块从文件里读取数据。解析内容：它把 JSON 的文本规则翻译成 Python 的数据类型。内存占用：虽然最终数据都在内存里，但它的类型是 dict 或 list，而不是 str



output_path = Path(__file__).parent / "json_output.json"

with output_path.open("w", encoding = "utf-8") as file:
    json.dump(candidates, file, indent=4)
    # 不加 indent（默认）：数据全部挤在一行，节省空间，但人类很难阅读。
    # 加上 indent=4：自动在每个层级换行，并缩进 4 个空格，结构一目了然。
    # json.dump() 的返回值是 None。


"""
================================================================================
KNOWLEDGE NOTE: Python `json` Module Core Functions
================================================================================

1. 从数据流向区分 (File vs String):
   - 带 's' 的函数 (dumps/loads): 处理 [S]tring (字符串)
   - 不带 's' 的函数 (dump/load): 处理 [F]ile (文件对象)

2. 核心函数对比表:
   +--------------------+--------------+-------------------+----------------------------+

   | 函数               | 是否有返回值 | 返回值类型        | 核心作用                   |
   +--------------------+--------------+-------------------+----------------------------+

   | json.load(f)       | 有           | dict / list 等    | 读文件：解析文件并载入内存 |
   | json.dump(obj, f)  | 没有 (None)  | None              | 写文件：直接保存到磁盘文件 |
   | json.dumps(obj)    | 有           | str (JSON格式)    | 转文本：对象转成JSON字符串 |
   | json.loads(str)    | 有           | dict / list 等    | 解析文本：字符串变回Python |
   +--------------------+--------------+-------------------+----------------------------+

3. 常用关键参数备忘 (针对 dump / dumps):
   - indent=4          : 美化输出，每一层缩进 4 个空格（方便人类阅读）
   - ensure_ascii=False: 允许输出真正的中文，而不是可读性差的 \\uXXXX 编码
================================================================================
"""