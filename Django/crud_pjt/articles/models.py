from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.TextField(default='강사')
    views = models.IntegerField(default=0)
    # blank -> 데이터가 없음 (조금 더 많이 씀) / NULL -> 에러 발생
    # upload_to = 미디어 파일 관리를 위해 사용
    image = models.ImageField(blank=True, upload_to="articles/%Y%m%d")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'
