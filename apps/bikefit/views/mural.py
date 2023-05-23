from django.shortcuts import render
from django.contrib import messages
from apps.bikefit.models import ModelMural
from apps.bikefit.forms import MuralForm


def mural_de_mensagens(request):
    if request.method == 'POST':
        form = MuralForm(request.POST)
        if form.is_valid():
            post = {'nome': request.POST['nome'], 'email': request.POST['email'], 'mensagem': request.POST['mensagem']}
            ModelMural.objects.create(**post)
            messages.success(request, 'Mensagem postada com sucesso!')
        else:
            messages.error(request, 'Atenção: este mural não aceita links.')

    postagens = ModelMural.objects.order_by('-id').all().values()

    form = MuralForm()
    return render(request, 'bikefit/muraldemensagens.html', {'form': form, 'postagens': postagens})
