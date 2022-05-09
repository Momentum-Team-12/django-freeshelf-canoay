from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title       = models.CharField(max_length=455)
    author      = models.CharField(max_length=455)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    patternlnk  = models.URLField(blank=True,null=True)

