from django.db import models

# Create your models here.
class Kind(models.Model):
    kind = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.kind}"

class Size(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.size}"

class Pizza(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    name = models.TextField(max_length=11, default="Default")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.FloatField(default=10)

    def __str__(self):
        return f"{self.kind},{self.name}, {self.size}"

class Toppings(models.Model):
    topping =  models.CharField(max_length=16)

    def __str__(self):
        return f"{self.topping}"

class Sub(models.Model):
    sub = models.CharField(max_length=25)
    smallPrice = models.FloatField(default=6.50)
    largePrice = models.FloatField(default=7.95)

    def __str__(self):
        return f"{self.sub}"

class Pasta(models.Model):
    pasta = models.CharField(max_length=24)
    price = models.FloatField(default=8.75)

    def __str__(self):
        return f"{self.pasta}"

class Salads(models.Model):
    salad = models.CharField(max_length=12)
    price = models.FloatField(default=8.25)

    def __str__(self):
        return f"{self.salad}"

class Dinner(models.Model):
    plate = models.CharField(max_length=13)
    smallPrice = models.FloatField(default=40)
    largePrice = models.FloatField(default=65)

    def __str__(self):
        return f"{self.plate}"

class OrderCart(models.Model):
    name = models.CharField(max_length=100)
    orders = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name}, {self.orders}"

############################################################