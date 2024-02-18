from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class DeleteProductView(APIView):
    def delete(self, request, format=None):
        product_name = request.data.get('name', '').strip().capitalize()
        try:
            product = Product.objects.get(name=product_name)
            product.delete()
            return Response({'detail': f'Продукт "{product_name}" успешно удален'}, 
                            status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'detail': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)

class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CreateProductView(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        product_name = request.data.get('name', '').strip().capitalize()
        if Product.objects.filter(name=product_name).exists():
            return Response({'detail': f'Продукт с именем "{product_name}" уже существует.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)