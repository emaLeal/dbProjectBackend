from django.db import models
from authentication.models import User

# Create your models here.
class Student(models.Model):
    student_code = models.CharField(max_length=15, default=None, primary_key=True)
    academic_register = models.CharField(max_length=15, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    