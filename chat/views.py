from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , permissions
import ollama
from .serializers import MessageSerializer , UserSerializer
from .models import Message


class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        model  = "llama2"
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid() :
            prompt = serializer.validated_data['user_prompt']
            client = ollama.Client()
            response = client.generate(model=model, prompt=prompt)
            serializer.save(bot_response=response.response,user_prompt=prompt)
            return Response({"response": response.response}, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
