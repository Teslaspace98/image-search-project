import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embeddings = np.load("embeddings.npy")
paths = np.load("paths.npy")

def get_label(path):
    return str(path).split("_")[-1].split(".")[0]

labels = np.array([get_label(p) for p in paths])

def evaluate(k=5):
    sims = cosine_similarity(embeddings)
    precisions, recalls = [], []
    for i in range(len(embeddings)):
        sims_i = sims[i].copy()
        sims_i[i] = -1
        top_k_idx = sims_i.argsort()[-k:][::-1]
        query_label = labels[i]
        total_relevant = np.sum(labels == query_label) - 1
        retrieved_relevant = np.sum(labels[top_k_idx] == query_label)
        precisions.append(retrieved_relevant / k)
        if total_relevant > 0:
            recalls.append(retrieved_relevant / min(total_relevant, k))
    print(f"Precision@{k}: {np.mean(precisions):.4f}")
    print(f"Recall@{k}: {np.mean(recalls):.4f}")

if __name__ == "__main__":
    evaluate(5)
