import pandas as pd
import streamlit as st
import pickle
def recommend(movie):
    # get movie index
    movie_index = movies[movies['title'] == movie].index[0]

    # get similarity scores
    distances = similarity[movie_index]

    # sort movies by similarity
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:9]  # skip the same movie

    # print recommended movies
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name=st.selectbox('How you like to be contacted?',movies['title'].values)
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)