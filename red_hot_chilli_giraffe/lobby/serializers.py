from rest_framework import serializers

from .models import Lobby


class LobbyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = ['id', 'host', 'participant', 'theme', 'messages', 'is_active', 'started']
