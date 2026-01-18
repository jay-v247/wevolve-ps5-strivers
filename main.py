from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

from models import GapRequest
from utils import analyze_skills
from roadmap import generate_roadmap

app = FastAPI(title="Skill Gap Analysis Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("career_trajectories.json") as f:
    CAREERS = json.load(f)

with open("salary_data.json") as f:
    SALARY = json.load(f)

@app.post("/analyze")
def analyze(data: GapRequest):
    analysis = analyze_skills(
        data.candidate.current_skills,
        data.target_role.required_skills
    )

    roadmap = generate_roadmap(analysis["missing_skills"])

    trajectory = CAREERS.get(data.target_role.title, [])

    salary_projection = {
        "current_role": SALARY.get(data.candidate.current_role, "N/A"),
        "target_role": SALARY.get(data.target_role.title, "N/A"),
        "next_role": SALARY.get(trajectory[0], "N/A") if trajectory else "N/A"
    }

    visualization = {
        "radar_chart": {
            "current": {
                "Frontend": 1,
                "Backend": 4,
                "Database": 3,
                "DevOps": 1
            },
            "required": {
                "Frontend": 4,
                "Backend": 4,
                "Database": 4,
                "DevOps": 4
            }
        }
    }

    alternative_roles = []
    if analysis["readiness_score"] < 30:
        alternative_roles = [
            "Backend Engineer",
            "Cloud Engineer",
            "DevOps Engineer"
        ]

    industry_trends = {
        "2025_trending_skills": [
            "Cloud Computing",
            "System Design",
            "DevOps"
        ]
    }

    return {
        "analysis": analysis,
        "learning_roadmap": roadmap,
        "career_trajectory": trajectory,
        "salary_projection": salary_projection,
        "visualization": visualization,
        "alternative_roles": alternative_roles,
        "industry_trends": industry_trends
    }
