from django.db import models

# Create your models here.

class Estudante(models.Model):
    nome = models.CharField()
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome