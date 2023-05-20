from django.shortcuts import render
from .models import Category, Product, ProductImage
from django.shortcuts import get_object_or_404


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request,
                  "category.html",
                  {"category": category, "products": category.products.all()})


def product_page(request, product_id):
    product = get_object_or_404(Product, pk=int(product_id))
    product_images = product.images

    context = {
        "product": product,
        "product_images": product_images,
    }

    return render(request,
                  "products/product.html",
                  context=context)
