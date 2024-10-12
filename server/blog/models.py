from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=75)

    def __str__(self):
        return self.title


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=65)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    details = models.TextField()
    image = models.ImageField(upload_to="blog_image")
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

# Create your models here.
