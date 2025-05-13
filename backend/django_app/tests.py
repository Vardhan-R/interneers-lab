from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

class SimpleTestCase(TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_dummy(self):
        self.assertTrue(True)

class GreetingAPITest(TestCase):
    def setUp(self):
        """Setup test client"""
        self.client = APIClient()
        self.url = "/hello/"

    def test_response_status_code(self):
        """Test if the response status code is 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_time(self):
        """Test if response time is below 500ms"""
        import time
        start_time = time.time()
        response = self.client.get(self.url)
        elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        self.assertLess(elapsed_time, 500, "Response took too long")

    def test_response_has_required_fields(self):
        """Test if the response contains 'message' field"""
        response = self.client.get(self.url)
        response_data = response.json()

        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

    def test_name_is_non_empty_string(self):
        """Test if the 'message' field is a non-empty string"""
        response = self.client.get(self.url)
        response_data = response.json()

        self.assertIsInstance(response_data, dict)
        self.assertIsInstance(response_data.get("message"), str)
        self.assertGreater(len(response_data["message"]), 0, "Message should not be empty")

    def test_validate_response_schema(self):
        """Test if the response matches the expected schema"""
        response = self.client.get(self.url)
        response_data = response.json()

        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)
        self.assertIsInstance(response_data["message"], str)
