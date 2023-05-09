from rest_framework import serializers
from .models import User, Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FriendshipSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Friendship
        fields = ['sender', 'receiver', 'status']