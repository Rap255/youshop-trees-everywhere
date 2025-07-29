from django.urls import path
from accounts import views

urlpatterns = [
    path("register-account",views.resgister_account,name="register_account"),
]