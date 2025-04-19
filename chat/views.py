from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import ollama
from .serializers import MessageSerializer
from .models import Message

class ChatView(APIView):
    def post(self, request):
        model  = "llama2"
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid() :
            prompt = serializer.validated_data['user_prompt']
            client = ollama.Client()
            response = client.generate(model=model, prompt=prompt)
            serializer.save(bot_response=response.response, user=request.user, user_prompt=prompt)
            return Response({"response": response.response}, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


