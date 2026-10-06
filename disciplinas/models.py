from django.db import models


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=128)
    professor = models.CharField(max_length=128)
    periodo = models.CharField(max_length=128)


def __str__(self):
    return self.nome