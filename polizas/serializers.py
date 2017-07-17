from rest_framework import serializers
from .models import Poliza
from accounts.serializers import UserSerializer



class PolizaSerializer(serializers.ModelSerializer):
	
	asesor= UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Poliza
		fields = '__all__'

	