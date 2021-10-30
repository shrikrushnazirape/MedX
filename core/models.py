
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields.related import OneToOneField
import uuid


# Create your models here.

class Doctor(models.Model):
    user= models.OneToOneField(User, on_delete=CASCADE)
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doc_details = models.TextField(max_length=500, null= True, blank= True)
    edu_details = models.TextField(max_length=500, null= True, blank= True)
    Address = models.TextField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=10, blank=True, null=True)
    clinic_name = models.CharField(max_length=100, blank=True, null=True)




class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dob = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank= True, null= True)
    bloodgroup = models.CharField(max_length=5,blank= True, null= True)
    contact = models.CharField(max_length=10, blank=True, null=True)
    pre_med_hist = models.TextField(max_length=100, blank= True, null= True)

  
    def getuuid(self):
        return self.patient_id


class Prescription(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=CASCADE)
    fees = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null= True)
    status = models.BooleanField(default=False);




class Medecine(models.Model):
    med_name = models.CharField(max_length=50, blank=True, null=True)
    qty = models.IntegerField(blank= True, null= True)
    prescription = models.ForeignKey(Prescription, on_delete=CASCADE)
    dose = models.CharField(blank=True, null=True, default="",max_length=100)

    def __str__(self):
        return self.med_name
    