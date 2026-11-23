# 🧠 Visual Product Similarity System (Amazon-Style)

## 🚀 Overview

This project builds an image-based recommendation system that finds visually similar products using deep learning and fast similarity search.

Upload an image → Get similar images instantly.

---

## 🔥 Features

* Image similarity search using embeddings
* Deep learning-based feature extraction (ResNet18)
* FAISS-based fast similarity search (Inner Product on normalized embeddings)
* Streamlit web app UI

---

## 🛠️ Tech Stack

* Python
* PyTorch
* NumPy
* FAISS
* Streamlit

---

## 📂 Project Structure

* app.py → UI
* search.py → FAISS-based similarity logic
* model.py → feature extraction
* embed.py → embeddings generation
* images/ → dataset

---

## ▶️ Run
python3 -m streamlit run app.py


---

## 💡 What it does

Takes an input image and returns visually similar images using AI, powered by a FAISS similarity index for fast lookup.