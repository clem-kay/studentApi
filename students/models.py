from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Student(models.Model):
    department = models.ForeignKey(Department,related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'