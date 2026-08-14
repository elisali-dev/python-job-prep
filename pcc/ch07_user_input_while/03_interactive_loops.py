# NOTE 常见truthiness 
bool([])     # False
bool("")     # False
bool(0)      # False

bool([1])    # True
bool("abc")  # True
bool(5)      # True
# NOTE 
# candidates =[]
# if not candidates: # True 如果 candidates 是 empty这个就是 True。 这个以后非常常见


# ================ Exercise 3  ==================== 
print(f"\n{'=' * 20} Exercise 3 {'=' * 20}")

candidates = []
while True:
    candidate_name = input("Candidate name: ")
    if candidate_name == "quit":
        break
    score = int(input("Score: "))
    candidate = {
        "name": candidate_name,
        "score": score
    }
    candidates.append(candidate)

print(candidates)


# ================ Exercise 5 ==================== 
print(f"\n{'=' * 20} Exercise {'=' * 20}")

# ================ Exercise 6 ==================== 
print(f"\n{'=' * 20} Exercise 4 — Break {'=' * 20}")


# ================ Closed Book Drill ==================== 
print(f"\n{'=' * 20} Drill {'=' * 20}")
