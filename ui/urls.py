from django.urls import path
from .views import home, recipe_list_view, add_recipe_view, add_new_product
from recipes.api import RecipeListView

urlpatterns = [
    path('', home, name='home'),
    path('recipe_list/', recipe_list_view, name='recipe_list'),    
    path('add_recipe/', add_recipe_view, name='add_recipe'),
    path('add_new_product/', add_new_product, name='add_new_product'),  
    path('api/recipe_list/', RecipeListView.as_view(), name='api_recipe_list')
]