from rest_framework import serializers
from .models import Recipe, RecipeProduct
from products.models import Product
from products.serializers import ProductSerializer

class RecipeProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = RecipeProduct
        fields = ['product', 'weight']
    
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product_name = product_data['name'].strip().capitalize()
        product, created = Product.objects.get_or_create(name=product_name)
        recipe_product = RecipeProduct.objects.create(product=product, **validated_data)
        return recipe_product

class RecipeSerializer(serializers.ModelSerializer):
    products_with_weights = RecipeProductSerializer(source='recipeproduct_set', many=True)

    class Meta:
        model = Recipe
        fields = ['name', 'products_with_weights']

    def create(self, validated_data):
        products_data = validated_data.pop('recipeproduct_set')
        recipe, created = Recipe.objects.get_or_create(name=validated_data['name'])
        for product_data in products_data:
            RecipeProductSerializer().create({'recipe': recipe, **product_data})
        return recipe

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        products_data = validated_data.get('recipeproduct_set')
        if products_data is not None:
            instance.recipeproduct_set.all().delete()
            for product_data in products_data:
                RecipeProductSerializer().create({'recipe': instance, **product_data})
        
        return instance