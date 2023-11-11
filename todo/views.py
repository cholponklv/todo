from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerialzier

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzier

