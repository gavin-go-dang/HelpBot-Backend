from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Message


class MessageReceivedPerWeekAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/v1/manage-project/message-count/"

    def test_get_message_received_per_week(self):
        # Create some messages with different created_at dates
        Message.objects.create(created_at=datetime.now() - timedelta(days=1))
        Message.objects.create(created_at=datetime.now() - timedelta(days=2))
        Message.objects.create(created_at=datetime.now() - timedelta(days=3))

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["count"]), 7)  # Assuming you expect data for 7 days
        self.assertEqual(len(response.data["date"]), 7)

        # Make sure the data is in the correct format
        self.assertIsInstance(response.data["count"][0], int)
        self.assertIsInstance(response.data["date"][0], str)
