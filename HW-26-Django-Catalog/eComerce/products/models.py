import base64
from django.db import models
from django.db.models import Q
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


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
        return str(self.id) + " " + self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")
    photo_encoded = models.TextField(null=True, blank=True)
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'is_main')

    def save(self, *args, **kwargs):
        if self.image:
            self.photo_encoded = self.encode_photo()
        super().save(*args, **kwargs)

    def encode_photo(self):
        with open(self.image.path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
        return f"data:{self.image.file.content_type};base64,{encoded_string}"

    def decode_photo(self):
        if self.photo_encoded:
            _, imgstr = self.photo_encoded.split(';base64,')
            data = base64.b64decode(imgstr)
            return Image.open(BytesIO(data))

    def __str__(self):
        return f"{self.product.id} {self.product.title} | {self.id}"


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, default="slug")
    parent = models.ForeignKey("Category", null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title