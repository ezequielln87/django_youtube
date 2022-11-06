from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from cliente.serializers import ClienteSerializer

from cliente.models import Cliente

class ClientesAPIv2ViewSet(ModelViewSet):
    queryset = Cliente.objects.all()

    serializer_class = ClienteSerializer
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

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            request.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def partial_update(self, request, *args, **kwargs):
        atendente = self.get_object()
        serializer = ClienteSerializer(
            instance=atendente,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )
    
    
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/cliente-list/",
        "Detail View": "/cliente-detail/<str:pk>/",
        "Create": "/cliente-create/",
        "Update": "/cliente-update/<str:pk>/",
        "Delete": "/cliente-delete/<str:pk>/",
    }
    return Response(api_urls)
    

@api_view(["GET"])
def clienteList(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def clienteDetail(request, pk):
    clientes = Cliente.objects.get(id=pk)
    serializer = ClienteSerializer(clientes, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def clienteCreate(request):
    serializer = ClienteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["PATCH"])
def clienteUpdate(request, pk):
    cliente = Cliente.objects.get(id=pk)
    serializer = ClienteSerializer(instance=cliente, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def clienteDelete(request, pk):
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()

    return Response("Item successfully deleted!")
