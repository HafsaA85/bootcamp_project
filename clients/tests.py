from django.test import TestCase
from .models import Client, Appointment
from django.contrib.auth.models import User

# Create your tests here.

class ClientModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client_profile = Client.objects.create(user=self.user, phone='1234567890')

    def test_client_str(self):
        self.assertEqual(str(self.client_profile), 'testuser')
