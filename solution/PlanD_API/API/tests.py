import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from API.models import Place
from API.serializers import PlaceSerializer

class AuthTesteCase(APITestCase):

    def test_authentication(self):
        self.user = User.objects.create_user(username='admin', password='admin@123')
        bad_response = self.client.get('/place/')
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.login(username='admin', password='admin@123')
        response = self.client.get('/place/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

class PlaceViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin@123')
        self.client.login(username='admin', password='admin@123')
        data = {'name': 'test1', 'slug': 't1', 'city': 'city1', 'state': 'state1'}
        self.client.post('/place/', data=data)

    def test_create(self):
        data = {'name': 'test', 'slug': 't', 'city': 'city', 'state': 'state'}
        response = self.client.post('/place/', data=data)
        duplicated_response = self.client.post('/place/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(duplicated_response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update(self):
        data = {'name': 'test1-new', 'state': 'state1-new'}
        response = self.client.put('/place/t1/', data=data)
        bad_response = self.client.put('/place/bad_slug/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_list(self):
        response = self.client.get('/place/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_filter(self):
        response = self.client.get('/place/t1/')
        bad_response = self.client.get('/place/bad_slug/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        response = self.client.delete('/place/t1/')
        response_not_found = self.client.delete('/place/bad_slug/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)