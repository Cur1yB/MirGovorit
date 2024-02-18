from django.shortcuts import render, get_object_or_404, redirect
from products.views import handle_add_new_product
from recipes.models import Recipe, RecipeProduct
from products.models import Product
from recipes.views import handle_add_product_to_recipe, handle_delete_product_from_recipe, handle_create_new_recipe
from recipes.serializers import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class RecipeListView(APIView):
    """
    API endpoint, который возвращает список рецептов в формате JSON.
    """
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

def add_new_product(request):
    if request.method == 'POST':
        handle_add_new_product(request)
        return redirect('add_recipe')
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def recipe_list_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def add_recipe_view(request):
    current_recipe_id = request.session.get('current_recipe_id', None)
    current_recipe = None
    if current_recipe_id:
        current_recipe = get_object_or_404(Recipe, pk=current_recipe_id)
        
    if request.method == 'POST':
        if 'add_product_to_recipe' in request.POST:
            handle_add_product_to_recipe(request, current_recipe)
        elif 'add_new_product' in request.POST:
            handle_add_new_product(request)
        elif 'delete_product_from_recipe' in request.POST:
            handle_delete_product_from_recipe(request, current_recipe)
        elif 'create_new_recipe' in request.POST:
            current_recipe = handle_create_new_recipe(request)
            if current_recipe:
                request.session['current_recipe_id'] = current_recipe.id
        elif 'select_recipe' in request.POST:
            selected_recipe_id = request.POST.get('recipe_id')
            request.session['current_recipe_id'] = selected_recipe_id
            current_recipe = get_object_or_404(Recipe, pk=selected_recipe_id)
        elif 'clear_recipe' in request.POST:
            if 'current_recipe_id' in request.session:
                del request.session['current_recipe_id']
            current_recipe = None

        return redirect('add_recipe')

    recipe_products = RecipeProduct.objects.filter(recipe=current_recipe) if current_recipe else []
    recipes = Recipe.objects.all()
    products = Product.objects.all()

    return render(request, 'add_recipe.html', {
        'current_recipe': current_recipe,
        'recipes': recipes,
        'products': products,
        'recipe_products': recipe_products
    })
