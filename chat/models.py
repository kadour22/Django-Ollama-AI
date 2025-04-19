from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Message(models.Model) :
    bot_response = models.CharField(max_length=10000 , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)   
    user_prompt = models.CharField(max_length=110000)


    def __str__(self) :
        return self.user.username + " : " + self.user_prompt[:20] + "..." + self.bot_response[:20] + "..." 