from django.db import models
from alunos.models import Alunos
from disciplinas.models import Disciplinas

class Avaliacoes(models.Model):
   
    STATUS_CHOICES = [
    ('PENDENTE','Pendente'), 
    ('RESPONDIDA','Respondida'), ]
    data = models.DateField()
    comentario = models.CharField(max_length=200)
    nota = models.DecimalField(max_digits=5,decimal_places=2)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='PENDENTE')

    
    aluno = models.ForeignKey(Alunos,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aluno} - {self.nota}"