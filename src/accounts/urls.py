from django.urls import path
from accounts import views

urlpatterns = [
    path("register-account",views.resgister_account,name="register_account"),
    path("list-accounts",views.list_accounts,name="list_accounts"),
    path("status-account/<int:id>",views.change_status_account,name="change_status_account"),
]