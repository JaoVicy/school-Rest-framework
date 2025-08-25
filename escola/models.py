from django.db import models

# Create your models here.

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(blank = False)
    cpf = models.CharField(max_length=11, unique=True)
    data_nacimento = models.DateField(null=True, blank=True)
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, blank=False)
    nivel = models.CharField(max_length=1, null=False, blank=False, choices = NIVEL, default = 'B')
    carga_horaria = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome