from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ui.urls')),
    path('products/', include('products.urls')),
    path('recipes/', include('recipes.urls')),
]
