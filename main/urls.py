from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from content_api.views import ItemViewSet

from foryou.views import StateViewSet

from guides.views import GuideViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')


router2 = routers.DefaultRouter()
router2.register(r'state', StateViewSet, basename='state')


router3 = routers.DefaultRouter()
router3.register(r'guides', GuideViewSet, basename='guides')

router4 = routers.DefaultRouter()
router4.register(r'cities', GuideViewSet, basename='cities')

router5 = routers.DefaultRouter()
router5.register(r'food', GuideViewSet, basename='food')

router6 = routers.DefaultRouter()
router6.register(r'locals', GuideViewSet, basename='locals')

router7 = routers.DefaultRouter()
router7.register(r'Spots', GuideViewSet, basename='Spots')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include('api.urls',)),

    url(r'api/', include(router.urls)),
    url(r'api/', include(router2.urls)),
    url(r'api/', include(router3.urls)),
    url(r'api/', include(router4.urls)),
    url(r'api/', include(router5.urls)),
    url(r'api/', include(router6.urls)),
    url(r'api/', include(router7.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
