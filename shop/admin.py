from django.contrib import admin
from .models import Product, Post, Point, Order, Category, Cart
# Register your models here.

admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Point)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Cart)