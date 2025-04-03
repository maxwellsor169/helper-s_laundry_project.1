from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Taken"), (1, "Available"))


# Create your models here.
class Machines(models.Model):
    """
    Describes the machines and our sevices 
    """
    machine_type = models.CharField(max_length=200)
    specification = models.TextField()
    machine_no = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    ordering = ["machine_type"]


def __str__(self):
    return f"{self.machine_type} : {self.specification} : {self.machine_no}"