from django.db import models


class Poliza(models.Model):
	

	tpersona = models.CharField(max_length=150, blank=True, null=True)
	ecivil = models.CharField(max_length=150, blank=True, null=True)
	genero = models.CharField(max_length=150, blank=True, null=True)
	rsocial = models.CharField(max_length=150, blank=True, null=True)
	apaterno = models.CharField(max_length=150, blank=True, null=True)
	amaterno = models.CharField(max_length=150, blank=True, null=True)
	pnombre = models.CharField(max_length=150, blank=True, null=True)
	snombre = models.CharField(max_length=150, blank=True, null=True)
	rfc = models.CharField(max_length=150, blank=True, null=True)
	curp = models.CharField(max_length=150, blank=True, null=True)
	edad = models.CharField(max_length=150, blank=True, null=True)
	tipoid = models.CharField(max_length=150, blank=True, null=True)
	numid = models.CharField(max_length=150, blank=True, null=True)
	fnacimiento = models.CharField(max_length=150, blank=True, null=True)
	fiel = models.CharField(max_length=150, blank=True, null=True)
	estado = models.CharField(max_length=150, blank=True, null=True)
	pais = models.CharField(max_length=150, blank=True, null=True)
	nacionalidad = models.CharField(max_length=150, blank=True, null=True)
	calle = models.CharField(max_length=150, blank=True, null=True)
	edificio = models.CharField(max_length=150, blank=True, null=True)
	noext = models.CharField(max_length=150, blank=True, null=True)
	noint = models.CharField(max_length=150, blank=True, null=True)
	otroext = models.CharField(max_length=150, blank=True, null=True)
	cp = models.CharField(max_length=150, blank=True, null=True)
	colonia = models.CharField(max_length=150, blank=True, null=True)
	municipio = models.CharField(max_length=150, blank=True, null=True)
	ciudad = models.CharField(max_length=150, blank=True, null=True)
	estado = models.CharField(max_length=150, blank=True, null=True)
	telefono = models.CharField(max_length=150, blank=True, null=True)
	correo = models.CharField(max_length=150, blank=True, null=True)
	fmercantil = models.CharField(max_length=150, blank=True, null=True)
	micargo = models.CharField(max_length=150, blank=True, null=True)
	fcargo = models.CharField(max_length=150, blank=True, null=True)
	sucargo = models.CharField(max_length=150, blank=True, null=True)
	fsucargo = models.CharField(max_length=150, blank=True, null=True)
	parentesco = models.CharField(max_length=150, blank=True, null=True)
	familiar = models.CharField(max_length=150, blank=True, null=True)
	honorarios = models.CharField(max_length=150, blank=True, null=True)
	institucion = models.CharField(max_length=150, blank=True, null=True)
	aempresarial = models.CharField(max_length=150, blank=True, null=True)
	actempresarial = models.CharField(max_length=150, blank=True, null=True)
	rtemp = models.CharField(max_length=150, blank=True, null=True)
	rperm = models.CharField(max_length=150, blank=True, null=True)
	resotro = models.CharField(max_length=150, blank=True, null=True)
	fpublico = models.CharField(max_length=150, blank=True, null=True)
	parpublico = models.CharField(max_length=150, blank=True, null=True)
	asalariado = models.CharField(max_length=150, blank=True, null=True)
	bhonorarios = models.CharField(max_length=150, blank=True, null=True)

	def __str__(self):
		return self.id