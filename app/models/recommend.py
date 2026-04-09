# def recommend_courses(req):
#     return {
#         "course_ids": ["c101", "c102", "c103", "c104", "c105"]
#     }

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# model = SentenceTransformer('all-MiniLM-L6-v2')

# courses = {
#     "c1": "Python programming basics",
#     "c2": "Data structures and algorithms",
#     "c3": "Machine learning introduction",
#     "c4": "Web development with React",
#     "c5": "Docker and DevOps"
# }

# def recommend_courses(req):
#     watched = req.watch_history

#     course_ids = list(courses.keys())
#     course_texts = list(courses.values())

#     embeddings = model.encode(course_texts)

#     watched_texts = [courses[c] for c in watched if c in courses]

#     if not watched_texts:
#         return {"course_ids": course_ids[:5]}

#     user_vector = np.mean(model.encode(watched_texts), axis=0)

#     similarities = cosine_similarity([user_vector], embeddings)[0]

#     ranked = sorted(zip(course_ids, similarities),
#                     key=lambda x: x[1],
#                     reverse=True)

#     top5 = [cid for cid, _ in ranked if cid not in watched][:5]

#     return {"course_ids": top5}


# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# model = SentenceTransformer('all-MiniLM-L6-v2')

# # 🔹 Course metadata
# courses = {
#     "c1": "Python programming basics",
#     "c2": "Data structures and algorithms",
#     "c3": "Machine learning introduction",
#     "c4": "Web development with React",
#     "c5": "Docker and DevOps"
# }

# course_ids = list(courses.keys())
# course_texts = list(courses.values())
# course_embeddings = model.encode(course_texts)


# # 🔹 Dummy user interaction data (collaborative)
# user_data = {
#     "u1": {"c1": 0.9, "c2": 0.5},
#     "u2": {"c2": 0.8, "c3": 0.7},
#     "u3": {"c1": 0.6, "c4": 0.9},
# }


# def recommend_courses(req):
#     student_id = req.student_id
#     watched = req.watch_history  # list of course IDs

#     # -------------------------------
#     # 1️⃣ CONTENT-BASED FILTERING
#     # -------------------------------
#     watched_texts = [courses[c] for c in watched if c in courses]

#     if watched_texts:
#         user_vector = np.mean(model.encode(watched_texts), axis=0)
#         content_scores = cosine_similarity([user_vector], course_embeddings)[0]
#     else:
#         content_scores = np.zeros(len(course_ids))


#     # -------------------------------
#     # 2️⃣ COLLABORATIVE FILTERING
#     # -------------------------------
#     collaborative_scores = np.zeros(len(course_ids))

#     if student_id in user_data:
#         target_vector = user_data[student_id]

#         for other_user, interactions in user_data.items():
#             if other_user == student_id:
#                 continue

#             # find common courses
#             common = set(target_vector.keys()) & set(interactions.keys())

#             if not common:
#                 continue

#             # similarity between users
#             sim = np.mean([target_vector[c] * interactions[c] for c in common])

#             # add scores from similar users
#             for c in interactions:
#                 if c not in target_vector:
#                     idx = course_ids.index(c)
#                     collaborative_scores[idx] += sim * interactions[c]


#     # -------------------------------
#     # 3️⃣ HYBRID SCORE (COMBINE)
#     # -------------------------------
#     final_scores = 0.6 * content_scores + 0.4 * collaborative_scores


#     # -------------------------------
#     # 4️⃣ RANK + FILTER
#     # -------------------------------
#     ranked = sorted(zip(course_ids, final_scores),
#                     key=lambda x: x[1],
#                     reverse=True)

#     recommendations = [c for c, _ in ranked if c not in watched][:5]

#     return {"course_ids": recommendations}


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_courses(req):
    from sentence_transformers import SentenceTransformer   # ✅ move here

    model = SentenceTransformer('all-MiniLM-L6-v2')

# 🔹 Course metadata
courses = {
    "c1": "Python programming basics",
    "c2": "Data structures and algorithms",
    "c3": "Machine learning introduction",
    "c4": "Web development with React",
    "c5": "Docker and DevOps"
}

course_ids = list(courses.keys())
course_texts = list(courses.values())

# 🔹 Dummy user interaction data
user_data = {
    "u1": {"c1": 0.9, "c2": 0.5},
    "u2": {"c2": 0.8, "c3": 0.7},
    "u3": {"c1": 0.6, "c4": 0.9},
}


def recommend_courses(req):
    student_id = req.student_id
    watched = req.watch_history

    # ✅ LOAD MODEL INSIDE FUNCTION
    model = SentenceTransformer('all-MiniLM-L6-v2')
    course_embeddings = model.encode(course_texts)

    # -------------------------------
    # CONTENT-BASED
    # -------------------------------
    watched_texts = [courses[c] for c in watched if c in courses]

    if watched_texts:
        user_vector = np.mean(model.encode(watched_texts), axis=0)
        content_scores = cosine_similarity([user_vector], course_embeddings)[0]
    else:
        content_scores = np.zeros(len(course_ids))

    # -------------------------------
    # COLLABORATIVE
    # -------------------------------
    collaborative_scores = np.zeros(len(course_ids))

    if student_id in user_data:
        target_vector = user_data[student_id]

        for other_user, interactions in user_data.items():
            if other_user == student_id:
                continue

            common = set(target_vector.keys()) & set(interactions.keys())

            if not common:
                continue

            sim = np.mean([target_vector[c] * interactions[c] for c in common])

            for c in interactions:
                if c not in target_vector:
                    idx = course_ids.index(c)
                    collaborative_scores[idx] += sim * interactions[c]

    # -------------------------------
    # HYBRID
    # -------------------------------
    final_scores = 0.6 * content_scores + 0.4 * collaborative_scores

    ranked = sorted(zip(course_ids, final_scores),
                    key=lambda x: x[1],
                    reverse=True)

    recommendations = [c for c, _ in ranked if c not in watched][:5]

    return {"course_ids": recommendations}
