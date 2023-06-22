from django.urls import path
from . import views


# URLconf
urlpatterns = [
    path("", views.play_home, name='play_home'),
    path("generate", views.generate_board),
#    path('show', views.chessboard, name='chessboard'),
    path('history', views.history),
    path('new', views.create_game),
    path('new/<str:id>/', views.waiting_for_player, name='waiting_for_player'),
#    path('new/<str:id>/', views.play_game, name='play_game'),
    path('chessboard/<str:id>/', views.chessboard, name='chessboard'),
    path('join/', views.join_code_view, name='join_code_view'),
]