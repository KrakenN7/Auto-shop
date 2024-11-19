from decimal import Decimal

from django.conf import settings

from main.models import Cars


class Cart:
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, car, quantity=1, override_quantity=False):
        car_id = str(car.id)
        if car_id not in self.cart:
            self.cart[car_id] = {
                "quantity": 0,
                "price": str(car.price),
            }
        if override_quantity:
            self.cart[car_id]["quantity"] = quantity
        else:
            self.cart[car_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, car):
        car_id = str(car.id)
        if car_id in self.cart:
            del self.cart[car_id]
            self.save()

    def __iter__(self):
        car_ids = self.cart.keys()
        cars = Cars.objects.filter(id__in=car_ids)
        cart = self.cart.copy()
        for car in cars:
            cart[str(car.id)]["car"] = car
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
