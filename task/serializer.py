from rest_framework import serializers
from task.models import Task
from django.utils import timezone
from django.contrib.auth.models import User



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','description','done')    