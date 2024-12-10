from django.db import models
from authentication.models import User

# Create your models here.
class Courses(models.Model):
    course_id = models.BigAutoField(primary_key=True, default=None)
    course_name = models.CharField(max_length=150, default="")
    teacher = models.ForeignKey(User, default="", on_delete=models.CASCADE)