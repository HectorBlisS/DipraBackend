from django.conf.urls import url
from .views import LoginView, LogoutView, ProfileViewset
from rest_framework.authtoken import views


urlpatterns = [

	url(r'^login/$',
		LoginView.as_view()),

	url(r'^logout/$',
		LogoutView.as_view()),

	url(r'^token-auth/', views.obtain_auth_token)
	
	]
