from django.shortcuts import render
from rest_framework import viewsets
from .models import Asesor
from .serializers import AsesorSerializer, AsesorSerializerList
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


