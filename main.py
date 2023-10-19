import pandas as pd
import numpy as np
import zipfile
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import functions as f

app = FastAPI()

app.mount("/static", StaticFiles(directory="public/static"), name="static")
app.mount("/launch", StaticFiles(directory="2_Datasets/launch"), name="launch")
app.mount("/csv", StaticFiles(directory="/"), name="csv")

templates = Jinja2Templates(directory="public/templates")



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    selected_data_hotels, selected_data_state, selected_data_city, selected_data_poi =  f.hotels_list_to_html()
    context = {"request": request, "selected_data_hotels":selected_data_hotels, "selected_data_state":selected_data_state, "selected_data_city":selected_data_city, "selected_data_poi":selected_data_poi}
    return templates.TemplateResponse("index.html", context)

@app.get("/recomendacion_1")
async def recomendacion_1( titulo: str ):
    # Ruta del archivo ZIP
    zip_file_path = '2_Datasets/launch/sentiments_to_frontend.zip'

    # Abre el archivo ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Lista los archivos en el ZIP (puede haber múltiples archivos, no necesariamente uno)
        zip_file_contents = zip_file.namelist()
        
        # Supongamos que queremos leer el primer archivo CSV en el ZIP
        csv_file_name = zip_file_contents[0]
        
        # Extrae el archivo CSV del ZIP
        with zip_file.open(csv_file_name) as csv_file:
            # Lee el archivo CSV con Pandas
            csv_recomendaciones_1 = pd.read_csv(csv_file)    
    recomendacion_1 = f.get_sentiments_count(titulo, csv_recomendaciones_1)
    return JSONResponse(content=recomendacion_1)

@app.get("/recomendacion_2")
async def recomendacion_2( titulo_2: str ):
    recomendacion_2 = f.recommendation_function(titulo_2)
    response_data = {"recomendacion_2":recomendacion_2}
    return JSONResponse(content=response_data)

@app.get("/busca_hotel")
async def busca_hotel( estado: str, ciudad: str, poi: str ):
    busca_hotel = f.filters(estado, ciudad, poi)
    response_data = {"busca_hotel":busca_hotel}
    return JSONResponse(content=response_data)

@app.get("/obtener_ciudades")
async def obtener_ciudades(estado: str):
    # Filtrar ciudades basadas en el estado seleccionado
    ciudades_filtradas, poi_filtrados  = f.list_filter_state(estado)
    response_data = {"ciudades": ciudades_filtradas, "poi": poi_filtrados}
    return response_data

@app.get("/obtener_poi")
async def obtener_poi(ciudad: str):
    # Filtrar puntos de interés basados en la ciudad seleccionada
    poi_filtrados  = f.list_filter_city(ciudad)
    response_data = {"poi": poi_filtrados}
    return response_data