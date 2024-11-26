from django.db import models
from django.contrib.auth.models import AbstractUser
from role.models import Role
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    '''Custom Model for an user that will be a teacher, monitor, student or admin'''
    
    class StateUser(models.TextChoices):
        PENDING = 'pending', _('Pending')
        ACTIVE = 'active', _('Active')
        INACTIVE = 'inactive', _('Inactive')
    document_id = models.CharField(max_length=15, unique=True, default="", primary_key=True)
    name = models.CharField(max_length=110, default="")
    state = models.CharField(max_length=10, choices=StateUser.choices, default=StateUser.PENDING)
    email = models.EmailField(max_length=255, unique=True, default="")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=4)
    
    REQUIRED_FIELDS = [
        'username',
        'name',
        'email',
        'state',
        'role'
        ]
    USERNAME_FIELD = 'document_id'
    objects = CustomUserManager()
    
    def __str__(self):
        return self.document_id

