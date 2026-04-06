# from pydantic import BaseModel
# from typing import List, Optional

# class RecommendRequest(BaseModel):
#     student_id: str
#     watch_history: List[str]

# class SummarizeRequest(BaseModel):
#     video_url: Optional[str] = None
#     transcript: Optional[str] = None

# class SkillGapRequest(BaseModel):
#     completed_topics: List[str]

# class QuizRequest(BaseModel):
#     session_transcript: str

from pydantic import BaseModel
from typing import List, Optional

# -------------------------------
# T1 – RECOMMEND
# -------------------------------
class RecommendRequest(BaseModel):
    student_id: str
    watch_history: List[str]

# -------------------------------
# T2 – SUMMARIZE
# -------------------------------
class SummarizeRequest(BaseModel):
    video_url: Optional[str] = None
    transcript: Optional[str] = None

# -------------------------------
# T3 – SKILL GAP
# -------------------------------
class SkillGapRequest(BaseModel):
    completed_topics: List[str]

# -------------------------------
# T4 – QUIZ
# -------------------------------
class QuizRequest(BaseModel):
    session_transcript: str