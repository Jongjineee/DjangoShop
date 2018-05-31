from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)/order_list/$', views.order_list, name='order_list'),
    url(r'^notice/$', views.notice, name='notice'),
    url(r'^notice/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    url(r'^suit_page/$', views.suit_page, name='suit_page'),
    url(r'^suit_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^suit_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^suit_page/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^outer_page/$', views.outer_page, name='outer_page'),
    url(r'^outer_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^outer_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^outer_page/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^top_page/$', views.top_page, name='top_page'),
    url(r'^top_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^top_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^top_page/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^shirts_page/$', views.shirts_page, name='shirts_page'),
    url(r'^shirts_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^shirts_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^shirts_page/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^bottom_page/$', views.bottom_page, name='bottom_page'),
    url(r'^bottom_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^bottom_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^bottom_page/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^shoes_page/$', views.shoes_page, name='shoes_page'),
    url(r'^shoes_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^shoes_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^shoes_page/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^acc_page/$', views.acc_page, name='acc_page'),
    url(r'^acc_page/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^acc_page/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^acc_page/(?P<pk>[0-9]+)/buyitnow/$', views.buyitnow, name='buyitnow'),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.cart, name='cart'),


]
