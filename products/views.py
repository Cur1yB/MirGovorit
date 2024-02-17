from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == 'POST':
        # Обработка добавления продукта
        if 'add' in request.POST:
            handle_add_new_product(request)
        # Обработка удаления продукта
        elif 'delete' in request.POST:
            product_id = request.POST.get('delete')
            try:
                product = Product.objects.get(id=product_id)
                product.delete()
            except Product.DoesNotExist:
                pass
        return redirect('add_product')
    products = Product.objects.all()
    return render(request, 'add_product.html', {'products': products})

def handle_add_new_product(request):
    product_name = request.POST.get('name', '').strip().capitalize()
    if product_name and not Product.objects.filter(name=product_name).exists():
        Product.objects.create(name=product_name)
        
def select_product_view(request):
    products = Product.objects.all()
    return render(request, 'select_product.html', {'products': products})