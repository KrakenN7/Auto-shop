from django.contrib import admin
from main.models import Cars, Category, CarSpecifications


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "available",
        "created",
        "updated",
        "discount",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available", "discount"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CarSpecifications)
class CarsSpecificationsAdmin(admin.ModelAdmin):
    list_display = [
        "car_id",
        "name",
        "distance",
        "engine_capacity",
        "engine_power",
        "owners",
        "pts",
        "customs",
        "slug",
    ]
    list_filter = [
        "car_id",
        "name",
        "distance",
        "engine_capacity",
        "engine_power",
        "owners",
        "pts",
        "customs",
        "slug",
    ]
    list_editable = [
        "distance",
        "engine_capacity",
        "engine_power",
        "owners",
        "pts",
        "customs",
    ]
    list_display_links = ["car_id"]
    prepopulated_fields = {"slug": ("name",)}
