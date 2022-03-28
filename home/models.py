from pyexpat import model
from tkinter import CASCADE
from django.db import models

class Owner(models.Model):
    CNIC = models.CharField(max_length=15, verbose_name='National ID Card Number', primary_key=True)
    full_Name = models.CharField(max_length=50, verbose_name='Full Name of the Owner')
    phone_numer = models.CharField(max_length=11)
    citizen_of = models.CharField(max_length=10, verbose_name='Select the Country')
    address_of_owner =  models.CharField(max_length=100)

    def __str__(self):
        return self.CNIC
        
# Code from CYPRIAN
class VehicleDetail(models.Model):
    vehicle_number = models.CharField(max_length=30, primary_key = True)
    owner = models.ForeignKey(Owner, on_delete = models.PROTECT)
    Model_number=models.CharField(max_length=30)
    Chasis_number=models.CharField(max_length=30)
    Engine_number=models.CharField(max_length=30)
    Vehicle_type =models.CharField(max_length=100)

    def __str__(self):
        return self.Vehicle_number
        

