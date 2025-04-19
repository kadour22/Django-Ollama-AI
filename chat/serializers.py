from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id', 'username','email','password']
        extra_kwargs = {
            'password': {'write_only': True} , 
            'email': {'required': True} ,
            'id': {'read_only': True} ,
        }


class MessageSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Message
        fields = "__all__"