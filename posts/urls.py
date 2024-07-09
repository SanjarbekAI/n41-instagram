from django.urls import path

from posts.views import PostListView, PostCommentListView, PostCreateAPIView, PostCommentCreateAPIView, PostLikeAPIView, \
    CommentLikeAPIView, PostUpdateAPIView, CommentUpdateAPIView, PostDeleteAPIView, UserPostListView, \
    UserLikedPostListView

app_name = 'posts'

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('list/liked/', UserLikedPostListView.as_view(), name='list-liked'),
    path('myself/', UserPostListView.as_view(), name='myself'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/like/', PostLikeAPIView.as_view(), name='like'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),


    path('<int:pk>/comments/', PostCommentListView.as_view(), name='comments-list'),
    path('<int:pk>/comments/create/', PostCommentCreateAPIView.as_view(), name='comments-create'),
    path('<int:pk>/comments/like/', CommentLikeAPIView.as_view(), name='comment-like'),
    path('<int:pk>/comment/update/', CommentUpdateAPIView.as_view(), name='update-comment'),
    # path('<int:pk>/comment/delete/', CommentUpdateAPIView.as_view(), name='update-comment'),
]
