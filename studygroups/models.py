from django.db import models

class Student(models.Model):
  firstName = models.CharField(max_length=255)
  lastName = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  house = models.CharField(max_length=20)