from django.urls import path, include
from rest_framework.routers import DefaultRouter

from API.views import PlacesViewSet

router = DefaultRouter()
router.register('place', PlacesViewSet, basename='place')

urlpatterns = [
    #path(r'^api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]