# 程序运行时，file 在磁盘上；Python 要先找到这个 path，再把 file content 读进 memory，变成 Python object。


#=========== EXER 1 Read a whole file ===============
from pathlib import Path 

path = Path("candidates.txt")
# 以后如果突然 FileNotFoundError，第一件事就是： print(Path.cwd())
# Path(__file__).parent  → folder containing the current Python file
# 还可以使用 file_path = Path(__file__).parent / "candidates.txt"
# The / operator here joins path components.

contents = path.read_text()

print(contents)

print(type(path))
print(type(contents))

# =========== Exercise 2 — Process line by line ==========
candidates = []
for line in contents.splitlines():
    print(f"Candidate records: {line}")
# =========== Exercise 3 — Parse the file into Python data ==========
    candidate = {
        "name":line.split(",")[0],
        "experience": int(line.split(",")[1]),
        "technical_score": int(line.split(",")[2])
    }
    # NOTE Tuple unpacking 的写法 更好
    # name, experience, technical_score = line.split(",")
    # candidate = {
    #   "name": name,
    #   "experience": int(experience),
    #   "technical_score": int(technical_score),
#           }
#

    candidates.append(candidate)

print(candidates)


print("\n===== Path Experiment =====")

print("Current working directory:")
print(Path.cwd())

print("\nCurrent Python file:")
print(__file__)

print("\nFolder containing this Python file:")
print(Path(__file__).parent)

# relative to CURRENT WORKING DIRECTORY
relative_path = Path("candidates.txt")

#relative to LOCATION OF THIS .py FILE
script_relative_path = Path(__file__).parent / "candidates.txt"

print("\nRelative path:")
print(relative_path)

print("\nPath based on script location:")
print(script_relative_path)

# A relative path is resolved from the current working directory,
# not automatically from the location of the Python script.