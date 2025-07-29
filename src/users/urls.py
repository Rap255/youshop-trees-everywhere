from django.urls import path
from users import views

urlpatterns = [
    path("register-user",views.resgister_users,name="register_user"),
    path("list-user",views.list_users,name="list_users")
]