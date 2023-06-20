from django.urls import path
from . import views

urlpatterns=[
    path('login', views.login, name='login'),
    path('', views.usr, name='usr'),
    path('register', views.register, name='register'),
]