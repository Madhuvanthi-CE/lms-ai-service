# def generate_quiz(req):
#     return {
#         "questions": [
#             {
#                 "question": "What is Python?",
#                 "options": ["Programming Language", "Snake", "Game", "OS"],
#                 "answer": "Programming Language"
#             }
#         ]
#     }

import re
from pydantic import BaseModel
from typing import List
import random

class QuizRequest(BaseModel):
    session_transcript: str


def generate_options(correct):
    distractors = [
        "To display UI",
        "To design hardware",
        "To run games",
        "To store images"
    ]

    options = random.sample(distractors, 3)
    options.append(correct)
    random.shuffle(options)

    return options


def generate_quiz(req: QuizRequest):
    text = req.session_transcript.lower()

    sentences = re.split(r'[.?!]', text)

    questions = []

    for sentence in sentences:
        sentence = sentence.strip()

        # IoT pattern
        if "sensor" in sentence and "data" in sentence:
            q = "What is the role of sensors in IoT?"
            ans = "Sensors collect data from the environment"

            questions.append({
                "question": q,
                "options": generate_options(ans),
                "answer": ans
            })

        if "cloud" in sentence:
            q = "What is the role of cloud in IoT?"
            ans = "Cloud stores and processes data"

            questions.append({
                "question": q,
                "options": generate_options(ans),
                "answer": ans
            })

        if "iot" in sentence:
            q = "What is IoT?"
            ans = "IoT is a network of connected devices"

            questions.append({
                "question": q,
                "options": generate_options(ans),
                "answer": ans
            })

    # fallback if nothing detected
    if not questions:
        questions.append({
            "question": "What is the main idea of the given content?",
            "options": generate_options("It explains a technical concept"),
            "answer": "It explains a technical concept"
        })

    return {"questions": questions[:5]}