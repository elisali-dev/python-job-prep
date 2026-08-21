import pytest

from candidate_processor import (
    validate_candidate,
    get_experience_level,
    is_qualified,
    build_report,
)


# 因为 pytest fixture 默认是 function scope：pytest 每运行一个 test function，都会重新 call 一次 candidate()，创建一个新的 dict。
# 所以每一个 test 都 get 一个 fresh copy of candidate dict
@pytest.fixture
def candidate():
    return {
        "name": "Alex",
        "years_experience": 3,
        "technical_score": 82,
    }

# test 1 
def test_get_experience_level(candidate):
    assert get_experience_level(candidate) == "Mid"

#test 2 
def test_is_qualified(candidate):
    assert is_qualified(candidate) is True

#test 3 
def test_validate_candidate_raises_value_error(candidate):
    # NOTE 这个不是copy, 是aliasing!它们指代同一个dict object 
    # NOTE 如果想要 modified copy,用 cand_b = candidate.copy() 
    cand_b = candidate
    cand_b["technical_score"] = 150
    with pytest.raises(ValueError):
        validate_candidate(cand_b)

#test 4 
def test_validate_candidate_raises_key_error(candidate):
    cand_b = candidate
    del cand_b["years_experience"]
    with pytest.raises(KeyError):
        validate_candidate(cand_b)

# test 5 
def test_build_report(candidate):
    report = build_report([candidate])
    # 测试整个 output contract：
    assert len(report) == 1
    assert report[0]["name"] == "Alex"
    assert report[0]["experience_level"] == "Mid"
    assert report[0]["technical_score"] == 82
    assert report[0]["decision"] == "Pass"
    # 一个 test 里面有多个 assert 完全没问题，因为这些 asserts 都是在验证同一个 behavior：



###### KEY TAKEAWAY #############

# # fixture
# → reusable test setup
# → 默认每个 test 得到 fresh instance/data
# 
# candidate.copy()
# → 明确创建 bad test data
# → 不修改原始 fixture object
# 
# pytest.raises()
# → assert exception behavior
# 
# multiple asserts
# → 可以共同验证一个 output contract