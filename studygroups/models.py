from django.db import models

# Create your models here.
class Criteria(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gpa = models.IntegerField()
    skills = models.CharField(max_length=64)
    schedule = models.CharField(max_length=512)

    def __str__(self):
        return first_name + " "  + last_name
