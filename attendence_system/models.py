from django.db import models
from django.db import models
from main.models import Employee, EmployeeWork


class EmployeePresence(models.Model):
    Employee = models.OneToOneField(Student, models.CASCADE)
    present = models.BooleanField(default=True)
    Employee_work = models.ForeignKey(EmployeeWork, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    # appear in the least again
# Create your models here.
