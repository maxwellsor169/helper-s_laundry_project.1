from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


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
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="machines/",
        force_format="WEBP",
        blank=False,
        null=3,
    )
    image_alt = models.CharField(max_length=100, null=3, blank=False)


class Meta:
    db_table = 'machines.machine_type'
    ordering = ["machine_type"]


def __str__(self):
    return f"{self.machine_type} : {self.specification} : {self.machine_no}"