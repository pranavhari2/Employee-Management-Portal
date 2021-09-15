from django.db import models

# Create your models here
# 
# c.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    
class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    DepartmentName = models.CharField(max_length=500)
    DateJoined = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
