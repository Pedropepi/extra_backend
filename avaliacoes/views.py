from django.http import JsonResponse
from .models import Avaliacoes


def listar_avaliacoes(request):
    avaliacoes = Avaliacoes.objects.all().values('id','nota', 'comentario', 
                                                 'status', 'data', 'aluno', 'disciplina')
    return JsonResponse(list(avaliacoes), safe=False)