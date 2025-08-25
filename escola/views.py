from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            "id": 1,
            "nome": "João da Silva",
            "idade": 20,
            "curso": "Engenharia de Software"
        }
        return JsonResponse(estudante)