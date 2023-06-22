from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    i_d = models.CharField(max_length=50, unique=True)
    is_waiting = models.CharField(max_length=10, default='True')
    moves =models.CharField(max_length=1000)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1', default='default_player_1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2', default='default_player_2')

    def __str__(self):
        return self.i_d

class JoinCode(models.Model):
    code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.code
