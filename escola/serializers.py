from rest_framework import serializers
from .models import Estudante, Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        field = ['id', 'nome', 'idade', 'email', 'cpf', 'data_nacimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        field = "__all__"