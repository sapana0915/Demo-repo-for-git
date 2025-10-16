from django.db import models

# Create your models here.


class Employee(models.Model):
    Emp_id = models.AutoField(primary_key=True)
    Emp_name = models.CharField(max_length=100)
    Emp_email = models.EmailField(max_length=100)
    Emp_address = models.CharField(max_length=100)

    def __str__(self):
        return self.Emp_name

class Department(models.Model):
    Dept_id = models.AutoField(primary_key=True)
    Dept_name = models.CharField(max_length=100)
    Dept_location = models.CharField(max_length=100)

    def __str__(self):
        return self.Dept_name
