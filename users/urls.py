from django.urls import path
from . import views

urlpatterns=[
    path('login', views.loginn, name='login'),
    path('', views.usr, name='usr'),
    path('register', views.register, name='register'),
    path('logout', views.logoutt, name='logut'),
]