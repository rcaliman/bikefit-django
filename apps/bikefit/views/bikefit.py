from django.shortcuts import render, redirect
from apps.bikefit.models import ModelCalculos
from apps.bikefit.utils import CalculaBikeFit
from datetime import datetime
from django.utils.timezone import make_aware
from apps.bikefit.forms import MedidasForm
from django.contrib import messages


def bikefit_home(request):
    form = MedidasForm()
    quantidade_calculos_dia = CalculaBikeFit.quantidade_de_calculos_do_dia()
    return render(request, 'bikefit/bikefit.html', {'form': form, 'quantidade_calculos_dia': quantidade_calculos_dia})


def bikefit_resultado(request):
    try:
        if request.method == 'POST':
            form = MedidasForm(request.POST)
            bikefit = CalculaBikeFit(
                cavalo=request.POST['cavalo'],
                esterno=request.POST['esterno'],
                braco=request.POST['braco'],
                email=request.POST['email'],
                data=make_aware(datetime.now()),
            )
            if form.is_valid():
                ModelCalculos.objects.create(**bikefit.dados)
                return render(request, 'bikefit/resultadobikefit.html', {'calculo': {**bikefit.dados, **bikefit.calculos}})
            else:
                messages.error(request, 'Algo está errado. Lembre-se que você deve inserir os dados em centímetros.')
                return redirect('bikefit')
    except ValueError:
        return redirect('bikefit')


def calculos_anteriores(request):
    if request.method == 'POST':
        dados_de_calculos_anteriores = []
        email_consultado = request.POST['email']
        medidas_salvas = ModelCalculos.objects.filter(
            email=email_consultado).order_by('-data').values()
        for medida in medidas_salvas:
            bikefit = CalculaBikeFit(
                cavalo=medida['cavalo'],
                esterno=medida['esterno'],
                braco=medida['braco'],
                data=medida['data'],
            )
            dados_de_calculos_anteriores.append(
                {**bikefit.dados, **bikefit.calculos})
        if len(dados_de_calculos_anteriores) == 0:
            messages.error(request, 'Desculpe mas não encontramos nenhum cálculo salvo')
        return render(request, 'bikefit/calculosanteriores.html', {'calculos': dados_de_calculos_anteriores})
    else:
        return render(request, 'bikefit/calculosanteriores.html')


def links(request):
    return render(request, 'bikefit/links.html')


def sobre(request):
    return render(request, 'bikefit/sobre.html')
