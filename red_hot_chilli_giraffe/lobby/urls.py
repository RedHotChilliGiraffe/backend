from rest_framework.routers import SimpleRouter

from .views import LobbyApiView, LobbyJoinView

lobby_router = SimpleRouter()

lobby_router.register(r"lobby", LobbyApiView, "lobby")
lobby_router.register(r"join", LobbyJoinView, "lobby_join")

from . import views
from django.urls import include, path

urlpatterns = [
    path("<int:lobby_id>/", views.room, name="room"),
]
