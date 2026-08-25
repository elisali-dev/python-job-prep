import csv


def load_candidates(filename):
    candidates = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            candidate = {
                "name": row["name"].strip(),
                "years_experience": float(
                    row["years_experience"]
                ),
                "technical_score": int(
                    row["technical_score"]
                ),
                "skills": [
                    skill.strip()
                    for skill in row["skills"].split("|")
                    if skill.strip()
                ],
            }

            candidates.append(candidate)

    return candidates


def save_report(report_text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report_text)