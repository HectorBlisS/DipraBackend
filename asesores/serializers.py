from .models import Asesor, Archivo, Clave, Curso, Cita
from rest_framework import serializers
from accounts.serializers import UserSerializer

##Serializers Asesor



class ArchivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Archivo
		fields = '__all__'

class ClaveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clave
		fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Curso
		fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cita
		fields = '__all__'

class AsesorSerializer(serializers.ModelSerializer):

	reclutador = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Asesor
		fields = '__all__'

class AsesorSerializerList(serializers.ModelSerializer):
	archivos_asesor = ArchivoSerializer( read_only=True, many=True)
	clave_asesor = ClaveSerializer( read_only=True, many=True)
	curso_asesor = CursoSerializer( read_only=True, many=True)
	cita_asesor = CitaSerializer( read_only=True, many=True)

	usuario = UserSerializer(read_only=True)
	reclutador = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Asesor
		fields = '__all__'
