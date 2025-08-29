from django.contrib import admin
from django.urls import path
from escola.views import EstudanteViewSet, CursoViewSet
from rest_framework import routers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("estudantes/", estudantes) # type: ignore
]
