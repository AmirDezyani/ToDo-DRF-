from django.shortcuts import render
from rest_framework import viewsets

from public.models import Todos
from public.serializers import TodosSerializer


class TodosViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer