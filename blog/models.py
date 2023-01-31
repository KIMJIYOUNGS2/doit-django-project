from django.db import models
import os
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 포스트의 작성자가 데이터베이스에서 삭제되었을 때 포스트도 삭제
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        # 포스트 번호와 제목 보여주기 [번호] 제목
        return f'[{self.pk}]\n{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)  # 파일 이름 출력

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]  # 확장자 출력
