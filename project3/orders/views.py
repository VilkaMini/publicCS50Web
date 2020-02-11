from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import Toppings, Sub, Pasta, Salads, Dinner, Size, Kind, Pizza, OrderCart

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    if not request.session:
        request.session["saved"] = []
        request.session["total"] = []

    context = menuHelper()
    context["ordered"] = request.session.get("saved", [])
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

def cart(request):
    context = menuHelper()
    saved_list = request.session.get("saved", [])
    name = request.user.get_full_name()
    cart = OrderCart(name=name)
    cart.orders = saved_list
    cart.save()
    request.session["saved"] = []
    request.session["total"] = []
    return render(request, "orders/index.html", context)

def pizza(request):
    kind = request.POST["pizzaKind"]
    size = request.POST["pizzaSize"]
    name = request.POST["pizzaName"]
    if name == "1 topping":
        topping1 = request.POST["topping1"]
        topping2 = '0'
        topping3 = '0'
    elif name == "2 toppings":
        topping1 = request.POST["topping1"]
        topping2 = request.POST["topping2"]
        topping3 = '0'
    elif name == "3 toppings":
        topping1 = request.POST["topping1"]
        topping2 = request.POST["topping2"]
        topping3 = request.POST["topping3"]
    else:
        topping1 = '0'
        topping2 = '0'
        topping3 = '0'
    price = Pizza.objects.all().filter(name=name, kind__kind=kind, size__size=size)
    price = price.values_list("price", flat=True)[0]
    context = menuHelper()
    saved_list = request.session.get("saved", [])
    saved_list.append([kind, size, name, topping1, topping2, topping3, str(price)])
    request.session["saved"] = saved_list
    totals = request.session.get("total", [])
    if len(totals) == 0:
        totals.append(price)
        request.session["total"] = totals
    else:
        totals[0] = totals[0] + price
    context["total"] = request.session.get("total", [])
    context["ordered"] = request.session.get("saved", [])
    return render(request, "orders/index.html", context)

def sub(request):
    size = request.POST["subSize"]
    name = request.POST["subName"]
    price = Sub.objects.all().filter(sub=name)
    if size == "Small":
        price = price.values_list("smallPrice", flat=True)[0]
    else:
        price = price.values_list("largePrice", flat=True)[0]
    context = menuHelper()
    saved_list = request.session.get("saved", [])
    saved_list.append([size, name, str(price)])
    request.session["saved"] = saved_list
    totals = request.session.get("total", [])
    if len(totals) == 0:
        totals.append(price)
        request.session["total"] = totals
    else:
        totals[0] = totals[0] + price
    context["total"] = request.session.get("total", [])
    context["ordered"] = request.session.get("saved", [])
    return render(request, "orders/index.html", context)

def pasta(request):
    name = request.POST["pastaName"]
    price = Pasta.objects.all().filter(pasta=name)
    price = price.values_list("price", flat=True)[0]
    context = menuHelper()
    saved_list = request.session.get("saved", [])
    saved_list.append([name, str(price)])
    request.session["saved"] = saved_list
    totals = request.session.get("total", [])
    if len(totals) == 0:
        totals.append(price)
        request.session["total"] = totals
    else:
        totals[0] = totals[0] + price
    context["total"] = request.session.get("total", [])
    context["ordered"] = request.session.get("saved", [])
    return render(request, "orders/index.html", context)

def salad(request):
    name = request.POST["saladName"]
    price = Salads.objects.all().filter(salad=name)
    price = price.values_list("price", flat=True)[0]
    context = menuHelper()
    saved_list = request.session.get("saved", [])
    saved_list.append([name, str(price)])
    request.session["saved"] = saved_list
    totals = request.session.get("total", [])
    if len(totals) == 0:
        totals.append(price)
        request.session["total"] = totals
    else:
        totals[0] = totals[0] + price
    context["total"] = request.session.get("total", [])
    context["ordered"] = request.session.get("saved", [])
    return render(request, "orders/index.html", context)

def dinner(request):
    size = request.POST["dinnerSize"]
    name = request.POST["dinnerName"]
    price = Dinner.objects.all().filter(plate=name)
    if size == "Small":
        price = price.values_list("smallPrice", flat=True)[0]
    else:
        price = price.values_list("largePrice", flat=True)[0]
    context = menuHelper()
    saved_list = request.session.get("saved", [])
    saved_list.append([size, name, str(price)])
    request.session["saved"] = saved_list
    totals = request.session.get("total", [])
    if len(totals) == 0:
        totals.append(price)
        request.session["total"] = totals
    else:
        totals[0] = totals[0] + price
    context["total"] = request.session.get("total", [])
    context["ordered"] = request.session.get("saved", [])
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
