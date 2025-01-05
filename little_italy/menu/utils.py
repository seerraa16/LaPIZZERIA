import requests
from django.conf import settings

def get_recipes(query):
    """
    Consulta la API de Edamam para obtener recetas relacionadas con el término de búsqueda.
    """
    base_url = "https://api.edamam.com/search"
    params = {
        "q": query,
        "app_id": settings.EDAMAM_APP_ID,
        "app_key": settings.EDAMAM_APP_KEY,
    }

    response = requests.get(base_url, params=params)

    # Verifica si la respuesta es exitosa
    if response.status_code == 200:
        return response.json()  # Devuelve los datos en formato JSON
    else:
        return {"error": "No se pudo conectar a la API", "status_code": response.status_code}



