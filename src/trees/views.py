from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.utils import form_formatter
from trees.controllers import TreesControllers
from accounts.controllers import AccountsControllers

@login_required
def list_trees(request):
    if request.method == "GET":
        request_filter = {
            "per_page":20
        }
        return render(
            request,"list_plants.html",{
                    "user_access":request.user.type_of_access.id,
                    "trees":TreesControllers.list_trees(request_filter)["trees"],
                    "user_id":request.user.id
                }
        )

@login_required
def list_my_trees(request,id):
    if request.method == "GET":
        request_filter = {
            "per_page":20
        }
        return render(
            request,"list_my_trees.html",{
                    "user_access":request.user.type_of_access.id,
                    "planted_trees":TreesControllers.list_my_trees(request_filter,id)["trees"],
                    "user_id":request.user.id
                }
        )
    
@login_required
def list_my_accounts(request,id):
    if request.method == "GET":
        request_filter = {
            "per_page":20
        }
        return render(
            request,"list_my_accounts.html",{
                    "user_access":request.user.type_of_access.id,
                    "accounts":AccountsControllers.list_accounts_by_user(id_user=request.user.id),
                    "user_id":request.user.id
                }
        )

@login_required
def resgister_tree(request):
    if request.method == "GET":
        return render(
            request,"register_plant.html",{
                    "user_access":request.user.type_of_access.id,
                    "user_id":request.user.id
                }
        )
    if request.method == "POST":
        request_json = form_formatter(request.POST)
        if tree_obj := TreesControllers.create_tree(request_json):
            return redirect("list_trees")
        else:
            return redirect("register_tree")

@login_required
def details_trees(request,id):
    if request.method == "GET":
        request_filter = {
            "per_page":100
        }

        return render(
            request,"list_planted_trees.html",{
                    "user_access":request.user.type_of_access.id,
                    "planted_trees":TreesControllers.list_planted_trees(request_filter,id)["planted_trees"],
                    "user_id":request.user.id
                }
        )
    
@login_required
def details_planed_tree_by_id(request,id):
    if request.method == "GET":
        request_filter = {
            "per_page":100
        }

        return render(
            request,"planted_tree_detail.html",{
                    "user_access":request.user.type_of_access.id,
                    "planted_tree":TreesControllers.list_planted_tree_by_id(id),
                    "user_id":request.user.id
                }
        )

@login_required
def resgister_plantedtree(request):
    if request.method == "GET":
        user_id = request.user.id
        request_filter = {
            "per_page":100
        }
        return render(
            request,"register_planted_tree.html",
            {
                "user_access":request.user.type_of_access.id,
                "accounts":AccountsControllers.list_accounts_by_user(user_id),
                "trees":TreesControllers.list_trees(request_filter)['trees'],
                "user_id":request.user.id
            }
        )
    if request.method == "POST":
        request_json = form_formatter(request.POST)
        request_json['user_id'] = user_id = request.user.id
        if tree_obj := TreesControllers.plant_tree(request_json):
            return redirect("home_standard")
        else:
            return redirect("resgister_plantedtree")