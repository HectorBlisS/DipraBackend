from django.contrib.auth import authenticate, login, logout

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


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


