from django.db import models
from products.models import Product
from django.utils import timezone
from .utils import coupon_code_gen

from django.core.exceptions import ValidationError


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SliderItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/")


    def __str__(self):
        return self.title


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.address


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.order.id) + " " + self.product.title
    

class Coupon(models.Model):
    code = models.CharField(max_length=32, default=coupon_code_gen())
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField()
    discount = models.FloatField()
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.code
    
    @property
    def is_valid(self):
        now = timezone.now()
        return self.valid_from <= now <= self.valid_to and self.active
    
    @staticmethod
    def verify_code(code):
        try:
            coupon = Coupon.objects.get(code=code)
            if coupon.is_valid:
                return coupon
        except Coupon.DoesNotExist:
            raise ValidationError('Invalid coupon code.')
    

    def use_coupon_on(self, product):
        discount_percentage = self.discount / 100
        discount_amount = product.price * discount_percentage
        final_price = product.price - discount_amount
        return final_price

