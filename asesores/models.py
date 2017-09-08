from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#All asesores models

class Asesor(models.Model):
	reclutador = models.ForeignKey(User, related_name="reclutador_asesor", blank=True, null=True)
	usuario = models.OneToOneField(User, related_name="asesor_user", blank=True, null=True)
	id_asesor  = models.CharField(max_length=100, blank=True, null=True)
	nombre = models.CharField(max_length=100, blank=True, null=True)
	telefono = models.CharField(max_length=100, blank=True, null=True)
	correo = models.CharField(max_length=100, blank=True, null=True)
	tipo = models.CharField(max_length=100, blank=True, null=True)
	fecha_reclutamiento = models.CharField(max_length=100, blank=True, null=True)
	candidato = models.BooleanField(default=True)
	status = models.CharField(max_length=100, blank=True, null=True)
	tarjetas = models.IntegerField(blank=True, null=True)	
	oficina = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.nombre

class Archivo(models.Model):
	TIPOS=(
		('documento','documento'),
		('buzon','buzon'),
		('carta','carta'),
		)
	
	asesor = models.ForeignKey(Asesor, related_name="archivos_asesor", blank=True, null=True)
	tipo = models.CharField(max_length=100, choices=TIPOS, default='documento')
	archivo = models.FileField(upload_to="asesores/documentos")
	nombre = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.nombre

class Cita(models.Model):
	asesor = models.ForeignKey(Asesor, related_name="cita_asesor", blank=True, null=True)
	fecha = models.CharField(max_length=100, blank=True, null=True)
	comentarios = models.TextField(blank=True, null=True)

	def __str__(self):
		return 'cita del dia {}'.format(self.fecha)

class Clave(models.Model):
	asesor = models.ForeignKey(Asesor, related_name="clave_asesor", blank=True, null=True)
	clave = models.CharField(max_length=100, blank=True, null=True)
	clave_stat = models.BooleanField(default=True)
	fecha_inicio = models.CharField(max_length=100, blank=True, null=True)
	fecha_final = models.CharField(max_length=100, blank=True, null=True)
	tipo = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.clave

class Curso(models.Model):
	asesor = models.ForeignKey(Asesor, related_name="curso_asesor", blank=True, null=True)
	nombre = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.nombre





