scores = [82, 91, 76, 95, 88]

for score in scores:
    print(f"Score: {score}")

print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Total: {sum(scores)}")

# confirm orignal list doesn't change
print(scores)

doubled_scores = []
for score in scores:
    doubled_scores.append(score * 2)
print(doubled_scores)


doubled_scores_v2 = [score * 2 for score in scores]
print (doubled_scores_v2)

