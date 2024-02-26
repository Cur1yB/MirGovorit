from recipes.serializers import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe

class RecipeListView(APIView):
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
class RecipeCreateUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            recipe_name = request.data.get('name', '').strip().capitalize()
            recipe = Recipe.objects.get(name=recipe_name)
            serializer = RecipeSerializer(recipe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Recipe.DoesNotExist:
            return Response({'detail': 'Рецепт не найден.'}, status=status.HTTP_404_NOT_FOUND)