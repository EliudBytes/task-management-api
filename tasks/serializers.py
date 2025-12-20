from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'owner', 'created_at', 'updated_at']
        # Prevent manual editing of these fields
        read_only_fields = ['owner', 'created_at', 'updated_at']
