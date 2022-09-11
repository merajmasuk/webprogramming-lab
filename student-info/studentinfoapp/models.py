from django.db import models

# Create your models here.
class User:
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(255)
    last_name = models.CharField(255)
    email = models.EmailField()


class Student:
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(255)
    last_name = models.CharField(255)
    dob = models.DateField
    faculty = models.CharField(255)
    hall = models.CharField(255)
