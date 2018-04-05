from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Product, Post
# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def profile(request):
    return render(request, 'shop/profile.html')

def notice(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'shop/notice.html', context)