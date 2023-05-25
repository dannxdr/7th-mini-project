from django.db import models

# Create your models here.
class User_info(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name='username')
    password = models.CharField(max_length=128, verbose_name='password')
    user_register = models.DateTimeField(auto_now_add =True, verbose_name='register_time')
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'