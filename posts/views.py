from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from posts.models import PostModel
from posts.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PostModel.objects.all()
