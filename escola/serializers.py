from rest_framework import serializers
from .models import Estudante, Curso, Matricula
from .validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'idade', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        if cpf_invalido(dados['cpf']) != 11:
            raise serializers.ValidationError({"cpf": "O CPF deve ser válido e conter exatamente 11 caracteres."})
        
        if nome_invalido(dados['name']):
            raise serializers.ValidationError({"nome": "O nome deve conter apenas letras."})
        
        if celular_invalido(dados['celular']) != 13:
            raise serializers.ValidationError({"celular": "O celular deve seguir o modelo padrão."})
        
        return dados

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve conter exatamente 11 caracteres.")
        return cpf
    
    def validate_nome(self, name):
        if not name.isalpha():
            raise serializers.ValidationError("O nome deve conter apenas letras.")
        return name
    
    def validade_celular(self,celular):
        if len(celular) != 13:
            raise serializers.ValidationError("O celular deve conter no mínimo 13 caracteres.")
        return celular

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