from rest_framework import serializers
from .models import Staff,Qualifications,Specialization,Lab,Medicine,Doctor,Appointment,Patient,Prescrible,Payment,Billing
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
    class Meta:
        model = Staff
        fields = "__all__"
class doctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
    
class appointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
class patientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
class prescribleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescrible
        fields = "__all__"
class paymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
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