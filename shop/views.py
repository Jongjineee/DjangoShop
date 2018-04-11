from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView
from .models import Product, Post, Point, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'shop/profile.html')

def notice(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'shop/notice.html', context)

def notice_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'shop/notice_detail.html', context)

def order_list(request, pk):
    user = User.objects.get(pk=pk)
    orders = Order.objects.filter(user=user)
    context = {'user': user, 'orders': orders}
    return render(request, 'shop/order_list.html', context)

def suit_page(reqeust):
    return render(reqeust, 'shop/suit.html')