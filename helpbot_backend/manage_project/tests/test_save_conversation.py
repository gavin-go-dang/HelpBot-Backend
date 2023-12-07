import io
from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ..models import Conversation
from ..models.project import Project


class GetRoomChatTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.project = Project.objects.create(id=1, name="Test Project", script_QA="Test QA Script")

    def test_get_room_chat(self):
        response = self.client.get("/api/v1/manage-project/get-room-chat/1/")  # Replace with your actual API endpoint

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.data)

        # Check if a conversation was saved
        conversation = Conversation.objects.last()
        self.assertIsNotNone(conversation)
        self.assertEqual(conversation.room, response.data["id"])
        self.assertEqual(conversation.project, self.project)

    def test_get_room_chat_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            response = self.client.get(
                "/api/v1/manage-project/get-room-chat/1/"
            )  # Replace with your actual API endpoint

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)

    def test_get_room_chat_invalid_json(self):
        id_file_content = "invalid json"
        with patch("builtins.open", return_value=io.StringIO(id_file_content)):
            response = self.client.get(
                "/api/v1/manage-project/get-room-chat/1/"
            )  # Replace with your actual API endpoint

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)
