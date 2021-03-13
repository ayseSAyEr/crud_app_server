from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    employee_ID = models.IntegerField()
    team = models.CharField(max_length=100)
    hourly_rate = models.FloatField()

    def __str__(self):
        return self.name