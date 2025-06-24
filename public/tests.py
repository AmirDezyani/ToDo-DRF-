from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from public.models import Todos
from rest_framework.test import APITestCase
import pdb


class TodoTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='secret123')

        self.client.login(username='alice', password='secret123')

        self.todo = Todos.objects.create(
            user=self.user,
            title='Buy milk',
            description='From the corner store',
            status=Todos.Status.Todo
        )
        self.list_url = reverse('todos-list')
        self.detail_url = lambda pk: reverse('todos-detail', args=[pk])

    def test_list_todos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(any(item['title'] == 'Buy milk'
                            for item in response.data))

    def test_create_todo(self):
        payload = {
            'user': self.user.pk,
            'title': 'Walk the dog',
            'description': 'Take Fido out',
            'status': Todos.Status.Todo
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_todo(self):
        url = self.detail_url(self.todo.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        payload = {
            'user': self.user.pk,
            'title': 'Walk the dog',
            'description': 'Take Fido out',
            'status': Todos.Status.Doing
        }
        url = self.detail_url(self.todo.pk)
        response = self.client.put(url , payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo(self):
        url = self.detail_url(self.todo.pk)
        response = self.client.patch(url,
                                     {'status': Todos.Status.Done},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.status, Todos.Status.Done)

    def test_delete_todo(self):
        url = self.detail_url(self.todo.pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)