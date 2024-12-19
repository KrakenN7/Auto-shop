from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from orders.models import Order, OrderItem


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.Post)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password "]
            user = auth.authenticate(
                username=username,
                password=password,
            )
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:car"))
    else:
        form = UserLoginForm()

    context = {"forms": form}

    return render(request, "users/login.html", context)


def registartion(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request,
                f"Пользователь {user.username} был успешно зарегестрирован",
            )
            return redirect(reverse("user:login"))
        else:
            form = UserRegistrationForm()
    return render(request, "users.registartion.html")


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Провиль был изменён",
            )
            return HttpResponseRedirect(reverse("user:profile"))
        else:
            form = ProfileForm(isinstance=request.user)

        orders = (
            Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "items", queryset=OrderItem.objects.select_related("car")
                )
            )
            .order_by("id")
        )

        context = {"form": form, "orders": orders}
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:car_list"))
