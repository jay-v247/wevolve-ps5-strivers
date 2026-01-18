import json

with open("skill_taxonomy.json") as f:
    TAXONOMY = json.load(f)

def analyze_skills(current_skills, required_skills):
    matching = [s for s in required_skills if s in current_skills]
    missing = [s for s in required_skills if s not in current_skills]

    gap = int((len(missing) / len(required_skills)) * 100)
    readiness = 100 - gap

    months = 0
    for skill in missing:
        for category in TAXONOMY.values():
            if skill in category:
                months += category[skill]["months"]

    return {
        "matching_skills": matching,
        "missing_skills": missing,
        "skill_gap_percentage": gap,
        "readiness_score": readiness,
        "estimated_learning_time_months": round(months, 1)
    }
