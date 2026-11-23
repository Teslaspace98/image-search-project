import os
import numpy as np
from model import extract_features

image_folder = "images"
embeddings = []
paths = []

for file in os.listdir(image_folder):
    path = os.path.join(image_folder, file)

    try:
        emb = extract_features(path)
        embeddings.append(emb)
        paths.append(path)
    except:
          pass

embeddings = np.array(embeddings)

np.save("embeddings.npy", embeddings)
np.save("paths.npy", paths)

print("Done embedding!")