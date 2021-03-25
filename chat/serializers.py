from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Chat, Room

class UserSerializer(serializers.ModelSerializer):
    """Serializer for django model User"""
    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for chat app models Room"""
    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ('id', 'creator', 'invited', 'date')


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chat"""
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):
    """Serializer for chat messages"""

    class Meta:
        model = Chat
        fields = ('room', 'text')