candidates = ["alice", "bob", "charlie", "david", "emma"]

print(candidates[:3])
print(candidates[-2:])

backup_candidates = candidates.copy()

backup_candidates.append("frank")

print(f"Original: {candidates}")
print(f"Backup: {backup_candidates}")
