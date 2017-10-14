from rest_framework import serializers
from .models import TaskManager 

class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManager
        fields = ('id', 'title', 'status', 'description')