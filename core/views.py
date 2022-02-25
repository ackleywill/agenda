from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

'''
def eventos(request, titulo):
    consulta = Evento.objects.get(titulo=titulo)

    return HttpResponse(consulta.titulo.local + " Foi!")
'''

#def index(request):
#    return redirect('/agenda/')


def lista_eventos(request):
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html',dados)
