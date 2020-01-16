from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Toppings, Sub, Pasta, Salads, Dinner

# Create your views here.
def index(request):
    context = {
        "toppings": Toppings.objects.all(),
        "Sub": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salads.objects.all(),
        "Dinner": Dinner.objects.all(),
    }
    return render(request, "orders/index.html", context)
def register(request):
    username = request.POST("username")
    password = request.POST("password")
    email = request.POST("email")
    first_name = request.POST("firstName")
    last_name = request.POST("lastName")
    

def login(request):
    username = request.POST("username")
    password = request.POST("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

def menu(request):
    context = {
        "toppings": Toppings.objects.all(),
        "Sub": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salads.objects.all(),
        "Dinner": Dinner.objects.all(),
    }
    return render(request, "orders/index.html", context)