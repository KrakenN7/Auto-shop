from django.shortcuts import render


def login(request):
    return render(request, "users/login.html")


def registartion(request):
    return render(request, "users.registartion.html")


def profile(request):
    return render(request, "users/profile.html")


def logout(request):
    pass
