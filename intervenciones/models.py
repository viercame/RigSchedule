from django.db import models

# Create your models here.
class Rig(models.Model):
    rig = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    potencia = models.IntegerField()
    tipoequipo = models.CharField(max_length=255)
    #pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Rig {self.id}: {self.rig} {self.empresa} {self.potencia} {self.tipoequipo}'




class Intervencion(models.Model):
    rig = models.ForeignKey(Rig,on_delete=models.SET_NULL, null=True)
    gerencia = models.CharField(max_length=3)
    vicepresidencia = models.CharField(max_length=3)
    campo = models.CharField(max_length=255)
    pozo = models.CharField(max_length=255)
    tipopozo = models.CharField(max_length=255)
    inicio = models.DateField()
    fin = models.DateField()
    duracion = models.IntegerField()
    entradaproduccion = models.DateField()
    campana = models.CharField(max_length=255)
    subcampana = models.CharField(max_length=255)
    codigopic = models.IntegerField()
    
    #Define opciones para actividad
    ABANDONO = 'ABANDONO'
    WELLSERVICE = 'WELLSERVICE'
    WORKOVER = 'WORKOVER'
    REGISTRO = 'REGISTRO'
    EXTERNO = 'EXTERNO'
    ACTIVIDAD_CHOICES = [
        (ABANDONO, 'Abandono'),
        (WELLSERVICE, 'WS'),
        (WORKOVER, 'WO'),
        (REGISTRO, 'REGISTRO'),    
        (EXTERNO, 'EXTERNO'),    
    ]
    actividad = models.CharField(
        max_length=11,
        choices=ACTIVIDAD_CHOICES,
        default=WORKOVER,
    )

#Define opciones para recurso
    CAPEX = 'CAPEX'
    OPEX = 'OPEX'
    ABEX = 'ABEX'
    RECURSO_CHOICES = [
        (CAPEX, 'CAPEX'),
        (OPEX, 'OPEX'),
        (ABEX, 'ABEX'),
    ]
    recurso = models.CharField(
        max_length=5,
        choices=RECURSO_CHOICES,
        default=CAPEX,
    )


    def __str__(self):
        return f'Intervencion {self.id}: {self.rig} {self.gerencia} {self.vicepresidencia} {self.campo} {self.pozo} {self.tipopozo} {self.inicio} {self.fin} {self.duracion} {self.entradaproduccion} {self.campana} {self.subcampana} {self.codigopic} {self.actividad} {self.recurso}'