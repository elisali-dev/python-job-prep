# based on engineering_csv_gap.py
import os 
import csv 
from pathlib import Path

print("Current working directory:")
print(os.getcwd()) # 返回的也是一个string, 返回你在哪里启动这个程序的文件夹, 比方说可能是 parent folder 或者OS terminal 当前 folder 
# BUG AttributeError: 'str' object has no attribute 'getcwd'
# print(__file__.getcwd())

print("Current python file:")
print(__file__) # will always be the same, 代表这个.py 文件自己在哪里


# ================= Relative Path ================
print("0:__name__", __name__)
print("1: __file__", __file__) # 当前 script, 是一个 string

print("2:", Path(__file__)) # 变成 Path object

print("3:", Path(__file__).resolve()) # 得到完整absolute path

print("4:", Path(__file__).resolve().parent) # 取它所在的folder 

# 当前这个python 文件所在的directory 
# NOTE .parent 是一个属性，而不是方法。你不应该加括号 ()。
# BUG BASE_DIR = Path(__file__).resolve().parent()
# NOTE use ALL CAPS for variable name to indicate it is supposed to be a CONSTANT 
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "models.csv" # 对于 Path object，/ 被定义成“拼接 path”。 # CSV_FILE 变量是一个 Path 对象

# =========== Open File ====================
#NOTE 要解决：不管我从 repo root 还是从 drills/ 启动，程序都应该找到和 script 放在一起的 models.csv。

with open(
    # "models.csv", # relative path 默认相对于 Current Working Directory
    CSV_FILE, # NOTE open() 函数既可以接收 string，也可以接收 Path 对象。
    "r",
    encoding = "UTF-8"
) as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
