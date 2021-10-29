
from django.contrib import admin
from django.urls import path
from . import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('result/', views.result, name="result"),
    path('About',views.about, name="about"),
    path('team',views.ourteams, name="ourteams"),
    path('form',views.ourservices, name="ourservices")

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
