from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import time
from machines.models import Machines


# Create your models here.
TIMESLOT_CHOICES = [
    ("08:00", "08:00 AM"),
    ("09:00", "09:00 AM"),
    ("10:00", "10:00 AM"),
    ("11:00", "11:00 AM"),
    ("12:00", "12:00 PM"),
]


class Appointment(models.Model):
    """
    This Represent Appointment for one machine 
    """
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="customer")
    machine_selected = models.ForeignKey('machines.Machines',
                                         on_delete=models.CASCADE,
                                         related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=5, choices=TIMESLOT_CHOICES)
    requests = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date", "appointment_time"]

    def __str__(self):
        return f"{self.booking_id}/{self.name} - {self.machine_selected} at {
            self.appointment_time} on {self.appointment_date}"
