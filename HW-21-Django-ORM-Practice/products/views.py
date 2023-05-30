from django.shortcuts import render
from .models import Category, Product


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    sort_option = request.POST.get('sort_option')

    sorting_options = {
        'price descending': '-price',
        'price ascending': 'price',
        'creation date descending': '-created_at',
        'creation date ascending': 'created_at',
    }

    products = category.products.all()

    if sort_option in sorting_options:
        sort_param = sorting_options[sort_option]
        products = products.order_by(sort_param)

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category.html', context)
