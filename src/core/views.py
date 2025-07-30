from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=username,password=password)
        if user:
            login_django(request, user)
            if request.user.type_of_access.id == 1:
                return redirect("home")
            else:
                return redirect("home_standard")
        else:
            return HttpResponse("Email ou senha invalido")

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.method == "GET":
        return render(
            request,"dashboard.html",{
                    "user_access":request.user.type_of_access.id,
                    "user_id":request.user.id,
                }
        )
    
@login_required
def home_user_standard(request):
    if request.method == "GET":
        return render(
            request,"home_user.html",{
                    "user_access":request.user.type_of_access.id,
                    "user_id":request.user.id
                }
        )