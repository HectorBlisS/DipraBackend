from rest_framework import serializers
from .models import Poliza


class PolizaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poliza
		fields = '__all__'