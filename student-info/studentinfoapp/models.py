from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class Student(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    faculty = models.CharField(max_length=255)
    hall = models.CharField(max_length=255)
