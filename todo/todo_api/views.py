from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from urllib import request
from django.http import HttpResponse


class TodoApi(APIView):
    def get(self,request, *args, **kwargs):
        todos = Todo.objects.all()
        serialize = TodoSerializer(todos, many= True)
        return Response(serialize)