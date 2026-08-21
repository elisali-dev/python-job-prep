# ============================================================
# Ch11 - 02 Testing Functions
# ============================================================


# ------------------------------------------------------------
# 1. Good tests cover different categories
# ------------------------------------------------------------

# NORMAL CASE
# → typical input
#
# Example:
# years = 3
# → Mid


# BOUNDARY CASE
# → value right at / around a rule boundary
#
# Example:
#
# 1 → Entry
# 2 → Mid
# 4 → Mid
# 5 → Senior


# INVALID CASE
# → input violates the function's contract
#
# Example:
# years = -1
#
# Whether this should raise an exception depends on
# how the production function is designed.


# ------------------------------------------------------------
# 2. Boundary tests are especially valuable
# ------------------------------------------------------------

# Rule:
#
# if years >= 5:
#     return "Senior"
#
#
# Testing only:
#
# years = 6
#
# would NOT catch this bug:
#
# if years > 5:
#
#
# But:
#
# years = 5
#
# catches it immediately.


# ------------------------------------------------------------
# 3. parametrize = same behavior, many data cases
# ------------------------------------------------------------

# @pytest.mark.parametrize(
#     "input, expected",
#     [
#         (...),
#         (...),
#     ],
# )
#
# pytest runs the same test once for each row.


# ------------------------------------------------------------
# 4. The parameter names must match the test function
# ------------------------------------------------------------

# @pytest.mark.parametrize(
#     "years, expected",
#     [...]
# )
#
# def test_experience_level(years, expected):
#     ...
#
#
# pytest injects values into:
#
# years
# expected


# ------------------------------------------------------------
# 5. Keep production code separate from test code
# ------------------------------------------------------------

# candidate_logic.py
# → code that does the work
#
# test_candidate_logic.py
# → code that checks the work


# ------------------------------------------------------------
# 6. Tests should be deterministic
# ------------------------------------------------------------

# Same input
# → same expected result
#
# A test should not depend on:
#
# random manual input
# current user interaction
# visual inspection


# ------------------------------------------------------------
# 7. Test behavior, not implementation details
# ------------------------------------------------------------

# Good:
#
# assert get_experience_level(5) == "Senior"
#
#
# Less useful:
#
# checking exactly how many if-statements
# the function contains
#
#
# We care about:
#
# input → behavior/output