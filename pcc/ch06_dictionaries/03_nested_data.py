# ================ Exercise 1 — dictionary containing list  ===================== 
print(f"\n{'=' * 20} Exercise 1 — dictionary containing list {'=' * 20}")

employee = {
    "name": "Emma",
    "skills": ["python", "sql", "git"],
}

print(employee["name"])
print(employee["skills"][0])
print(employee["skills"][-1])

for skill in employee["skills"]:
    print(f"Skill: {skill}")

# ================ Exercise 2 — dictionary containing dictionary ===================== 
print(f"\n{'=' * 20} Exercise 2 — dictionary containing dictionary {'=' * 20}")

candidate = {
    "name": "Alex",
    "contact": {
        "email": "alex@example.com",
        "city": "Detroit",
    },
}
# 输出：
# Name: Alex
# Email: alex@example.com
# City: Detroit
# 要求都从 nested dictionary 里取。
print (f"Name: {candidate["name"]}")
print (f"Email: {candidate["contact"]["email"]}")
print(f"City: {candidate["contact"]["city"]}")

# ================ Exercise 3 — list of dictionaries ===================== 
print(f"\n{'=' * 20} Exercise 3 — list of dictionaries {'=' * 20}")

candidates = [
    {
        "name": "Alex",
        "score": 82,
    },
    {
        "name": "Emma",
        "score": 94,
    },
    {
        "name": "Sam",
        "score": 76,
    },
]

for candidate in candidates:
    print(f"{candidate["name"]}: {candidate["score"]}")


# ================ Exercise 4 — condition inside loop ===================== 
print(f"\n{'=' * 20} Exercise 4 — condition inside loop {'=' * 20}")

for candidate in candidates:
    if candidate["score"] >= 80:
        print(f"{candidate["name"]} passes")

# ================ Exercise 5 — nested ML data ===================== 
print(f"\n{'=' * 20} Exercise 5 — nested ML data {'=' * 20}")

training_run = {
    "model": "transformer",
    "config": {
        "epochs": 20,
        "batch_size": 32,
        "device": "cuda",
    },
    "metrics": {
        "accuracy": 0.91,
        "loss": 0.22,
    },
}

print(f"Model: {training_run.get("model","Not recorded")}")
print(f"Epochs: {training_run['config']["epochs"]}")
print(f"Device: {training_run['config']["device"]}")
print(f"Accuracy: {training_run['metrics']["accuracy"]}")
#BUG 典型的 copy/paste bug
# print(f"Accuracy: {training_run['metrics']["loss"]}")
print(f"Loss: {training_run['metrics']["loss"]}")

# ================ Exercise 6 — loop inner dictionary ===================== 
print(f"\n{'=' * 20} Exercise 6 — loop inner dictionary {'=' * 20}")

for key, val in training_run["metrics"].items():
    print(f"{key}: {val}")


# ================ Exercise 7 — list inside dictionary + condition ===================== 
print(f"\n{'=' * 20} Exercise 7 — list inside dictionary + condition {'=' * 20}")

candidate = {
    "name": "Alex",
    "skills": ["python", "sql", "pytorch", "git"],
}

requirements = ["python", "pytorch", "docker"]

for requirement in requirements:
    if requirement in candidate["skills"]:
        print(f"Has {requirement}")



