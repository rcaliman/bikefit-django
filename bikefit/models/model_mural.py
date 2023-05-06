from django.db import models
from datetime import datetime


class ModelMural(models.Model):
    mensagem = models.TextField(null=False)
    nome = models.TextField(null=False)
    email = models.TextField(null=False)
    data = models.DateField(default=datetime.now)

    def __str__(self):
        return self.mensagem[0:20]

    class Meta:
        verbose_name = 'postagem'
        verbose_name_plural = "postagens"
