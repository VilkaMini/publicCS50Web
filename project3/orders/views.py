from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import Toppings, Sub, Pasta, Salads, Dinner

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = {
        "toppings": Toppings.objects.all(),
        "Sub": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salads.objects.all(),
        "Dinner": Dinner.objects.all(),
    }
    return render(request, "orders/index.html", context)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        if User.objects.filter(username=username).exists():
            return render(request, "orders/register.html", {"message": "Username Exists"})
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return render(request, "orders/login.html")
    else:
        return render(request, "orders/register.html")


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials"})
    else:
        return render(request, "orders/login.html")


def logoutUser(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged Out"})


def menu(request):
    context = {
        "toppings": Toppings.objects.all(),
        "Sub": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salads.objects.all(),
        "Dinner": Dinner.objects.all(),
    }
    return render(request, "orders/index.html", context)