from django.db import models
from django.contrib import admin
# Create your models here.
class Employee(models.Model):
    Employee_name = models.CharField(max_length=20, help_text="Enter Employee Name")
    age = models.IntegerField(help_text="Enter age of Employee")
    dob = models.DateField(help_text="Enter Date of Birth")
    reg_no = models.IntegerField(help_text="Enter the Register Number")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Employee_name', 'age', 'dob','reg_no']