from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.index),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
