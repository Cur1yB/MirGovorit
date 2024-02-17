from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeProduct, Recipe
from products.models import Product

def handle_add_product_to_recipe(request, current_recipe):
    product_id = request.POST.get('product_id')
    weight = request.POST.get('product_weight')
    product = get_object_or_404(Product, pk=product_id)
    
    recipe_product, created = RecipeProduct.objects.get_or_create(
        recipe=current_recipe, product=product, defaults={'weight': weight})

    if not created:
        recipe_product.weight = weight
        recipe_product.save()
        
def handle_delete_product_from_recipe(request, current_recipe):
    product_id = request.POST.get('product_id')
    recipe_product = get_object_or_404(RecipeProduct, recipe=current_recipe, product_id=product_id)
    recipe_product.delete()
    
def handle_create_new_recipe(request):
    recipe_name = request.POST.get('new_recipe_name', '').strip()
    if recipe_name:
        new_recipe = Recipe.objects.create(name=recipe_name)
        request.session['current_recipe_id'] = new_recipe.id
        return new_recipe
    return None

def create_new_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('new_recipe_name', '').strip()
        if recipe_name:
            recipe = Recipe.objects.create(name=recipe_name)
            request.session['current_recipe_id'] = recipe.id  # Сохранение ID рецепта в сессии
            return redirect('add_recipe')
    return redirect('home')

def select_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        request.session['current_recipe_id'] = recipe_id
        return redirect('add_recipe')
    return redirect('home')

def remove_product_from_recipe(request, product_id):
    recipe_product_id = product_id
    if request.method == 'POST':
        recipe_product = get_object_or_404(RecipeProduct, id=recipe_product_id)
        recipe_product.delete()
        return redirect('add_recipe')  # Перенаправление после удаления продукта
    return redirect('home')  # Перенаправление, если метод не POST

def delete_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        # Удаляем текущий ID рецепта из сессии, если он совпадает с удаленным рецептом
        if request.session.get('current_recipe_id') == recipe_id:
            del request.session['current_recipe_id']
        return redirect('add_recipe')  # Перенаправляем пользователя на страницу управления рецептами
    else:
        return redirect('home')  # Перенаправляем на главную, если метод не POST
    
def show_selected_product_recipes(request):
    product_id = request.GET.get('product_id')
    if product_id:
        return redirect('show_recipes_without_product', product_id=product_id)
    else:
        # Если ID продукта не указан, вернуть пользователя на страницу выбора продукта
        return redirect('select_product')
    
def show_recipes_without_product(request, product_id):
    # Получаем рецепты, где продукт отсутствует или его вес меньше 10 грамм
    recipes_with_product = RecipeProduct.objects.filter(
        product_id=product_id,
        weight__gte=10
    ).values_list('recipe', flat=True)
    
    recipes_without_product = Recipe.objects.exclude(
        id__in=recipes_with_product
    )

    return render(request, 'recipes_without_product.html', {'recipes_without_product': recipes_without_product})
