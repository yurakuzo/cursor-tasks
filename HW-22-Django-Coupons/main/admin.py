from django.contrib import admin
from .models import MenuItem, SliderItem, OrderItems, Order, Coupon
from django.utils.html import format_html


admin.site.register(MenuItem)
admin.site.register(SliderItem)


class OrderAdmin(admin.ModelAdmin):
    list_display = fields = ['id', 'first_name', "last_name", "address", "email"]

    def queryset(self,request):
        qs = super(Order, self).queryset(request)
        return qs.all()


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "valid_from", "valid_to", "discount", "active"]
    
    def discount(self, discount):
        print('discount =', discount)
        return format_html(f"{discount}%")
    


admin.site.register(Order, OrderAdmin)