from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    i_d = models.CharField(max_length=50)
    moves =models.CharField(max_length=1000)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1')

    def __str__(self):
        return self.i_d
