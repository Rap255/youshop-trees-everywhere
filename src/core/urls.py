from django.urls import path
from core import views

urlpatterns = [
    path("login",views.login,name="login"),
    path("home",views.home,name="home"),
    path("home-standard",views.home_user_standard,name="home-standard"),
]