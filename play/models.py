from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    id1= models.CharField(max_length=50)
    moves=models.CharField(max_length=200)
    player1=models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1')
    player2=models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2')
