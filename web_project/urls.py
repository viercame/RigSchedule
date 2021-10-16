"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from intervenciones.views import detalleIntervencion, editarIntervencion, eliminarIntervencion, nuevaIntervencion
from rigs.views import detalleRig, editarRig, nuevoRig

#from webapp.views import bienvenido, despedirse
from webapp.views import bienvenido, rigs


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bienvenido/', bienvenido)
    path('', bienvenido, name='index'),
    #path('despedida', despedirse)
    path('detalle_intervencion/<int:id>', detalleIntervencion),
    path('detalle_rig/<int:id>', detalleRig),
    path('nueva_intervencion', nuevaIntervencion),
    path('nuevo_rig', nuevoRig),
    path('editar_intervencion/<int:id>', editarIntervencion),
    path('editar_rig/<int:id>', editarRig),
    path('eliminar_intervencion/<int:id>', eliminarIntervencion),
    path('eliminar_rig/<int:id>', eliminarIntervencion),
    path('gestion_rigs', rigs, name='inicio_rig'),
    
]
