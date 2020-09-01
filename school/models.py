from django.db import models

"""
Multiple Inheritance and create comman 
model then use same field in other tables.
CommanInfo model use meta class and meta 
class define the abstract=True. 
"""

class CommanInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Student(CommanInfo):
    fees = models.IntegerField()
    date = None

class Teacher(CommanInfo):
    salary = models.IntegerField()

class Contractor(CommanInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()
