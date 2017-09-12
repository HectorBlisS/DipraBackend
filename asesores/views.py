from django.shortcuts import render
from rest_framework import viewsets
from .models import Asesor, Archivo, Cita, Clave, Curso
from .serializers import AsesorSerializer, AsesorSerializerList, ArchivoSerializer, CitaSerializer, ClaveSerializer, CursoSerializer
from rest_framework.generics import ListAPIView
# Create your views here.


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        # print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return qs
        return qs.filter(asesor=self.request.user)
        #return qs



class AsesorViewset(OwnerMixin, viewsets.ModelViewSet):
	queryset = Asesor.objects.all()
	serializer_class = AsesorSerializer

class AsesorViewsetList(OwnerMixin, viewsets.ModelViewSet):
	queryset = Asesor.objects.all()
	serializer_class = AsesorSerializerList

class ArchivoViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

class ArchivosAsesorViewset(ListAPIView):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

    def get_queryset(self):
        print(self.request.data)
        print(self.kwargs['id'])
        asesor=Asesor.objects.get(id=self.kwargs['id'])
        
        qs = super(ArchivosAsesorViewset, self).get_queryset()        
        return qs.filter(asesor=asesor)

class CitaViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class ClaveViewset(viewsets.ModelViewSet):
    queryset = Clave.objects.all()
    serializer_class = ClaveSerializer

class CursoViewset(OwnerMixin, viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


#



