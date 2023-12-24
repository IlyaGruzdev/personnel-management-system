from django.urls import path , include
from . import consumers
from django.urls import re_path
 
# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("project/<int:project_id>", consumers.ChatConsumer.as_asgi()),
]