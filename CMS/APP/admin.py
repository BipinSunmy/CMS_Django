from django.contrib import admin
from .models import Qualifications,Staff,Patient,Payment,Prescrible,Appointment,Billing,Medicine,Lab,Doctor,Specialization,Time,BloodGroup
from rest_framework.authtoken.models import Token
# Register your models here.

admin.site.register(Qualifications)
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(Payment)
admin.site.register(Prescrible)
admin.site.register(Appointment)
admin.site.register(Billing)
admin.site.register(Medicine)
admin.site.register(Lab)
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Time)
admin.site.register(BloodGroup)
admin.site.register(Token)