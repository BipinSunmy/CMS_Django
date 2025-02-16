from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets
from .models import BloodGroup, Staff,Qualifications,Specialization,Lab,Medicine,Doctor,Appointment,Patient,Prescrible,Payment,Billing, Time
from .serializers import staffSerializers,GroupSerializer,SigupSerializer,qualificationSerializers,specializationSerializers,labSerializers,medicineSerializers,doctorSerializers,patientSerializers,appointmentSerializers,prescribleSerializers,paymentSerializers,billingSerializers,userSerializers,timeSerializers,bloodSerializers,LoginSerializer
from django.contrib.auth.models import Group,User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from datetime import date
# Create your views here.
class userView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers
class qualificationView(viewsets.ModelViewSet):
    queryset = Qualifications.objects.all()
    serializer_class = qualificationSerializers

class specializationView(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = specializationSerializers
class labView(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = labSerializers
class medicineView(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = medicineSerializers
class bloodView(viewsets.ModelViewSet):
    queryset = BloodGroup.objects.all()
    serializer_class = bloodSerializers
class staffView(viewsets.ModelViewSet):
    serializer_class = staffSerializers
    queryset = Staff.objects.all()
    def get_queryset(self):
        queryset = Staff.objects.all()
        l_id = self.request.query_params.get('l_id')
        if l_id is not None:
            l_id = l_id.strip().lower()
            if l_id == "null" or l_id=="":
                queryset = queryset.filter(l_id__isnull=True)
            elif l_id:
                queryset =  Staff.objects.filter(l_id=l_id)
        return queryset
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            # Handle unique constraint errors
            if 'email' in str(e):
                return Response({"error": "The email is already in use."}, status=status.HTTP_400_BAD_REQUEST)
            elif 'phone' in str(e):
                return Response({"error": "The phone number is already in use."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "A unique constraint error occurred."}, status=status.HTTP_400_BAD_REQUEST)
class doctorView(viewsets.ModelViewSet):
    serializer_class = doctorSerializers
    queryset = Doctor.objects.all()
    def get_queryset(self):
        queryset = Doctor.objects.all()
        l_id = self.request.query_params.get('l_id')
        Available = self.request.query_params.get('Available')
        if l_id is not None:
            l_id = l_id.strip().lower()
            if l_id == "null" or "":
                queryset = Doctor.objects.filter(l_id__isnull=True)
            elif l_id:
                queryset =  Doctor.objects.filter(l_id=l_id) 
        if Available is not None:
            queryset =  Doctor.objects.filter(Available=Available) 
        return queryset
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            # Handle unique constraint errors
            if 'email' in str(e):
                return Response({"error": "The email is already in use."}, status=status.HTTP_400_BAD_REQUEST)
            elif 'phone' in str(e):
                return Response({"error": "The phone number is already in use."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "A unique constraint error occurred."}, status=status.HTTP_400_BAD_REQUEST)

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class appointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = appointmentSerializers
    def get_queryset(self):
        queryset = Appointment.objects.all()
        DoA = self.request.query_params.get('DoA')
        if DoA:
            queryset = Appointment.objects.filter(DoA=DoA)
        return queryset
class patientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = patientSerializers
class PrescribleView(viewsets.ModelViewSet):
    queryset = Prescrible.objects.all()
    serializer_class = prescribleSerializers
class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = paymentSerializers
class BillingView(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = billingSerializers
class timeView(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = timeSerializers
class signupView(APIView):
    
    def post(self, request):
        serializer = SigupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user_id": user.id,
                "username": user.username,
                "token": token.key,
                "role": user.groups.all()[0].id
            })
        else:
            # Check if the error is related to duplicate username
            errors = serializer.errors
            if 'username' in errors and 'unique' in ''.join(errors['username']):
                return Response({
                    "status": "error",
                    "message": "The username already exists. Please choose another username."
                }, status=status.HTTP_400_BAD_REQUEST)
            # Handle other validation errors
            return Response({
                "status": "error",
                "message": "Invalid data.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class loginView(APIView):
    '''this api will handle login and return
        token for authentication
    '''
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                '''we are retriving the token for authenticated user'''
                token = Token.objects.get(user=user)
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "user_id" : user.id,
                    "username": user.username,
                    "role": user.groups.all()[0].id if user.groups.exists() else None,
                    "data": {
                        "Token": token.key
                    }  
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message":"Invalid Email or password"
                }
                return Response(response,status=status.HTTP_401_UNAUTHORIZED)
        
        response = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message":"Bad request",
                    "data": serializer.data
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)