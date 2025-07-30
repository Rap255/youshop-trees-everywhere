from django.urls import path
from trees import views

urlpatterns = [
    path("register-tree",views.resgister_tree,name="register_tree"),
    path("register-planted-tree",views.resgister_plantedtree,name="resgister_plantedtree"),
    path("list-tree",views.list_trees,name="list_trees"),
    path("detail-tree/<int:id>",views.details_trees,name="detail_tree"),
    path("detail-planted-tree/<int:id>",views.details_planed_tree_by_id,name="detail_planted_tree"),
    path("list-my-tree/<int:id>",views.list_my_trees,name="list_my_trees"),
    path("list-my-accounts/<int:id>",views.list_my_accounts,name="list_my_accounts")
]
