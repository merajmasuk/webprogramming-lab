from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=63)
    present_address = models.CharField(max_length=127)
    registration_date = models.DateTimeField(auto_now_add=True)
    reg_no = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return f'{self.name} reg {self.reg_no}'

    def __iter__(self):
        yield 'name', self.name
        yield 'present_address', self.present_address
        yield 'registration_date', self.registration_date
        yield 'reg_no', self.reg_no
