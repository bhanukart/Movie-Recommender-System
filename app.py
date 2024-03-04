import streamlit as st
import pickle
import requests
st.title('Movie Recommender System')

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=17030d9455094969392996f3d2509bf4&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters



movies_list = pickle.load(open('movies.pkl','rb'))
movies_df = movies_list
movies=movies_df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox('Choose a movie you are watching/interested', movies)

if st.button('Recommend'):
    name,posters = recommend(selected_movie_name)
    col0,col1,col2 = st.columns(3)
    with col0:
        st.text(selected_movie_name)
        selected_id = []
        for k, v in enumerate(movies_df[movies_df['title'] == selected_movie_name].movie_id):
            selected_id = v
    with col1:
        col1 = st.text(" ")
    with col2:
        col2 = st.text(" ")
    selected_movie_poster=fetch_poster(selected_id)
    st.image(selected_movie_poster)

    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])