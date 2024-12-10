from django.db import models
from courses.models import Courses
from student.models import Student
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Classes(models.Model):
    class_id = models.BigAutoField(unique=True, primary_key=True, default=None)
    class_name = models.CharField(max_length=120, default="")
    room = models.CharField(max_length=10, default="")
    schedule = models.CharField(max_length=200, default="")
    date = models.DateField()
    course = models.ForeignKey(Courses, default=None, on_delete=models.CASCADE)
    
class Material(models.Model):
    file_id = models.BigAutoField(unique=True, primary_key=True, default=True)
    file_name = models.CharField(max_length=100, default="")
    file_path = models.CharField(max_length=100, default="")
    file_type = models.CharField(max_length=10, default="")
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, default=None)
    
class Attendance(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        ATTEND = 'attend', _('Attend')
        NOT_ATTEND = 'not_attend', _('Did not Attend')
            
    attendance = models.BigAutoField(unique=True, primary_key=True, default=None)
    student_code = models.ForeignKey(Student, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING)
    hour = models.TimeField(default=None)
    location = models.CharField(max_length=50, default=None)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, default=None)