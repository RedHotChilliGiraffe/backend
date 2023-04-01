from typing import List

from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from red_hot_chilli_giraffe.accounts.serializers import UserRegisterSerializer, UserProfileSerializer


# Create your views here.
class RegisterView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes: List[str] = []

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserProfileSerializer(user, context={"request": request}).data
        return Response(data, status=status.HTTP_201_CREATED)


class ProfileView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["get"], detail=False, url_name="read")
    def profile(self, request, *args, **kwargs):
        data = UserProfileSerializer(request.user, context={"request": request}).data
        return Response(data)
