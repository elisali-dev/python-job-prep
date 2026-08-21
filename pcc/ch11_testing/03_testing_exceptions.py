# 有些 function 的“正确行为”不是 return 某个 value，而是 应该 raise 某个 exception。那 test 怎么验证“它确实 raise 了正确的 exception”？
# 这时候用： pytest.raises(...)


# ============================================================
# Ch11 - 03 Testing Exceptions
# ============================================================

import pytest


# ------------------------------------------------------------
# 1. Sometimes the expected behavior IS an exception
# ------------------------------------------------------------

# Example production code:
#
# def validate_score(score):
#     if not 0 <= score <= 100:
#         raise ValueError(
#             "Score must be between 0 and 100."
#         )
#
#
# For score = 150, the correct behavior is:
#
# raise ValueError
#
# NOT:
# return False
# return None
# print("invalid")


# ------------------------------------------------------------
# 2. pytest.raises()
# ------------------------------------------------------------

# with pytest.raises(ValueError):
#     validate_score(150)
#
#
# This test PASSES only if code inside the with block
# raises ValueError.


# ------------------------------------------------------------
# 3. Why "with"?
# ------------------------------------------------------------

# pytest.raises(...) acts as a context manager.
#
# with pytest.raises(ValueError):
#     risky_call()
#
#
# pytest watches what happens inside the block.


# Flow:
#
# enter pytest.raises(ValueError)
#       ↓
# run function
#       ↓
# ValueError raised?
#
# YES → test passes
# NO  → test fails
#
# Wrong exception?
# → test fails


# ------------------------------------------------------------
# 4. Example
# ------------------------------------------------------------

# def validate_score(score):
#     if not 0 <= score <= 100:
#         raise ValueError("Invalid score")
#
#
# def test_invalid_score():
#     with pytest.raises(ValueError):
#         validate_score(150)


# ------------------------------------------------------------
# 5. No exception = failure
# ------------------------------------------------------------

# Suppose:
#
# with pytest.raises(ValueError):
#     validate_score(82)
#
#
# validate_score(82) does NOT raise.
#
# Therefore pytest reports:
#
# Failed: DID NOT RAISE <class 'ValueError'>


# ------------------------------------------------------------
# 6. Wrong exception = failure
# ------------------------------------------------------------

# If test expects:
#
# pytest.raises(ValueError)
#
# but code actually raises:
#
# KeyError
#
# then test fails.


# ------------------------------------------------------------
# 7. You can inspect the exception object
# ------------------------------------------------------------

# with pytest.raises(ValueError) as exc_info:
#     validate_score(150)
#
# print(exc_info.value)
#
# exc_info.value is the actual exception object.


# ------------------------------------------------------------
# 8. match= can check the message
# ------------------------------------------------------------

# with pytest.raises(
#     ValueError,
#     match="between 0 and 100",
# ):
#     validate_score(150)
#
#
# Now pytest checks BOTH:
#
# exception type
# +
# exception message


# ------------------------------------------------------------
# 9. Test valid and invalid behavior separately
# ------------------------------------------------------------

# Valid case:
#
# validate_score(82)
# → should NOT raise
#
#
# Invalid case:
#
# validate_score(150)
# → should raise ValueError
#
#
# Both behaviors matter.


# ------------------------------------------------------------
# Main takeaway
# ------------------------------------------------------------

# assert
# → verify returned/output behavior
#
# pytest.raises(...)
# → verify exception behavior