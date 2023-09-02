from django.db import models

class Teacher(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)