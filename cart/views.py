from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from main.models import Cars
from cart.cart import Cart
from cart.forms import CartAddCarForm


@require_POST
def cart_add(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Cars, id=car_id)
    form = CartAddCarForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            car=car,
            quantity=cd["quantity"],
            override_quantity=cd["override"],
        )
    return redirect("cart:cart_detail")


@require_POST
def cart_remove(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Cars, id=car_id)
    cart.remove(car)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    context = {"cart": cart}
    return render(request, "cart/detail.html", context)
