from django.db import models

<<<<<<< HEAD
# Create your models here.
class Criteria(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gpa = models.IntegerField()
    skills = models.CharField(max_length=64)
    schedule = models.CharField(max_length=512)

    def __str__(self):
        return first_name + " "  + last_name
=======
class Student(models.Model):
  firstName = models.CharField(max_length=255)
  lastName = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  house = models.CharField(max_length=20)
>>>>>>> 74bf2ceaec1f9c3ae22043f8842452f9f18a9f3f
