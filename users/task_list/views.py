from django.shortcuts import render

# Create your views here.
from .serializers import RegisterSerializer, UserSerializer, TaskSerializer
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import Post_list
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView    
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Messsage':serializer.data}, status=201)
        return Response(serializer.errors, status=400)

class UserLoginView(APIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        try:
            email = data['email']
            password = data['password']
        except KeyError:
            return Response({'error': 'Email and password are required fields'}, status=400)

        user = authenticate(email=email, password=password)
        if user:
           
            return Response({'message': 'Login successful'})
        else:
            # Authentication failed
            return Response({'error': 'Invalid credentials'}, status=401)

        # if user:
        #     token, created = Token.objects.get_or_create(user=user)
        #     return Response({'token': token.key})
        # else:
        #     return Response({'error': 'Invalid credentials'}, status=400)



class Create_Tasks(APIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = Post_list
    def post(self, request):
        
        print('the data')
        serializer = Post_list(data=request.data)
        # if request.user.is_authenticated:
        print('if condition')
        if serializer.is_valid():
            serializer.save()
            # print('if condition 111', list(serializer))
            return Response(serializer.data)
        else:
            return Response({'detail': serializer.errors}, status=400)




class Tasks(APIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
    def get(self, request):
        get_list = Task.objects.all()
        serializer = Post_list(get_list, many=True)
        return Response(serializer.data)

class Tasks_get_update_delete(APIView):

    # permission_classes = (permissions.AllowAny,)
    serializer_class = Post_list
    # Get the single record
    def get(self, request, id):
        try:
    
            post_data_item = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"message": "Post not found"})

        serializer = Post_list(post_data_item)

        return Response(serializer.data)
    
    # Update the single Task
    def put(self, request, id):
        try:
            post_item = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"message": "Post not found"})

        serializer = Post_list(post_item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Delete the single task
    def delete(self, request, id):
        try:
            post_data_item = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"message": "Post not found"})

        post_data_item.delete()
        return Response({"message": "Post deleted"})



def login(request):
    return render(request, 'login.html')


def registartion(request):
    return render(request, 'Registertion.html')


def task_data(request):
    return render(request, 'task.html')

def list_data(request):
    return render(request, 'list_data.html')
