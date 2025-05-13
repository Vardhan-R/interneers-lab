from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

class MyTest(TestCase):
    def setUp(self):
        """Setup test client"""
        self.client = APIClient()
        self.url = ""

    def test_redirects_to_home(self):
        response = self.client.get("/", follow=False)

        # Check that it's a 302 redirect
        self.assertEqual(response.status_code, 302)

        # Check the redirection URL is /home/
        self.assertEqual(response["Location"], "/home")
