from django.db import models


class Poliza(models.Model):
	nombre = models.CharField(max_length=140)

	def __str__(self):
		return self.nombre