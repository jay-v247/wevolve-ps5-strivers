from pydantic import BaseModel
from typing import List

class Candidate(BaseModel):
    name: str
    current_role: str
    current_skills: List[str]
    experience_years: int
    education: str


class TargetRole(BaseModel):
    title: str
    required_skills: List[str]
    typical_experience: str

class GapRequest(BaseModel):
    candidate: Candidate
    target_role: TargetRole
