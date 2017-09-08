from rest_framework import serializers
from .models import Poliza, Cliente, Vehiculo, Recibo, Prospecto
from accounts.serializers import UserSerializer




class ReciboSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recibo
		fields = '__all__'

class PolizaAdmin(serializers.ModelSerializer):
	class Meta:
		model = Poliza
		fields = '__all__'
	def create(self, validated_data):
		
		
		poliza = Poliza.objects.create(**validated_data)
		print(validated_data)
		print(poliza)
		pago = validated_data.pop('pago')
		if pago=='Anual':
			Recibo.objects.create(poliza=poliza, numero=1)
		if pago=='Semestral':
			for i in range(0,2):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		if pago=='Cuatrimestral':
			for i in range(0,3):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		if pago=='Trimestral':
			for i in range(0,4):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		if pago=='Mensual':
			for i in range(0,12):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		
		return poliza


class PolizaSerializer(serializers.ModelSerializer):
	
	#vehiculos=VehiculoSerializer(read_only=True, many=True)
	asesor= UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Poliza
		fields = '__all__'
	def create(self, validated_data):
		
		
		poliza = Poliza.objects.create(**validated_data)
		print(validated_data)
		print(poliza)
		pago = validated_data.pop('pago')
		if pago=='Anual':
			Recibo.objects.create(poliza=poliza, numero=1)
		if pago=='Semestral':
			for i in range(0,2):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		if pago=='Cuatrimestral':
			for i in range(0,3):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		if pago=='Trimestral':
			for i in range(0,4):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		if pago=='Mensual':
			for i in range(0,12):
				Recibo.objects.create(poliza=poliza, numero=i+1)
		
		return poliza


class ClienteSerializer(serializers.ModelSerializer):
	poliza_cliente= PolizaSerializer(read_only=True, many=True)
	asesor= UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Cliente
		fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Vehiculo
		fields = '__all__'

class PolizaRelatedSerializer(serializers.ModelSerializer):
	recibo_poliza = ReciboSerializer(read_only=True, many=True)
	vehiculos=VehiculoSerializer(read_only=True, many=True)
	cliente=ClienteSerializer(read_only=True)
	asesor= UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Poliza
		fields = '__all__'



class VehiculoSerializer2(serializers.ModelSerializer):
	poliza = PolizaSerializer(read_only=True)
	class Meta:
		model = Vehiculo
		fields = '__all__'

class ProspectSerializer(serializers.ModelSerializer):
	asesor = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Prospecto
		fields = '__all__'



	