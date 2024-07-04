from django.urls import path

from posts.views import PostListView, PostCommentListView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/comments/', PostCommentListView.as_view(), name='comments-list'),
]
