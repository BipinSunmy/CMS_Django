from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.forms import ValidationError
# Create your models here.

class Qualifications(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Specialization(models.Model):
    specialization = models.CharField(max_length=25)
    def __str__(self):
        return self.specialization
    
class Lab(models.Model):
    test = models.CharField(max_length=30)
    def __str__(self):
        return self.test

class Medicine(models.Model):
    medicine = models.CharField(max_length=30)
    def __str__(self):
        return self.medicine

class Time(models.Model):
    Timings = models.CharField(max_length=25)
    def __str__(self):
        return self.Timings
def staff_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 21:
        raise ValidationError('The staff member must be at least 21 years old.')
class Staff(models.Model):
    l_id = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    Qualification = models.ManyToManyField(Qualifications)
    DoB = models.DateField(validators=[staff_age])
    salary = models.IntegerField() 
    def __str__(self):
        return self.f_name
def doctor_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 25:
        raise ValidationError('The staff member must be at least 21 years old.')
class Doctor(models.Model):
    doc_id = models.AutoField(primary_key=True)
    l_id = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    email = models.EmailField()
    specialization = models.ForeignKey(Specialization,on_delete=models.SET_NULL,null=True)
    Qualification = models.ManyToManyField(Qualifications)
    DoB = models.DateField(validators=[doctor_age]) 
    fee = models.IntegerField()
    phone = models.CharField(max_length=10)
    Available = models.BooleanField(default=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    salary = models.IntegerField()
    def __str__(self):
        return self.f_name
class Patient(models.Model):
    name = models.CharField(max_length=25)
    DoB = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    blood = models.CharField(max_length=10)
    def __str__(self):
        return self.name
def past_day(value):
    today = date.today()
    if value < today:
        raise ValidationError('You cant choose any previous date')
class Appointment(models.Model):
    a_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    token = models.IntegerField(blank=True)
    DoA = models.DateField(validators=[past_day]) 
    time = models.ForeignKey(Time,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.DoA:
            self.DoA = date.today()
        today = self.DoA
        doctor_appointments = Appointment.objects.filter(d_id=self.d_id, DoA=today)
        if doctor_appointments.count() >= 25:
            raise ValueError(f"Token limit of 25 reached for Doctor {self.d_id} on {today}.")
        latest_appointment = doctor_appointments.order_by('token').last()
        self.token = (latest_appointment.token + 1) if latest_appointment else 1
        super(Appointment, self).save(*args, **kwargs)
    def __str__(self):
        return self.p_id.name

class Prescrible(models.Model):
    p_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    d_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    notes = models.CharField(max_length=150)
    medicine = models.ManyToManyField(Medicine,default=None)
    test = models.ManyToManyField(Lab,default=None)
    def __str__(self):
        return f"Doctor : {self.d_id.f_name} and Patient : {self.p_id.name}"
class Billing(models.Model):
    d_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    a_id = models.ForeignKey(Appointment,on_delete=models.CASCADE)
    def __str__(self):
        return f"Doctor : {self.d_id.f_name} , Fee : {self.d_id.fee}"
class Payment(models.Model):
    p_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    b_id = models.ForeignKey(Billing,on_delete=models.CASCADE)
    types = models.CharField(max_length=25)
    def __str__(self):
        return self.p_id.name
