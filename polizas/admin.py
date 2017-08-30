from django.contrib import admin
from .models import Poliza, Cliente, Vehiculo, Recibo, Prospecto

class PolizaAdmin(admin.ModelAdmin):
	list_display = ['id','asesor','cliente','apertura']
	list_filter = ['asesor','cliente','apertura']

admin.site.register(Poliza, PolizaAdmin)
admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Recibo)
admin.site.register(Prospecto)
