from django.http.response import HttpResponse
from django.shortcuts import render
from intervenciones.models import Intervencion, Rig



# Create your views here.

def bienvenido(request):
#    mensajes = {'msg1' : 'Valor mensaje 1', 'msg2':'Valor mensaje 2'}
    no_intervenciones = Intervencion.objects.count()
    #personas = Persona.objects.all()
    intervenciones = Intervencion.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_intervenciones': no_intervenciones, 'intervenciones':intervenciones})
    #return render(request, 'bienvenido.html', mensajes)

def rigs(request):
#    mensajes = {'msg1' : 'Valor mensaje 1', 'msg2':'Valor mensaje 2'}
    no_rigs = Rig.objects.count()
    #domicilios = Domicilio.objects.all()
    rigs = Rig.objects.order_by('id')
    return render(request, 'rigs.html', {'no_rigs': no_rigs, 'rigs':rigs})



# def despedirse(request):
#     return HttpResponse('Despedida desde Django')
