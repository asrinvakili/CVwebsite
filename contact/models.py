from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    subject = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



