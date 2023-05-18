from django.shortcuts import render
from rest_framework import viewsets
from .serializaer import TaskSerializers
from .models import Task


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()