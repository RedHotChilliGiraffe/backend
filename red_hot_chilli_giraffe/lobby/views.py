from typing import List

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import render


from red_hot_chilli_giraffe.accounts.models import User
from .models import Lobby
from .serializers import LobbyCreateSerializer

class LobbyApiView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        queryset = Lobby.objects.filter(is_active=True, started=False)
        serializer = LobbyCreateSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        request.data['host'] = request.user.id
        serializer = LobbyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LobbyJoinView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lobby.objects.all()
    serializer_class = LobbyCreateSerializer
    
    # join lobby
    def create(self, request):
        participant = request.user
        queryset = Lobby.objects.get(id=request.data['id'])
        
        queryset.participant = participant
        queryset.is_active = False
        queryset.started = True
        queryset.save()

        return Response("Hej paweł i zuzia", status=status.HTTP_200_OK)
    
def room(request, lobby_id):
    return render(request, "chat/room.html", {"lobby_id": lobby_id})
    
    