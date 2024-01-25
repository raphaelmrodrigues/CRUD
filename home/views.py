from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def home(request):
    status = request.GET.get('status')
    usuario = Usuario.objects.get(id = request.session['usuario'])
    usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'usuarios': usuarios,
                                         'usuario': usuario,
                                         'usuario_logado': request.session.get('usuario'),
                                         'status': status})

def excluir_usuario(request):
    pass

def adicionar_usuario(request):
    pass

def editar_usuario(request):
    pass