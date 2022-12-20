from django.shortcuts import render
from posts.models import Product
# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def posts_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
    return render(request, 'product/product.html', context={
        'products': products
    })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all()
        }

        return render(request, 'product/detail.html', context=context)


