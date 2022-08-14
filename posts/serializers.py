from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Post, Comment


# 댓글 전체 Serializer
class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")



# 게시글 전체 Serializer
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer
    comments = CommentSerializer(many=True, read_only=True) # 댓글 시리얼라이저를 포함하여 댓글 추가, 다수 댓글 포함

    class Meta:
        model = Post
        fields = ('pk', 'profile', 'title', 'body', 'image', 'published_date', 'likes')

# 게시글 하나 생성 Serializer
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'image')


