import streamlit as st
from search import search
from db import log_search, get_recent_searches

st.title("Image Search 🔍")

uploaded = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded:
    with open("query.jpg", "wb") as f:
        f.write(uploaded.getbuffer())

    results = search("query.jpg")
    log_search("query.jpg", results)

    st.image("query.jpg", caption="Query Image")

    st.write("Similar Images:")

    for img in results:
        st.image(img)

st.sidebar.header("Recent Searches")
for query_image, timestamp in get_recent_searches():
    st.sidebar.write(f"{query_image} — {timestamp}")
