from django.contrib import admin
from .models import Toppings, Pizza, Size, Kind, Sub, Pasta, Salads, Dinner

# Register your models here.
admin.site.register(Toppings)
admin.site.register(Size)
admin.site.register(Kind)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner)