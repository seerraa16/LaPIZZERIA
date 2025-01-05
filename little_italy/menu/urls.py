from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('recipes/', views.recipe_search, name='recipe_search'),  # Ruta para buscar recetas
]
