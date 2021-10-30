
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('result/', views.result, name="result"),
    path('About',views.about, name="about"),
    path('team',views.ourteams, name="ourteams"),
    path('form',views.ourservices, name="ourservices")
]
