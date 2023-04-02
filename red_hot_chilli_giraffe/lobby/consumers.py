import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from red_hot_chilli_giraffe.lobby.models import Lobby
import openai


def make_new_message(conversation):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )


openai.api_key = "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"


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.lobby_id = self.scope["url_route"]["kwargs"]["lobby_id"]
        self.lobby = Lobby.objects.get(id=self.lobby_id)
        
        self.group_name = "{}".format(self.lobby_id)
        
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        
        self.accept()
        
        if not self.lobby.participant:
            conversation = [
                        {"role": "system", "content": f"Lets play D&D in {self.lobby.theme} scenario. You are a game master."},
                        {"role": "user", "content": "New Game"},
            ]
            response = make_new_message(conversation)
            conversation.append(response['choices'][0]['message'])
            
            self.lobby.messages = conversation
            self.lobby.save()
        else:
            self.lobby.is_active = False
            self.lobby.started = True
        
        
        
        self.send(text_data=json.dumps(self.lobby.messages))
        

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        

    #wywoływane nie wiem kiedy XD


    def receive(self, text_data):
        message = text_data
        self.lobby.messages.append({"role": "user", "content": message})
        print(self.lobby.messages)

        response = make_new_message(self.lobby.messages)
        self.lobby.messages.append(response['choices'][0]['message'])

        self.lobby.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "chat_message", "messages": self.lobby.messages}
        )
    
    def chat_message(self, event):
        messages = event["messages"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(messages))
        