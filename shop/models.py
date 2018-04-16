from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from sorl.thumbnail import ImageField

class Category(models.Model):
    sort = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.sort)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    image = ImageField(upload_to='photos')
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.name, self.pub_date)


class Point(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    all_point = models.IntegerField()
    able_point = models.IntegerField()


class Order(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    order_date = models.DateTimeField(auto_now_add=True)
    all_order_list = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user_order_all', blank=True)
    wish_list = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user_wish_order', blank=True)


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





