from django.db import models

class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=20)
    department_name = models.CharField(max_length=50)

class Employees(models.Model):
    eid = models.CharField(primary_key=True, max_length=20)
    ename = models.CharField(max_length=50)
    email = models.EmailField()
    econtact = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

