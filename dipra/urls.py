from django.conf.urls import url, include
from django.contrib import admin
from main import urls as mainURLs
from rest_framework import routers
from polizas.views import PolizaViewset, ClienteViewset, PolizaList, VehiculoViewset, VehiculosPoliza, PolizasCliente, ReciboViewset
from accounts import urls as accountsURLs
from accounts.views import ProfileViewset, AsesoresList, PerfilesViewSet, match_client



router = routers.DefaultRouter()
router.register(r'polizas', PolizaViewset)
router.register(r'recibos', ReciboViewset)
router.register(r'clientes', ClienteViewset)
router.register(r'profiles', ProfileViewset)
router.register(r'policys', PolizaList)
router.register(r'vehicles', VehiculoViewset)
router.register(r'perfiles',PerfilesViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api/', include(router.urls)),
	url(r'^api/match', match_client),
	url(r'^api/asesores/', AsesoresList.as_view()),
	url(r'^api/mispolizas',PolizasCliente.as_view()),
	url(r'^api/vehiculospoliza/(?P<id>\d+)/$', VehiculosPoliza.as_view()),
	url(r'^auth/', include(accountsURLs)),
    url(r'^', include(mainURLs))
]
