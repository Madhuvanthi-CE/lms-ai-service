# def summarize_text(req):
#     return {
#         "summary": "This is a dummy summary of the video content."
#     }

# from transformers import pipeline
# import whisper

# # Load models
# summarizer = pipeline("summarization", model="t5-small")
# whisper_model = whisper.load_model("base")

# def summarize_text(req):
#     text = req.transcript

#     # If video URL provided → convert to text
#     if req.video_url:
#         result = whisper_model.transcribe(req.video_url)
#         text = result["text"]

#     if not text:
#         return {"summary": "No input provided"}

#     # BART summary
#     summary = summarizer(text, max_length=120, min_length=40)

#     return {"summary": summary[0]['summary_text']}

# from transformers import pipeline
# import whisper
# import os

# # Load models
# summarizer = pipeline("summarization", model="t5-small")
# whisper_model = whisper.load_model("base")


# # 🔹 Split long text into chunks
# def chunk_text(text, max_len=500):
#     return [text[i:i+max_len] for i in range(0, len(text), max_len)]


# def summarize_text(req):
#     text = req.transcript

#     # -------------------------------
#     # 1️⃣ VIDEO → TEXT (WHISPER)
#     # -------------------------------
#     if req.video_url:
#         try:
#             if not os.path.exists(req.video_url):
#                 return {"summary": "Invalid video file path"}

#             result = whisper_model.transcribe(req.video_url)
#             text = result["text"]

#         except Exception as e:
#             return {"summary": f"Whisper error: {str(e)}"}

#     # -------------------------------
#     # 2️⃣ VALIDATION
#     # -------------------------------
#     if not text or len(text.strip()) == 0:
#         return {"summary": "No input provided"}

#     # -------------------------------
#     # 3️⃣ CHUNKING (IMPORTANT)
#     # -------------------------------
#     chunks = chunk_text(text)

#     summaries = []

#     for chunk in chunks:
#         try:
#             result = summarizer(
#                 chunk,
#                 max_length=100,
#                 min_length=30,
#                 do_sample=False
#             )
#             summaries.append(result[0]['summary_text'])
#         except:
#             continue

#     # -------------------------------
#     # 4️⃣ FINAL SUMMARY
#     # -------------------------------
#     final_summary = " ".join(summaries)

#     # Keep only ~3–5 sentences
#     sentences = final_summary.split(".")
#     final_summary = ". ".join(sentences[:5]).strip()

#     return {"summary": final_summary}

# from transformers import pipeline
# import os

# def summarize_text(req):
#     from transformers import pipeline   # ✅ lazy import
#     import whisper                      # ✅ lazy import

#     summarizer = pipeline("summarization")

# # 🔴 DO NOT LOAD HERE
# summarizer = None
# whisper_model = None


# # ✅ LOAD ONLY WHEN NEEDED
# def load_models():
#     global summarizer, whisper_model

#     if summarizer is None:
#         summarizer = pipeline("summarization", model="t5-small")

#     if whisper_model is None:
#         whisper_model = whisper.load_model("tiny")  # use tiny for Render


# # 🔹 Split long text into chunks
# def chunk_text(text, max_len=500):
#     return [text[i:i+max_len] for i in range(0, len(text), max_len)]


# def summarize_text(req):
#     load_models()  # ✅ IMPORTANT

#     text = req.transcript

#     # -------------------------------
#     # 1️⃣ VIDEO → TEXT (WHISPER)
#     # -------------------------------
#     if req.video_url:
#         try:
#             if not os.path.exists(req.video_url):
#                 return {"summary": "Invalid video file path"}

#             result = whisper_model.transcribe(req.video_url)
#             text = result["text"]

#         except Exception as e:
#             return {"summary": f"Whisper error: {str(e)}"}

#     # -------------------------------
#     # 2️⃣ VALIDATION
#     # -------------------------------
#     if not text or len(text.strip()) == 0:
#         return {"summary": "No input provided"}

#     # -------------------------------
#     # 3️⃣ CHUNKING
#     # -------------------------------
#     chunks = chunk_text(text)

#     summaries = []

#     for chunk in chunks:
#         try:
#             result = summarizer(
#                 chunk,
#                 max_length=100,
#                 min_length=30,
#                 do_sample=False
#             )
#             summaries.append(result[0]['summary_text'])
#         except:
#             continue

#     # -------------------------------
#     # 4️⃣ FINAL SUMMARY
#     # -------------------------------
#     final_summary = " ".join(summaries)

#     sentences = final_summary.split(".")
#     final_summary = ". ".join(sentences[:5]).strip()

#     return {"summary": final_summary}

# import os

# # 🔴 GLOBAL MODELS (initially empty)
# summarizer = None
# whisper_model = None


# # ✅ LOAD MODELS ONLY WHEN NEEDED
# def load_models():
#     global summarizer, whisper_model

#     if summarizer is None:
#         from transformers import pipeline
#         summarizer = pipeline("summarization", model="t5-small")

#     if whisper_model is None:
#         import whisper
#         whisper_model = whisper.load_model("tiny")  # lightweight


# # 🔹 Split long text
# def chunk_text(text, max_len=500):
#     return [text[i:i+max_len] for i in range(0, len(text), max_len)]


# # ✅ MAIN FUNCTION
# def summarize_text(req):
#     load_models()  # 🔥 MUST

#     text = req.transcript

#     # -------------------------------
#     # 1️⃣ VIDEO → TEXT
#     # -------------------------------
#     if req.video_url:
#         try:
#             if not os.path.exists(req.video_url):
#                 return {"summary": "Invalid video file path"}

#             result = whisper_model.transcribe(req.video_url)
#             text = result["text"]

#         except Exception as e:
#             return {"summary": f"Whisper error: {str(e)}"}

#     # -------------------------------
#     # 2️⃣ VALIDATION
#     # -------------------------------
#     if not text or len(text.strip()) == 0:
#         return {"summary": "No input provided"}

#     # -------------------------------
#     # 3️⃣ CHUNKING
#     # -------------------------------
#     chunks = chunk_text(text)

#     summaries = []

#     for chunk in chunks:
#         try:
#             result = summarizer(
#                 chunk,
#                 max_length=100,
#                 min_length=30,
#                 do_sample=False
#             )
#             summaries.append(result[0]['summary_text'])
#         except Exception:
#             continue

#     # -------------------------------
#     # 4️⃣ FINAL SUMMARY
#     # -------------------------------
#     final_summary = " ".join(summaries)

#     sentences = final_summary.split(".")
#     final_summary = ". ".join(sentences[:5]).strip()

#     return {"summary": final_summary}

from transformers import pipeline
import whisper
import os

# Load models
summarizer = pipeline("summarization", model="t5-small")
whisper_model = whisper.load_model("base")


# 🔹 Split long text into chunks
def chunk_text(text, max_len=500):
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]


def summarize_text(req):
    text = req.transcript

    # -------------------------------
    # 1️⃣ VIDEO → TEXT (WHISPER)
    # -------------------------------
    if req.video_url:
        try:
            if not os.path.exists(req.video_url):
                return {"summary": "Invalid video file path"}

            result = whisper_model.transcribe(req.video_url)
            text = result["text"]

        except Exception as e:
            return {"summary": f"Whisper error: {str(e)}"}

    # -------------------------------
    # 2️⃣ VALIDATION
    # -------------------------------
    if not text or len(text.strip()) == 0:
        return {"summary": "No input provided"}

    # -------------------------------
    # 3️⃣ CHUNKING (IMPORTANT)
    # -------------------------------
    chunks = chunk_text(text)

    summaries = []

    for chunk in chunks:
        try:
            result = summarizer(
                chunk,
                max_length=100,
                min_length=30,
                do_sample=False
            )
            summaries.append(result[0]['summary_text'])
        except:
            continue

    # -------------------------------
    # 4️⃣ FINAL SUMMARY
    # -------------------------------
    final_summary = " ".join(summaries)

    # Keep only ~3–5 sentences
    sentences = final_summary.split(".")
    final_summary = ". ".join(sentences[:5]).strip()

    return {"summary": final_summary}
