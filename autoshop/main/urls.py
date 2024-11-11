from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.popular_list, name="popularlist"),
    path("shop", views.car_list, name="car_list"),
    path(
        "shop/category/<slug:category_slug>",
        views.car_list,
        name="car_list_by_category",
    ),
    path("<slug:slug>/", views.car_detail, name="car_detail"),
]
