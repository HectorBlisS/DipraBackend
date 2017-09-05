from django.contrib.auth import authenticate, login, logout

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer, ProfileSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from polizas.models import Cliente
from asesores.models import Asesor




class isSelfOrAdmin(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_object_permission(self, request, view, obj):
    	if request.method in permissions.SAFE_METHODS:
    		return True

    	elif request.user.is_staff or obj.user == request.user:
    			return True


class LoginView(views.APIView):
	@method_decorator(csrf_protect)
	def post(self, request):
		user = authenticate(
				username=request.data.get('username'),
				password=request.data.get('password'))
		if user is None or not user.is_active:
			return Response({
				'status': 'Unauthorized',
				'message': 'Username or password incorrect'
				}, status=status.HTTP_401_UNAUTHORIZED)

		login(request, user)
		return Response(UserSerializer(user).data)


class LogoutView(views.APIView):
	def get(self, request):
		logout(request)
		return Response({}, status=status.HTTP_204_NO_CONTENT)
		

class ProfileViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny,]

	def get_permissions(self):
		print(self.request.method)
		if self.action == 'update':
		# if self.request.method == 'PUT':
			self.permission_classes = [isSelfOrAdmin, permissions.IsAuthenticatedOrReadOnly]

		return super(ProfileViewset, self).get_permissions()


class SelfProfile(views.APIView):
	permission_classes = [permissions.IsAuthenticated,]

	def get(self, request):
		profile, created = Profile.objects.get_or_create(user=request.user)
		# serializer = ProfileSerializer(profile, many=False)
		# return Response(serializer.data)

		serializer = UserSerializer(request.user)
		return Response(serializer.data)

	def post(self, request):
		profile, created = Profile.objects.get_or_create(user=request.user)
		# serializer = ProfileSerializer(profile, many=False)
		# return Response(serializer.data)

		print(request.data['photo'])

		if request.data['photo']:
			profile.photo = request.data['photo']
			profile.save()

		# if request.data['uid']:
		# 	profile.uid = request.data['uid']
		# 	profile.save()
		

		serializer = UserSerializer(request.user)
		return Response(serializer.data)

class AsesoresList(ListAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
	def get_queryset(self):
		qs = super(AsesoresList, self).get_queryset()
		return qs.filter(profile__aprobado=True) 

class PerfilesViewSet(viewsets.ModelViewSet):
	queryset=Profile.objects.all()
	serializer_class=ProfileSerializer


from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@api_view(['GET', 'POST'])
def match_client(request):
	if request.method == 'POST':
		print(request.data)
		print(request.user)
		cliente = Cliente.objects.get(idcliente=request.data['clienteId'])
		cliente.user = request.user
		
		cliente.save()
		

		return Response({"message": "Macheado el cliente", "data": request.data})
	return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def match_asesor(request):
	if request.method == 'POST':
		print(request.data)
		print(request.user)
		asesor = Asesor.objects.get(id_asesor=request.data['asesorId'])
		asesor.usuario = request.user
		
		asesor.save()
		

		return Response({"message": "Macheado el asesor", "data": request.data})
	return Response({"message": "Hello, world!"})



