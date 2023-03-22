from django.db import models

# Create your models here.


class Members (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Student (models.Model):
    firstname = models.CharField(max_length=31)
    lastname = models.CharField(max_length=31)
    roll = models.IntegerField
    reg = models.IntegerField
    dob = models.DateField
    dept = models.CharField(max_length=31)
    hall = models.CharField(max_length=31)
    session = models.CharField(max_length=10)
    email = models.EmailField
    phone = models.CharField(max_length=14)
    blood_group = models.CharField(max_length=3)    # TODO: make enum


class Course (models.Model):
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=31)
    credits = models.IntegerField
    course_teacher = models.CharField(max_length=63)
    grades = models.IntegerField
