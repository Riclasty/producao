from django.shortcuts import render
from bolsa.models import Familia

# Create your views here.


def index(request):
    familias = Familia.objects.all()
    context ={ 'familias': familias}
    return render(request, 'index.html', context)


def only(request, pessoa_id):
    familia = Familia.objects.get(pk=pessoa_id)
    pessoas = familia.pessoas.all()

    return render(
        request,
        'membro.html',
        {
            'familia': familia,
            'pessoas': pessoas
        }
    )