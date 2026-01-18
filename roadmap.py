import json

with open("skill_taxonomy.json") as f:
    TAXONOMY = json.load(f)

def generate_roadmap(missing_skills):
    roadmap = []
    phase = 1

    for category, skills in TAXONOMY.items():
        needed_skills = [s for s in missing_skills if s in skills]

        if needed_skills:
            duration = sum(skills[s]["months"] for s in needed_skills)
            roadmap.append({
                "phase": phase,
                "duration_months": round(duration, 1),
                "focus": category,
                "skills_to_learn": needed_skills,
                "priority": "High",
                "reasoning": "Required for Senior Full Stack role"
            })
            phase += 1

    return roadmap
