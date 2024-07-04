from django.contrib import admin

from posts.models import PostModel, CommentLikeModel, PostCommentModel, PostLikeModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'user', 'created_at']
    search_fields = ['caption', 'user', 'id']
    list_filter = ['created_at', 'updated_at']


@admin.register(PostCommentModel)
class PostCommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user', 'created_at']
    search_fields = ['comment', 'id']
    list_filter = ['created_at', 'updated_at']


@admin.register(PostLikeModel)
class PostLikeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at', 'updated_at']


@admin.register(CommentLikeModel)
class CommentLikeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at', 'updated_at']