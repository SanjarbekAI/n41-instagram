from django.db import models
from shared.models import BaseModel
from users.models import UserModel


class PostModel(BaseModel):
    image = models.ImageField(upload_to='posts')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.full_name

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class PostLikeModel(BaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return self.user.full_name

    class Meta:
        db_table = 'post_likes'
        verbose_name = 'post like'
        verbose_name_plural = 'post likes'


class PostCommentModel(BaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_comments')
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', null=True, blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'post_comments'
        verbose_name = 'post comment'
        verbose_name_plural = 'post comments'


class CommentLikeModel(BaseModel):
    comment = models.ForeignKey(PostCommentModel, on_delete=models.CASCADE, related_name='comments_likes')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment_likes')

    def __str__(self):
        return self.comment.comment

    class Meta:
        db_table = 'comment_likes'
        verbose_name = 'comment like'
        verbose_name_plural = 'comment likes'



