from django.urls import path, include
from .views import api 
from usuario import views

app_name = "usuario"

from django.views.generic import TemplateView

urlpatterns = [
    path("api/user/detail/<int:pk>/", views.PerfilAPIv2ViewSet.as_view({"get": "retrieve", "patch": "update"}), name="api_user_detail"),
    path("api/user/image/<int:pk>/", views.DetalhesAPIv2ViewSet.as_view({"get": "retrieve"}), name="api_user_image"),
    path("api/user/image-update/<int:pk>/", views.DetalhesAPIv2ViewSet.as_view({"put": "update"}), name="api_user_image_edit"),
    # path("api/user/list/", views.DetalhesAPIv2ViewSet.as_view({"get": "list"}), name="api_user_list"),
    # path("api/user/add/", views.DetalhesAPIv2ViewSet.as_view({"post": "create"}), name="api_user_add"),
    # path("api/user/edit/<int:pk>/", views.DetalhesAPIv2ViewSet.as_view({"patch": "partial_update"}), name="api_user_edit"),
]