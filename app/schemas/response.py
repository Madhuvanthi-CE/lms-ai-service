# from pydantic import BaseModel
# from typing import List

# class RecommendResponse(BaseModel):
#     course_ids: List[str]

# class SummarizeResponse(BaseModel):
#     summary: str

# class SkillGapResponse(BaseModel):
#     gaps: List[str]
#     recommended_courses: List[str]

# class MCQ(BaseModel):
#     question: str
#     options: List[str]
#     answer: str

# class QuizResponse(BaseModel):
#     questions: List[MCQ]

from pydantic import BaseModel
from typing import List

# -------------------------------
# T1 – RECOMMEND
# -------------------------------
class RecommendResponse(BaseModel):
    course_ids: List[str]

# -------------------------------
# T2 – SUMMARIZE
# -------------------------------
class SummarizeResponse(BaseModel):
    summary: str

# -------------------------------
# T3 – SKILL GAP (FIXED)
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
# T4 – QUIZ
# -------------------------------
class MCQ(BaseModel):
    question: str
    options: List[str]
    answer: str

class QuizResponse(BaseModel):
    questions: List[MCQ]