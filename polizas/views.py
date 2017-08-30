from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .serializers import PolizaSerializer, ClienteSerializer, PolizaRelatedSerializer, VehiculoSerializer, VehiculoSerializer2, ReciboSerializer, ProspectSerializer
from .models import Poliza, Cliente, Vehiculo, Recibo, Prospecto
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        # print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return qs
        return qs.filter(asesor=self.request.user)
        #return qs



class PolizaViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Poliza.objects.all()
    serializer_class = PolizaSerializer
    permission_classes = [permissions.IsAuthenticated,]

class PolizaList(OwnerMixin, viewsets.ModelViewSet):
    queryset = Poliza.objects.all()
    serializer_class=PolizaRelatedSerializer
    permission_classes = [permissions.IsAuthenticated,]


class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculosPoliza(ListAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer2

    def get_queryset(self):
        print(self.request.data)
        print(self.kwargs['id'])
        poliza=Poliza.objects.get(id=self.kwargs['id'])
        qs = super(VehiculosPoliza, self).get_queryset()        
        return qs.filter(poliza=poliza)

class PolizasCliente(ListAPIView):
    queryset = Poliza.objects.all()
    serializer_class = PolizaSerializer

    def get_queryset(self):
        print('lol',self.request.user)
        cliente=Cliente.objects.get(user=self.request.user)
        qs = super(PolizasCliente, self).get_queryset()        
        return qs.filter(cliente=cliente)    

class ClienteViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated,]

class ReciboViewset(viewsets.ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer

class ProspectoViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectSerializer

