from django.shortcuts import render, redirect
from posts.models import Product, Category
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
            'reviews': product.review_set.all(),
            'categories': product.categories.all()
        }

        return render(request, 'product/detail.html', context=context)


def categories_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', 0))

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

        return render(request, 'categories/index.html', context=context)

def categories_create_view(request):
    if request.method == 'GET':
        return render(request, 'categories/create.html')

    if request.method == 'POST':
        errors = {}

        if len(request.POST.get('title')) < 8:
            errors['title_error'] = 'min lenght in field title 8!'

        if len(request.POST.get('description')) < 1:
            errors['description_error'] = 'this field is required'

        if len(errors.keys()) > 0:
            return render(request, 'categories/create.html', context=errors)

        Product.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            author=request.POST.get('author')
        )
        return redirect('/product/')

