from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class CarOwner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created', editable=False)
    updated_at = models.DateTimeField('date updated')

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(CarOwner, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name


class Car(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField('date created', editable=False)
    updated_at = models.DateTimeField('date updated')

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.license_number
