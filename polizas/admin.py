from django.contrib import admin
from .models import Poliza, Cliente, Vehiculo, Recibo, Prospecto

class PolizaAdmin(admin.ModelAdmin):
	list_display = ['id','user','asesor','fecha_poliza','idcliente','genero']
	list_filter = ['user','asesor', 'genero', 'fecha_poliza']

admin.site.register(Poliza, PolizaAdmin)
admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Recibo)
admin.site.register(Prospecto)
