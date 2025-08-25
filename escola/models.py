from django.db import models

# Create your models here.

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(blank = False)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome