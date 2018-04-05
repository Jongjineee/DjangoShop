from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = ImageField(upload_to='photos')
    price = models.IntegerField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{} {}'.format(self.name, self.pub_date)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
