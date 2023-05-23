from django.urls import path
from .views import bikefit_home, bikefit_resultado, calculos_anteriores, mural_de_mensagens, links, sobre

urlpatterns = [
    path('', bikefit_home, name='bikefit'),
    path('resultadobikefit/', bikefit_resultado, name='resultadobikefit'),
    path('calculosanteriores/', calculos_anteriores, name='calculosanteriores'),
    path('muraldemensagens/', mural_de_mensagens, name='muraldemensagens'),
    path('links/', links, name='links'),
    path('sobre/', sobre, name='sobre'),
]
