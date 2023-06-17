from django.db import models

# Create your models here.
class Members(models.Model):
    user_name= models.CharField(max_length=50)
    pass_word= models.CharField(max_length=50)
    e_mail=models.EmailField(max_length=50)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)

    def __str__(self):
        return self.user_name