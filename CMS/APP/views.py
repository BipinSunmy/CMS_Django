from django.shortcuts import render
from rest_framework import viewsets
from .models import Staff,Qualifications,Specialization,Lab,Medicine,Doctor,Appointment,Patient,Prescrible,Payment,Billing
from .serializers import staffSerializers,GroupSerializer,SigupSerializer,qualificationSerializers,specializationSerializers,labSerializers,medicineSerializers,doctorSerializers,patientSerializers,appointmentSerializers,prescribleSerializers,paymentSerializers,billingSerializers,userSerializers
from django.contrib.auth.models import Group,User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
    
class staffView(viewsets.ModelViewSet):
    serializer_class = staffSerializers
    queryset = Staff.objects.all()
    def get_queryset(self):
        queryset = Staff.objects.all()
        l_id = self.request.query_params.get('l_id')
        if l_id:
            queryset =  Staff.objects.filter(l_id=l_id)
        return queryset
class doctorView(viewsets.ModelViewSet):
    serializer_class = doctorSerializers
    queryset = Doctor.objects.all()
    def get_queryset(self):
        queryset = Doctor.objects.all()
        l_id = self.request.query_params.get('l_id')
        if l_id:
            queryset =  Doctor.objects.filter(l_id=l_id)
        return queryset

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class appointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = appointmentSerializers
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


class signupView(APIView):
    def post(self,request):
        serializer = SigupSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user_id": user.id,
                "username" : user.username,
                "role": user.groups.all()[0].id
            })
        else:
            res = {'status': status.HTTP_400_BAD_REQUEST,
                   'data': serializer.errors}
            return Response(res, status = status.HTTP_400_BAD_REQUEST)
        