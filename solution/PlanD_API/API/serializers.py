
from rest_framework import serializers
from API.models import Place

'''
Serialization based on Model
'''
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
    