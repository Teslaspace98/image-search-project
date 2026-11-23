import numpy as np
import faiss
from model import extract_features

embeddings = np.load("embeddings.npy").astype("float32")
paths = np.load("paths.npy")

dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

def search(query_image, top_k=5):
    query_emb = extract_features(query_image).astype("float32")
    query_emb = np.expand_dims(query_emb, axis=0)

    distances, indices = index.search(query_emb, top_k)

    results = [paths[i] for i in indices[0]]

    return results