from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from usuario.serializers import PerfilSerializer, UserSerializer
from django.contrib.auth.models import User
from usuario.models import UserProfile


class PerfilAPIv2ViewSet(ModelViewSet):
    queryset = User.objects.all()

    serializer_class = PerfilSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk,
        )

        self.check_object_permissions(self.request, obj)

        return obj


class DetalhesAPIv2ViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk', '')

        obj = get_object_or_404(
            self.get_queryset(),
            user=pk,            
        )        

        self.check_object_permissions(self.request, obj)

        return obj
