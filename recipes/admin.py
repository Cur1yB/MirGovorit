from django.contrib import admin
from .models import Recipe, RecipeProduct

class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1  # Количество форм для добавления продуктов, отображаемых по умолчанию

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',) 
    inlines = [RecipeProductInline] 
