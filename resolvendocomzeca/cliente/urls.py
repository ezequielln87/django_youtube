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
    # path("list/", site.ClienteListView.as_view(), name="list"),
    # path("add/", site.ClienteCreateView.as_view(), name="add"),
    # path("edit/<int:pk>/", site.ClienteUpdateView.as_view(), name="edit"),
    # path("delete/<int:pk>/", site.ClienteDeleteView.as_view(), name="delete"),
    # path("detail/<int:pk>/", site.ClienteDetailView.as_view(), name="detail"),
    # path("search/", site.ClienteSearchView.as_view(), name="search"),
    path("api/", views.apiOverview, name="api-overview"),
    path("api/clientelist/", views.clienteList, name="api-list"),
    path("api/clientedetail/<str:pk>/", views.clienteDetail, name="api-detail"),
    path("api/clientecreate/", views.clienteCreate, name="api-create"),
    path("api/clienteupdate/<str:pk>/", views.clienteUpdate, name="api-update"),
    path("api/clientedelete/<str:pk>/", views.clienteDelete, name="api-delete"),
]