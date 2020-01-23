from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import Toppings, Sub, Pasta, Salads, Dinner, Size, Kind

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = menuHelper()
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


def pizza(request):
    kind = request.POST["pizzaKind"]
    size = request.POST["pizzaSize"]
    name = request.POST["pizzaName"]
    context = menuHelper()
    print(kind, size, name)
    return render(request, "orders/index.html", context)

def sub(request):
    size = request.POST["subSize"]
    name = request.POST["subName"]
    context = menuHelper()
    print(size, name)
    return render(request, "orders/index.html", context)

def pasta(request):
    name = request.POST["pastaName"]
    context = menuHelper()
    print(name)
    return render(request, "orders/index.html", context)

def salad(request):
    name = request.POST["saladName"]
    context = menuHelper()
    print(name)
    return render(request, "orders/index.html", context)

def dinner(request):
    size = request.POST["dinnerSize"]
    name = request.POST["dinnerName"]
    context = menuHelper()
    print(size, name)
    return render(request, "orders/index.html", context)


def menuHelper():
    context = {
        "size": Size.objects.all(),
        "kind": Kind.objects.all(),
        "toppings": Toppings.objects.all(),
        "Sub": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salads.objects.all(),
        "Dinner": Dinner.objects.all(),
    }
    return context
