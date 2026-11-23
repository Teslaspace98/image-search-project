import numpy as np
import faiss
from model import extract_features

embeddings = np.load("embeddings.npy").astype('float32')
paths = np.load("paths.npy")

faiss.normalize_L2(embeddings)
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

def search(query_image, top_k=5):
    query_emb = extract_features(query_image).astype('float32').reshape(1, -1)
    faiss.normalize_L2(query_emb)
    distances, indices = index.search(query_emb, top_k)
    results = [paths[i] for i in indices[0]]
    return results
