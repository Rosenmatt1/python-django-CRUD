from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.Charfield(max_length=50)

class Employee(models.Model):
    fullname = models.Charfield(max_length=100)
    emp_code = models.Charfield(max_length=3)
    mobile = models.Charfield(max_length=15)
    position = models.Charfield(max_length=100)
