# import warnings
# from fastapi import FastAPI

# # Suppress the deprecated resume_download FutureWarning from huggingface_hub
# warnings.filterwarnings("ignore", message=".*resume_download.*")

# from app.schemas.request import *
# from app.schemas.response import *

# from app.models.recommend import recommend_courses
# from app.models.summarize import summarize_text
# from app.models.skill_gap import analyze_skill_gap
# from app.models.quiz import generate_quiz
# from app.models.skill_gap import analyze_skill_gap, SkillGapRequest, SkillGapResponse


# app = FastAPI(title="LMS AI Service", version="1.0")

# @app.get("/health")
# def health():
#     return {"status": "ok", "version": "1.0"}

# @app.post("/recommend", response_model=RecommendResponse)
# def recommend(req: RecommendRequest):
#     return recommend_courses(req)

# @app.post("/summarize", response_model=SummarizeResponse)
# def summarize(req: SummarizeRequest):
#     return summarize_text(req)

# @app.post("/skill-gap", response_model=SkillGapResponse)
# def skill_gap(req: SkillGapRequest):
#     return analyze_skill_gap(req)
# # @app.post("/skill-gap", response_model=SkillGapResponse)
# # def skill_gap(req: SkillGapRequest):
# #     return analyze_skill_gap(req)

# # @app.post("/skill-gap", response_model=SkillGapResponse)
# # def skill_gap(req: SkillGapRequest):
# #     return analyze_skill_gap(req)

# @app.post("/generate-quiz", response_model=QuizResponse)
# def quiz(req: QuizRequest):
#     return generate_quiz(req)

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware

# # Import all features
# from app.models.recommend import recommend_courses, RecommendRequest
# from app.models.summarize import summarize_text, SummarizeRequest
# from app.models.skill_gap import analyze_skill_gap, SkillGapRequest, SkillGapResponse
# from app.models.quiz import generate_quiz, QuizRequest

# app = FastAPI(title="LMS AI Service", version="1.0")

# # -------------------------------
# # CORS (VERY IMPORTANT for MERN)
# # -------------------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # change later if needed
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------------------
# # HEALTH CHECK
# # -------------------------------
# @app.get("/health")
# def health():
#     return {"status": "ok", "version": "1.0"}

# # -------------------------------
# # T1 – RECOMMEND
# # -------------------------------
# @app.post("/recommend")
# def recommend(req: RecommendRequest):
#     try:
#         return recommend_courses(req)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # -------------------------------
# # T2 – SUMMARIZE
# # -------------------------------
# @app.post("/summarize")
# def summarize(req: SummarizeRequest):
#     try:
#         return summarize_text(req)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # -------------------------------
# # T3 – SKILL GAP
# # -------------------------------
# @app.post("/skill-gap", response_model=SkillGapResponse)
# def skill_gap(req: SkillGapRequest):
#     try:
#         return analyze_skill_gap(req)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # -------------------------------
# # T4 – QUIZ
# # -------------------------------
# @app.post("/generate-quiz")
# def quiz(req: QuizRequest):
#     try:
#         return generate_quiz(req)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import warnings
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Suppress warnings (optional)
warnings.filterwarnings("ignore", message=".*resume_download.*")

# -------------------------------
# IMPORT REQUEST & RESPONSE MODELS
# -------------------------------
from app.schemas.request import (
    RecommendRequest,
    SummarizeRequest,
    SkillGapRequest,
    QuizRequest
)

from app.schemas.response import (
    RecommendResponse,
    SummarizeResponse,
    SkillGapResponse,
    QuizResponse
)

# -------------------------------
# IMPORT MODEL LOGIC
# -------------------------------
from app.models.recommend import recommend_courses
from app.models.summarize import summarize_text
from app.models.skill_gap import analyze_skill_gap
from app.models.quiz import generate_quiz

# -------------------------------
# CREATE APP
# -------------------------------
app = FastAPI(title="LMS AI Service", version="1.0")

# -------------------------------
# ENABLE CORS (IMPORTANT)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for MERN)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# HEALTH CHECK
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}


# -------------------------------
# T1 – RECOMMEND
# -------------------------------
@app.post("/recommend", response_model=RecommendResponse)
def recommend(req: RecommendRequest):
    try:
        return recommend_courses(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
# T2 – SUMMARIZE
# -------------------------------
@app.post("/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest):
    try:
        return summarize_text(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
# T3 – SKILL GAP
# -------------------------------
@app.post("/skill-gap", response_model=SkillGapResponse)
def skill_gap(req: SkillGapRequest):
    try:
        return analyze_skill_gap(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
# T4 – QUIZ
# -------------------------------
@app.post("/generate-quiz", response_model=QuizResponse)
def quiz(req: QuizRequest):
    try:
        return generate_quiz(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/")
def home():
    return {"message": "LMS AI Service is running"}

