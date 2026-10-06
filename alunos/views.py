from django.http import JsonResponse
from .models import Alunos


def listar_alunos(request):
    alunos = Alunos.objects.all().values('id','nome', 'email', 'ra', 'curso')
    return JsonResponse(list(alunos), safe=False)