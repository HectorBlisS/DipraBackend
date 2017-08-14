from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .utils import *




class HomeView(View):
	def get(self, request):
		return HttpResponse("PlanB")



# Mailing pending

class WelcomeMail(APIView):
	def get(self, request):
		# objeto = {
		# 	"to":["contacto@fixter.org", "admin@fixter.org"],
		# 	"from_email":"hola@planb.com.mx",
		# 	"subject":"Dipra Notifyer",
		# 	"template":"mail/default.html",
		# 	"ctx":{
		# 		"titulo":"¡Te damos la Bienvenida!",
		# 		"subtitulo":"Estmos muy contentos de que te hayas unido a nuestra comunidad",
		# 		"parrafo1":"SY estamos invitación a las Sedes interesadas, si gustan acompañarnos, sería un gusto poderles conocer y conozcan más sobre nuestra labor educativa que realizamos a través de las Sedes de Educación Regional en los diferentes estados.",
		# 		"parrafo2":"Cada año tenemos una reunión anual de directivos de Sedes de Bachillerato, que hemos llamado nuestra convención educativa 2017, donde bien de diferentes estados donde hay una Sede de Educación Regional que son tiempos de koinonía, revisión de situaciones en cada Sede, temas a discutir sobre la educación y educación cristiana, proyectos y apretura de Sedes, entre otros temas.",
		# 		"username":"bliss",
		# 	}
		# }
		enviar_mails()
		return Response("pollo", status=status.HTTP_200_OK)
