candidates = ["charlie", "alice", "david", "bob"]

print(f"Original: {candidates}")

alpha_cand = sorted(candidates)
print(f"Alphabetical: {alpha_cand}")

print(f"Original still: {candidates}")

candidates.reverse()
print(f"Resverse original oder: {candidates}")

print(f"Number of candidates: {len(candidates)}")