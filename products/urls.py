from django.urls import path, include
from .views import add_product, select_product_view
from .api import CreateProductView, ProductListView, DeleteProductView

urlpatterns = [
    path('add_product/', add_product, name='add_product'),
    path('select_product/', select_product_view, name='select_product'),
    path('api/create_product/', CreateProductView.as_view(), name='api_create_product'),
    path('api/product_list/', ProductListView.as_view(), name='api_product_list'),
    path('api/delete_product/', DeleteProductView.as_view(), name='api_delete_product'),
] 