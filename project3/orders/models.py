from django.db import models

# Create your models here.
class Kind(models.Model):
    kind = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.kind}"

class Size(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.size}"

class Toppings(models.Model):
    topping =  models.CharField(max_length=16)

    def __str__(self):
        return f"{self.topping}"

class Pizza(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping1 = models.ForeignKey(Toppings, on_delete=models.CASCADE, blank=True, related_name="Topping1") 
    topping2 = models.ForeignKey(Toppings, on_delete=models.CASCADE, blank=True, related_name="Topping2")
    topping3 = models.ForeignKey(Toppings, on_delete=models.CASCADE, blank=True, related_name="Topping3")

    def __str__(self):
        return f"{self.kind}, {self.size}, {self.topping1}, {self.topping2}, {self.topping3}"