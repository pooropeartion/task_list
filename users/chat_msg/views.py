from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ChatMessageSerializer


from django.shortcuts import render

def chatroom(request):
    return render(request, 'chat_room.html')
