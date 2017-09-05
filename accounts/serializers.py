from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from polizas.models import Cliente
from asesores.models import Asesor



class ClienteSerializer2(serializers.ModelSerializer):
	class Meta:
		model=Cliente
		fields='__all__'

class AsesorSerializer2(serializers.ModelSerializer):
	class Meta:
		model=Asesor
		fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Profile
		fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
	asesor_user=AsesorSerializer2(many=False, read_only=True)
	profile = ProfileSerializer(many=False, read_only=True)
	cliente_asesor=ClienteSerializer2(many=True, read_only=True)
	usuario=ClienteSerializer2(read_only=True)
	class Meta:
		model = User
		fields = "__all__"

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user




