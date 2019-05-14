from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

# Create your models here

class MyUser(AbstractUser):
    password_check = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Post(models.Model):    
    # 사용자 선택 폼
    men = models.CharField(max_length=20, default="")
    soup = models.CharField(max_length=20, default="")
    hoke = models.CharField(max_length=20, default="")
    topping = models.CharField(max_length=20, default="")
    extra = models.CharField(max_length=20, default="")
    # 사용자 글 작성
    img = models.FileField(null=True)
    user = models.CharField(max_length=50, default="")
    content = models.TextField(default ="내용을 입력해주세요..")
    title = models.CharField(max_length=50, default="제목을 입력해주세요..")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        
class Ramen(models.Model):
    ramen_img = models.FileField(null=True)
    ramen_name = models.CharField(max_length=50, default="")


class Topping(models.Model):
    topping_img = models.FileField(null=True)
    topping_name = models.CharField(max_length=50, default="")

class Extra(models.Model):
    extra_img = models.FileField(null=True)
    extra_name = models.CharField(max_length=50, default="")


class Comment(models.Model):
    SCORE_CHOICES = (
        ('★☆☆☆☆', '별 한개'),
        ('★★☆☆☆', '별 두개'),
        ('★★★☆☆', '별 세개'),
        ('★★★★☆', '별 네개'),
        ('★★★★★', '별 다섯개'),
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    score = models.CharField(max_length=10, choices=SCORE_CHOICES)
    addcontent = models.TextField()

# 기본적으로 로그인 기본화면은 구현완료, 각 포스트별 권한 추가해야함
