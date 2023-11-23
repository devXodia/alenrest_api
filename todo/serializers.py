from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # user = request.user
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
        ]


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = CurrentUserDefault()
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Todo
        # user = request.user
        fields = ["id", "title", "description", "created_at", "user", "time_passed"]
