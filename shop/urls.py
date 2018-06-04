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
    url(r'^(?P<category_id>[0-9]+)/$', views.show_category, name='show_category'),
    url(r'^(?P<category_id>[0-9]+)/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<category_id>[0-9]+)/(?P<pk>[0-9]+)/insert_cart$', views.insert_cart, name='insert_cart'),
    url(r'^(?P<category_id>[0-9]+)/(?P<pk>[0-9]+)/buyitnow$', views.buyitnow, name='buyitnow'),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.cart, name='cart'),

]
