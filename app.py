import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS (Netflix Style)
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #E50914;
        text-align: center;
    }
    .movie-card {
        background-color: #1c1c1c;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        transition: 0.3s;
    }
    .movie-card:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🎬 MOVIES RECOMMENDER</p>', unsafe_allow_html=True)

# Load data
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Dropdown
selected_movie = st.selectbox("🎥 Choose a movie", movies['title'].values)

# Button
if st.button("🔥 Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("✨ Recommended Movies")

    cols = st.columns(3)

    for i, movie in enumerate(recommendations):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="movie-card">
                    <h4>{movie}</h4>
                </div>
            """, unsafe_allow_html=True)