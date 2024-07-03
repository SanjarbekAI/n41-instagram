from rest_framework import serializers
from posts.models import PostModel, PostLikeModel
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['uuid', 'avatar', 'username']


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField('get_likes_count')
    comment_count = serializers.SerializerMethodField('get_comments_count')
    me_liked = serializers.SerializerMethodField('get_me_liked')
    user = UserSerializer(read_only=True)

    class Meta:
        model = PostModel
        fields = ['image', 'caption', 'uuid', 'likes_count', 'user', 'me_liked', 'comment_count']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_me_liked(self, obj):
        request = self.context.get('request', None)
        return PostLikeModel.objects.filter(post=obj, user=request.user).exists()
