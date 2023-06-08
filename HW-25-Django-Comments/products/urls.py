from django.urls import path
from .views import category_page, product_page


urlpatterns = [
    path("category/<slug>", category_page, name="category_page"),
    path("product/<int:product_id>", product_page, name="product")
]
