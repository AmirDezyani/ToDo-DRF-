from django.contrib.auth.models import User
from rest_framework import serializers

from accounts_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'gender')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile')

