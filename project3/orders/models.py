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

class Sub(models.Model):
    sub = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.sub}"

class Pasta(models.Model):
    pasta = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.pasta}"

class Salads(models.Model):
    salad = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.salad}"

class Dinner(models.Model):
    plate = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.plate}"

############################################################
class Pizza(models.Model):
    # user ID
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping1 = models.ForeignKey(Toppings, on_delete=models.CASCADE, blank=True, related_name="Topping1") 
    topping2 = models.ForeignKey(Toppings, on_delete=models.CASCADE, blank=True, related_name="Topping2")
    topping3 = models.ForeignKey(Toppings, on_delete=models.CASCADE, blank=True, related_name="Topping3")

    def __str__(self):
        return f"{self.kind}, {self.size}, {self.topping1}, {self.topping2}, {self.topping3}"

class Subs(models.Model):
    # user ID
    sub = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="Sub")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sub}, {self.size}"

class Pastas(models.Model):
    # user ID
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pasta}"

class Salad(models.Model):
    # user ID
    salad = models.ForeignKey(Salads, on_delete=models.CASCADE, related_name="saladOrder")

    def __str__(self):
        return f"{self.salad}"

class DinnerPlate(models.Model):
    # user ID
    plate = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.plate}, {self.size}"