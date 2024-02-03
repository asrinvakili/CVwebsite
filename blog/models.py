from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    count_views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

