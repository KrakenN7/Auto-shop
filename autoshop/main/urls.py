from django.urls import path

from main import views

urlpatterns = [
    path("", views.popular_list, name="popularlist"),
    path("<slug:slug>/", views.cars_details, name="car_datail"),
]
