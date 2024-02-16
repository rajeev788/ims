from django.db import models



# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=300)
    username=models.CharField(max_length=300,null=True,default='user')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

