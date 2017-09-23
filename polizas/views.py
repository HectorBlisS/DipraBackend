from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from django.db.models import Q
    
from django.contrib.auth.models import User
from .serializers import PolizaSerializer, ClienteSerializer, PolizaRelatedSerializer, VehiculoSerializer, VehiculoSerializer2, ReciboSerializer, ProspectSerializer, PolizaAdmin
from .models import Poliza, Cliente, Vehiculo, Recibo, Prospecto
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.generics import ListAPIView


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        # print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return qs
        return qs.filter(asesor=self.request.user)
        #return qs


from rest_framework.pagination import PageNumberPagination

class PolizaPaginator(PageNumberPagination):
    page_size = 1
    page_size_query_params = 'page_size'
    max_page_size = 30

class PolizaViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Poliza.objects.all()
    serializer_class = PolizaSerializer
    permission_classes = [permissions.IsAuthenticated,]
    

class PolizaList(OwnerMixin, viewsets.ModelViewSet):
    queryset = Poliza.objects.all()
    serializer_class=PolizaRelatedSerializer
    permission_classes = [permissions.IsAuthenticated,]
    pagination_class = PolizaPaginator

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        
        queryset_list = super(PolizaList,self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(emisor__icontains=query)|
                Q(carpeta__icontains=query)|
                Q(idpoliza__icontains=query)|
                Q(asesor__username__icontains=query)|
                Q(cliente__idcliente__icontains=query)|
                Q(asesor__asesor_user__id_asesor__icontains=query)
                )
        return queryset_list


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
        print(poliza);
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
    pagination_class = PolizaPaginator
    #permission_classes = [permissions.IsAuthenticated,]
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = super(ClienteViewset, self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(idcliente__icontains=query)|
                Q(pnombre__icontains=query)|
                Q(rsocial__icontains=query)
                )
        return queryset_list

class ReciboViewset(viewsets.ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer

class ProspectoViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectSerializer

class AdminPolizaViewset(viewsets.ModelViewSet):
    queryset = Poliza.objects.all()
    serializer_class = PolizaAdmin

