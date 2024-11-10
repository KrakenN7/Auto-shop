from django.urls import path

from main import views

urlpatterns = [
    path("", views.popular_list, name="popularlist"),
    path("<slug:slug>/", views.car_details, name="car_datail"),
]
