import streamlit as st
import pickle
import pandas as pd
import requests

def fectch_poster(movie_id):
    data = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cf63823a3dbea483c5f041c352363443&language=en-US'.format(movie_id))
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_idx = newdf[newdf['title'] == movie].index[0]
    distance = similar[movie_idx]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_names = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = newdf.iloc[i[0]].id
        recommended_movies_names.append(newdf.iloc[i[0]].title)
        recommended_movies_posters.append(fectch_poster(movie_id))
    return recommended_movies_names, recommended_movies_posters

movies_list = pickle.load(open('movies.pkl', 'rb'))
newdf = pd.DataFrame(movies_list)

movies_list = movies_list['title'].values

similar = pickle.load(open('similar.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'How would you like to be contacted?',
    (movies_list))
# st.write('You selected:', option)

if st.button('Suggest Something'):
    recommended_movie_names, recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
# website link
# https://get-your-recommendation.herokuapp.com/
