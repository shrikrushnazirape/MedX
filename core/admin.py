from django.contrib import admin

# Register your models here
from . import models
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Prescription)
admin.site.register(models.Medecine)
