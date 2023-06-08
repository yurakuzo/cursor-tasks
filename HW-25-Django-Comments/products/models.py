from django.db import models
from django.db.models import Q


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(null=False)
    discount_price = models.IntegerField(null=True, blank=True)
    show_on_main_page = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    @property
    def main_image(self):
        return ProductImage.objects.filter(Q(product_id=self.id) & Q(is_main=True)).first().image

    @property
    def images(self):
        return ProductImage.objects.filter(Q(product_id=self.id))

    def __str__(self):
        return f"Product<{self.id}, {self.title}>"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/products/")
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'is_main')

    def __str__(self):
        return f"Product<{self.product.id}, {self.product.title}> Image<{self.id}>"


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, default="slug")
    parent = models.ForeignKey("Category", null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Category <{self.title}>"
