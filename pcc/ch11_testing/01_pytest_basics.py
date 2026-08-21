# NOTE how to use this file?
# in command line at repo root % pytest pcc/ch11_testing/01_pytest_basics.py -v

# NOTE More about Pytest
# pytest 既是一个 Python package/library，也是一个 command-line testing tool/framework。
# python → general Python interpreter
# 用 python run 这个 file 的话, python 只把test_something() 当普通 function。你如果没有 call它,它不会执行
# pytest → specialized test runner built with Python
# 用 pytest 的意思是 启动 pytest test runner，让它扫描这个文件，自动找到所有 test_... functions，运行它们，并告诉我哪些 pass / fail。

# python program.py → run a Python program
# python -m pytest → ask Python to run the pytest testing module
# pytest → shortcut CLI provided by the pytest package

# NOTE testing 里最基本的 expected vs actual 思维。assert actual == expected


# ============================================================
# Ch11 - 01 Pytest Basics
# Knowledge Notes
# ============================================================


# 1. A test compares ACTUAL behavior with EXPECTED behavior.
#
# Example:
#
# actual = get_experience_level(candidate)
# expected = "Mid"
#
# assert actual == expected


# 2. assert means:
#
# "This condition MUST be True."
#
# If True:
# → test continues / passes
#
# If False:
# → AssertionError


# Example:
#
# assert 2 + 2 == 4       # pass
# assert 2 + 2 == 5       # fail


# 3. pytest automatically discovers test functions
# whose names start with:
#
# test_
#
# Example:
#
# def test_get_experience_level():
#     ...


# 4. A test should usually follow:
#
# ARRANGE
# → prepare input
#
# ACT
# → call the code being tested
#
# ASSERT
# → compare result with expectation


# Example:
#
# def test_mid_level_candidate():
#     # Arrange
#     candidate = {
#         "years_experience": 3,
#     }
#
#     # Act
#     result = get_experience_level(candidate)
#
#     # Assert
#     assert result == "Mid"


# 5. Why tests matter:
#
# Before:
# change code
# → manually run
# → visually inspect output
#
# With tests:
# change code
# → run pytest
# → tests automatically tell us what broke


# 6. Tests are especially useful for boundary conditions.
#
# Example:
#
# 1 year → Entry
# 2 years → Mid
# 4 years → Mid
# 5 years → Senior
#
# These boundaries are where bugs often happen.


# 7. Test functions normally do NOT need print().
#
# pytest reports pass/fail automatically.
#
# We care about:
#
# assert actual == expected


# ============================================================
# Main takeaway
# ============================================================
#
# production code:
# → does the work
#
# test code:
# → checks whether production code behaves correctly


def get_experience_level(years):
    if years >= 5:
        return "Senior"
    elif years >= 2:
        return "Mid"
    else:
        return "Entry"


def test_mid_candidate():
    result = get_experience_level(4)
    assert result == "Mid"


def test_senior_candidate():
    assert get_experience_level(6) == "Mid"
# “左边 actual、右边 expected”只是我们写 test 时常用的 convention： assert actual == expected

# @pytest.mark. parametrize Python decorator 功能 
import pytest

from candidate_logic import get_experience_level


@pytest.mark.parametrize(
    "years, expected",
    [
        (1, "Entry"),
        (2, "Mid"),
        (4, "Mid"),
        (5, "Senior"),
    ],
)
def test_experience_level(years, expected):
    actual = get_experience_level(years)

    assert actual == expected