from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from services.utils import form_formatter
from accounts.controllers import AccountsControllers

@login_required
def resgister_account(request):
    if request.method == "GET":
        return render(
            request,"register_account.html",{"user_access":request.user.type_of_access.id}
        )
    if request.method == "POST":
        request_json = form_formatter(request.POST)
        if account_obj := AccountsControllers.create_account(request_json):
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