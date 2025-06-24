from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from accounts_app.models import Profile
from accounts_app.serializers import ProfileSerializer, UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
