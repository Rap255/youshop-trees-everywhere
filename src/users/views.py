from django.shortcuts import render, redirect
from users.controllers import UsersControllers
from django.contrib.auth import login as login_django, logout
from services.utils import form_formatter
from django.contrib.auth.decorators import login_required


@login_required
def resgister_users(request):
    if request.method == "GET":
        return render(
            request,"register_account.html",{"user_access":request.user.type_of_access.id}
        )
    if request.method == "POST":
        request_json = form_formatter(request.POST)
        if account_obj := UsersControllers.create_account(request_json):
            return redirect("register_account")
        else:
            return render(
                request,
                "register_account.html",
                {
                    "user_access":request.user.type_of_access.id,
                    "error":account_obj["data"]
                }
            )
        

@login_required
def list_users(request):
    if request.method == "GET":
        request_filter = {
            "per_page":100
        }
        return render(
            request,"list_users.html",{"user_access":request.user.type_of_access.id,"users":UsersControllers.list_users(request_filter)["users"]}
        )
    