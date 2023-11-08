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

        # Kiểm tra xem dữ liệu phản hồi có khớp với dữ liệu mong đợi từ cơ sở dữ liệu hay không
        expected_data = AnswerSerializers([self.message1, self.message2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_delete_message(self):
        url = f"{self.url}{self.message1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Kiểm tra xem tin nhắn có bị xóa khỏi cơ sở dữ liệu hay không
        self.assertFalse(Message.objects.filter(id=self.message1.id).exists())
