from django.http import JsonResponse
from .models import Disciplinas


def listar_disciplinas(request):
    disciplinas = Disciplinas.objects.all().values('id','nome', 'codigo', 'professor', 'periodo')
    return JsonResponse(list(disciplinas), safe=False)