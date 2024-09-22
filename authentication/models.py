from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    document_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code = models.CharField(max_length=15, unique=True)
    address_direction = models.CharField(max_length=90)
    photo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    
    REQUIRED_FIELDS = [
        'username',
        'email',
        'first_name',
        'last_name',
        ]
    USERNAME_FIELD = 'code'
    objects = CustomUserManager()
    
    def __str__(self):
        return self.code
