from django.urls import path
from trees import views

urlpatterns = [
    path("register-tree",views.resgister_tree,name="register_tree"),
    path("list-tree",views.list_trees,name="list_trees"),
    path("dateail-tree/<int:id>",views.details_trees,name="detail_tree")
]