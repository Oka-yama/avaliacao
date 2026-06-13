from django.shortcuts import render
from .models import Produto
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def sobre(request):
    return render(request, 'app/sobre.html')

def produtos(request):
    lista_produtos = Produto.objects.filter(disponivel = True)
    contexto = {
        'produtos': lista_produtos
    }
    return render(request, 'app/produtos.html', contexto)

def contato(request):
    return render(request, 'app/contato.html')

@login_required
def painel_interno(request):
    return render(request, 'app/painel_interno.html')