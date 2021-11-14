from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=40)
    class Meta:
        db_table = "Student"

class Employee(models.Model):
    eid = models.CharField(max_length=34)
    ename = models.CharField(max_length=45)
    econtact = models.CharField(max_length=46)

    class Meta:
        db_table = "employee"
