from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from posts.models import PostModel, PostCommentModel
from posts.serializers import PostSerializer, CommentSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PostModel.objects.all()


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return PostCommentModel.objects.filter(post_id=post_id)