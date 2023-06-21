from django.urls import path
from . import views


# URLconf
urlpatterns = [
    path("", views.play_home, name='play_home'),
    path("generate", views.generate_board),
    path('show', views.chessboard, name='chessboard'),
]