from django.db import models
from products.models import Product

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name
    
    def get_products_with_weights(self):
        return self.recipeproduct_set.select_related('product').all()

class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    class Meta:
        unique_together = ('recipe', 'product')

    def __str__(self):
        return f"{self.product.name} в {self.recipe.name} - {self.weight} г"