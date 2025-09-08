from rest_framework import serializers
from .models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'idade', 'email', 'cpf', 'data_nacimento', 'celular']

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve conter exatamente 11 caracteres.")
        return cpf
    
    def validate_nome(self, name):
        if not name.isalpha():
            raise serializers.ValidationError("O nome deve conter apenas letras.")
        return name

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
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']