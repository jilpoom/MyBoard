from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
# Create your models here.

class Post(models.Model):
    #related_name => 서로 참조하는 관계에서 외래키 선언, Post -> User는 성립하나 User -> Post는 성립하지 않음, related_name으로 관계 맺기
    #같은 외래키로써 User를 참조하는 필드 두 개(author, likes) -> related_name을 설정하지 않으면 User에서 접근할 때 구분되지 않는 오류 발생
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    published_date = models.DateTimeField(default=timezone.now)

# 댓글 기능
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()