from django.shortcuts import render
from rest_framework import viewsets
from .models import Asesor
from .serializers import AsesorSerializer, AsesorSerializerList
# Create your views here.

class AsesorViewset(viewsets.ModelViewSet):
	queryset = Asesor.objects.all()
	serializer_class = AsesorSerializer

class AsesorViewsetList(viewsets.ModelViewSet):
	queryset = Asesor.objects.all()
	serializer_class = AsesorSerializerList


