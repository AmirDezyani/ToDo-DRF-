from django.contrib.auth.models import User
from accounts_app.models import Profile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
import pdb
import random


class ProfileViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # self.user = User.objects.create_user(username='alice', password='secret123')

        self.payload = [{
            "username": ''.join(random.choice('abcdefgh123456') for _ in range(8)),
            "email": f"user{_}@example.com",
            "first_name": "amir",
            "last_name": "big pp",
            "password": "secret123",
            "profile": {
                "gender": True
            }
        } for _ in range(9)]

        # self.client.login(username='admin', password='admin')

        self.list_url = reverse('profile-list')
        self.detail_url = lambda pk: reverse('profile-detail', args=[pk])
        self.response = []
        for data in self.payload:
            response = self.client.post(self.list_url, data, format='json')
            self.response.append(response.data)

    def test_create_user(self):
        username = ''.join(random.choice('abcdefgh123456') for _ in range(8))
        payload = {
            "username": username,
            "email": "user@example.com",
            "first_name": "amir",
            "last_name": "big pp",
            "password": "secret123",
            "profile": {
                "gender": True
          }
        }
        response = self.client.post(self.list_url, payload, format='json')
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 10)
        self.assertIn('profile', response.data)
        self.assertEqual(response.data['profile']['gender'], True)

    def test_get_list_user(self):
        response = self.client.get(self.list_url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_user(self):
        user = random.choice(self.response)
        pk = user['id']
        url = self.detail_url(pk)
        response = self.client.get(url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        user = random.choice(self.response)
        pk = user['id']
        url = self.detail_url(pk)

        put_data = user.copy()
        put_data['first_name'] = 'adadsfs'
        put_data['profile'].pop('image', None)

        response = self.client.put(url, put_data, format='json')
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        user = random.choice(self.response)
        pk = user['id']
        url = self.detail_url(pk)
        response = self.client.delete(url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 8)