# AI Resume Screener using FAISS + Sentence Embeddings (Offline)

import os
import glob
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_resumes(resume_folder):
    resumes = []
    filenames = []
    for file_path in glob.glob(os.path.join(resume_folder, "*.txt")):
        with open(file_path, "r", encoding="utf-8") as f:
            resumes.append(f.read())
            filenames.append(os.path.basename(file_path))
    return resumes, filenames

def embed_texts(model, texts):
    return model.encode(texts)

def rank_resumes(jd_vector, resume_vectors, top_k=5):
    index = faiss.IndexFlatL2(len(jd_vector[0]))
    index.add(np.array(resume_vectors))
    D, I = index.search(jd_vector, top_k)
    return D[0], I[0]

def main():
    print("📄 Loading model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("📝 Reading job description...")
    job_description = load_job_description("job_description.txt")
    jd_vector = embed_texts(model, [job_description])

    print("📂 Reading resumes...")
    resume_texts, filenames = load_resumes("resumes")
    resume_vectors = embed_texts(model, resume_texts)

    print("🔍 Ranking resumes by relevance...")
    scores, indices = rank_resumes(jd_vector, resume_vectors, top_k=min(5, len(resume_vectors)))

    print("\n✅ Top Resume Matches:")
    for idx, score in zip(indices, scores):
        match_score = 1 / (1 + score)  # Convert L2 distance to match score
        print(f"{filenames[idx]} - Match Score: {match_score:.3f}")

if __name__ == "__main__":
    main()
