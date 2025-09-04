from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAdminUser] # Apenas administradores podem acessar
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticatedOrReadOnly] # Qualquer usuário autenticado pode criar, mas apenas leitura para não autenticados
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']) # Filtra as matrículas pelo ID do estudante
        return queryset
    serializer_class = ListMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']) # Filtra as matrículas pelo ID do curso
        return queryset
    serializer_class = ListaMatriculasCursoSerializer