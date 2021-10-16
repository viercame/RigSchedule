from django.shortcuts import get_object_or_404, redirect, render

from intervenciones.forms import  RigForm
from intervenciones.models import Rig

# Create your views here.

def nuevoRig(request):
    if request.method == 'POST':
        formaRig = RigForm(request.POST)
        if formaRig.is_valid():
            formaRig.save()
            return redirect('inicio_rig')
    else:
        formaRig = RigForm()
    
    return render(request, 'rigs/nuevo.html', {'formaRig': formaRig})


def detalleRig(request, id):
    rig=get_object_or_404(Rig, pk=id)
    return render(request, 'rigs/detalle.html', {'rig': rig})


def editarRig(request, id):
    domicilio = get_object_or_404(Rig, pk=id)

    if request.method == 'POST':
        formaRig = RigForm(request.POST, instance=domicilio)
        if formaRig.is_valid():
            formaRig.save() #Salva cambios en la base de datos
            return redirect('inicio_rig')
    else:
        formaRig = RigForm(instance=domicilio)
        
    return render(request, 'rigs/editar.html', {'formaRig': formaRig})
    

def eliminarRig(request, id):
    rig = get_object_or_404(Rig, pk=id)
    if rig:
        rig.delete()

    return redirect('inicio_rig')


