from django.conf.urls import url, include
from django.contrib import admin
from main import urls as mainURLs
from rest_framework import routers
from polizas.views import PolizaViewset
from accounts import urls as accountsURLs



router = routers.DefaultRouter()
router.register(r'polizas', PolizaViewset)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api/', include(router.urls)),
	url(r'^auth/', include(accountsURLs)),
    url(r'^', include(mainURLs))
]
