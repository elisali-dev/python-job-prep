from pathlib import Path

# ==========  Exercise 1 — Write one string =======================
# NOTE Path / "文件名" 是处理文件路径的标准推荐做法
# Path(__file__).parent 返回的是一个 Path 对象, 不是字符串
# NOTE 这不是 string concatenation, 这是 Python pathlib 模块中特有的 路径拼接（Path Join） 语法。
# / 是 path 对象的运算符
path = Path(__file__).parent / "message.txt"

path.write_text("Python file writing works!")
print(path.read_text())


# =========== Exercise 2 — Observe overwrite behavior ==========
path.write_text("First version", encoding="utf-8")
path.write_text("Second version", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
print(path.read_bytes())


# ========== Exercise 3 — Write candidate records ============
candidates = [
    {
        "name": "Alex",
        "years_experience": 3,
        "technical_score": 82,
    },
    {
        "name": "Emma",
        "years_experience": 6,
        "technical_score": 92,
    },
]
candidate_str =''
for candidate in candidates:
    name = candidate["name"]
    years_experience = candidate["years_experience"]
    technical_score = candidate["technical_score"]

    candidate_str += f"{name},{years_experience},{technical_score}\n"

print(candidate_str)

path_3 = Path(__file__).parent/"candidate_output.txt"
path_3.write_text(candidate_str)

#NOTE ===== 更常见处理方式 list + join =======
lines = []

for candidate in candidates:
    line = (
        f"{candidate['name']},"
        f"{candidate['years_experience']},"
        f"{candidate['technical_score']}"
    )

    lines.append(line)

print(lines)

# 用 "\n" 把 list 里的多个 strings 连接起来。
# 以后生成 CSV-like output、SQL、reports、logs 时你会经常看到 join()。
candidate_str = "\n".join(lines)


#============ More about join() ===============
#NOTE join 是设计用字符串调用的!!! 而且后边接起来的东西也必须都是 string!! 

#NOTE join() 是 string（字符串） 的专属方法。它不是列表（list）的方法，也不是通用的全局函数。核心原理解析谁能调用它：只有字符串对象才能调用 .join()。在 "\n".join(lines) 中，调用者是 "\n"（一个字符串）。它能接收什么：它接收一个可迭代对象（比如 list、tuple 或 set）作为参数。它的设计逻辑：Python 这样设计是为了节省内存。由字符串来控制连接符，可以更高效地在内存中一次性分配空间并拼接数据。

# 如果调用 join 时，列表中包含了非字符串（比如数字、布尔值），Python 会直接报错：TypeError: sequence item 0: expected str instance, int found。
# 如果列表里有数字，你必须先用 str() 把它们转换成字符串。最优雅的写法是配合 map() 函数或列表推导式

#  正确做法：字符串调用，传入列表
my_list = ["a", "b", "c"]
result = "-".join(my_list)  # 结果: "a-b-c"

#  错误做法：列表没有 join 方法
# my_list.join("-")       # 会报错: AttributeError

mixed_list = ["a", 1, "b", 2]
# result = "-".join(mixed'-list)  # 报错：TypeError

# 方法 1：使用 map() 批量转换（推荐，最快）
result = "-".join(map(str, mixed_list))  # 结果: "a-1-b-2"

# 方法 2：使用列表推导式
result = "-".join([str(item) for item in mixed_list])  # 结果: "a-1-b-2"



#========== Overwrite vs append ==========
path = Path(__file__).parent / "log.txt"

# 'w' = write 会覆盖原内容
with path.open("w", encoding="utf-8") as file:
    file.write("First line\n")

#========= Context Manager : with ... ===========
