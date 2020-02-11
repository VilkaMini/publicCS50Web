from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("pizza", views.pizza, name="pizza"),
    path("sub", views.sub, name="sub"),
    path("pasta", views.pasta, name="pasta"),
    path("salad", views.salad, name="salad"),
    path("dinner", views.dinner, name="dinner"),
    path("cart", views.cart, name="cart"),
]
