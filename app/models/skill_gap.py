# def analyze_skill_gap(req):
#     return {
#         "gaps": ["DSA", "Machine Learning"],
#         "recommended_courses": ["c201", "c202"]
#     }

# skill_tree = {
#     "Web": ["HTML", "CSS", "JavaScript"],
#     "DSA": ["Arrays", "Trees", "Graphs"],
#     "AI": ["ML", "DL", "NLP"],
#     "DevOps": ["Docker", "CI/CD"]
# }

# def analyze_skill_gap(req):
#     completed = set(req.completed_topics)

#     gaps = []
#     recommendations = []

#     for domain, skills in skill_tree.items():
#         missing = [s for s in skills if s not in completed]

#         if missing:
#             gaps.extend(missing)
#             recommendations.append(f"{domain} course")

#     return {
#         "gaps": gaps,
#         "recommended_courses": recommendations
#     }

# skill_tree = {
#     "Web": ["html", "css", "javascript"],
#     "DSA": ["arrays", "trees", "graphs"],
#     "AI/ML": ["machine learning", "deep learning", "nlp"],
#     "DevOps": ["docker", "ci/cd"],
#     "Systems": ["os", "networking"]
# }

# def analyze_skill_gap(req):
#     # 🔹 Normalize input
#     completed = set([t.lower() for t in req.completed_topics])

#     gap_report = []
#     recommended_courses = []

#     for domain, skills in skill_tree.items():
#         missing = [s for s in skills if s not in completed]

#         if missing:
#             gap_report.append({
#                 "domain": domain,
#                 "missing_skills": missing
#             })

#             # smarter recommendation
#             recommended_courses.append({
#                 "domain": domain,
#                 "course": f"{domain} Fundamentals"
#             })

#     return {
#         "gaps": gap_report,
#         "recommended_courses": recommended_courses
#     }

from pydantic import BaseModel
from typing import List

def analyze_skill_gap(req):
    from sklearn...   # ✅ lazy import

# -------------------------------
# 1️⃣ SKILL TREE (STANDARD)
# -------------------------------
skill_tree = {
    "Web": ["html", "css", "javascript"],
    "DSA": ["arrays", "trees", "graphs"],
    "AI/ML": ["machine learning", "deep learning", "nlp"],
    "DevOps": ["docker", "ci/cd"],
    "Systems": ["os", "networking"]
}


# -------------------------------
# 2️⃣ REQUEST MODEL
# -------------------------------
class SkillGapRequest(BaseModel):
    completed_topics: List[str]


# -------------------------------
# 3️⃣ RESPONSE MODELS
# -------------------------------
class GapItem(BaseModel):
    domain: str
    missing_skills: List[str]


class CourseItem(BaseModel):
    domain: str
    course: str


class SkillGapResponse(BaseModel):
    gaps: List[GapItem]
    recommended_courses: List[CourseItem]


# -------------------------------
# 4️⃣ MAIN LOGIC
# -------------------------------
def analyze_skill_gap(req: SkillGapRequest):
    # Normalize input (case-insensitive)
    completed = set([t.lower().strip() for t in req.completed_topics])

    gaps = []
    recommended_courses = []

    for domain, skills in skill_tree.items():
        missing_skills = [s for s in skills if s not in completed]

        if missing_skills:
            gaps.append({
                "domain": domain,
                "missing_skills": missing_skills
            })

            recommended_courses.append({
                "domain": domain,
                "course": f"{domain} Fundamentals Course"
            })

    return {
        "gaps": gaps,
        "recommended_courses": recommended_courses
    }
