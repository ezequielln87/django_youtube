from rest_framework import serializers
from cliente.models import Cliente
# from django.contrib.auth.models import User


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "cpf", "email", "telefone"]