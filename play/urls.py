from django.urls import path
from . import views


# URLconf
urlpatterns = [
    path("", views.board),
    path("generate", views.generate_board),
    path('show', views.chessboard, name='chessboard'),
]