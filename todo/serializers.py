from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "created_at"]
