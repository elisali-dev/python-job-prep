def format_candidate_report(candidate:dict[str,str|int|float|list[str]], evaluation:dict[str,str|set[str]]) -> str:
    matched_skills = evaluation["matched_skills"]

    if matched_skills:
        matched_skills_text = ", ".join(matched_skills)
    else:
        matched_skills_text = "None"

    return (
        f"Candidate: {candidate['name']}\n"
        f"Experience: {candidate['years_experience']} years\n"
        f"Level: {evaluation['experience_level']}\n"
        f"Technical Score: {candidate['technical_score']}\n"
        f"Matched Skills: {matched_skills_text}\n"
        f"Decision: {evaluation['decision']}"
    )