from django.db import models


class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ra = models.CharField(max_length=128)
    curso = models.CharField(max_length=128)


def __str__(self):
    return self.nome