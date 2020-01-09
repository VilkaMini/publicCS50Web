from django.contrib import admin
from .models import Toppings, Pizza

# Register your models here.
admin.site.register(Toppings)
admin.site.register(Pizza)