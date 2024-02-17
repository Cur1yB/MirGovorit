from django.urls import path
from .views import add_product, select_product_view

urlpatterns = [
    path('add_product/', add_product, name='add_product'),
    path('select_product/', select_product_view, name='select_product'),
]