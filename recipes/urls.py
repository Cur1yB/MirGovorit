from django.urls import path
from .views import (select_recipe, create_new_recipe, delete_recipe, remove_product_from_recipe, 
                    show_selected_product_recipes, select_recipe, show_recipes_without_product)
from .api import RecipeListView, RecipeCreateUpdateView

urlpatterns = [
    path('select_recipe/', select_recipe, name='select_recipe'),  
    path('create_recipe/', create_new_recipe, name='create_recipe'), 
    path('delete_recipe/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
    path('remove_product_from_recipe/<int:product_id>/', remove_product_from_recipe, name='remove_product_from_recipe'),
    path('show_selected_product_recipes/', show_selected_product_recipes, name='show_selected_product_recipes'),
    path('recipes_without_product/<int:product_id>/', show_recipes_without_product, name='show_recipes_without_product'),
    path('api/recipe_list/', RecipeListView.as_view(), name='api_recipe_list'),
    path('api/create_update_recipe/', RecipeCreateUpdateView.as_view(), name='api_recipe_create_update')
]