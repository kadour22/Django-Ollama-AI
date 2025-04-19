from django.urls import path
from . import views

urlpatterns = [
    path('ai-chat/', views.ChatView.as_view(), name='chat'),
    path('user/', views.ChatView.as_view(), name='chat'),
]