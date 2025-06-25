from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from accounts_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'image', 'gender')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model  = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True, 'required': False},}

    @transaction.atomic
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        password = validated_data.pop('password', None)

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        if password:
            instance.set_password(password)
        instance.save()

        if profile_data:
            Profile.objects.filter(user=instance).update(**profile_data)

        return instance