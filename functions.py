import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

import zipfile

# Función para crear una lista de hoteles a través de ajax
def hotels_list_to_html():
    df_hotel = pd.read_csv("2_Datasets/launch/hotels_name_to_frontend.csv")
    df_hotel = df_hotel.dropna(subset=['name'])
    return df_hotel["name"].tolist()

    

def get_recommendations_for_title(title, preview_recommendations):
    # Cargar el DataFrame precalculado desde el archivo CSV
    recommendations = preview_recommendations[preview_recommendations['movie_title'] == title]
    if not recommendations.empty:
        recommended_titles = recommendations.iloc[0]['recommended_titles']
        return recommended_titles.split(', ')
    else:
        return ["Película no encontrada en la Base de Datos."]

def get_sentiments_count(title, preview_recommendations):

    # Cargar el DataFrame precalculado desde el archivo CSV
    recommendations = preview_recommendations[preview_recommendations['name'] == title]
    # Inicializar un diccionario para almacenar las cuentas
    sentiment_counts = {}

    # Iterar a través de las filas del DataFrame filtrado
    for index, fila in recommendations.iterrows():
        etiqueta = fila['sentiment_text']
        
        # Agregar la etiqueta al diccionario de cuentas
        if etiqueta in sentiment_counts:
            sentiment_counts[etiqueta] += 1
        else:
            sentiment_counts[etiqueta] = 1

    
    if not recommendations.empty:
        # La lista 'cuentas' ahora contiene las cuentas de sentimiento para el hotel específico
        return sentiment_counts
    else:
        return ["Hotel no encontrado en la Base de Datos."]
    
    
def cargar_datos_y_generar_recomendaciones():
    # Ruta del archivo ZIP
    zip_file_path = '2_Datasets/beta/hotelbeds/df_hotels_.zip'

    # Abre el archivo ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Lista los archivos en el ZIP (puede haber múltiples archivos, no necesariamente uno)
        zip_file_contents = zip_file.namelist()
        
        # Supongamos que queremos leer el primer archivo CSV en el ZIP
        csv_file_name = zip_file_contents[0]
        
        # Extrae el archivo CSV del ZIP
        with zip_file.open(csv_file_name) as csv_file:
            # Lee el archivo CSV con Pandas
            df_hotels = pd.read_csv(csv_file)

    # Instanciamos el CountVectorizer
    vectorizer = CountVectorizer()

    # Eliminamos las "stop words", palabras comunes no informativas
    stop = list(stopwords.words('english'))
    tfidf = TfidfVectorizer(stop_words=stop)

    # Calculamos los features para cada ítem (texto)
    tfidf_matrix = tfidf.fit_transform(df_hotels['review'])

    # Calculamos las similitudes entre todos los documentos
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Cantidad de hoteles a recomendar
    n = 6

    # Creamos un diccionario para guardar el resultado
    results = {} 

    for idx, row in df_hotels.iterrows():
        # Guardamos los índices similares basados en la similitud coseno.
        # Los ordenamos en modo ascendente, siendo 0 nada de similitud y 1 total.
        similar_indices = cosine_similarities[idx].argsort()[:-n-2:-1] 

        # Guardamos los N más cercanos
        similar_items = [i for i in similar_indices]
        results[f"{row['name']}"] = df_hotels.iloc[similar_items[1:], [1, 9, 2, 8, 7, 3, 4, 5, 6]]

    
    # Definimos una función de recomendación
    def recommend(hotel):
        df_recommend = pd.DataFrame(results[hotel])
        df_recommend = df_recommend[['name', 'stars', 'address', 'city_name', 'state_name', 'phones', 'web']]
        return df_recommend.to_html(index=False, justify="center")

    return recommend

# Cargar datos y generar la función de recomendación
recommendation_function = cargar_datos_y_generar_recomendaciones()