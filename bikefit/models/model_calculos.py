from django.db import models
from datetime import datetime


class ModelCalculos(models.Model):
    data = models.DateTimeField(default=datetime.now)
    cavalo = models.FloatField(null=False, blank=False)
    esterno = models.FloatField(null=False, blank=False)
    braco = models.FloatField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'calculo'

    class Meta:
        verbose_name_plural = "Cálculos"
