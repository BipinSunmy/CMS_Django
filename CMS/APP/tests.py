from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Staff, Qualifications
from rest_framework.test import APIClient

# Create your tests here.

class TestAPIEndpoints(APITestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Adding Mock Qualification Creation
        self.qualification = Qualifications.objects.create(name="Master's Degree")
        
        self.signup_url = reverse('sigup')
        self.staff_url = reverse('staff-list')  
        self.staff_data = {
            "f_name": "Navneet",
            "l_name": "Remanand",
            "email": "navneet.remanand@gmail.com",
            "phone": "1234567890",
            "Qualification": [self.qualification.id],
            "DoB": "1999-12-29",
            "salary": 1000000
        }

    def test_signup(self):
        data = {
            "username": "navneet_remanand",
            "password": "Navrem2912!",
            "groups": [1]
        }

        response = self.client.post(self.signup_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("user_id", response.data)
        self.assertIn("username", response.data)
        self.assertIn("role", response.data)

    def test_signup_invalid_data(self):
        data = {
            "username": "navneet_remanand",
            "password": "nrem",  
            "groups": [1]
        }

        response = self.client.post(self.signup_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_staff_create(self):
        
        response = self.client.post(self.staff_url, self.staff_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_staff_list(self):
        
        response = self.client.get(self.staff_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_staff_update(self):
        
        staff_member = Staff.objects.create(**self.staff_data)
        updated_data = {"f_name": "Bipin"}
        
        response = self.client.put(reverse('staff-detail', args=[staff_member.id]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        staff_member.refresh_from_db()
        self.assertEqual(staff_member.f_name, "Bipin")

    def test_staff_delete(self):
        
        staff_member = Staff.objects.create(**self.staff_data)
        
        response = self.client.delete(reverse('staff-detail', args=[staff_member.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)