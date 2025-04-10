from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse

from rest_framework import status

User = get_user_model()


class UserRegisterTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """set all urls to test"""
        cls.url = reverse("register-api")  # get url from urls.py

    def test_register_success(self):
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone_number": "+201234567888",
            "password": "StrongPassword123!",
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=payload["email"]).exists())

    def test_register_duplicate_email(self):
        User.objects.create_user(
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com",
            phone_number="+201234567888",
            password="StrongPassword123!",
        )

        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com",
            "phone_number": "+201098872271",
            "password": "AnotherStrongPass123!",
        }

        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
