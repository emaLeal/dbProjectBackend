from django.db import models

# Create your models here.
class Role(models.Model):
    id = models.BigAutoField(primary_key=True, default=4)
    description = models.CharField(max_length=30)