from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from API.views import PlacesViewSet

router = DefaultRouter()
router.register('place', PlacesViewSet, basename='place')

urlpatterns = [
    #path(r'^api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
