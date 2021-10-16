from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory
from intervenciones.forms import IntervencionForm
from intervenciones.models import Intervencion
# Create your views here.

def detalleIntervencion(request, id):
    #persona = Persona.objects.get(pk=id)
    intervencion=get_object_or_404(Intervencion, pk=id)
    return render(request, 'intervenciones/detalle.html', {'intervencion': intervencion})

#PersonaForm = modelform_factory(Persona, exclude=[])



def nuevaIntervencion(request):
    if request.method == 'POST':
        formaIntervencion = IntervencionForm(request.POST)
        if formaIntervencion.is_valid():
            formaIntervencion.save()
            return redirect('index')
    else:
        formaIntervencion = IntervencionForm()
    
    return render(request, 'intervenciones/nuevo.html', {'formaIntervencion': formaIntervencion})

def editarIntervencion(request, id):
    intervencion = get_object_or_404(Intervencion, pk=id)

    if request.method == 'POST':
        formaIntervencion = IntervencionForm(request.POST, instance=intervencion)
        if formaIntervencion.is_valid():
            formaIntervencion.save() #Salva cambios en la base de datos
            return redirect('index')
    else:
        formaIntervencion = IntervencionForm(instance=intervencion)
    
    return render(request, 'intervenciones/editar.html', {'formaIntervencion': formaIntervencion})


def eliminarIntervencion(request, id):
    intervencion = get_object_or_404(Intervencion, pk=id)
    if intervencion:
        intervencion.delete()

    return redirect('index')

