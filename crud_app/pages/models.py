from django.db import models
from django.utils.timezone import now

# tables is created in this area

# Create employee table
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hire_date = models.DateField(default=now, editable=False)
    hourly_rate = models.FloatField()
    working_percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
# create team table
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.team_name

# create team employee table
class TeamEmployee(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, default=0, related_name='employee_id')
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='t_id')
    is_lead = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.employee_id.name}, {self.employee_id.surname}, {self.team_id.team_name}"