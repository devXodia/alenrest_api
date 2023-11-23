from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(
            title=request.POST.get("title", ""),
            description=request.POST.get("description", ""),
            user=request.user,
        )
        serialized_obj = serializers.serialize(
            "json",
            [
                todo,
            ],
        )
        return HttpResponse(serialized_obj, content_type="application/json")
