from django.contrib import admin

# Register your models here.

from .models import Estudante, Curso

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'email', 'cpf', 'data_nacimento', 'celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao',)
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('codigo',)