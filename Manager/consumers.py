import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async


from .models import *
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope["url_route"]["kwargs"]["project_id"]  
        self.roomGroupName = "chat_"+str(self.project_id)
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_layer 
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "send_chat_message",
                "message" : message , 
                "username" : username,
            })
    async def send_chat_message(self , event) : 
        message = event["message"]
        username = event["username"]
        user = await sync_to_async(CustomUser.objects.get)(username=username)
        await self.send(text_data = json.dumps({"message":message ,"user":{"username": user.username, "avatar": user.avatar.url}}))