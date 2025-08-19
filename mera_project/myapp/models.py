from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.CharField(max_length=55)
    designation = models.CharField(max_length=60)
    department = models.CharField(max_length=70)
    qualification = models.CharField(max_length=65)

    def __str__(self):
        return self.name



