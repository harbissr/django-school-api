from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    student_email = models.EmailField(max_length=100, blank=False)
    personal_email = models.EmailField(max_length=100)
    locker_number = models.IntegerField(blank=False)
    locker_combination = models.CharField(max_length=8, blank=False)
    good_student = models.BooleanField(blank=False)
