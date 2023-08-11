# Importamos las bibliotecas

import pandas as pd 
import numpy as np
from fastapi import FastAPI
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Indicamos título y descripción de la API
app = FastAPI(title='Proyecto individual 1: Recomendacion de peliculas',
            description='Machine Learning Operations (MLOps) by: Guillermo Del Rio')


# Global variables
df_movie_final = None
df = None
cv = None
count_matrix = None
cosine_sim = None
indices = None


# carga inicial de datos
@app.on_event("startup")
async def load_data():
    global df_movie_final, df, cv, count_matrix, nn, indices

    # Cargando los dataframes
    df_movie_final = pd.read_csv('movies_final.csv')
    df = pd.read_csv("movies_transformado.csv")

    cv = CountVectorizer(stop_words='english', max_features=5500)
    count_matrix = cv.fit_transform(df_movie_final['combined_features'])

    nn = NearestNeighbors(metric='cosine', algorithm='auto')
    nn.fit(count_matrix)

    indices = pd.Series(df_movie_final.index, index=df_movie_final['title']).drop_duplicates()
    

@app.get('/')
async def read_root():
    return {'API Recomendacion de Peliculas. Dirígite a http://127.0.0.1:8000/docs'}

@app.get('/about/')
async def about():
    return {'Proyecto individual 1: Recomendacion de peliculas Machine Learning Operations (MLOps) '}


# Función de películas por idioma
@app.get('/peliculas_idioma/({Idioma})')
def peliculas_idioma( Idioma: str ):
    '''
    Se ingresa un idioma. Debe devolver la cantidad de películas producidas en ese idioma.
        Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma
    '''
    idioma_deseado = df[df['original_language'] == Idioma]
    num_peliculas = len(idioma_deseado)
    return {f"{num_peliculas} peliculas se lanzaron en {Idioma}"}



# Función de películas por duración
@app.get('/peliculas_duracion/({Pelicula})')
def peliculas_duracion( Pelicula: str ):
    '''
     Se ingresa una pelicula. Debe devolver la duracion y el año.
        Ejemplo de retorno: X . Duración: x. Año: x
    '''
    pelicula = df[df["title"]== Pelicula].iloc[0]
    duracion = pelicula["runtime"]
    anio = pelicula["release_year"]
    return {f"{Pelicula}. Duracion: {duracion} Año: {anio}"}



# Función de películas por franquicia
@app.get('/franquicia/({Franquicia})')
def franquicia( Franquicia: str ):
    '''
     Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
        Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia
    '''
    valor_encontrado = df[df['belongs_to_collection_name']==Franquicia]
    series = len(valor_encontrado)
    total = valor_encontrado['return'].sum()
    promedio = valor_encontrado['return'].mean()

    return {f"Franquicia: {Franquicia}\nCantidad de Películas: {series}\nGanancias Totales: {total}\nPromedio de las Ganancias: {promedio}"}


# Función de películas por país
@app.get('/peliculas_pais/({Pais})')
def peliculas_pais(Pais: str):
    peliculas_por_pais = df[df['production_countries'].str.contains(Pais)]
    cantidad_peliculas = len(peliculas_por_pais)
    
    return {f"Se produjeron {cantidad_peliculas} películas en el país {Pais}"}


# Función de productoras_exitosas
@app.get('/productoras_exitosas/({Productora})')
def productoras_exitosas(Productora: str):
    peliculas_por_productora = df[df['production_companies'].str.contains(Productora)]
    total_revenue = peliculas_por_productora['revenue'].sum()
    cantidad_peliculas = len(peliculas_por_productora)
    
    return {f"La productora {Productora} ha tenido un revenue de {total_revenue} y ha realizado {cantidad_peliculas} películas"}


# Función get_director
@app.get('/get_director/({nombre_director})')
def get_director(nombre_director):
    director_movies = df[df['director'] == nombre_director]
    
    if director_movies.empty:
        return "Director no encontrado en el dataset."
    
    success_info = []
    
    for index, row in director_movies.iterrows():
        movie_info = {
            'title': row['title'],
            'release_date': row['release_date'],
            'revenue': row['revenue'],
            'budget': row['budget'],
            'profit': row['revenue'] - row['budget']
        }
        
        success_info.append(movie_info)
    
    return success_info


# Función de recomendación
@app.get('/recomendacion/({title})')
def recomendacion(title):
    if title not in df_movie_final['title'].values:
        return 'La pelicula no se encuentra en el data set'
    else:
        index = indices[title]
        
        # nos da los 5 knn mas cercanos
        distances, indices_knn = nn.kneighbors(count_matrix[index], n_neighbors=6)
        
        movie_indices = indices_knn[0][1:]

        # nos da una lista con las 5 pelicuals mas cercanas
        return df_movie_final['title'].iloc[movie_indices].tolist()





















