

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

#     # return {"summary": final_summary}
