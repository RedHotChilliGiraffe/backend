"""
ASGI config for red_hot_chilli_giraffe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import red_hot_chilli_giraffe.lobby.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'red_hot_chilli_giraffe.settings')
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(red_hot_chilli_giraffe.lobby.routing.websocket_urlpatterns))
        ),
    }
)
