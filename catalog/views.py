from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def contact(request):
    global context
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(f'{name} {email} {message}')

        context = {
            'title': 'Контакты'
        }
    return render(request, 'catalog/contact.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
