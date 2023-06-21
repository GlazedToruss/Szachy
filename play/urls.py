from django.urls import path
from . import views


# URLconf
urlpatterns = [
    path("", views.play_home, name='play_home'),
    path("generate", views.generate_board),
    path('show', views.chessboard, name='chessboard'),
    path('history', views.history),
    path('new', views.create_game),
    path('new/<str:id>/', views.waiting_for_player),
    path("join", views.join),
]