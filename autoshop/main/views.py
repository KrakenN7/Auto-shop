from django.shortcuts import render, get_object_or_404

from main.models import Cars, CarSpecifications, Category


def popular_list(request):
    cars = Cars.objects.filter(available=True)[:3]
    return render(
        request,
        "main/index/index.html",
        {"cars": cars},
    )


def car_detail(request, slug):
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

    return render(
        request,
        "main/car/detail.html",
        context,
    )


def car_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cars = Cars.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(
            Category,
            slug=category_slug,
        )
        cars = cars.filter(category=category)

    context = {
        "category": category,
        "categories": categories,
        "cars": cars,
    }
    return render(
        request,
        "main/car/list.html",
        context,
    )
