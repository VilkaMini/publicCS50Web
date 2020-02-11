from django.contrib import admin
from .models import Toppings, Pizza, Size, Kind, Sub, Pasta, Salads, Dinner, OrderCart

# Register your models here.
admin.site.register(Toppings)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner)
admin.site.register(Sub)
admin.site.register(Pizza)
admin.site.register(OrderCart)