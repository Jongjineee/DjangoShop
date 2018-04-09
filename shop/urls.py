from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^notice/$', views.notice, name='notice'),
    url(r'^notice/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),

]
