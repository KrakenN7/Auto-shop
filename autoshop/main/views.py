from django.shortcuts import render, get_list_or_404
from main.models import Cars


def popular_list(request):
    cars = Cars.objects.filter(available=True)[:3]
    return render(
        request,
        "main/index/index.html",
        {"cars": cars},
    )


def cars_details(request, slug):
    car = get_list_or_404(
        Cars,
        slug=slug,
        available=True,
    )
    return render(request, "main/car/detail.html", {"car": car})
