from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_used')  
    search_fields = ('name',)  

    list_filter = ('times_used',)

    fields = ('name', 'times_used')

admin.site.register(Product, ProductAdmin)