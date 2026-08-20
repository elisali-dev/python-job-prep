
from pathlib import Path

path = Path(__file__).parent / "candidates.txt"

with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line)
    print(file.closed)

print(file.closed)


# ============================================================
# with / Context Manager
# ============================================================


# ------------------------------------------------------------
# 1. Opening a file creates a resource
# ------------------------------------------------------------

# file = open("data.txt", "r")
#
# The program now has an open file resource.
#
# After using it, the file should be closed:
#
# file.close()


# ------------------------------------------------------------
# 2. Manual open / close
# ------------------------------------------------------------

# file = open("data.txt", "r", encoding="utf-8")
#
# contents = file.read()
#
# file.close()


# Problem:
#
# What if an exception happens before file.close()?
#
# Then cleanup may not happen correctly.


# ------------------------------------------------------------
# 3. with automatically manages cleanup
# ------------------------------------------------------------

# with open("data.txt", "r", encoding="utf-8") as file:
#     contents = file.read()
#
#
# When the with block finishes,
# Python automatically closes the file.


# Mental model:
#
# enter with block
#     ↓
# open resource
#     ↓
# use resource
#     ↓
# leave block
#     ↓
# automatically clean up / close resource


# ------------------------------------------------------------
# 4. "as file" creates a variable for the opened object
# ------------------------------------------------------------

# with open("data.txt", "r") as file:
#
# "file" refers to the opened file object
# inside the with block.


# ------------------------------------------------------------
# 5. The variable may still exist after the with block,
#    but the underlying file is closed
# ------------------------------------------------------------

# with open("data.txt") as file:
#     print(file.closed)   # False
#
# print(file.closed)       # True


# ------------------------------------------------------------
# 6. with works even if an exception happens
# ------------------------------------------------------------

# with open("data.txt") as file:
#     contents = file.read()
#     something_that_fails()
#
#
# Even if the code fails,
# Python still closes the file properly.


# This is one of the main reasons to use "with".


# ------------------------------------------------------------
# 7. pathlib also supports context managers
# ------------------------------------------------------------

# from pathlib import Path
#
# path = Path("data.txt")
#
# with path.open("r", encoding="utf-8") as file:
#     contents = file.read()


# ------------------------------------------------------------
# 8. read_text() does not require us to manage the file manually
# ------------------------------------------------------------

# path.read_text()
#
# is a higher-level convenience method.
#
# Python opens the file, reads it, and closes it internally.


# Therefore for simple whole-file reading:
#
# path.read_text()
#
# is often cleaner.


# But with/open is useful when:
#
# - reading large files line by line
# - appending
# - controlling file mode
# - streaming data
# - working with APIs/libraries that return resources


# ------------------------------------------------------------
# 9. Reading line by line
# ------------------------------------------------------------

# with path.open("r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
#
#
# This does NOT require loading the entire file into memory first.


# Compare:
#
# path.read_text()
# → whole file becomes one big string
#
#
# for line in file:
# → process one line at a time


# ------------------------------------------------------------
# 10. Connection to exceptions
# ------------------------------------------------------------

# with helps CLEAN UP resources.
#
# try/except helps HANDLE errors.
#
# They solve different problems.


# You can combine them:
#
# try:
#     with path.open("r", encoding="utf-8") as file:
#         contents = file.read()
#
# except FileNotFoundError:
#     print("File not found.")


# ------------------------------------------------------------
# Main takeaway
# ------------------------------------------------------------

# with
# → safely manage a resource's lifetime
#
# try/except
# → handle errors
#
# raise
# → create/propagate errors
