from django.shortcuts import render
from .models import TaskManager
from .serializers import TaskManagerSerializer
from rest_framework import generics
# Create your views here.


class TM_List(generics.ListCreateAPIView):
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer


class TM_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer