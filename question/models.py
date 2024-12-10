from django.db import models
from django.db.models import UniqueConstraint
from classes.models import Classes
from authentication.models import User

# Create your models here.
class Question(models.Model):
    question_id = models.BigAutoField(default=None, primary_key=True)
    question = models.CharField(max_length=255, default="")
    qr_url = models.CharField(max_length=255, default="")
    class_id = models.ForeignKey(Classes, default=None, on_delete=models.CASCADE)
    
class Options(models.Model):
    option_id = models.BigAutoField(default=None, primary_key=True)
    description = models.CharField(max_length=255, default="")
    question_id = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)
    
class StudentQuestion(models.Model):
    student_code = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer = models.ForeignKey(Options, default=None, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['student_code', 'question_id'], name='unique_host_migration'),
        ]