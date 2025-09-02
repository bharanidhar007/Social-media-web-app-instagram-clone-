
from rest_framework import serializers
from .models import Post, Comment
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    class Meta: model = Post; fields = ('id','author','caption','image','created_at','likes_count')
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta: model = Comment; fields = ('id','post','author','text','created_at'); read_only_fields=('post',)
