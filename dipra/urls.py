from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from main import urls as mainURLs
from rest_framework import routers
from polizas.views import PolizaViewset, ClienteViewset, PolizaList, VehiculoViewset, VehiculosPoliza, PolizasCliente, ReciboViewset, ProspectoViewset, AdminPolizaViewset
from accounts import urls as accountsURLs
from accounts.views import ProfileViewset, AsesoresList, PerfilesViewSet, match_client, match_asesor
from asesores.views import AsesorViewset, AsesorViewsetList,ArchivoViewset,ClaveViewset, CursoViewset, CitaViewset, ArchivosAsesorViewset



router = routers.DefaultRouter()
router.register(r'polizas', PolizaViewset)
router.register(r'recibos', ReciboViewset)
router.register(r'clientes', ClienteViewset)
router.register(r'profiles', ProfileViewset)
router.register(r'policys', PolizaList)
router.register(r'vehicles', VehiculoViewset)
router.register(r'perfiles',PerfilesViewSet)
router.register(r'prospectos', ProspectoViewset)
router.register(r'candidatos', AsesorViewset)
router.register(r'candidatoslist', AsesorViewsetList)
router.register(r'adminpolizas', AdminPolizaViewset)
router.register(r'archivos', ArchivoViewset)
router.register(r'claves', ClaveViewset)
router.register(r'cursos', CursoViewset)
router.register(r'citas', CitaViewset)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api/', include(router.urls)),
	url(r'^api/match', match_client),
	url(r'^api/asesormatch', match_asesor),
	url(r'^api/asesores/', AsesoresList.as_view()),
	url(r'^api/mispolizas',PolizasCliente.as_view()),
	url(r'^api/vehiculospoliza/(?P<id>\d+)/$', VehiculosPoliza.as_view()),
	url(r'^api/archivosasesor/(?P<id>\d+)/$', ArchivosAsesorViewset.as_view()),
	url(r'^auth/', include(accountsURLs)),
    url(r'^', include(mainURLs)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),
]
