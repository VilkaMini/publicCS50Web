from django.http import HttpResponse
from django.shortcuts import render

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
