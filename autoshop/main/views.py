from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

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
    page = request.GET.get("page", 1)
    category = None
    categories = Category.objects.all()
    cars = Cars.objects.filter(available=True)
    paginator = Paginator(cars, 2)
    current_page = paginator.page(int(page))

    if category_slug:
        category = get_object_or_404(
            Category,
            slug=category_slug,
        )
        paginator = Paginator(cars.filter(category))
        current_page = paginator.page(int(page))

    context = {
        "category": category,
        "categories": categories,
        "cars": current_page,
        "slug_url": category_slug,
    }
    return render(
        request,
        "main/car/list.html",
        context,
    )
