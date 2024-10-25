from django.db import models

# Create your models here.

# modelo do banco de dados 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=200)
    tags = models.JSONField(default=list)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title