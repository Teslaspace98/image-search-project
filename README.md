# Visual Product Similarity Search

GUVI x HCL Capstone Project 4 — content-based image similarity search system.

## Overview
Given a query image, the system retrieves the most visually similar images from a reference dataset using deep learning embeddings and vector similarity search.

## Pipeline
1. **Dataset**: Oxford-IIIT Pet Dataset (subset renamed to `pet_{index}_{label}.jpg` to enable label-based evaluation)
2. **Feature extraction**: ResNet18 (ImageNet-pretrained) embeddings via `model.py`
3. **Similarity search**: FAISS `IndexFlatIP` over L2-normalized embeddings (equivalent to cosine similarity)
4. **UI**: Streamlit app for image upload and results display
5. **SQL layer**: SQLite database logs every search (query image, ranked results, timestamp), shown as "Recent Searches" in the app sidebar

## Evaluation
Measured with `eval.py` (same-label images treated as relevant):
- Precision@5: 0.65
- Recall@5: 0.71

## Tech Stack
Python, PyTorch/Torchvision, FAISS, Streamlit, SQLite, NumPy, scikit-learn

## Files
- `model.py` — ResNet18 feature extractor
- `prepare_dataset.py` — prepares Oxford-Pet dataset, builds `embeddings.npy` / `paths.npy`
- `search.py` — FAISS-based similarity search
- `db.py` — SQLite search history logging
- `app.py` — Streamlit UI
- `eval.py` — Precision@K / Recall@K evaluation script

## How to Run
\`\`\`
pip install -r requirements.txt
streamlit run app.py
\`\`\`
