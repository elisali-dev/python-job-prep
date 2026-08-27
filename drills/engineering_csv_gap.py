import csv 

# LEARNING NOTE 
        # csv.DictReader(file)：把每一行解析为字典（Dictionary）。Key 是表头，Value 是单元格内容。
        # csv.reader(file)：把每一行解析为列表（List）。每个单元格是列表中的一个元素，只能通过索引（如 row[0], row[1]）来访问。

# ======= Exercise 1 — 用 csv.reader ===========
print("====== Exercise 1: csv.reader(file)=========")
with open(
    "models.csv",
    "r",
    encoding = "UTF-8"
) as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# ======= Exercise 2 — 用 csv.DictReader ===========
print("===== Exercise 2: csv.DictReader(file)=========")
with open("models.csv","r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# ======= Exercise 3 — 用 csv.DictReader ===========
print("===== Exercise 3 & 4 : csv.DictReader(file) and make it a Python list=========")

# 数据 pipeline transition
models = []

with open("models.csv","r", encoding="UTF-8") as file:
    # 惰性读取（逐行读取）机制。它只是创建了一个迭代器对象（Iterator），相当于做好了逐行读取的准备，但此时还没有真正去读文件的内容。
    # 自动解析首行：它会自动把 CSV 文件的第一行当做表头（Key)，之后的每一行都会被解析为以表头为键的字典
    reader = csv.DictReader(file)
    # 要真正开始逐行读取，你需要用 for 循环去遍历这个 reader 对象. 这非常适合处理超大文件，不会占用太多内存。
    for row in reader:
        accuracy = float(row["accuracy"])
        latency_ms = int(row["latency_ms"])
        print(row["model_name"])
        print(accuracy)
        print(latency_ms)
        model = {
            "model_name": row["model_name"],
            "accuracy": accuracy, 
            "latency_ms": latency_ms,
        }
        models.append(model)

print(models)



