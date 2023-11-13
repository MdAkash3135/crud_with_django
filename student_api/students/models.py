from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)


    def __str__(self):
        return self.name