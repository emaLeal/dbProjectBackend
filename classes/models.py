from django.db import models
from courses.models import Courses

# Create your models here.
class Classes(models.Model):
    class_id = models.BigAutoField(unique=True, primary_key=True, default=None)
    class_name = models.CharField(max_length=120, default="")
    room = models.CharField(max_length=10, default="")
    schedule = models.CharField(max_length=200, default="")
    date = models.DateField()
    course = models.ForeignKey(Courses, default=None, on_delete=models.CASCADE)