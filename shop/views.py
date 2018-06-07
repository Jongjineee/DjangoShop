from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Product, Post, Point, Order, Category, Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import OrderForm
# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'shop/index.html', context)


def profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'shop/profile.html')


def notice(request):
    post_list = Post.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts, 'categories': categories}
    return render(request, 'shop/notice.html', context)


def notice_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'shop/notice_detail.html', context)


def order_list(request, pk):
    categories = Category.objects.all()
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
    context = {'user': user, 'orders': orders, 'categories': categories}
    return render(request, 'shop/order_list.html', context)


def show_category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category).order_by('pub_date')
    lank_products = Product.objects.filter(category=category).order_by('-hit')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products, 'category': category, 'categories': categories}
    return render(request, 'shop/category.html', context)


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get(pk=pk)
    category = Category.objects.get(pk=product.category.pk)
    Product.objects.filter(pk=pk).update(hit=product.hit+1)
    point = int(product.price * 0.01)
    context = {"product": product, "point": point, "category": category, "categories": categories}
    return render(request, 'shop/detail.html', context)


def cart(request, pk):
    categories = Category.objects.all()
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
    context = {'user': user, 'cart': cart, 'categories': categories}
    return render(request, 'shop/cart.html', context)


def insert_cart(request, pk):

    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        user = request.user

        if Cart.objects.filter(products=product):
            cart=Cart.objects.get(products=product)
            Cart.objects.filter(products=product).update(quantity=cart.quantity+1)
            messages.success(request, '장바구니 등록 완료')
            return redirect('shop:product_detail', pk)

        else:
            cart = Cart(user=user, products=product)
            cart.save()
            messages.success(request, '장바구니 등록 완료')
            return redirect('shop:product_detail', pk)

def buyitnow(request, pk) :
    categories = Category.objects.all()
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        user = request.user

        context = {'user': user, 'product': product, 'categories': categories}

        return render(request, 'shop/order_pay.html', context)

