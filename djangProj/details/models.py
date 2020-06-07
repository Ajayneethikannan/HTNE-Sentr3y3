from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from picklefield.fields import PickledObjectField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True)
    is_admin = models.BooleanField(default=False)
    is_underage = models.BooleanField(default=True)
    image = models.ImageField(upload_to='faces', null=True, blank=True)

    def __str__(self):
        return self.username

class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apps')
    title = models.CharField(max_length=100)
    time_limit = models.IntegerField(default=3600, blank=True) # Time limit in seconds default 1 hour
    grace_time = models.IntegerField(default=0) # Grace time to delay time_exceeded event
    time_today = models.IntegerField(default=0)
    week_time = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)

    time_exceeded = models.BooleanField(default=False) # Pausing an application depends only on this

    forbidden = models.BooleanField(default=False)
    warning = models.TextField(default='None')

    def __str__(self):
        return f'{self.user.username} {self.title}'
