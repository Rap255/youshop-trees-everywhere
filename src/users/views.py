from django.shortcuts import render, redirect
from users.controllers import UsersControllers
from django.contrib.auth import login as login_django, logout
from services.utils import form_formatter
from django.contrib.auth.decorators import login_required
from accounts.controllers import AccountsControllers


@login_required
def resgister_users(request):
    if request.method == "GET":
        return render(
            request,"register_user.html",{"user_access":request.user.type_of_access.id,"accounts":AccountsControllers.list_accounts({"per_page":100})["accounts"]}
        )
    if request.method == "POST":
        request_json = form_formatter(request.POST)
        request_json["username"] = request_json["email"]
        if user_obj := UsersControllers.create_user(request_json):
            return redirect("list_users")
        else:
            return redirect("register_user")
        

@login_required
def list_users(request):
    if request.method == "GET":
        request_filter = {
            "per_page":100
        }
        return render(
            request,"list_users.html",{"user_access":request.user.type_of_access.id,"users":UsersControllers.list_users(request_filter)["users"]}
        )
    