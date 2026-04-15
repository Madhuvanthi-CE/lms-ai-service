# 🚀 LMS AI Service

A FastAPI-based microservice that provides AI-powered features for a Learning Management System (LMS). This service handles recommendation, skill analysis, and quiz generation for engineering students.

---

## 🔹 Features

### ✅ Course Recommendation

* Suggests top 5 courses based on student watch history

### ✅ Skill Gap Analyzer

* Identifies missing skills across domains like Web, DSA, AI/ML, etc.

### ✅ Quiz Generator

* Generates MCQs from session transcripts using NLP

### ⚠️ Video Summarizer (Local Only)

* Uses Whisper + T5/BART
* Not deployed due to memory limitations (works locally)

---

## 🔹 Tech Stack

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic
* scikit-learn
* KeyBERT / NLP

---

## 🔹 GitHub Repository

👉 https://github.com/Madhuvanthi-CE/lms-ai-service

---

## 🔹 Live Deployment

👉 https://lms-ai-service-1.onrender.com
👉 https://lms-ai-service-1.onrender.com/docs

---

## 🔹 API Endpoints

| Endpoint         | Method | Description           |
| ---------------- | ------ | --------------------- |
| `/health`        | GET    | Check service status  |
| `/recommend`     | POST   | Course recommendation |
| `/skill-gap`     | POST   | Skill gap analysis    |
| `/generate-quiz` | POST   | Quiz generation       |

---

## 🔹 How to Test APIs

1. Open:
   👉 https://lms-ai-service-1.onrender.com/docs

2. Select any endpoint

3. Click **"Try it out"**

4. Enter input JSON

5. Click **Execute**

---

### 🔹 Sample Inputs

#### ▶ Recommend

```json
{
  "student_id": "S1",
  "watch_history": ["web", "python"]
}
```

#### ▶ Skill Gap

```json
{
  "completed_topics": ["html", "css"]
}
```

#### ▶ Quiz

```json
{
  "session_transcript": "FastAPI is used to build APIs in Python"
}
```

---

## 🔹 Why Summarizer Not Deployed

* Uses heavy models (Whisper + T5/BART)
* Render free tier memory limit ≈ 512MB
* Causes:

  * Out of memory errors
  * Deployment crashes

👉 So summarizer is **disabled in deployment**

---

## 🔹 Run Locally (All Features Including Summarizer)

### 1. Clone Repo

```bash
git clone https://github.com/Madhuvanthi-CE/lms-ai-service
cd lms-ai-service
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Server

```bash
uvicorn app.main:app --reload
```

---

### 5. Open Swagger

```bash
http://127.0.0.1:8000/docs
```



## 🔹 Project Structure

```bash
app/
 ├── main.py
 ├── models/
 ├── schemas/
 ├── routes/
notebooks/
requirements.txt
README.md


## 🔹 Future Improvements

* Deploy summarizer on GPU server
* Improve recommendation model
* Add frontend integration
* Real-time analytics



## 🔹 Status

✔ API Developed
✔ Deployed Successfully
✔ Swagger Working
✔ Core Features Working
✔ Summarizer Works Locally



## 🎯 Conclusion

This project successfully delivers an AI-powered backend service for LMS platforms. While deployment limitations restrict heavy models, the system is fully functional and scalable.

