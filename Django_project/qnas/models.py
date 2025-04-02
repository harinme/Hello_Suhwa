from django.db import models

# Create your models here.
class Qna(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)