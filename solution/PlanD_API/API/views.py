from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response as response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated 

from API.models import Place
from API.serializers import PlaceSerializer


# Create your views here.
'''
ModelViewSet that performs the CRUD 
'''
class PlacesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #simple security method
    '''
    Actions performed without filtering a specific object
    '''
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'slug'

    '''
    Actions performed filtering a specific object
    '''
    @action(methods=['get','delete','put'], detail=True)
    def filtered_actions(self, request, pk=None):
        place = self.get_object() #gets the object using the slug given in the URL
        return response(place, status=status.HTTP_200_OK)