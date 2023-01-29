from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author: 추후에 작성

    def __str__(self):
        return f'[{self.pk}]\n{self.title}'  # 포스트 번호와 제목 보여주기 [번호] 제목

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
