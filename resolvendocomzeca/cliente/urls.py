from django.urls import path
from .views import site 
from cliente import views

app_name = "cliente"

from django.views.generic import TemplateView

# search
# add
# edit
# delete
# list

urlpatterns = [
    path("api/list/", views.ClientesAPIv2ViewSet.as_view({"get": "list"}), name="api_list"),
    path("api/add/", views.ClientesAPIv2ViewSet.as_view({"post": "create"}), name="api_add"),
    path("api/edit/<int:pk>/", views.ClientesAPIv2ViewSet.as_view({"patch": "partial_update"}), name="api_edit"),
    path("api/delete/<int:pk>/", views.ClientesAPIv2ViewSet.as_view({"delete": "destroy"}), name="api_delete"),

    path("api/client/list/", views.ClientesAPIv2ViewSet.as_view({"get": "list"}), name="api_list"),
    path("api/client/add/", views.ClientesAPIv2ViewSet.as_view({"post": "create"}), name="api_add"),
    path("api/client/edit/<int:pk>/", views.ClientesAPIv2ViewSet.as_view({"patch": "partial_update"}), name="api_edit"),
    path("api/client/delete/<int:pk>/", views.ClientesAPIv2ViewSet.as_view({"delete": "destroy"}), name="api_delete"),
    
    # path("api/user/detail/<int:pk>/", views.PerfilAPIv2ViewSet.as_view({"get": "retrieve"}), name="api_user_detail"),
    # path("api/user/list/", views.PerfilAPIv2ViewSet.as_view({"get": "list"}), name="api_user_list"),

    path("api/", views.apiOverview, name="api-overview"),
    path("api/clientelist/", views.clienteList, name="api-list"),
    path("api/clientedetail/<str:pk>/", views.clienteDetail, name="api-detail"),
    path("api/clientecreate/", views.clienteCreate, name="api-create"),
    path("api/clienteupdate/<str:pk>/", views.clienteUpdate, name="api-update"),
    path("api/clientedelete/<str:pk>/", views.clienteDelete, name="api-delete"),
]