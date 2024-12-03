from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect

from users.forms import UserLoginForm


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
    return render(request, "users.registartion.html")


def profile(request):
    return render(request, "users/profile.html")


def logout(request):
    pass
