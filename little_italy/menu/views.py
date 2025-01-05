from django.shortcuts import render
from .utils import get_recipes
# Create your views here.

def recipe_search(request):
    """
    Vista para buscar recetas usando la API de Edamam.
    """
    query = request.GET.get('query', '')  # Obtén el término de búsqueda del usuario
    recipes = get_recipes(query) if query else None  # Consulta la API si hay un término

    return render(request, 'menu/recipes.html', {'recipes': recipes, 'query': query})

def home(request):
    return render(request, 'menu/home.html')