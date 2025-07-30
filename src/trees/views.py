from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.utils import form_formatter
from trees.controllers import TreesControllers

@login_required
def list_trees(request):
    if request.method == "GET":
        request_filter = {
            "per_page":20
        }
        return render(
            request,"list_plants.html",{"user_access":request.user.type_of_access.id,"trees":TreesControllers.list_trees(request_filter)["trees"]}
        )
    

@login_required
def resgister_tree(request):
    if request.method == "GET":
        return render(
            request,"register_plant.html",{"user_access":request.user.type_of_access.id}
        )
    if request.method == "POST":
        request_json = form_formatter(request.POST)
        if tree_obj := TreesControllers.create_tree(request_json):
            return redirect("list_trees")
        else:
            return redirect("register_tree")
