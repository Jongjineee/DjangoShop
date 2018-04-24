from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Product, Post, Point, Order, Category, Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
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
    paginator = Paginator(post_list, 10)
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
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {'user': user, 'orders': orders}
    return render(request, 'shop/order_list.html', context)


def suit_page(request):
    suit = Category.objects.get(sort='suit')
    lank_products = Product.objects.filter(category=suit).order_by('-hit')
    products = Product.objects.filter(category=suit).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/suit.html', context)

def outer_page(request):
    outer = Category.objects.get(sort='outer')
    lank_products = Product.objects.filter(category=outer).order_by('-hit')[:5]
    products = Product.objects.filter(category=outer).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/outer.html', context)

def acc_page(request):
    acc = Category.objects.get(sort='acc')
    lank_products = Product.objects.filter(category=acc).order_by('-hit')[:5]
    products = Product.objects.filter(category=acc).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/acc.html', context)

def bottom_page(request):
    bottom = Category.objects.get(sort='bottom')
    lank_products = Product.objects.filter(category=bottom).order_by('-hit')[:5]
    products = Product.objects.filter(category=bottom).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/bottom.html', context)

def shirts_page(request):
    shirts = Category.objects.get(sort='shirts')
    lank_products = Product.objects.filter(category=shirts).order_by('-hit')[:5]
    products = Product.objects.filter(category=shirts).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/shirts.html', context)

def shoes_page(request):
    shoes = Category.objects.get(sort='shoes')
    lank_products = Product.objects.filter(category=shoes).order_by('-hit')[:5]
    products = Product.objects.filter(category=shoes).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/shoes.html', context)

def top_page(request):
    top = Category.objects.get(sort='top')
    lank_products = Product.objects.filter(category=top).order_by('-hit')[:5]
    products = Product.objects.filter(category=top).order_by('pub_date')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products}
    return render(request, 'shop/top.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    Product.objects.filter(pk=pk).update(hit=product.hit+1)
    point = int(product.price * 0.01)
    context = {"product": product, "point": point}
    return render(request, 'shop/detail.html', context)


def cart(request, pk):
    user = User.objects.get(pk=pk)
    cart = Cart.objects.filter(user=user)
    paginator = Paginator(cart, 5)
    page = request.GET.get('page')
    try:
        cart = paginator.page(page)
    except PageNotAnInteger:
        cart = paginator.page(1)
    except EmptyPage:
        cart = paginator.page(paginator.num_pages)
    context = {'user': user, 'cart': cart}
    return render(request, 'shop/cart.html', context)

def insert_cart(request, pk):
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.filter(user=request.user)
    cart.product = product
    cart.save()
    messages.success(request, '장바구니 등록 완료')

    return redirect('shop:product_detail', pk)
