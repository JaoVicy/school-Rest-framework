from rest_framework import serializers
from .models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'idade', 'email', 'cpf', 'data_nacimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.ReadOnlyField() #Campo referente ao get_periodo_display

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj): # A def esta referênciando o campo periodo, o get_ + nome do campo, é a convenção
        return obj.get_periodo_display() # Pega o valor legível do campo periodo (com o uso do display)