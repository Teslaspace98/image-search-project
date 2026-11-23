import streamlit as st
from search import search

st.title("Image Search 🔍")

uploaded = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded:
    with open("query.jpg", "wb") as f:
        f.write(uploaded.getbuffer())

    results = search("query.jpg")

    st.image("query.jpg", caption="Query Image")

    st.write("Similar Images:")

    for img in results:
        st.image(img)