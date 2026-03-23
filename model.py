import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load data
movies = pd.read_csv('movies.csv')

# Select required columns
movies = movies[['id','title','overview','genres','keywords']]

# Drop null values
movies.dropna(inplace=True)

# Convert string to list
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# Split overview into words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces
def collapse(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

# Create tags
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords']

# Final dataframe
new_df = movies[['id','title','tags']]

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Similarity
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_df, open('movies.pkl','wb'))
pickle.dump(similarity, open('similarity.pkl','wb'))

print("Model created successfully!")