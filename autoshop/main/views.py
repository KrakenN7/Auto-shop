from django.shortcuts import render, get_object_or_404

from main.models import Cars, CarSpecifications


def popular_list(request):
    cars = Cars.objects.filter(available=True)[:3]
    return render(
        request,
        "main/index/index.html",
        {"cars": cars},
    )


def car_details(request, slug):
    car = get_object_or_404(
        Cars,
        slug=slug,
        available=True,
    )
    car_specs = CarSpecifications.objects.filter(car_id=car.id)

    context = {
        "car": car,
        "car_specs": car_specs,
    }

    return render(request, "main/car/detail.html", context)
