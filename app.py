import streamlit as st
from model import recommend

st.title("🎬 Movie Recommender System")

movie_name = st.text_input("Enter a movie name")

if st.button("Recommend"):
    try:
        results = recommend(movie_name)
        for movie in results:
            st.write(movie)
    except:
        st.write("Movie not found")