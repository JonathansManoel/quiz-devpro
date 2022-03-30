from django.db import models


# Create your models here.
from jsonfield import JSONField


class Pergunta(models.Model):
    enunciado = models.TextField()
    disponivel = models.BooleanField(default=False)
    alternativas = JSONField()
    alternativa_correta = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])
