from django.db import models

# Create your models here.
class Student(models.Model):
    temp = models.FloatField()
    curr_time = models.TimeField()
    def __str__(self):
        return str(self.temp)
    