#一个绿色的 test 只能证明它实际检查到的 behavior，不代表整段程序“全都正确”。
# pytest test_candidate_logic.py -v
# NOTE 如果没有 -v 那么 pytest 就用 compact mode 然后输出是............. 一个dot 代表一个 test case PASSED; 如果想看到名字就得 用 -v
from candidate_logic import get_experience_level, is_qualified, validate_score

import pytest

@pytest.mark.parametrize(
    "years, expected",
    [
        (1, "Entry"),
        (2, "Mid"),
        (4, "Mid"),
        (5, "Senior"),
        (6, "Senior"),
    ],
)
def test_experience_level(years, expected):
    actual = get_experience_level(years)
    assert actual == expected


# fixture 解决的问题是 多个 tests 都需要相同的 setup data , 
@pytest.fixture
def candidate():
    return {
        "name": "Alex",
        "years_experience": 3,
        "technical_score": 82,
    }


def test_candidate_is_qualified(candidate):
    assert is_qualified(
        candidate["years_experience"],
        candidate["technical_score"],
    ) is True


def test_candidate_name(candidate):
    assert candidate["name"] == "Alex"




@pytest.mark.parametrize(
    "years, score, expected",
    [
        (3, 82, True),    # normal pass
        (2, 75, True),    # both exactly at boundary
        (1, 90, False),   # experience too low
        (3, 74, False),   # score too low
        (1, 74, False),   # both too low
    ],
)
def test_is_qualified(years, score, expected):
    actual = is_qualified(years, score)

    assert actual is expected



def test_invalid_score_raises_value_error():
    with pytest.raises(ValueError):
        validate_score(150)
        validate_score(82) # 这个不会执行,因为一旦上面的 150 raise ValueError, python会立刻离开当前正常执行路径, ytest.raises() 捕获这个 exception，然后退出 with block。
#一个绿色的 test 只能证明它实际检查到的 behavior，不代表整段程序“全都正确”。

 # 例如你想测试很多 invalid scores：
@pytest.mark.parametrize(
        "score",
        [
            -100, 
            -1,
            101,
            150,
            1000,
        ]
)
def test_invalid_score_raises_value_error(score):
    with pytest.raises(ValueError):
        validate_score(score)


# 也可以先生成 test data , 再传进 decorator 
invalid_scores = [-100, -1, 101, 150, 1000]
# 也可以用list comprehension
invalid_scores = [score for score in range(101, 106)]

@pytest.mark.parametrize("score", invalid_scores)
def test_invalid_score_raises_value_error(score):
    with pytest.raises(ValueError):
        validate_score(score)

# ============================================================
# get_experience_level()
# ============================================================


# NOTE Q: why only one assert in one test function 
# Answer: 在 pytest 测试函数中，你可以根据需要写任意多个 assert 语句。但是当某一个 assert 失败时，函数会立即停止执行并报错，后面的 assert 不会被执行。

def test_entry_level():
    assert get_experience_level(1) == "Entry"

def test_mid_lower_boundary():
    assert get_experience_level(2) == "Mid"    

def test_mid_upper_boundary():
    assert get_experience_level(4) == "Mid"

def test_senior_boundary():
    assert get_experience_level(5) == "Senior"


# ============================================================
# is_qualified()
# ============================================================

def test_qualified_candidate():
    assert is_qualified(3, 82) is True


def test_experience_boundary():
    assert is_qualified(2, 75) is True


def test_not_enough_experience():
    assert is_qualified(1, 90) is False


def test_score_below_boundary():
    assert is_qualified(3, 74) is False
    # 也可以写成 assert is_qualified(3, 82) == True
    # 也可以(更常见) assert is_qualified(3, 82)


# tests 不只是告诉你“程序坏了”，还能很快缩小到哪一个 behavior 被你改坏了。

# Normal case
# → 普通典型数据
# → years=3
# 
# Boundary case
# → rule 改变的边界
# → years=1 / 2 / 4 / 5
# 
# Invalid/error case
# → 不合法输入
# → 下一节 test exceptions