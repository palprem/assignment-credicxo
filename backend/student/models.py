from django.db import models
from users.models import Users
# Create your models here.

class Student(models.Model):
    id = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=50,null=True, unique=True)
    full_name  = models.CharField(max_length=100, null=True)
    