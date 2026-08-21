from pathlib import Path
import json

def load_candidates(path):
    """
    Read JSON file and return Python candidate data.
    """
    with open(path, "r", encoding = "utf-8") as file:
            return json.load(file)




def validate_candidate(candidate):
    """
    Validate required fields and values.
    """
    exp = candidate["years_experience"]
    score = candidate["technical_score"]
    _ = candidate["name"]  # 只是为了触发可能存在的 KeyError
    if not (exp >= 0 and 0 <= score <= 100):
        raise ValueError("Business rule invalid: years_experience must be >= 0 and technical_score must be between 0 and 100")



def get_experience_level(candidate):
    years = candidate["years_experience"]

    if years >= 5:
        return "Senior"
    elif years >= 2:
        return "Mid"
    else:
        return "Entry"
    


def is_qualified(candidate):
    return candidate["years_experience"] >=2 and candidate["technical_score"] >= 75 

def build_report(candidates):
    report = []

    for candidate in candidates:
        validate_candidate(candidate)
        name = candidate["name"]
        experience_level = get_experience_level(candidate)
        score = candidate["technical_score"]
        report_record = {
            "name": name,
            "experience_level": experience_level,
            "technical_score": score
        } 
        if is_qualified(candidate):
            report_record["decision"] = "Pass"
        else:
            report_record["decision"] = "Reject"
        report.append(report_record)

    return report 

    
def save_report(report, path):
    with path.open("w",encoding="utf-8") as file:
        json.dump(report, file,indent=4)
