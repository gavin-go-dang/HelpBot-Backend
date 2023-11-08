from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Message
from ..serializers import AnswerSerializers


class MessageAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/api/v1/manage-project/message/"

        self.message1 = Message.objects.create(content="Hello")
        self.message2 = Message.objects.create(content="World")

    def test_get_messages(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = AnswerSerializers([self.message1, self.message2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_delete_message(self):
        url = f"{self.url}{self.message1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Message.objects.filter(id=self.message1.id).exists())
