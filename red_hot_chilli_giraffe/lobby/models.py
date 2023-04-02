from django.db import models
from red_hot_chilli_giraffe.accounts.models import User

# Create your models here.

class Lobby(models.Model):
    theme = models.CharField(max_length=40, help_text="Enter theme of lobby")
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host")
    participant = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, related_name="participant")
    messages = models.JSONField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    started = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.host}: {self.theme}"
