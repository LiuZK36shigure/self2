from django.db import models

# Create your models here.
class Teacher(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teacher_photos')