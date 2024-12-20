from django.contrib import admin
from orders.models import Order, OrderItem


class OrderrItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["car"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderrItemInline]
