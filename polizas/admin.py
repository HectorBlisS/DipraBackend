from django.contrib import admin
from .models import Poliza, Cliente, Vehiculo, Recibo

admin.site.register(Poliza)
admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Recibo)