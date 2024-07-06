from django.urls import path

from posts.views import PostListView, PostCommentListView, PostCreateAPIView, PostCommentCreateAPIView, PostLikeAPIView, \
    CommentLikeAPIView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/comments/', PostCommentListView.as_view(), name='comments-list'),
    path('<int:pk>/comments/create/', PostCommentCreateAPIView.as_view(), name='comments-create'),

    path('<int:pk>/like/', PostLikeAPIView.as_view(), name='like'),
    path('comment/<int:pk>/like/', CommentLikeAPIView.as_view(), name='comment-like'),
]
