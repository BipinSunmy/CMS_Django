from rest_framework import serializers
from .models import Staff,Qualifications,Specialization,Lab,Medicine,Doctor,Appointment,Patient,Prescrible,Payment,Billing, Time,BloodGroup
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","groups"]
class qualificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qualifications
        fields = "__all__"

class timeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"
    
class specializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"
class labSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"
class medicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
class staffSerializers(serializers.ModelSerializer):
    qua_name = qualificationSerializers(source="Qualification",many=True,read_only=True)
    class Meta:
        model = Staff
        fields = ("id","l_id","f_name","l_name","email","phone","Qualification","DoB","salary","address","DoJ","isActive","qua_name")
    def validate(self, data):
        # Check for unique email
        if Staff.objects.filter(email=data.get('email')).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

        # Check for unique phone
        if Staff.objects.filter(phone=data.get('phone')).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError({"phone": "This phone number is already in use."})

        return data
class doctorSerializers(serializers.ModelSerializer):
    qua_name = qualificationSerializers(source="Qualification",many=True,read_only=True)
    spec = specializationSerializers(source="specialization",read_only=True) 
    class Meta:
        model = Doctor
        fields = ("doc_id","l_id","f_name","l_name","email","phone","specialization","Qualification","address","DoJ","DoB","salary","fee","Available","start_date","end_date","qua_name","spec")
    def validate(self, data):
        if Doctor.objects.filter(email=data.get('email')).exclude(doc_id=self.instance.doc_id if self.instance else None).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

        # Check for unique phone
        if Doctor.objects.filter(phone=data.get('phone')).exclude(doc_id=self.instance.doc_id if self.instance else None).exists():
            raise serializers.ValidationError({"phone": "This phone number is already in use."})
        return data

class patientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
class appointmentSerializers(serializers.ModelSerializer):
    patient_name = patientSerializers(source="p_id",read_only=True)
    doctor_name = doctorSerializers(source="d_id",read_only=True)
    timing = timeSerializers(source="time",read_only=True)
    class Meta:
        model = Appointment
        fields = ["a_id","d_id","p_id","patient_name", "doctor_name", "token", "DoA", "timing","time", "status"]
class prescribleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescrible
        fields = "__all__"
class paymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
class bloodSerializers(serializers.ModelSerializer):
    class Meta:
        model = BloodGroup
        fields = "__all__"
class billingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Group
        fields = "__all__"

class SigupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)
    class Meta:
        model = User
        fields = ["username","password","groups"]
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']