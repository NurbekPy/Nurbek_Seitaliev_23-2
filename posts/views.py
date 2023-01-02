from django.shortcuts import render, redirect
from posts.models import Product, Category, Review
from posts.forms import CategoryCreateForm, ReviewCreateForm

# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def posts_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
    return render(request, 'product/product.html', context={
        'products': products,
        'user': None if request.user.is_anonymous else request.user
    })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'categories': product.categories.all(),
            'review_form': ReviewCreateForm
        }

        return render(request, 'product/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                product_id=id,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/product/{id}')
        else:
            return render(request, 'product/detail.html', context={
                'product': product,
                'reviews': product.review_set.all(),
                'categories': product.categories.all(),
                'review_form': form
            })

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
        return render(request, 'categories/create.html', context={
            'form': CategoryCreateForm
        })

    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST)

        if form.is_valid():

            Product.objects.create(
                writer=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                author=form.cleaned_data.get('author')
            )
            return redirect('/posts/')
        else:
            return render(request, 'categories/create.html', context={
                'form': form
            })
