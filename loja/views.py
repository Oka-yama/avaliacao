from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def sobre(request):
    return render(request, 'app/sobre.html')

def catalogo(request):
    return render(request, 'app/catalogo.html')

def contato(request):
    return render(request, 'app/contato.html')