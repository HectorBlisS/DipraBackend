from django.contrib import admin
from .models import Asesor, Archivo, Cita, Clave, Curso

# Register your models here.

admin.site.register(Asesor)
admin.site.register(Archivo)
admin.site.register(Cita)
admin.site.register(Clave)
admin.site.register(Curso)