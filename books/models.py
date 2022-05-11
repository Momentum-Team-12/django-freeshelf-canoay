from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title       = models.CharField(max_length=455)
    author      = models.CharField(max_length=455)
    patternlnk  = models.URLField(blank=True,null=True)
    description = models.TextField(max_length=1000, null=True, blank=True) 
    created_at  = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name='books', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=455, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)
    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Favorite (models.Model):
    book = models.ForeignKey('Book', related_name='favorites', on_delete = models.CASCADE)
    user = models.ForeignKey('User', related_name='favorites', on_delete = models.CASCADE)
