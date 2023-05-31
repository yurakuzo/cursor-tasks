from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from products.models import Product
from .models import Order, OrderItems, Coupon
from .forms import NewUserForm


def main(request):
    products = Product.objects.filter(show_on_main_page=True)
    return render(request, "index.html", {"products": products})


def add_to_cart(request, product_id: int):
    product_obj = Product.objects.get(id=product_id)
    is_product_already_exist = False
    if not request.session.get("cart"):
        request.session["cart"] = []
    else:
        for product in request.session.get("cart", []):
            if product_id == product["id"]:
                product["quantity"] = product["quantity"] + 1
                product["price"] = product_obj.price * product["quantity"]
                is_product_already_exist = True

    if not is_product_already_exist:
        request.session["cart"].append({"id": product_id, "quantity": 1, "price": product_obj.price})
    request.session.modified = True
    return HttpResponseRedirect("/")


def delete_item(request, pk):
    cart = request.session.get("cart", [])
    index = next(index for (index, item) in enumerate(cart) if item['id'] == pk)
    del cart[index]
    request.session["cart"] = cart
    return redirect("cart")


def cart(request, coupon_msg=''):
    cart_products = []
    discounts = []
    for cart_item in request.session.get("cart", []):
        product = Product.objects.get(id=cart_item["id"])
        product.quantity = cart_item["quantity"]
        product.total_price = cart_item["price"]
        cart_products.append(product)
        
    if (code := request.session.get("coupon_code", False)):
        code = Coupon.objects.get(code=code)
        discounts = [code.use_coupon_on(product)
                     for product in cart_products]
        print("discounts =", discounts)
    
    context = {
        "cart_products": cart_products,
        "coupon_msg": coupon_msg,
        "discounts": sum(discounts),
        "total_price": sum([obj.total_price for obj in cart_products]),
        "coupon": request.session.get("coupon_code", False)
    }
    return render(request, "cart.html", context=context)


def checkout(request):
    total_price = 0
    for cart_item in request.session.get("cart", []):
        total_price = total_price + cart_item["price"]

    return render(request, "checkout.html", {"total_price": total_price})


def checkout_proceed(request):
    if request.method == "POST":
        order = Order()
        order.first_name = request.POST.get("first_name")
        order.last_name = request.POST.get("last_name")
        order.email = request.POST.get("email")
        order.address = request.POST.get("address")
        order.address2 = request.POST.get("address2")
        order.country = request.POST.get("country")
        order.city = request.POST.get("city")
        order.postcode = request.POST.get("postcode")
        total = 0
        for item in request.session.get("cart", []):
            total = total + item["price"]
        order.total_price = total
        order.save()
        for item in request.session.get("cart", []):
            order_item = OrderItems()
            order_item.product_id = item["id"]
            order_item.order_id = order.id
            order_item.price = item["price"]
            order_item.quantity = item["quantity"]
            order_item.save()
    return HttpResponseRedirect("/")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    form = NewUserForm()
    return render(request, "sign-up.html", {"form": form})


def sign_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
        return HttpResponseRedirect('/')
    return render(request, "sign-in.html")


def sign_out(request):
    logout(request)
    return HttpResponseRedirect("/")


def apply_coupon(request):
    if request.method == "POST":
        input_code = request.POST.get("input_code")
        try:
            coupon = Coupon.verify_code(input_code)
            request.session["coupon_code"] = coupon.code
            messages.success(request, "Coupon applied successfully.")
            return cart(request, coupon_msg="Coupon applied successfully.")
        
        except ValidationError:
            request.session["coupon_code"] = None
            messages.error(request, 'Invalid coupon code')
            return cart(request, coupon_msg='Invalid coupon code')

# TODO: додати сумарну ціну та з знижкою
