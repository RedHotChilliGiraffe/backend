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
        print(self.lobby_id)
        self.lobby = Lobby.objects.get(id=self.lobby_id)
        print(self.lobby.participant)
        
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
        print(json.dumps(self.lobby.messages))
        
        

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        
        
        
        
        
        
    #wywoływane nie wiem kiedy XD
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("otrzymuję góra")
        message = text_data_json["message"]
        
        # conversation = self.lobby.messages.append({"role": "user", "content": message},)

        # make_new_message(conversation)
        
        # response = make_new_message(conversation)
        # conversation.append(response['choices'][0]['message'])
        
        # self.lobby.messages = json.loads(conversation)
        # self.lobby.save()
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "chat_message", "message": response['choices'][0]['message']['content']}
        )
    
    def chat_message(self, event):
        print("otrzymuję")
        message = event["message"]

        # Send message to WebSocket
        