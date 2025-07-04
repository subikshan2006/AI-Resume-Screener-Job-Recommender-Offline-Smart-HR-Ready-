# 🤖 AI Resume Screener (Offline Semantic Resume Ranking using FAISS + Embeddings)

This project is a fully offline, intelligent resume screening system that uses NLP vector embeddings to rank resumes against a job description. It replicates what recruiters do manually — but at lightning speed, and without needing cloud APIs or internet access.

---

## 🔍 Overview

Companies often receive hundreds of resumes per job. This tool helps automatically find the best candidates by:

- Reading the job description and all resumes
- Generating semantic embeddings for each using NLP
- Using **FAISS vector similarity search** to find the closest matches
- Scoring each resume and presenting the top-ranked ones

> Ideal for HR teams, recruiters, developers building hiring tools, or students building AI/ML portfolios.

---

## 🎯 Key Features

✅ Works 100% offline — no API keys or internet needed  
✅ Fast resume scanning using FAISS (Facebook AI Similarity Search)  
✅ Uses powerful NLP embeddings from `sentence-transformers`  
✅ Simple folder structure and Python script — no framework needed  
✅ Highly customizable for advanced use cases

---

## 📁 Project Structure
```
resume_matcher/
├── main.py # Core script to run matching
├── README.md # This file
├── job_description.txt # Text file with the job description
└── resumes/ # Folder with candidate resumes
├── resume1.txt
├── resume2.txt
└── resume3.txt
```

---

## ⚙️ Technologies Used

| Task                      | Technology                      |
|---------------------------|----------------------------------|
| NLP Embeddings            | `sentence-transformers` (MiniLM) |
| Vector Search             | `faiss-cpu`                      |
| Programming Language      | Python 3.8+                      |
| Local File Processing     | `os`, `glob`, `numpy`            |

> Model Used: `all-MiniLM-L6-v2` – a lightweight, fast, and accurate model for sentence embeddings.

---

## 🚀 How It Works

1. Load the job description and all resumes from text files
2. Generate sentence embeddings for each using a pre-trained model
3. Use FAISS to perform similarity search based on vector distance
4. Sort and display the most relevant resumes with match scores

---

## 🧪 Sample Output
```
✅ Best Matches:
resume1.txt - Match Score: 0.923
resume3.txt - Match Score: 0.771
resume2.txt - Match Score: 0.583

yaml
Copy
Edit
```
The match score is based on inverse L2 distance in vector space — the higher, the better the match to the job.

---

## 📚 Example Input Files

### `job_description.txt` (Example)

Junior Machine Learning Engineer

We are looking for a passionate entry-level ML engineer with experience in:

Python and NLP libraries

Local LLMs (LLaMA2, Mistral, Whisper)

FAISS or vector search engines

LangChain or embedding-based retrieval systems

shell
Copy
Edit

### `resumes/resume1.txt` (Example)
```
Name: Alex Johnson
Education: B.Tech in AI
Skills: Python, LLaMA2, FAISS, LangChain
Projects: JARVIS Assistant, Resume Matcher

yaml
Copy
Edit
```
---

## ✅ Step-by-Step Setup Guide
```
 1. Install Required Libraries

bash
pip install sentence-transformers faiss-cpu
2. Add Your Data
Add the job description to job_description.txt

Place .txt resumes into the resumes/ folder

3. Run the Script
bash
Copy
Edit
python main.py
That’s it! You’ll instantly see the most relevant resumes ranked and scored.

💡 Use Cases & Extensions
🔍 Local resume filtering for HR teams

🧠 College projects for NLP and vector search

🧪 Add PDF support with pdfminer.six

🌐 Build a Streamlit UI to let HR browse results

🧑‍💼 Add LLaMA2 for explanation: “Why is this resume a match?”

📌 Why This Project Matters
This project shows you're skilled in:

Real-world NLP

Embedding-based vector search

LLM tool integration (Whisper, LLaMA, etc.)

Building offline intelligent tools (important for privacy/security)

It’s not just another Python script — it’s a demonstration of how AI can replace tedious manual screening using fast, scalable, and accurate methods.

```

## About the Developer

Subikshan.p

This project was created as part of an AI/ML engineering portfolio targeting remote US-based junior roles. It showcases skills in:

Natural Language Processing (NLP)

Offline AI tools using Python

Resume parsing and vector similarity

Human-friendly AI automation

GitHub: https://github.com/subikshan2006

LinkedIn: https://www.linkedin.com/in/subikshan-p-7a7002317/

