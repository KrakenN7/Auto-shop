from django.shortcuts import render

from orders.models import OrderItem
from orders.forms import OrderCreatetForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreatetForm(request.POST, request=request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    car=item["car"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()

            context = {
                "order": order,
                "form": form,
            }

            return render(request, "order/createed.html", context)

    else:
        form = OrderCreatetForm(request=request)
        context = {"cart": cart, "form": form}
        return render(request, "order/created.html", context)
