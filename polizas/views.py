from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import PolizaSerializer
from .models import Poliza


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        # print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return qs
        # return qs.filter(author=self.request.user)
        return qs



class PolizaViewset(OwnerMixin, viewsets.ModelViewSet):
	queryset = Poliza.objects.all()
	serializer_class = PolizaSerializer