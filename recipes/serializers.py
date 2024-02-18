from rest_framework import serializers
from .models import Recipe, RecipeProduct
from products.serializers import ProductSerializer

class RecipeProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = RecipeProduct
        fields = ['product', 'weight']

class RecipeSerializer(serializers.ModelSerializer):
    products_with_weights = RecipeProductSerializer(source='recipeproduct_set', many=True)  # Изменено для отображения продуктов с весом
    
    class Meta:
        model = Recipe
        fields = ['name', 'products_with_weights']
        
